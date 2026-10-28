(() => {
  'use strict';
  const root = document.documentElement;
  const theme = document.querySelector('.theme');
  function setTheme(value) {
    root.dataset.theme = value;
    theme?.setAttribute('aria-pressed', String(value === 'dark'));
  }
  let saved;
  try { saved = localStorage.getItem('portfolio-theme'); } catch { /* Storage can be disabled. */ }
  const preference = window.matchMedia('(prefers-color-scheme: dark)');
  setTheme(saved === 'light' || saved === 'dark' ? saved : preference.matches ? 'dark' : 'light');
  theme?.addEventListener('click', () => {
    saved = root.dataset.theme === 'dark' ? 'light' : 'dark';
    setTheme(saved);
    try { localStorage.setItem('portfolio-theme', saved); } catch { /* Preference remains session-local. */ }
  });
  preference.addEventListener('change', event => { if (!saved) setTheme(event.matches ? 'dark' : 'light'); });
  const menu = document.querySelector('.menu-toggle');
  const nav = document.getElementById('mobile-nav');
  function closeMenu() { if (nav) nav.hidden = true; menu?.setAttribute('aria-expanded', 'false'); }
  menu?.addEventListener('click', () => {
    nav.hidden = !nav.hidden;
    menu.setAttribute('aria-expanded', String(!nav.hidden));
  });
  nav?.querySelectorAll('a').forEach(link => link.addEventListener('click', closeMenu));
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && nav && !nav.hidden) { closeMenu(); menu.focus(); }
  });
  window.matchMedia('(min-width: 761px)').addEventListener('change', event => { if (event.matches) closeMenu(); });
  document.querySelectorAll('[data-filter]').forEach(button => {
    button.addEventListener('click', () => {
      document.querySelectorAll('[data-filter]').forEach(other => other.setAttribute('aria-pressed', String(other === button)));
      let count = 0;
      document.querySelectorAll('[data-category]').forEach(project => {
        project.hidden = button.dataset.filter !== 'all' && project.dataset.category !== button.dataset.filter;
        if (!project.hidden) count++;
      });
      const status = document.querySelector('.filter-status');
      if (status) status.textContent = root.lang === 'de' ? `${count} Projekte angezeigt` : `${count} projects shown`;
    });
  });
  document.querySelector('.copy-email')?.addEventListener('click', async event => {
    const status = document.querySelector('.copy-status');
    const copiedMessage = event.currentTarget.dataset.copied;
    try {
      await navigator.clipboard.writeText('sagar.kriplani@outlook.com');
      status.textContent = copiedMessage;
    } catch {
      status.textContent = root.lang === 'de' ? 'Bitte Adresse auswählen und kopieren: sagar.kriplani@outlook.com' : 'Select and copy: sagar.kriplani@outlook.com';
    }
  });
  document.querySelector('.print-cv')?.addEventListener('click', () => window.print());
})();

(() => {
  'use strict';
  const lang = document.documentElement.lang;
  const input = document.getElementById('evidence-search');
  const records = [...document.querySelectorAll('[data-evidence-category]')];
  const filterButtons = [...document.querySelectorAll('[data-evidence-filter]')];
  let selected = 'all';
  function applyEvidenceFilter() {
    const query = (input?.value || '').trim().toLocaleLowerCase(lang);
    let count = 0;
    records.forEach(record => {
      const categoryMatches = selected === 'all' || record.dataset.evidenceCategory === selected;
      const searchMatches = record.textContent.toLocaleLowerCase(lang).includes(query);
      record.hidden = !(categoryMatches && searchMatches);
      if (!record.hidden) count++;
    });
    const status = document.querySelector('.evidence-count');
    if (status) status.textContent = `${count} ${lang === 'de' ? 'Nachweise' : 'records'}`;
    const empty = document.querySelector('.evidence-empty');
    if (empty) empty.hidden = count !== 0;
  }
  input?.addEventListener('input', applyEvidenceFilter);
  filterButtons.forEach(button => button.addEventListener('click', () => {
    selected = button.dataset.evidenceFilter;
    filterButtons.forEach(other => other.setAttribute('aria-pressed', String(other === button)));
    applyEvidenceFilter();
  }));
  const galleryCards = [...document.querySelectorAll('[data-gallery-group]')];
  if (galleryCards.length) {
    const filters = [...document.querySelectorAll('[data-gallery-filter]')];
    const more = document.getElementById('gallery-more');
    let selected = new URLSearchParams(location.search).get('project') || 'all';
    if (!filters.some(b => b.dataset.galleryFilter === selected)) selected = 'all';
    let limit = 12;
    function updateGallery() {
      const matches = galleryCards.filter(c => selected === 'all' || c.dataset.galleryGroup === selected);
      galleryCards.forEach(c => { c.hidden = true; });
      matches.slice(0, limit).forEach(c => { c.hidden = false; });
      filters.forEach(b => b.setAttribute('aria-pressed', String(b.dataset.galleryFilter === selected)));
      more.hidden = limit >= matches.length;
      document.querySelector('.gallery-status').textContent = `${Math.min(limit, matches.length)} / ${matches.length} ${lang === 'de' ? 'Abbildungen' : 'figures'}`;
      const query = selected === 'all' ? '' : '?project=' + encodeURIComponent(selected);
      history.replaceState(null, '', location.pathname + query);
      const languageLink = document.querySelector('.language');
      if (languageLink) languageLink.search = query;
    }
    filters.forEach(b => b.addEventListener('click', () => { selected=b.dataset.galleryFilter;limit=12;updateGallery(); }));
    more.addEventListener('click', () => { limit+=12;updateGallery(); });
    updateGallery();
  }
  const dialog = document.querySelector('.document-viewer');
  if (!dialog || typeof dialog.showModal !== 'function') return;
  const links = [...document.querySelectorAll('a[data-viewer]')];
  let current = null;
  let zoomLevel = 1;
  function setZoom(level) { zoomLevel=Math.max(1,Math.min(4,level));const img=dialog.querySelector('.viewer-image');img.style.width=(zoomLevel*100)+'%';img.style.maxWidth='none';img.style.maxHeight=zoomLevel===1?'68dvh':'none';img.style.objectFit='contain'; }
  dialog.querySelector('.viewer-zoom-in').addEventListener('click',()=>setZoom(zoomLevel+.5));
  dialog.querySelector('.viewer-zoom-out').addEventListener('click',()=>setZoom(zoomLevel-.5));
  dialog.querySelector('.viewer-fit').addEventListener('click',()=>setZoom(1));
  function show(link) {
    current = link;
    setZoom(1);
    const caption = link.dataset.caption || link.querySelector('img')?.alt || '';
    dialog.querySelector('.viewer-image').src = link.href;
    dialog.querySelector('.viewer-image').alt = caption;
    dialog.querySelector('#viewer-caption').textContent = caption;
    dialog.querySelector('.viewer-download').href = link.href;
    if (!dialog.open) dialog.showModal();
    dialog.scrollTop = 0;
  }
  function step(direction) {
    const visible = links.filter(link => !link.closest('[hidden]'));
    const index = visible.indexOf(current);
    if (visible.length) show(visible[(index + direction + visible.length) % visible.length]);
  }
  links.forEach(link => link.addEventListener('click', event => { event.preventDefault(); show(link); }));
  dialog.querySelector('.viewer-close').addEventListener('click', () => dialog.close());
  dialog.querySelector('.viewer-prev').addEventListener('click', () => step(-1));
  dialog.querySelector('.viewer-next').addEventListener('click', () => step(1));
  dialog.addEventListener('keydown', event => {
    if (event.key === '+') { event.preventDefault(); setZoom(zoomLevel+.5); }
    if (event.key === '-') { event.preventDefault(); setZoom(zoomLevel-.5); }
    if (event.key === '0') { event.preventDefault(); setZoom(1); }
    if (event.key === 'ArrowRight') { event.preventDefault(); step(1); }
    if (event.key === 'ArrowLeft') { event.preventDefault(); step(-1); }
  });
  dialog.addEventListener('click', event => { if (event.target === dialog) dialog.close(); });
})();
