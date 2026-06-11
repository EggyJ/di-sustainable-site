#!/usr/bin/env python3
"""
SDSI Faculty Docx Importer
==========================
把老师个人信息收集表 (.docx) 解析为 data.js 格式的 JSON 数据，
同时提取并压缩图片到 images/ 目录。

用法:
  python3 scripts/import_docx.py /path/to/老师.docx [--output data.js] [--images-dir images/]

文档结构要求:
  1. 姓名：XXX
  2. 个人照片高清图
  3. 个人介绍（300字以内）
  4. 代表性成果（1-2个）
  5. 课程
  6. 图片（至少5张）
  1. Full name：XXX  (英文版，可选)

作者: D&I SDSI Project
"""

import sys, os, re, json, argparse, textwrap
from pathlib import Path

try:
    from docx import Document
except ImportError:
    print("ERROR: python-docx not installed. Run: pip install python-docx Pillow")
    sys.exit(1)

try:
    from PIL import Image
    HAS_PIL = True
except ImportError:
    HAS_PIL = False
    print("WARNING: Pillow not installed. Images will be copied as-is (no WebP conversion).")

# ─── Config ───────────────────────────────────────────────
WEBP_QUALITY = 85          # WebP quality (0-100)
MAX_IMAGE_WIDTH = 1600      # Resize images wider than this
PHOTO_MAX_WIDTH = 800       # Portrait photo max width
PHOTO_MAX_HEIGHT = 1000     # Portrait photo max height
PHOTO_QUALITY = 90          # Photo quality (higher)

# ─── Helpers ─────────────────────────────────────────────
def slugify(text):
    """Create URL-safe ID from name (Chinese pinyin fallback to latin chars)."""
    # Remove common Chinese punctuation
    text = re.sub(r'[^\w\s-]', '', text.strip())
    # If contains Chinese, try to keep it simple
    if re.search(r'[\u4e00-\u9fff]', text):
        # Extract Latin parts first, then use transliteration fallback
        latin = re.findall(r'[a-zA-Z]+', text)
        if latin:
            return '-'.join(latin).lower()
        return 'faculty-' + str(abs(hash(text)) % 10000)
    return '-'.join(text.lower().split())

def truncate(s, max_len):
    return s if len(s) <= max_len else s[:max_len-3] + '...'

def save_image(blob, dest_path, content_type, max_w=None, max_h=None, quality=WEBP_QUALITY):
    """Save image blob, optionally convert to WebP and resize."""
    dest = Path(dest_path)
    dest.parent.mkdir(parents=True, exist_ok=True)

    if HAS_PIL and content_type in ('image/png', 'image/jpeg', 'image/jpg'):
        img = Image.open(__import__('io').BytesIO(blob))
        # Convert RGBA to RGB for JPEG
        if img.mode in ('RGBA', 'P'):
            img = img.convert('RGB')
        # Resize
        w, h = img.size
        if max_w and w > max_w:
            ratio = max_w / w
            img = img.resize((int(w * ratio), int(h * ratio)), Image.LANCZOS)
        if max_h and h > max_h:
            ratio = max_h / h
            img = img.resize((int(w * ratio), int(h * ratio)), Image.LANCZOS)
        webp_path = dest.with_suffix('.webp')
        img.save(webp_path, 'webp', quality=quality)
        return webp_path.name
    else:
        # Fallback: save as-is
        ext = content_type.split('/')[-1] if '/' in content_type else 'png'
        if ext == 'jpeg': ext = 'jpg'
        final_path = dest.with_suffix(f'.{ext}')
        with open(final_path, 'wb') as f:
            f.write(blob)
        return final_path.name

def find_image_in_paragraph(para):
    """Check if a paragraph contains an embedded image. Returns rel_id or None."""
    from docx.oxml.ns import qn
    for run in para.runs:
        drawings = run._element.findall('.//' + qn('w:drawing'))
        for d in drawings:
            blip = d.findall('.//' + qn('a:blip'))
            if blip:
                embed = blip[0].get(qn('r:embed'))
                if embed:
                    return embed
    return None

# ─── Main Parser ─────────────────────────────────────────
def parse_docx(filepath, images_dir):
    """Parse a single SDSI info collection docx and return structured data."""
    doc = Document(filepath)
    paras = [(i, p.text.strip(), p) for i, p in enumerate(doc.paragraphs)]

    result = {
        'id': '',
        'name_zh': '',
        'name_en': '',
        'photo': '',
        'photo_file': '',
        'bio_zh': '',
        'bio_en': '',
        'achievements': [],
        'courses': [],
        'gallery': [],
        'tags_zh': [],
        'tags_en': [],
        '_seen_rids': set(),  # Track which image rIds we've already extracted
    }

    # ── Phase 1: Split into Chinese and English sections ──
    # Find where English version starts (look for "1. Full name")
    en_start = None
    for i, text, _ in paras:
        if re.match(r'^1\.\s*Full\s+name', text, re.I):
            en_start = i
            break

    zh_paras = [(i, t, p) for i, t, p in paras if en_start is None or i < en_start]
    en_paras = [(i, t, p) for i, t, p in paras if en_start is not None and i >= en_start]

    # ── Phase 2: Parse Chinese section ──
    parse_section(zh_paras, result, images_dir, lang='zh', doc=doc)

    # ── Phase 3: Parse English section ──
    if en_paras:
        parse_section(en_paras, result, images_dir, lang='en', doc=doc)

    # ── Phase 4: Merge ZH+EN gallery captions ──
    result['gallery'] = merge_gallery_captions(result['gallery'], images_dir)

    # Name: prefer combined ZH+EN
    name_parts = []
    if result['name_en']:
        name_parts.append(result['name_en'])
    if result['name_zh'] and result['name_zh'] != result['name_en']:
        # Extract just Chinese chars for display
        zh_only = re.findall(r'[\u4e00-\u9fff]+', result['name_zh'])
        if zh_only:
            name_parts.append(''.join(zh_only))
    result['name'] = ' '.join(name_parts)

    # ID from name
    result['id'] = slugify(result['name_en'] or result['name_zh'])

    # Bio: merge ZH+EN
    bio_parts = []
    if result['bio_zh']:
        bio_parts.append(result['bio_zh'])
    if result['bio_en'] and result['bio_en'] != result['bio_zh']:
        bio_parts.append(result['bio_en'])
    result['bio'] = '\n'.join(bio_parts) if len(bio_parts) > 1 else bio_parts[0] if bio_parts else ''

    # Tags: extract from bio keywords (basic heuristic)
    result['tags'] = extract_tags(result['bio_zh'] + ' ' + result['bio_en'])

    # Achievements: merge ZH+EN
    result['achievements'] = merge_achievements(result['achievements'])

    # Remove internal fields
    for k in ['name_zh', 'name_en', 'bio_zh', 'bio_en', 'photo_file', 'tags_zh', 'tags_en', '_seen_rids']:
        result.pop(k, None)

    return result

def parse_section(paras, result, images_dir, lang='zh', doc=None):
    """Parse either Chinese or English section paragraphs."""
    is_zh = (lang == 'zh')

    # Build a list of text with index
    texts = []
    for i, text, p in paras:
        if text:
            texts.append((i, text))

    for idx, (i, text) in enumerate(texts):
        # ── Name ──
        if is_zh and re.match(r'^1\.\s*姓名[：:]', text):
            result['name_zh'] = re.sub(r'^1\.\s*姓名[：:]\s*', '', text).strip()
        elif not is_zh and re.match(r'^1\.\s*Full\s+name[：:]', text, re.I):
            result['name_en'] = re.sub(r'^1\.\s*Full\s+name[：:]\s*', '', text).strip()

        # ── Photo ──
        # Photo is handled by extract_photo() below

        # ── Bio ──
        elif is_zh and re.match(r'^3\.\s*个人介绍', text):
            bio_texts = []
            for j in range(idx+1, len(texts)):
                if re.match(r'^[4-6]\.\s', texts[j][1]):
                    break
                bio_texts.append(texts[j][1])
            result['bio_zh'] = ' '.join(bio_texts).strip()
        elif not is_zh and re.match(r'^3\.\s*Personal\s+Profile', text, re.I):
            bio_texts = []
            for j in range(idx+1, len(texts)):
                if re.match(r'^[4-6]\.\s', texts[j][1]):
                    break
                bio_texts.append(texts[j][1])
            result['bio_en'] = ' '.join(bio_texts).strip()

        # ── Achievements ──
        elif is_zh and re.match(r'^4\.\s*代表性成果', text):
            result['achievements'].extend(parse_achievements(texts, idx, lang='zh'))
        elif not is_zh and re.match(r'^4\.\s*Representative\s+works', text, re.I):
            result['achievements'].extend(parse_achievements(texts, idx, lang='en'))

        # ── Courses ──
        elif is_zh and re.match(r'^5\.\s*课程', text):
            result['courses'].extend(parse_courses(texts, idx))
        elif not is_zh and re.match(r'^5\.\s*Courses', text, re.I):
            result['courses'].extend(parse_courses(texts, idx))

        # ── Gallery Images ──
        elif is_zh and re.match(r'^6\.\s*图片', text):
            result['gallery'].extend(parse_gallery(texts, idx, paras, doc, images_dir, lang='zh', seen_rids=result.get('_seen_rids', set())))
        elif not is_zh and re.match(r'^6\.\s*Images', text, re.I):
            result['gallery'].extend(parse_gallery(texts, idx, paras, doc, images_dir, lang='en', seen_rids=result.get('_seen_rids', set())))

    # ── Photo extraction: scan paragraphs near section 2 ──
    # Look in original paragraphs for images between section 2 and section 3
    extract_photo(paras, result, images_dir, is_zh, doc)

def extract_photo(paras, result, images_dir, is_zh, doc):
    """Extract the personal photo from section 2."""
    # Find paragraphs between section 2 header and section 3 header
    in_photo_section = False
    photo_paras = []
    for i, text, para in paras:
        if is_zh and re.match(r'^2\.\s*个人照片', text):
            in_photo_section = True
            continue
        elif is_zh and re.match(r'^3\.\s*个人介绍', text):
            in_photo_section = False
            break
        elif not is_zh and re.match(r'^2\.\s*High-resolution\s+Personal\s+photo', text, re.I):
            in_photo_section = True
            continue
        elif not is_zh and re.match(r'^3\.\s*Personal\s+Profile', text, re.I):
            in_photo_section = False
            break
        if in_photo_section:
            photo_paras.append((i, text, para))

    # Find image in these paragraphs
    for i, text, para in photo_paras:
        rid = find_image_in_paragraph(para)
        if rid and doc:
            rel = doc.part.rels.get(rid)
            if rel and 'image' in rel.reltype:
                img_blob = rel.target_part.blob
                content_type = rel.target_part.content_type
                name = slugify(result.get('name_en') or result.get('name_zh') or 'unknown')
                filename = save_image(img_blob, os.path.join(images_dir, f'photo-{name}'),
                                      content_type, max_w=PHOTO_MAX_WIDTH, max_h=PHOTO_MAX_HEIGHT,
                                      quality=PHOTO_QUALITY)
                result['photo'] = f'images/{filename}'
                result['photo_file'] = filename
                return

def parse_achievements(texts, start_idx, lang='zh'):
    """Parse numbered achievement items."""
    achievements = []
    current = None
    for j in range(start_idx + 1, len(texts)):
        text = texts[j][1]
        # Stop at next major section
        if re.match(r'^[5-6]\.\s', text):
            break
        # Detect numbered achievement: "1.XXX" or "1. XXX"
        m = re.match(r'^(\d+)\.\s*(.+)', text)
        if m:
            if current:
                achievements.append(current)
            current = {'name': m.group(2).rstrip('。').strip(), 'description': '', 'lang': lang}
        elif current and text.strip():
            # This is the description paragraph
            if not current['description']:
                current['description'] = text.strip().rstrip('。')
            else:
                current['description'] += ' ' + text.strip().rstrip('。')
    if current:
        achievements.append(current)
    return achievements

def parse_courses(texts, start_idx):
    """Parse course entries (currently simple text after section 5)."""
    courses = []
    for j in range(start_idx + 1, len(texts)):
        text = texts[j][1]
        if re.match(r'^[6]\.\s', text):
            break
        if text.strip():
            courses.append({'name': text.strip(), 'description': ''})
    return courses

def parse_gallery(texts, start_idx, all_paras, doc, images_dir, lang='zh', seen_rids=None):
    """Extract gallery images with captions.
    Image and caption are in SEPARATE paragraphs: image above, caption below.
    seen_rids: set of already-extracted rIds to avoid duplicates from CN+EN sections.
    """
    gallery = []
    if seen_rids is None:
        seen_rids = set()

    # Build map: orig_paragraph_index -> para object for ALL paragraphs
    para_map = {}
    for orig_idx, text, para in all_paras:
        para_map[orig_idx] = para

    # Get all paragraph indices in the range after section 6 header
    # We need to scan sequentially including empty paragraphs
    start_para_idx = texts[start_idx][0] if start_idx < len(texts) else 0
    end_para_idx = None

    # Find end: next major section
    for j in range(start_idx + 1, len(texts)):
        text = texts[j][1]
        if lang == 'zh' and re.match(r'^1\.\s*Full\s+name', text, re.I):
            end_para_idx = texts[j][0]
            break

    if end_para_idx is None:
        end_para_idx = max(para_map.keys()) + 1

    # Scan all paragraphs in range, looking for images + captions
    all_indices = sorted([k for k in para_map.keys() if start_para_idx < k < end_para_idx])

    for idx_pos, pidx in enumerate(all_indices):
        para = para_map[pidx]
        rid = find_image_in_paragraph(para)
        if rid and doc:
            rel = doc.part.rels.get(rid)
            if rel and 'image' in rel.reltype:
                img_blob = rel.target_part.blob
                content_type = rel.target_part.content_type

                # Look for caption in the next few paragraphs
                caption = ''
                en_caption = ''
                for look_ahead in range(1, 4):
                    if idx_pos + look_ahead < len(all_indices):
                        next_para = para_map[all_indices[idx_pos + look_ahead]]
                        next_text = next_para.text.strip()
                        if next_text and not find_image_in_paragraph(next_para):
                            if not caption:
                                caption = next_text
                            elif not en_caption and next_text != caption:
                                en_caption = next_text
                            break

                filename_base = slugify(caption[:30]) if caption else f'gallery-{len(gallery)+1}'
                filename = save_image(img_blob, os.path.join(images_dir, filename_base),
                                      content_type, max_w=MAX_IMAGE_WIDTH, quality=WEBP_QUALITY)

                entry = {
                    'src': f'images/{filename}',
                    'caption': caption,
                }
                if en_caption:
                    entry['caption_en'] = en_caption
                gallery.append(entry)

    return gallery

def extract_tags(bio_text):
    """Extract research tags from bio text using keyword matching."""
    tag_keywords = [
        ('Sustainable Design', ['可持续设计', 'sustainable design']),
        ('Social Innovation', ['社会创新', 'social innovation']),
        ('Systemic Design', ['系统设计', 'systemic design']),
        ('Ecosystem Conservation', ['生态系统保护', 'ecosystem conservation']),
        ('Sustainable Healthcare', ['可持续医疗', 'sustainable healthcare', '社区护理']),
        ('Elderly Care', ['老年人照护', 'elderly care', '养老', '老年护理']),
        ('Zero Waste', ['零废弃', 'zero waste', '废物']),
        ('Participatory Design', ['参与式设计', 'participatory design']),
        ('Ecology', ['生态', 'ecology', 'ecological']),
        ('Green Building', ['绿色校园', 'green building', '绿色建筑']),
        ('Urban Planning', ['城市规划', 'urban planning']),
        ('Data Visualization', ['数据可视化', 'data visualization']),
        ('Bio-Acoustics', ['声景', 'bio-acoustic']),
        ('More-than-Human', ['more-than-human']),
        ('Community Empowerment', ['社区赋权', 'community empowerment']),
        ('Inclusive Design', ['包容性', 'inclusive design']),
    ]

    tags = []
    bio_lower = bio_text.lower()
    for tag, keywords in tag_keywords:
        for kw in keywords:
            if kw.lower() in bio_lower and tag not in tags:
                tags.append(tag)
                break
    return tags

def merge_gallery_captions(gallery, images_dir):
    """Deduplicate gallery images and merge ZH+EN captions."""
    import hashlib
    seen = {}
    deduped = []

    for entry in gallery:
        src = entry.get('src', '')
        # Resolve actual file path: src is "images/xxx.webp", images_dir is "images"
        basename = os.path.basename(src)
        filepath = os.path.join(images_dir, basename)
        fhash = src
        try:
            with open(filepath, 'rb') as f:
                fhash = hashlib.md5(f.read()).hexdigest()
        except (FileNotFoundError, IOError):
            pass

        if fhash in seen:
            existing = seen[fhash]
            new_cap = entry.get('caption', '')
            old_cap = existing.get('caption', '')

            def has_cjk(s):
                return bool(re.search(r'[\u4e00-\u9fff]', s))

            if has_cjk(old_cap) and not has_cjk(new_cap) and new_cap:
                existing['caption_en'] = new_cap
            elif has_cjk(new_cap) and not has_cjk(old_cap) and old_cap:
                existing['caption'] = new_cap
                existing['caption_en'] = old_cap

            # Delete duplicate file
            try:
                os.remove(filepath)
            except (FileNotFoundError, IOError):
                pass
        else:
            seen[fhash] = entry
            deduped.append(entry)

    return deduped

def merge_achievements(achievements):
    """Merge ZH and EN achievements into combined entries."""
    zh_items = [a for a in achievements if a.get('lang') == 'zh']
    en_items = [a for a in achievements if a.get('lang') == 'en']

    merged = []
    for i, zh in enumerate(zh_items):
        entry = {
            'name': zh['name'],
            'description': zh['description'],
        }
        # Find matching EN item
        if i < len(en_items):
            en = en_items[i]
            if en['name'] and en['name'] != zh['name']:
                entry['name'] = f"{zh['name']} / {en['name']}"
            if en['description'] and en['description'] != zh['description']:
                entry['description'] = f"{zh['description']}\n\n{en['description']}"
        merged.append(entry)

    # If only EN items exist
    if not zh_items and en_items:
        merged = [{'name': a['name'], 'description': a['description']} for a in en_items]

    # Remove lang field
    for m in merged:
        m.pop('lang', None)

    return merged

# ─── Main ─────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description='Import SDSI faculty docx to data.js format')
    parser.add_argument('files', nargs='+', help='One or more .docx files to process')
    parser.add_argument('--output', '-o', default=None, help='Output JSON file path (default: stdout)')
    parser.add_argument('--images-dir', '-i', default='images', help='Directory for extracted images (default: images/)')
    parser.add_argument('--append', '-a', action='store_true', help='Append to existing data.js instead of replacing')
    args = parser.parse_args()

    all_data = []

    # Load existing data if appending
    output_path = args.output
    if args.append and output_path and os.path.exists(output_path):
        with open(output_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Remove "window.__SITE_DATA__ = " prefix and ";" suffix
            content = re.sub(r'^window\.__SITE_DATA__\s*=\s*', '', content)
            content = re.sub(r';\s*$', '', content)
            try:
                all_data = json.loads(content)
                print(f"Loaded {len(all_data)} existing records")
            except json.JSONDecodeError:
                print("WARNING: Could not parse existing file, starting fresh")

    # Process each file
    for filepath in args.files:
        if not os.path.exists(filepath):
            print(f"ERROR: File not found: {filepath}")
            continue

        print(f"\n{'='*60}")
        print(f"Processing: {os.path.basename(filepath)}")
        print(f"{'='*60}")

        data = parse_docx(filepath, args.images_dir)

        print(f"  Name:       {data.get('name', 'N/A')}")
        print(f"  ID:         {data.get('id', 'N/A')}")
        print(f"  Photo:      {data.get('photo', '(none)')}")
        print(f"  Bio:        {len(data.get('bio', ''))} chars")
        print(f"  Works:      {len(data.get('achievements', []))}")
        print(f"  Courses:    {len(data.get('courses', []))}")
        print(f"  Gallery:    {len(data.get('gallery', []))} images")
        print(f"  Tags:       {', '.join(data.get('tags', []))}")

        all_data.append(data)

    # Output
    if output_path:
        json_content = json.dumps(all_data, ensure_ascii=False, indent=2)
        js_content = f'window.__SITE_DATA__ = {json_content};'
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(js_content)
        print(f"\n✅ Written to {output_path} ({len(all_data)} records)")
    else:
        print(f"\n{'='*60}")
        print(json.dumps(all_data, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
