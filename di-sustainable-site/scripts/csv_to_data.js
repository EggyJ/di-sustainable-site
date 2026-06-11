#!/usr/bin/env node
/**
 * CSV → data.js Converter (Bilingual ZH/EN)
 * =============================================
 * Reads faculty_data.csv and generates data.js for the website.
 *
 * CSV format (97 columns):
 *   Basic (9): id, name_zh, name_en, title_zh, title_en, photo, bio_zh, bio_en, tags
 *   Works (32): 8 × (name_zh, name_en, desc_zh, desc_en)
 *   Courses (32): 8 × (name_zh, name_en, desc_zh, desc_en)
 *   Gallery (24): 8 × (src, caption_zh, caption_en)
 *
 * Usage:
 *   node scripts/csv_to_data.js                     # default: faculty_data.csv → data.js
 *   node scripts/csv_to_data.js -i data.csv -o out.js
 */

const fs = require('fs');
const path = require('path');

// ─── Parse args ────────────────────────────────────────────
const args = process.argv.slice(2);
let inputFile = 'faculty_data.csv';
let outputFile = 'data.js';
const baseDir = path.resolve(__dirname, '..');

for (let i = 0; i < args.length; i++) {
  if (args[i] === '-i' && args[i + 1]) inputFile = args[++i];
  if (args[i] === '-o' && args[i + 1]) outputFile = args[++i];
}

// ─── Read CSV ───────────────────────────────────────────────
function parseCSV(text) {
  const rows = [];
  let pos = 0;

  function parseField() {
    if (pos >= text.length) return null;
    if (pos === 0 && text.charCodeAt(0) === 0xFEFF) pos = 1;
    if (text[pos] === ',' || text[pos] === '\n' || text[pos] === '\r') {
      if (text[pos] === ',') pos++;
      return '';
    }
    if (text[pos] === '"') {
      pos++;
      let field = '';
      while (pos < text.length) {
        if (text[pos] === '"') {
          if (pos + 1 < text.length && text[pos + 1] === '"') {
            field += '"';
            pos += 2;
          } else {
            pos++;
            break;
          }
        } else {
          field += text[pos];
          pos++;
        }
      }
      if (pos < text.length && text[pos] === ',') pos++;
      return field;
    }
    let field = '';
    while (pos < text.length && text[pos] !== ',' && text[pos] !== '\n' && text[pos] !== '\r') {
      field += text[pos];
      pos++;
    }
    if (pos < text.length && text[pos] === ',') pos++;
    return field;
  }

  function parseRow() {
    const fields = [];
    while (pos < text.length && (text[pos] !== '\n' && text[pos] !== '\r')) {
      const field = parseField();
      if (field === null) return null;
      fields.push(field);
    }
    while (pos < text.length && (text[pos] === '\n' || text[pos] === '\r')) pos++;
    return fields;
  }

  while (pos < text.length) {
    const row = parseRow();
    if (row && row.some(f => f !== '')) rows.push(row);
  }
  return rows;
}

// ─── Process ───────────────────────────────────────────────
const inputPath = path.resolve(inputFile);
const outputPath = path.resolve(outputFile);

if (!fs.existsSync(inputPath)) {
  console.error(`ERROR: File not found: ${inputPath}`);
  process.exit(1);
}

const csvText = fs.readFileSync(inputPath, 'utf-8');
const rows = parseCSV(csvText);
const headers = rows[0] || [];
const dataRows = rows.slice(1);

if (headers.length < 9) {
  console.error(`ERROR: Expected at least 9 columns, got ${headers.length}`);
  console.error('Headers:', headers);
  process.exit(1);
}

const result = [];

for (const row of dataRows) {
  // Column mapping (97 columns):
  // 0: id, 1: name_zh, 2: name_en, 3: title_zh, 4: title_en, 5: photo,
  // 6: bio_zh, 7: bio_en, 8: tags
  // Works: 9-40 (8 × 4 fields)
  // Courses: 41-72 (8 × 4 fields)
  // Gallery: 73-96 (8 × 3 fields)

  const get = (idx) => (idx < row.length ? (row[idx] || '') : '');

  const id = get(0);
  const name_zh = get(1);
  const name_en = get(2);
  const title_zh = get(3);
  const title_en = get(4);
  const photo = get(5);
  const bio_zh = get(6);
  const bio_en = get(7);
  const tagsRaw = get(8);
  const tags = tagsRaw.split('|').map(t => t.trim()).filter(Boolean);

  // Achievements (columns 9-40: 8 works × 4 fields each)
  const achievements = [];
  for (let i = 0; i < 8; i++) {
    const base = 9 + i * 4;
    const nz = get(base);
    const ne = get(base + 1);
    const dz = get(base + 2);
    const de = get(base + 3);
    if (!nz && !ne) continue;
    achievements.push({ name_zh: nz, name_en: ne, description_zh: dz, description_en: de });
  }

  // Courses (columns 41-72: 8 courses × 4 fields each)
  const courses = [];
  for (let i = 0; i < 8; i++) {
    const base = 41 + i * 4;
    const nz = get(base);
    const ne = get(base + 1);
    const dz = get(base + 2);
    const de = get(base + 3);
    if (!nz && !ne) continue;
    courses.push({ name_zh: nz, name_en: ne, description_zh: dz, description_en: de });
  }

  // Gallery (columns 73-96: 8 items × 3 fields each)
  const gallery = [];
  for (let i = 0; i < 8; i++) {
    const base = 73 + i * 3;
    const src = get(base);
    const cap_zh = get(base + 1);
    const cap_en = get(base + 2);
    if (!src) continue;
    gallery.push({ src, caption_zh: cap_zh, caption_en: cap_en });
  }

  // Validate photo exists
  if (photo) {
    const photoPath = path.join(baseDir, photo);
    if (!fs.existsSync(photoPath)) {
      console.warn(`  WARNING: Photo not found: ${photo} (${name_en || name_zh})`);
    }
  }

  // Validate gallery images exist
  for (const g of gallery) {
    if (g.src) {
      const gPath = path.join(baseDir, g.src);
      if (!fs.existsSync(gPath)) {
        console.warn(`  WARNING: Gallery image not found: ${g.src} (${name_en || name_zh})`);
      }
    }
  }

  result.push({
    id, name_zh, name_en, title_zh, title_en, photo,
    bio_zh, bio_en, tags, achievements, courses, gallery,
  });

  console.log(`  ${id}: ${name_en || name_zh} (${achievements.length} works, ${courses.length} courses, ${gallery.length} gallery)`);
}

// Write data.js
const jsContent = `window.__SITE_DATA__ = ${JSON.stringify(result, null, 2)};\n`;
fs.writeFileSync(outputPath, jsContent, 'utf-8');

console.log(`\n  Written to ${outputPath} (${result.length} faculty)`);
