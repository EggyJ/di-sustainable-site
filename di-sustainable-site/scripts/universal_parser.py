#!/usr/bin/env python3
"""
Universal SDSI Faculty Docx Parser
====================================
Handles all known SDSI Info Collection doc formats:
  A. Standard numbered: 1. 姓名, 2. 个人照片, 3. 个人介绍...
  B. Unnumbered headers: 姓名, 个人照片, 个人介绍...
  C. EN-first docs: Full name, Photo, Personal Profile...
  D. Mixed inline ZH+EN
  E. Empty template + content appended after

Usage:
  python3 scripts/universal_parser.py file1.docx [file2.docx ...] --output data.js --images-dir images/
"""

import sys, os, re, json, argparse, hashlib, textwrap
from pathlib import Path

try:
    from docx import Document
except ImportError:
    print("ERROR: python-docx not installed."); sys.exit(1)

try:
    from PIL import Image
    HAS_PIL = True
except ImportError:
    HAS_PIL = False

# ─── Config ───
WEBP_QUALITY = 85
MAX_IMAGE_WIDTH = 1600
PHOTO_MAX_WIDTH = 800
PHOTO_MAX_HEIGHT = 1000
PHOTO_QUALITY = 90

# ─── Helpers ───
def has_cjk(s):
    return bool(re.search(r'[\u4e00-\u9fff]', s))

def slugify(text):
    text = re.sub(r'[^\w\s-]', '', text.strip())
    if re.search(r'[\u4e00-\u9fff]', text):
        latin = re.findall(r'[a-zA-Z]+', text)
        if latin: return '-'.join(latin).lower()
        return 'faculty-' + str(abs(hash(text)) % 10000)
    return '-'.join(text.lower().split())

def save_image(blob, dest_path, content_type, max_w=None, max_h=None, quality=WEBP_QUALITY):
    dest = Path(dest_path)
    dest.parent.mkdir(parents=True, exist_ok=True)
    if HAS_PIL and content_type in ('image/png', 'image/jpeg', 'image/jpg'):
        img = Image.open(__import__('io').BytesIO(blob))
        if img.mode in ('RGBA', 'P'): img = img.convert('RGB')
        w, h = img.size
        if max_w and w > max_w:
            ratio = max_w / w
            img = img.resize((int(w*ratio), int(h*ratio)), Image.LANCZOS)
        if max_h and h > max_h:
            ratio = max_h / h
            img = img.resize((int(w*ratio), int(h*ratio)), Image.LANCZOS)
        webp_path = dest.with_suffix('.webp')
        img.save(webp_path, 'webp', quality=quality)
        return webp_path.name
    else:
        ext = content_type.split('/')[-1] if '/' in content_type else 'png'
        if ext == 'jpeg': ext = 'jpg'
        final_path = dest.with_suffix(f'..{ext}')
        with open(final_path, 'wb') as f:
            f.write(blob)
        return final_path.name

def find_image_in_paragraph(para):
    from docx.oxml.ns import qn
    for run in para.runs:
        drawings = run._element.findall('.//' + qn('w:drawing'))
        for d in drawings:
            blip = d.findall('.//' + qn('a:blip'))
            if blip:
                embed = blip[0].get(qn('r:embed'))
                if embed: return embed
    return None

# ─── Section Detection Patterns ───
# All ZH patterns accept optional number prefix: "1. " or "1、" or none
_NP = r'(?:\d+[.、]\s*)?'  # optional number prefix

PAT_NAME_ZH   = re.compile(rf'^{_NP}姓名[：:\s]*')
PAT_NAME_EN   = re.compile(rf'^{_NP}Full\s+name[：:\s]*')
PAT_PHOTO_ZH  = re.compile(rf'^{_NP}个人照片')
PAT_PHOTO_EN  = re.compile(rf'^{_NP}(?:High-resolution\s+)?Personal\s+photo|^Photo\s*$')
PAT_BIO_ZH    = re.compile(rf'^{_NP}个人介绍')
PAT_BIO_EN    = re.compile(rf'^{_NP}Personal\s+Profile')
PAT_WORK_ZH   = re.compile(rf'^{_NP}代表性成果')
PAT_WORK_EN   = re.compile(rf'^{_NP}Representative\s+works')
PAT_COURSE_ZH = re.compile(rf'^{_NP}课程')
PAT_COURSE_EN = re.compile(rf'^{_NP}Courses')
PAT_GALLERY_ZH= re.compile(rf'^{_NP}图片')
PAT_GALLERY_EN= re.compile(rf'^{_NP}Images')

ALL_PAT = [PAT_NAME_ZH, PAT_NAME_EN, PAT_PHOTO_ZH, PAT_PHOTO_EN,
           PAT_BIO_ZH, PAT_BIO_EN, PAT_WORK_ZH, PAT_WORK_EN,
           PAT_COURSE_ZH, PAT_COURSE_EN, PAT_GALLERY_ZH, PAT_GALLERY_EN]

def match_section(text):
    """Return section type or None."""
    t = text.strip()
    for i, pat in enumerate(ALL_PAT):
        if pat.match(t): return i
    return None

SECTION_NAMES = ['name_zh','name_en','photo_zh','photo_en','bio_zh','bio_en',
                 'work_zh','work_en','course_zh','course_en','gallery_zh','gallery_en']

# ─── Main Parser ───
def parse_docx(filepath, images_dir):
    doc = Document(filepath)
    all_paras = [(i, p.text.strip(), p) for i, p in enumerate(doc.paragraphs)]

    result = {
        'id': '', 'name': '', 'name_zh': '', 'name_en': '',
        'photo': '', 'title': '',
        'bio_zh': '', 'bio_en': '',
        'achievements': [], 'courses': [], 'gallery': [],
        'tags': [],
    }

    # ── Phase 1: Extract text sections ──
    current_section = None
    section_data = {}  # section_name -> list of text lines

    for i, text, para in all_paras:
        if not text:
            continue
        sec = match_section(text)
        if sec is not None:
            current_section = SECTION_NAMES[sec]
            section_data.setdefault(current_section, [])
            # Handle inline name: "姓名：娄永琪" or "Full name: Hyejin Lee"
            if current_section in ('name_zh', 'name_en') and ('：' in text or ':' in text):
                inline_name = re.sub(r'^.*?[：:]\s*', '', text).strip()
                if inline_name:
                    section_data[current_section].append(inline_name)
            continue

        if current_section:
            # Check for numbered sub-items (achievements: "1、xxx" or "2、xxx")
            # These break achievements into separate items
            if current_section in ('work_zh', 'work_en'):
                # Check for achievement number prefix
                m = re.match(r'^[（(]?(?:一|二|三|四|五|[1-9])[)）]、?\s*', text)
                if m:
                    section_data[current_section].append(('ITEM_BREAK', text))
                    continue

            section_data[current_section].append(text)

    # ── Phase 2: Process extracted data ──
    # Name
    name_zh_lines = section_data.get('name_zh', [])
    name_en_lines = section_data.get('name_en', [])
    result['name_zh'] = name_zh_lines[0] if name_zh_lines else ''
    result['name_en'] = name_en_lines[0] if name_en_lines else ''

    # If only one name field, try to split
    if result['name_zh'] and not result['name_en']:
        if has_cjk(result['name_zh']):
            # Keep only Latin chars and spaces between them
            latin = re.sub(r'[\u4e00-\u9fff·]+', ' ', result['name_zh']).strip()
            latin = re.sub(r'\s+', ' ', latin).strip()
            if latin:
                result['name_en'] = latin
    elif result['name_en'] and not result['name_zh']:
        zh = re.findall(r'[\u4e00-\u9fff]+', result['name_en'])
        if zh:
            result['name_zh'] = ''.join(zh)

    # Build combined name
    parts = []
    if result['name_en']: parts.append(result['name_en'])
    if result['name_zh'] and result['name_zh'] != result['name_en']:
        parts.append(result['name_zh'])
    result['name'] = ' '.join(parts) if parts else result['name_zh'] or result['name_en']
    result['id'] = slugify(result['name_en'] or result['name_zh'] or 'unknown')

    # Bio
    result['bio_zh'] = ' '.join(section_data.get('bio_zh', []))
    result['bio_en'] = ' '.join(section_data.get('bio_en', []))

    # ── Phase 3: Extract images ──
    # Photo
    photo = extract_photo_from_paras(all_paras, images_dir, result)
    if photo:
        result['photo'] = photo

    # Gallery images
    gallery_entries = extract_gallery_from_paras(all_paras, images_dir)
    # Dedup by content hash
    gallery_entries = dedup_gallery(gallery_entries, images_dir)
    result['gallery'] = gallery_entries

    # ── Phase 4: Process achievements ──
    for lang in ('zh', 'en'):
        raw = section_data.get(f'work_{lang}', [])
        items = []
        current_item = None
        for line in raw:
            if isinstance(line, tuple) and line[0] == 'ITEM_BREAK':
                if current_item:
                    items.append(current_item)
                current_item = {'name': line[1], 'description': '', 'lang': lang}
            elif current_item:
                current_item['description'] += (' ' if current_item['description'] else '') + line
            else:
                # First line is the name
                current_item = {'name': line, 'description': '', 'lang': lang}
        if current_item:
            items.append(current_item)
        result['achievements'].extend(items)

    # Merge ZH+EN achievements
    result['achievements'] = merge_achievements(result['achievements'])

    # ── Phase 5: Process courses ──
    for lang in ('zh', 'en'):
        raw = section_data.get(f'course_{lang}', [])
        # Courses: try to detect course names (usually short lines)
        current_course = None
        for line in raw:
            if not line: continue
            # Heuristic: short lines (< 80 chars) are likely course names
            if len(line) < 80 and current_course:
                # Save previous course
                if current_course['name']:
                    result['courses'].append(current_course)
                current_course = {'name': line, 'description': '', 'lang': lang}
            elif current_course:
                current_course['description'] += ' ' + line
            else:
                current_course = {'name': line, 'description': '', 'lang': lang}
        if current_course and current_course['name']:
            result['courses'].append(current_course)

    # Merge courses
    result['courses'] = merge_courses(result['courses'])

    # ── Phase 6: Build combined bio ──
    bio_parts = []
    if result['bio_zh']: bio_parts.append(result['bio_zh'])
    if result['bio_en'] and result['bio_en'] != result['bio_zh']:
        bio_parts.append(result['bio_en'])
    result['bio'] = '\n'.join(bio_parts) if len(bio_parts) > 1 else (bio_parts[0] if bio_parts else '')

    # ── Phase 7: Extract tags ──
    result['tags'] = extract_tags(result['bio_zh'] + ' ' + result['bio_en'])

    # Clean up internal fields
    for k in ['name_zh', 'name_en', 'bio_zh', 'bio_en']:
        if k in result: result.pop(k)

    return result


def extract_photo_from_paras(all_paras, images_dir, result):
    """Find photo in paragraphs near photo section headers."""
    in_photo = False
    name = result.get('name_en') or result.get('name_zh') or 'unknown'
    seen = set()

    for i, text, para in all_paras:
        if PAT_PHOTO_ZH.match(text) or PAT_PHOTO_EN.match(text):
            in_photo = True
            continue
        if in_photo:
            # Check if we've hit a different section
            sec = match_section(text)
            if sec is not None:
                break
            rid = find_image_in_paragraph(para)
            if rid and rid not in seen:
                seen.add(rid)
                rel = para.part.rels.get(rid)
                if rel and 'image' in rel.reltype:
                    filename = save_image(rel.target_part.blob,
                        os.path.join(images_dir, f'photo-{slugify(name)}'),
                        rel.target_part.content_type,
                        max_w=PHOTO_MAX_WIDTH, max_h=PHOTO_MAX_HEIGHT, quality=PHOTO_QUALITY)
                    return f'images/{filename}'
    return ''


def extract_gallery_from_paras(all_paras, images_dir):
    """Extract gallery images with captions."""
    entries = []
    in_gallery = False
    seen_rids = set()

    for i, text, para in all_paras:
        if PAT_GALLERY_ZH.match(text) or PAT_GALLERY_EN.match(text):
            in_gallery = True
            continue

        if in_gallery:
            sec = match_section(text)
            if sec is not None:
                in_gallery = False
                continue

            rid = find_image_in_paragraph(para)
            if rid and rid not in seen_rids:
                seen_rids.add(rid)
                rel = para.part.rels.get(rid)
                if rel and 'image' in rel.reltype:
                    # Look ahead for caption
                    caption = ''
                    caption_en = ''
                    for j in range(i+1, min(i+6, len(all_paras))):
                        nt = all_paras[j][1].strip()
                        nrid = find_image_in_paragraph(all_paras[j][2])
                        if nrid: break  # next image, stop
                        if not nt: continue
                        nsec = match_section(nt)
                        if nsec is not None: break
                        # Skip "图X:" prefix
                        clean = re.sub(r'^图\d+[：:\s]*', '', nt).strip()
                        clean = re.sub(r'^恩智\s*\d+-\d+[.、]\s*', '', clean).strip()
                        clean = re.sub(r'^Figure\s*\d+[.:\s]*', '', clean).strip()
                        if clean:
                            if not caption:
                                caption = clean
                            elif not caption_en and not has_cjk(clean):
                                caption_en = clean
                            break

                    basename = slugify(caption[:30]) if caption else f'gallery-{len(entries)+1}'
                    filename = save_image(rel.target_part.blob,
                        os.path.join(images_dir, basename),
                        rel.target_part.content_type,
                        max_w=MAX_IMAGE_WIDTH, quality=WEBP_QUALITY)

                    entry = {'src': f'images/{filename}', 'caption': caption}
                    if caption_en: entry['caption_en'] = caption_en
                    entries.append(entry)

    return entries


def dedup_gallery(gallery, images_dir):
    """Dedup gallery by file content hash."""
    seen = {}
    result = []
    for entry in gallery:
        src = entry.get('src', '')
        basename = os.path.basename(src)
        filepath = os.path.join(images_dir, basename)
        try:
            with open(filepath, 'rb') as f:
                fhash = hashlib.md5(f.read()).hexdigest()
        except (FileNotFoundError, IOError):
            fhash = src

        if fhash in seen:
            # Merge captions
            existing = seen[fhash]
            new_cap = entry.get('caption', '')
            old_cap = existing.get('caption', '')
            if has_cjk(old_cap) and not has_cjk(new_cap) and new_cap:
                existing['caption_en'] = new_cap
            elif has_cjk(new_cap) and not has_cjk(old_cap) and old_cap:
                existing['caption'] = new_cap
                existing['caption_en'] = old_cap
            # Remove duplicate file
            try: os.remove(filepath)
            except: pass
        else:
            seen[fhash] = entry
            result.append(entry)
    return result


def merge_achievements(achievements):
    """Merge ZH and EN achievements."""
    zh = [a for a in achievements if a.get('lang') == 'zh']
    en = [a for a in achievements if a.get('lang') == 'en']
    merged = []
    for i, z in enumerate(zh):
        entry = {'name': z['name'], 'description': z['description']}
        if i < len(en):
            e = en[i]
            if e['name'] and e['name'] != z['name']:
                entry['name'] = f"{z['name']} / {e['name']}"
            if e['description'] and e['description'] != z['description']:
                entry['description'] = f"{z['description']}\n\n{e['description']}"
        merged.append(entry)
    if not zh and en:
        merged = [{'name': a['name'], 'description': a['description']} for a in en]
    for m in merged:
        m.pop('lang', None)
    return merged


def merge_courses(courses):
    """Merge ZH and EN courses (simple: combine unique names)."""
    seen_names = set()
    merged = []
    for c in courses:
        name = c.get('name', '')
        if name and name not in seen_names:
            seen_names.add(name)
            merged.append({'name': name, 'description': c.get('description', '')})
    return merged


def extract_tags(bio_text):
    tag_kw = [
        ('Sustainable Design', ['可持续设计', 'sustainable design']),
        ('Social Innovation', ['社会创新', 'social innovation']),
        ('Systemic Design', ['系统设计', 'systemic design']),
        ('Ecosystem Conservation', ['生态系统保护', 'ecosystem conservation']),
        ('Sustainable Healthcare', ['可持续医疗', 'sustainable healthcare', '社区护理']),
        ('Elderly Care', ['老年人照护', 'elderly care', '养老', '老年护理']),
        ('Zero Waste', ['零废弃', 'zero waste', '废物']),
        ('Participatory Design', ['参与式设计', 'participatory design']),
        ('Ecology', ['生态', 'ecology', 'ecological']),
        ('Green Campus', ['绿色校园', 'green campus', '绿色建筑']),
        ('Green Building', ['绿色建筑', 'green building']),
        ('Urban Planning', ['城市规划', 'urban planning']),
        ('Data Visualization', ['数据可视化', 'data visualization']),
        ('Bio-Acoustics', ['声景', 'bio-acoustic', 'sound design']),
        ('More-than-Human', ['more-than-human']),
        ('Community Empowerment', ['社区赋权', 'community empowerment']),
        ('Inclusive Design', ['包容性', 'inclusive design']),
        ('Digital Fabrication', ['数字制造', 'digital fabrication', 'fablab', 'maker']),
        ('Environmental Design', ['环境设计', 'environmental design']),
        ('Sustainability Economics', ['可持续发展经济', 'sustainable development economics']),
        ('Design for Health', ['医疗设计', 'healthcare design', 'transition design']),
        ('Regenerative Design', ['再生设计', 'regenerative design']),
        ('Service Design', ['服务设计', 'service design']),
        ('Design Entrepreneurship', ['社会创业', 'social entrepreneurship']),
        ('Sound Design', ['声音设计', 'sound design']),
        ('Human-AI-Robot Collaboration', ['human-ai', 'robotic', 'hybrid creativity']),
    ]
    tags = []
    bio_lower = bio_text.lower()
    for tag, keywords in tag_kw:
        for kw in keywords:
            if kw.lower() in bio_lower and tag not in tags:
                tags.append(tag)
                break
    return tags


# ─── Main ───
def main():
    parser = argparse.ArgumentParser(description='Universal SDSI docx parser')
    parser.add_argument('files', nargs='+')
    parser.add_argument('--output', '-o', default=None)
    parser.add_argument('--images-dir', '-i', default='images')
    args = parser.parse_args()

    all_data = []
    for fp in args.files:
        if not os.path.exists(fp):
            print(f"ERROR: Not found: {fp}"); continue
        print(f"\n{'='*60}")
        print(f"Processing: {os.path.basename(fp)}")
        print(f"{'='*60}")
        data = parse_docx(fp, args.images_dir)
        print(f"  Name:     {data.get('name','?')}")
        print(f"  ID:       {data.get('id','?')}")
        print(f"  Photo:    {data.get('photo','(none)')}")
        print(f"  Bio:      {len(data.get('bio',''))} chars")
        print(f"  Works:    {len(data.get('achievements',[]))}")
        print(f"  Courses:  {len(data.get('courses',[]))}")
        print(f"  Gallery:  {len(data.get('gallery',[]))}")
        print(f"  Tags:     {', '.join(data.get('tags',[]))}")
        all_data.append(data)

    if args.output:
        js = f'window.__SITE_DATA__ = {json.dumps(all_data, ensure_ascii=False, indent=2)};\n'
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(js)
        print(f"\n  Written to {args.output} ({len(all_data)} records)")
    else:
        print(f"\n{json.dumps(all_data, ensure_ascii=False, indent=2)}")

if __name__ == '__main__':
    main()
