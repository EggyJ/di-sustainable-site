#!/usr/bin/env python3
"""Append remaining 9 faculty to the 4 already in data.js"""
import json, os

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_JS = os.path.join(PROJECT_DIR, "data.js")

with open(DATA_JS, 'r', encoding='utf-8') as f:
    content = f.read()
content = content.replace("window.__SITE_DATA__ = ", "").rstrip().rstrip(";")
data = json.loads(content)
print(f"Currently have {len(data)} faculty")

# Read remaining faculty from a separate JSON file
extra_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "remaining_faculty.json")
with open(extra_file, 'r', encoding='utf-8') as f:
    remaining = json.load(f)

data.extend(remaining)

output = "window.__SITE_DATA__ = " + json.dumps(data, ensure_ascii=False, indent=2) + ";\n"
with open(DATA_JS, 'w', encoding='utf-8') as f:
    f.write(output)

print(f"Written {len(data)} faculty members total")

# Validate
with open(DATA_JS, 'r') as f:
    c = f.read()
c = c.replace("window.__SITE_DATA__ = ", "").rstrip().rstrip(";")
validated = json.loads(c)
print(f"Validated: {len(validated)} faculty members")
for fd in validated:
    print(f"  {fd['name_zh']}: {len(fd['achievements'])} ach, {len(fd['courses'])} courses, {len(fd['gallery'])} gallery")
