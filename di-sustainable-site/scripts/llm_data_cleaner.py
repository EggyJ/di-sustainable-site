#!/usr/bin/env python3
"""
LLM-based faculty data cleaner.
Reads current data.js, sends each faculty's raw text to an LLM prompt
that separates ZH/EN, splits packed achievements into distinct entries,
and only keeps confidently-matched gallery items.
Output: cleaned JSON ready for data.js.
"""

import json
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(SCRIPT_DIR)
DATA_JS = os.path.join(PROJECT_DIR, "data.js")
OUTPUT_JSON = os.path.join(PROJECT_DIR, "cleaned_data.json")

# Read data.js
with open(DATA_JS, "r", encoding="utf-8") as f:
    content = f.read()

# Remove window.__SITE_DATA__ = prefix and trailing ;
content = content.strip()
if content.startswith("window.__SITE_DATA__"):
    content = content[len("window.__SITE_DATA__"):]
    content = content.lstrip(" =\n")
if content.endswith(";"):
    content = content[:-1]

faculty_list = json.loads(content)
print(f"Loaded {len(faculty_list)} faculty members")

# Get list of actual image files
images_dir = os.path.join(PROJECT_DIR, "images")
actual_images = set()
if os.path.isdir(images_dir):
    for fname in os.listdir(images_dir):
        if fname.endswith(".webp"):
            actual_images.add(f"images/{fname}")
    for fname in os.listdir(images_dir):
        if fname.endswith(".x-emf"):
            actual_images.add(f"images/{fname}")
print(f"Found {len(actual_images)} image files")

# Generate prompts for each faculty
prompts = []
for i, fac in enumerate(faculty_list):
    # Build a raw text representation for this faculty
    raw = {
        "id": fac.get("id", ""),
        "current_photo": fac.get("photo", ""),
        "current_name_zh": fac.get("name_zh", ""),
        "current_name_en": fac.get("name_en", ""),
        "current_title_zh": fac.get("title_zh", ""),
        "current_title_en": fac.get("title_en", ""),
        "current_bio_zh": fac.get("bio_zh", ""),
        "current_bio_en": fac.get("bio_en", ""),
        "current_tags": fac.get("tags", []),
    }

    # Collect ALL text from achievements (mixed ZH/EN blobs)
    all_achievement_texts = []
    for a in fac.get("achievements", []):
        parts = []
        if a.get("name_zh"):
            parts.append(a["name_zh"])
        if a.get("name_en"):
            parts.append(a["name_en"])
        if a.get("description_zh"):
            parts.append(a["description_zh"])
        if a.get("description_en"):
            parts.append(a["description_en"])
        if parts:
            all_achievement_texts.append("\n".join(parts))

    # Collect ALL text from courses
    all_course_texts = []
    for c in fac.get("courses", []):
        parts = []
        if c.get("name_zh"):
            parts.append(c["name_zh"])
        if c.get("name_en"):
            parts.append(c["name_en"])
        if c.get("description_zh"):
            parts.append(c["description_zh"])
        if c.get("description_en"):
            parts.append(c["description_en"])
        if parts:
            all_course_texts.append("\n".join(parts))

    # Collect gallery info (src + any captions)
    gallery_info = []
    for g in fac.get("gallery", []):
        gallery_info.append({
            "src": g.get("src", ""),
            "caption_zh": g.get("caption_zh", ""),
            "caption_en": g.get("caption_en", ""),
        })

    raw["raw_achievement_texts"] = all_achievement_texts
    raw["raw_course_texts"] = all_course_texts
    raw["gallery_info"] = gallery_info

    prompt = f"""你是一个数据清洗助手。请处理以下教师数据，做以下事情：

## 任务
1. **分离中英文**：每个字段必须有独立的中文版和英文版。如果原文只有一种语言，另一种留空字符串 ""
2. **拆分混杂内容**：
   - achievements（研究成果/项目）：每个条目应该是**一个独立的项目/论文/成就**。如果一个文本块里描述了多个项目，拆分成多个独立条目
   - 每个条目的 name 应该是项目/论文标题，description 是简要描述（1-3句话）
   - 如果原文中一个 achievement 的 description_zh 或 description_en 里实际包含了多个不同项目的内容，必须拆分
3. **课程（courses）**：确保 name_zh 是纯中文课程名，name_en 是纯英文课程名。description 也是同样要求
4. **图片（gallery）**：
   - 只保留那些有明确中文或英文caption描述的图片
   - 文件名是 "gallery-1.webp"、"gallery-2.webp" 等通用名称且没有caption的图片，直接删除（这些是之前错误分配的）
   - 文件名以 ".x-emf" 结尾的图片也删除（格式不兼容网页）
   - 确保caption_zh只包含中文，caption_en只包含英文
5. **标签（tags）**：如果tags中有中文的，改为对应的英文
6. **bio**：确保 bio_zh 是纯中文，bio_en 是纯英文。如果当前只有一种语言，尝试从其他文本中提取另一种语言的bio

## 输出格式
请严格按以下JSON格式输出，不要有任何多余文字：
```json
{{
  "name_zh": "中文名",
  "name_en": "English name",
  "title_zh": "中文职称",
  "title_en": "English title",
  "bio_zh": "纯中文个人简介",
  "bio_en": "Pure English bio",
  "tags": ["English Tag 1", "English Tag 2"],
  "achievements": [
    {{
      "name_zh": "项目中文名",
      "name_en": "Project English Name",
      "description_zh": "中文描述",
      "description_en": "English description"
    }}
  ],
  "courses": [
    {{
      "name_zh": "中文课程名（不含书名号）",
      "name_en": "English Course Name",
      "description_zh": "中文课程描述",
      "description_en": "English course description"
    }}
  ],
  "gallery": [
    {{
      "src": "images/xxx.webp",
      "caption_zh": "中文图片说明",
      "caption_en": "English caption"
    }}
  ]
}}
```

## 当前数据（原始，可能混杂中英文）

{json.dumps(raw, ensure_ascii=False, indent=2)}
"""

    prompts.append({
        "index": i,
        "faculty_id": fac.get("id", ""),
        "name": fac.get("name_zh", fac.get("name_en", "")),
        "raw_data": raw,
        "prompt": prompt,
    })

# Save prompts to a file for batch processing
prompts_file = os.path.join(SCRIPT_DIR, "llm_prompts.jsonl")
with open(prompts_file, "w", encoding="utf-8") as f:
    for p in prompts:
        f.write(json.dumps(p, ensure_ascii=False) + "\n")

print(f"Generated {len(prompts)} LLM prompts")
print(f"Prompts saved to: {prompts_file}")
print(f"\nNext step: Process each prompt with an LLM and collect structured JSON output")
