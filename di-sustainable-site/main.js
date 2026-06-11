/* ─── Shared JS: Language System, Data, Detail View ─── */
/* Loaded by index.html, faculty.html, projects.html, courses.html */

let __LANG = 'zh';
window.__SHOW_ALL_PROJECTS = false;

/* --- Translation --- */
const T = (key) => ({
  nav_home:     __LANG==='zh'?'首页':'Home',
  nav_projects: __LANG==='zh'?'项目':'Projects',
  nav_faculty:  __LANG==='zh'?'教师':'Faculty',
  nav_courses:  __LANG==='zh'?'课程':'Courses',
  metric_faculty: __LANG==='zh'?'教师':'Faculty',
  metric_projects: __LANG==='zh'?'项目':'Projects',
  metric_courses:  __LANG==='zh'?'课程':'Courses',
  sec_works:    __LANG==='zh'?'代表性成果':'Selected Work',
  sec_courses:  __LANG==='zh'?'课程':'Courses',
  sec_gallery:  __LANG==='zh'?'图片':'Gallery',
  label_faculty: __LANG==='zh'?'教师':'Faculty',
  label_course:  __LANG==='zh'?'课程':'Course',
  no_projects:  __LANG==='zh'?'暂无项目':'No projects yet',
  no_faculty:   __LANG==='zh'?'暂无教师':'No faculty yet',
  no_courses:   __LANG==='zh'?'暂无课程':'No courses yet',
  untitled:     __LANG==='zh'?'未命名':'Untitled',
  projects_suffix: __LANG==='zh'?'个项目':' projects',
  members_suffix:  __LANG==='zh'?'位成员':' members',
  courses_suffix:  __LANG==='zh'?'门课程':' courses',
  show_all_projects: __LANG==='zh'?'全部项目 \u2192':'View All Projects \u2192',
  show_featured:     __LANG==='zh'?'\u2190 精选案例':'\u2190 Featured Cases',
  view_all_projects: __LANG==='zh'?'查看全部项目 \u2192':'View All Projects \u2192',
  view_all_faculty:  __LANG==='zh'?'查看全部教师 \u2192':'View All Faculty \u2192',
  view_all_courses:  __LANG==='zh'?'查看全部课程 \u2192':'View All Courses \u2192',
  no_bio:           __LANG==='zh'?'暂无简介':'No bio yet.',
  back_to_list:     __LANG==='zh'?'\u2190 返回列表':'\u2190 Back to List',
  detail_project:   __LANG==='zh'?'项目详情':'Project Detail',
  detail_course:    __LANG==='zh'?'课程详情':'Course Detail',
  about_faculty:    __LANG==='zh'?'关于教师':'About Faculty',
  related_projects: __LANG==='zh'?'相关项目':'Related Projects',
  related_courses:  __LANG==='zh'?'相关课程':'Related Courses',
  view_faculty:     __LANG==='zh'?'查看教师主页 \u2192':'View Faculty Profile \u2192',
})[key] || key;

function langField(obj, field){
  const zh = obj[field+'_zh'] || '';
  const en = obj[field+'_en'] || '';
  return __LANG==='zh' ? (zh || en) : (en || zh);
}

function setLang(lang){
  __LANG = lang;
  document.documentElement.lang = lang === 'zh' ? 'zh-CN' : 'en';
  document.querySelectorAll('#lang-toggle .lang-btn').forEach(b=>{
    b.classList.toggle('active', b.dataset.lang === lang);
  });
  document.querySelectorAll('[data-lang-zh]').forEach(el=>{
    const text = lang === 'zh' ? el.dataset.langZh : el.dataset.langEn;
    if(text) el.innerHTML = text;
  });
  document.querySelectorAll('[data-t]').forEach(el=>{
    el.textContent = T(el.dataset.t);
  });
  // Re-render current page
  if(typeof renderPage === 'function') renderPage();
  closeDetail();
}

/* --- Data --- */
function getData(){
  if(window.__SITE_DATA__) return window.__SITE_DATA__;
  try{ return JSON.parse(localStorage.getItem('di_faculty')) || [] }
  catch(e){ return [] }
}
function getFeaturedProjects(){
  if(window.__FEATURED_PROJECTS__) return window.__FEATURED_PROJECTS__;
  return [];
}

/* --- Utilities --- */
function getInitials(name){ return name ? name.charAt(0) : '?' }
function esc(s){ return (s||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;') }

/* --- Detail View (shared) --- */
function openDetail(id){
  const data = getData();
  const f = data.find(x=>x.id===id);
  if(!f) return;
  const name = f.name_zh || f.name_en || T('untitled');
  const title = __LANG==='zh' ? (f.title_zh||f.title_en) : (f.title_en||f.title_zh);
  const bio = langField(f,'bio');
  const c = document.getElementById('detail-content');
  c.innerHTML = `
    <div class="detail-top">
      <div class="detail-photo">
        ${f.photo ? `<img src="${f.photo}" alt="${esc(name)}">` : `<div class="placeholder">${getInitials(name)}</div>`}
      </div>
      <div class="detail-meta">
        <h1>${esc(name)}</h1>
        <div class="title">${esc(title)||''}</div>
        <div class="detail-tags">${(f.tags||[]).map(t=>`<span class="tag">${esc(t)}</span>`).join('')}</div>
        ${bio ? `<div class="bio" style="margin-top:20px">${esc(bio)}</div>` : `<div class="bio" style="margin-top:20px;color:var(--color-text-muted)">${T('no_bio')}</div>`}
      </div>
    </div>
    ${(f.achievements||[]).length ? `
    <div class="detail-section">
      <h2>${T('sec_works')}</h2>
      ${(f.achievements||[]).map(a=>`<div class="achievement-card"><h3>${esc(langField(a,'name'))}</h3><p>${esc(langField(a,'description'))}</p></div>`).join('')}
    </div>` : ''}
    ${(f.courses||[]).length ? `
    <div class="detail-section">
      <h2>${T('sec_courses')}</h2>
      ${(f.courses||[]).map(c=>`<div class="course-card"><h3>${esc(langField(c,'name'))}</h3><p>${esc(langField(c,'description'))}</p></div>`).join('')}
    </div>` : ''}
    ${(f.gallery||[]).length ? `
    <div class="detail-section">
      <h2>${T('sec_gallery')}</h2>
      <div class="gallery-grid">
        ${(f.gallery||[]).map(g=>{
          const cap = langField(g,'caption');
          return `<div class="gallery-item"><img src="${g.src}" alt="${esc(cap)}" loading="lazy">${cap ? `<div class="caption">${esc(cap)}</div>` : ''}</div>`;
        }).join('')}
      </div>
    </div>` : ''}
  `;
  document.getElementById('detail-overlay').classList.add('active');
  document.body.style.overflow = 'hidden';
}

function closeDetail(){
  document.getElementById('detail-overlay').classList.remove('active');
  document.body.style.overflow = '';
}
document.addEventListener('keydown', e=>{ if(e.key==='Escape') closeDetail() });

/* --- Project Detail View --- */
function openProjectDetail(facultyId, achIndex){
  const data = getData();
  const f = data.find(x=>x.id===facultyId);
  if(!f || !f.achievements || !f.achievements[achIndex]) return;
  const a = f.achievements[achIndex];
  const achName = langField(a,'name');
  const achDesc = langField(a,'description');
  const fName = f.name_zh || f.name_en;
  const fTitle = __LANG==='zh' ? (f.title_zh||f.title_en) : (f.title_en||f.title_zh);
  const otherAch = (f.achievements||[]).filter((_,i)=>i!==achIndex);
  const c = document.getElementById('detail-content');
  c.innerHTML = `
    <div class="breadcrumb-bar">
      <a href="javascript:void(0)" onclick="closeDetail()" class="breadcrumb-back">${T('back_to_list')}</a>
      <span class="breadcrumb-label">${T('detail_project')}</span>
    </div>
    <div class="item-detail-hero">
      <h1 class="item-detail-title">${esc(achName)}</h1>
      ${achDesc ? `<div class="item-detail-desc">${esc(achDesc)}</div>` : ''}
    </div>
    <div class="item-detail-faculty-bar" onclick="openDetail('${f.id}')" style="cursor:pointer">
      <div class="faculty-bar-left">
        ${f.photo ? `<div class="faculty-bar-avatar"><img src="${f.photo}" alt="${esc(fName)}"></div>` : `<div class="faculty-bar-avatar placeholder-avatar">${getInitials(fName)}</div>`}
        <div>
          <div class="faculty-bar-name">${esc(fName)}</div>
          <div class="faculty-bar-title">${esc(fTitle)||''}</div>
        </div>
      </div>
      <span class="faculty-bar-link">${T('view_faculty')}</span>
    </div>
    ${otherAch.length ? `
    <div class="detail-section">
      <h2>${T('related_projects')}</h2>
      ${otherAch.map(a=>`<div class="achievement-card"><h3>${esc(langField(a,'name'))}</h3><p>${esc(langField(a,'description'))}</p></div>`).join('')}
    </div>` : ''}
  `;
  document.getElementById('detail-overlay').classList.add('active');
  document.body.style.overflow = 'hidden';
  window.scrollTo(0,0);
  document.getElementById('detail-overlay').scrollTo(0,0);
}

/* --- Course Detail View --- */
function openCourseDetail(facultyId, crsIndex){
  const data = getData();
  const f = data.find(x=>x.id===facultyId);
  if(!f || !f.courses || !f.courses[crsIndex]) return;
  const crs = f.courses[crsIndex];
  const crsName = langField(crs,'name');
  const crsDesc = langField(crs,'description');
  const fName = f.name_zh || f.name_en;
  const fTitle = __LANG==='zh' ? (f.title_zh||f.title_en) : (f.title_en||f.title_zh);
  const otherCrs = (f.courses||[]).filter((_,i)=>i!==crsIndex);
  const c = document.getElementById('detail-content');
  c.innerHTML = `
    <div class="breadcrumb-bar">
      <a href="javascript:void(0)" onclick="closeDetail()" class="breadcrumb-back">${T('back_to_list')}</a>
      <span class="breadcrumb-label">${T('detail_course')}</span>
    </div>
    <div class="item-detail-hero">
      <h1 class="item-detail-title">${esc(crsName)}</h1>
      ${crsDesc ? `<div class="item-detail-desc">${esc(crsDesc)}</div>` : ''}
    </div>
    <div class="item-detail-faculty-bar" onclick="openDetail('${f.id}')" style="cursor:pointer">
      <div class="faculty-bar-left">
        ${f.photo ? `<div class="faculty-bar-avatar"><img src="${f.photo}" alt="${esc(fName)}"></div>` : `<div class="faculty-bar-avatar placeholder-avatar">${getInitials(fName)}</div>`}
        <div>
          <div class="faculty-bar-name">${esc(fName)}</div>
          <div class="faculty-bar-title">${esc(fTitle)||''}</div>
        </div>
      </div>
      <span class="faculty-bar-link">${T('view_faculty')}</span>
    </div>
    ${(f.achievements||[]).length ? `
    <div class="detail-section">
      <h2>${T('related_projects')}</h2>
      ${(f.achievements||[]).map(a=>`<div class="achievement-card"><h3>${esc(langField(a,'name'))}</h3><p>${esc(langField(a,'description'))}</p></div>`).join('')}
    </div>` : ''}
    ${otherCrs.length ? `
    <div class="detail-section">
      <h2>${T('related_courses')}</h2>
      ${otherCrs.map(cr=>`<div class="course-card"><h3>${esc(langField(cr,'name'))}</h3><p>${esc(langField(cr,'description'))}</p></div>`).join('')}
    </div>` : ''}
  `;
  document.getElementById('detail-overlay').classList.add('active');
  document.body.style.overflow = 'hidden';
  window.scrollTo(0,0);
  document.getElementById('detail-overlay').scrollTo(0,0);
}

/* --- Nav active state helper --- */
function setActiveNav(page){
  document.querySelectorAll('.nav-links a').forEach(a=>{
    a.classList.toggle('active', a.dataset.page === page);
  });
}

/* --- Featured Project Detail View (multi-faculty) --- */
function openFeaturedProjectDetail(projectId){
  const projects = getFeaturedProjects();
  const data = getData();
  const p = projects.find(x=>x.id===projectId);
  if(!p) return;
  const pName = __LANG==='zh' ? p.name_zh : p.name_en;
  const pDesc = __LANG==='zh' ? p.description_zh : p.description_en;
  // Resolve faculty members
  const faculties = p.faculty_ids.map(id=>data.find(x=>x.id===id)).filter(Boolean);
  const c = document.getElementById('detail-content');
  c.innerHTML = `
    <div class="breadcrumb-bar">
      <a href="javascript:void(0)" onclick="closeDetail()" class="breadcrumb-back">${T('back_to_list')}</a>
      <span class="breadcrumb-label">${T('detail_project')}</span>
    </div>
    <div class="item-detail-hero">
      <h1 class="item-detail-title">${esc(pName)}</h1>
      ${pDesc ? `<div class="item-detail-desc">${esc(pDesc)}</div>` : ''}
    </div>
    ${p.images.length ? `
    <div class="detail-section">
      <h2>${__LANG==='zh'?'项目图片':'Project Gallery'}</h2>
      <div class="featured-img-grid">
        ${p.images.map(im=>`<div class="featured-img-item"><img src="${im.src}" alt="${esc(pName)}" loading="lazy"></div>`).join('')}
      </div>
    </div>` : ''}
    ${faculties.length ? `
    <div class="detail-section">
      <h2>${__LANG==='zh'?'相关教师':'Related Faculty'}</h2>
      <div class="featured-faculty-list">
        ${faculties.map(f=>{
          const fName = f.name_zh || f.name_en || '';
          const fTitle = __LANG==='zh' ? (f.title_zh||f.title_en) : (f.title_en||f.title_zh);
          return `<div class="featured-faculty-card" onclick="openDetail('${f.id}')">
            <div class="ffc-avatar">${f.photo ? `<img src="${f.photo}" alt="${esc(fName)}">` : `<span>${getInitials(fName)}</span>`}</div>
            <div class="ffc-info">
              <div class="ffc-name">${esc(fName)}</div>
              <div class="ffc-title">${esc(fTitle)||''}</div>
            </div>
            <span class="ffc-link">\u2192</span>
          </div>`;
        }).join('')}
      </div>
    </div>` : ''}
  `;
  document.getElementById('detail-overlay').classList.add('active');
  document.body.style.overflow = 'hidden';
  window.scrollTo(0,0);
  document.getElementById('detail-overlay').scrollTo(0,0);
}
