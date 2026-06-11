#!/usr/bin/env node
/**
 * data.js → CSV Exporter (Bilingual ZH/EN)
 * ========================================
 * Reads data.js and exports to faculty_data.csv (97-column format).
 *
 * CSV format (97 columns):
 *   Basic (9): id, name_zh, name_en, title_zh, title_en, photo, bio_zh, bio_en, tags
 *   Works (32): 8 × (name_zh, name_en, desc_zh, desc_en)
 *   Courses (32): 8 × (name_zh, name_en, desc_zh, desc_en)
 *   Gallery (24): 8 × (src, caption_zh, caption_en)
 */

const fs = require('fs');
const path = require('path');

const baseDir = path.resolve(__dirname, '..');

// Parse data.js
const dataJs = fs.readFileSync(path.join(baseDir, 'data.js'), 'utf-8');
const eqIdx = dataJs.indexOf('=');
const jsonStr = dataJs.substring(eqIdx + 1).trim().replace(/;\s*$/, '');
const data = JSON.parse(jsonStr);

// CSV helpers
function escField(val) {
  if (val == null) return '';
  const s = String(val);
  if (s.includes('"') || s.includes(',') || s.includes('\n') || s.includes('\r')) {
    return '"' + s.replace(/"/g, '""') + '"';
  }
  return s;
}

// Build header row
const header = [
  'id', 'name_zh', 'name_en', 'title_zh', 'title_en', 'photo', 'bio_zh', 'bio_en', 'tags',
  // Works: 8 × 4
  ...Array.from({length: 8}, (_, i) => `work${i+1}_name_zh`),
  ...Array.from({length: 8}, (_, i) => `work${i+1}_name_en`),
  ...Array.from({length: 8}, (_, i) => `work${i+1}_desc_zh`),
  ...Array.from({length: 8}, (_, i) => `work${i+1}_desc_en`),
  // Courses: 8 × 4
  ...Array.from({length: 8}, (_, i) => `course${i+1}_name_zh`),
  ...Array.from({length: 8}, (_, i) => `course${i+1}_name_en`),
  ...Array.from({length: 8}, (_, i) => `course${i+1}_desc_zh`),
  ...Array.from({length: 8}, (_, i) => `course${i+1}_desc_en`),
  // Gallery: 8 × 3
  ...Array.from({length: 8}, (_, i) => `gallery${i+1}_src`),
  ...Array.from({length: 8}, (_, i) => `gallery${i+1}_caption_zh`),
  ...Array.from({length: 8}, (_, i) => `gallery${i+1}_caption_en`),
];
console.log('Header columns:', header.length);

// Build data rows
const rows = data.map(f => {
  const row = [
    f.id,
    f.name_zh || '',
    f.name_en || '',
    f.title_zh || '',
    f.title_en || '',
    f.photo || '',
    f.bio_zh || '',
    f.bio_en || '',
    (f.tags || []).join(';'),
  ];

  // Works: 8 slots × 4 fields
  for (let i = 0; i < 8; i++) {
    const a = (f.achievements || [])[i] || {};
    row.push(escField(a.name_zh), escField(a.name_en), escField(a.description_zh), escField(a.description_en));
  }

  // Courses: 8 slots × 4 fields
  for (let i = 0; i < 8; i++) {
    const c = (f.courses || [])[i] || {};
    row.push(escField(c.name_zh), escField(c.name_en), escField(c.description_zh), escField(c.description_en));
  }

  // Gallery: 8 slots × 3 fields
  for (let i = 0; i < 8; i++) {
    const g = (f.gallery || [])[i] || {};
    row.push(escField(g.src), escField(g.caption_zh), escField(g.caption_en));
  }

  return row;
});

// Write CSV with UTF-8 BOM
const bom = '\uFEFF';
const csvContent = bom + header.map(escField).join(',') + '\n' +
  rows.map(r => r.map(escField).join(',')).join('\n') + '\n';

const outPath = path.join(baseDir, 'faculty_data.csv');
fs.writeFileSync(outPath, csvContent, 'utf-8');

console.log(`Exported ${data.length} faculty to ${outPath}`);
console.log(`Columns: ${header.length}`);

// Stats
let totalWorks = 0, totalCourses = 0, totalGallery = 0;
data.forEach(f => {
  totalWorks += (f.achievements || []).length;
  totalCourses += (f.courses || []).length;
  totalGallery += (f.gallery || []).length;
});
console.log(`Total: ${totalWorks} works, ${totalCourses} courses, ${totalGallery} gallery items`);
