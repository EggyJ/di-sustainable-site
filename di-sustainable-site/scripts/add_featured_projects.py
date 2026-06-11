#!/usr/bin/env python3
"""Add __FEATURED_PROJECTS__ to data.js"""
import json, os

SITE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(SITE_DIR, 'data.js')

with open(DATA_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

eq_idx = content.index('=')
json_str = content[eq_idx+1:].strip().rstrip(';').strip()
data = json.loads(json_str)

# Build featured projects with all images and multi-faculty associations
featured = [
    {
        "id": "design-harvests",
        "name_zh": "设计丰收",
        "name_en": "Design Harvests",
        "description_zh": data[data.index(next(x for x in data if x['id']=='lou-yongqi'))]['achievements'][0]['description_zh'],
        "description_en": data[data.index(next(x for x in data if x['id']=='lou-yongqi'))]['achievements'][0]['description_en'],
        "faculty_ids": ["lou-yongqi", "francesca-valsecchi", "zhu-xiaocun"],
        "images": [
            {"src": "images/design-harvests-p1.webp", "caption_zh": "", "caption_en": ""},
            {"src": "images/design-harvests-p2.webp", "caption_zh": "", "caption_en": ""},
            {"src": "images/design-harvests-p3.webp", "caption_zh": "", "caption_en": ""},
            {"src": "images/design-harvests-p4.webp", "caption_zh": "", "caption_en": ""},
            {"src": "images/design-harvests-p5.webp", "caption_zh": "", "caption_en": ""},
            {"src": "images/design-harvests-p6.webp", "caption_zh": "", "caption_en": ""},
            {"src": "images/design-harvests-p7.webp", "caption_zh": "", "caption_en": ""},
        ]
    },
    {
        "id": "nice-2035",
        "name_zh": "NICE 2035 原型街",
        "name_en": "NICE 2035 Prototype Street",
        "description_zh": data[data.index(next(x for x in data if x['id']=='lou-yongqi'))]['achievements'][1]['description_zh'],
        "description_en": data[data.index(next(x for x in data if x['id']=='lou-yongqi'))]['achievements'][1]['description_en'],
        "faculty_ids": ["lou-yongqi", "wu-duan", "danwen-ji"],
        "images": [
            {"src": "images/nice2035-p1.webp", "caption_zh": "", "caption_en": ""},
            {"src": "images/nice2035-p2.webp", "caption_zh": "", "caption_en": ""},
            {"src": "images/nice2035-p3.webp", "caption_zh": "", "caption_en": ""},
        ]
    },
    {
        "id": "wdcc-2025",
        "name_zh": "WDCC 2025 设计无界，生生不息主题展",
        "name_en": "WDCC 2025: Design Without Boundaries, Endless Growth",
        "description_zh": data[data.index(next(x for x in data if x['id']=='lou-yongqi'))]['achievements'][2]['description_zh'],
        "description_en": data[data.index(next(x for x in data if x['id']=='lou-yongqi'))]['achievements'][2]['description_en'],
        "faculty_ids": ["lou-yongqi", "lu-wen"],
        "images": [
            {"src": "images/wdcc-p0.webp", "caption_zh": "", "caption_en": ""},
            {"src": "images/wdcc-p1.webp", "caption_zh": "", "caption_en": ""},
            {"src": "images/wdcc-p2.webp", "caption_zh": "", "caption_en": ""},
            {"src": "images/wdcc-p3.webp", "caption_zh": "", "caption_en": ""},
            {"src": "images/wdcc-p4.webp", "caption_zh": "", "caption_en": ""},
            {"src": "images/wdcc-p5.webp", "caption_zh": "", "caption_en": ""},
            {"src": "images/wdcc-p6.webp", "caption_zh": "", "caption_en": ""},
            {"src": "images/wdcc-p7.webp", "caption_zh": "", "caption_en": ""},
            {"src": "images/wdcc-p8.webp", "caption_zh": "", "caption_en": ""},
            {"src": "images/wdcc-p9.webp", "caption_zh": "", "caption_en": ""},
        ]
    }
]

# Append to data.js
featured_json = json.dumps(featured, ensure_ascii=False, indent=2)
new_content = content.rstrip().rstrip(';').strip() + '\n\nwindow.__FEATURED_PROJECTS__ = ' + featured_json + ';\n'

with open(DATA_FILE, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f'Added {len(featured)} featured projects to data.js')
for fp in featured:
    print(f'  {fp["id"]}: {fp["name_en"]} ({len(fp["images"])} images, {len(fp["faculty_ids"])} faculty)')
