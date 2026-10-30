(() => {
  'use strict';
  const root = document.documentElement;
  const theme = document.querySelector('.theme');
  function setTheme(value) {
    root.dataset.theme = value;
    theme?.setAttribute('aria-pressed', String(value === 'dark'));
  }
  // theme.js restores an explicit choice before first paint; OS preferences do not
  // override the owner's light-first default or a visitor's chosen appearance.
  setTheme(root.dataset.theme === 'dark' ? 'dark' : 'light');
  theme?.addEventListener('click', () => {
    const value = root.dataset.theme === 'dark' ? 'light' : 'dark';
    setTheme(value);
    try { localStorage.setItem('portfolio-theme', value); } catch { /* Preference remains session-local. */ }
  });
  document.querySelector('.reset-theme')?.addEventListener('click', () => {
    try { localStorage.removeItem('portfolio-theme'); } catch { /* Storage can be disabled. */ }
    setTheme('light');
    document.querySelector('.theme-reset-status').textContent = root.lang === 'de' ? 'Gespeicherte Darstellung entfernt. Das helle Design wird verwendet.' : 'Saved theme removed. Using the default light theme.';
  });
  const menu = document.querySelector('.menu-toggle');
  const nav = document.getElementById('mobile-nav');
  function closeMenu() { if (nav) nav.hidden = true; menu?.setAttribute('aria-expanded', 'false'); }
  menu?.addEventListener('click', () => {
    nav.hidden = !nav.hidden;
    menu.setAttribute('aria-expanded', String(!nav.hidden));
  });
  document.addEventListener('click', event => { if (nav && !nav.hidden && !event.target.closest('.header')) closeMenu(); });
  nav?.querySelectorAll('a').forEach(link => link.addEventListener('click', closeMenu));
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && nav && !nav.hidden) { closeMenu(); menu.focus(); }
  });
  window.matchMedia('(min-width: 901px)').addEventListener('change', event => { if (event.matches) closeMenu(); });
  const languageLink = document.querySelector('.language');
  function preserveSection() {
    if (languageLink) languageLink.hash = location.hash;
    document.querySelectorAll('[data-profile]').forEach(link => { link.hash = location.hash; });
  }
  preserveSection();
  window.addEventListener('hashchange', preserveSection);
  const topButton = document.querySelector('.back-to-top');
  if (topButton && 'IntersectionObserver' in window) {
    const sentinel = document.createElement('span');
    sentinel.className = 'scroll-sentinel'; sentinel.setAttribute('aria-hidden', 'true');
    document.body.prepend(sentinel);
    new IntersectionObserver(entries => { topButton.hidden = entries[0].isIntersecting || window.scrollY < 600; }).observe(sentinel);
    const footer = document.querySelector('.footer');
    if (footer) new IntersectionObserver(entries => document.body.classList.toggle('footer-visible', entries[0].isIntersecting)).observe(footer);
  }
  document.querySelectorAll('[data-filter]').forEach(button => {
    button.addEventListener('click', () => {
      document.querySelectorAll('[data-filter]').forEach(other => other.setAttribute('aria-pressed', String(other === button)));
      const archive = document.querySelector('.project-archive');
      if (archive) archive.open = true;
      let count = 0;
      document.querySelectorAll('[data-category]').forEach(project => {
        project.hidden = button.dataset.filter !== 'all' && project.dataset.category !== button.dataset.filter;
        if (!project.hidden) count++;
      });
      const status = document.querySelector('.filter-status');
      if (status) status.textContent = root.lang === 'de' ? `${count} Projekte angezeigt` : `${count} projects shown`;
    });
  });
  function revealContextTarget() {
    let id;
    try { id = decodeURIComponent(location.hash.slice(1)); } catch { return; }
    const target = document.getElementById(id);
    if (!target) return;
    const project = target.closest('[data-category]');
    if (project?.hidden) document.querySelector('[data-filter="all"]')?.click();
    let parent = target.parentElement;
    while (parent) { if (parent.tagName === 'DETAILS') parent.open = true; parent = parent.parentElement; }
  }
  revealContextTarget();
  window.addEventListener('hashchange', revealContextTarget);
  document.querySelectorAll('[data-open-evidence]').forEach(link => link.addEventListener('click', () => {
    const project = link.closest('.project');
    if (project) project.querySelector('.case-details').open = true;
    document.getElementById(link.hash.slice(1))?.focus({preventScroll:true});
  }));
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
  const evidenceQuery = new URLSearchParams(location.search);
  let selected = evidenceQuery.get('category') || 'all';
  if (!filterButtons.some(button => button.dataset.evidenceFilter === selected)) selected = 'all';
  if (input) input.value = evidenceQuery.get('q') || '';
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
    filterButtons.forEach(button => button.setAttribute('aria-pressed', String(button.dataset.evidenceFilter === selected)));
    const params = new URLSearchParams();
    if (selected !== 'all') params.set('category', selected);
    if (input?.value.trim()) params.set('q', input.value.trim());
    const search = params.toString() ? '?' + params.toString() : '';
    history.replaceState(null, '', location.pathname + search + location.hash);
    const languageLink = document.querySelector('.language');
    if (languageLink) languageLink.search = search;
  }
  input?.addEventListener('input', applyEvidenceFilter);
  filterButtons.forEach(button => button.addEventListener('click', () => {
    selected = button.dataset.evidenceFilter;
    filterButtons.forEach(other => other.setAttribute('aria-pressed', String(other === button)));
    applyEvidenceFilter();
  }));
  if (records.length) applyEvidenceFilter();
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
  let decryptedURL = null;
  let unlockVersion = 0;
  const unlockForm = dialog.querySelector('.document-unlock');
  const passwordInput = dialog.querySelector('#document-password');
  const unlockStatus = dialog.querySelector('.unlock-status');
  const imageStage = dialog.querySelector('.viewer-image-stage');
  function clearDocument() {
    unlockVersion++;
    dialog.querySelector('.viewer-image').removeAttribute('src');
    dialog.querySelector('.viewer-original-download').removeAttribute('href');
    dialog.querySelector('.viewer-original-download').hidden = true;
    dialog.querySelector('.viewer-download').hidden = true;
    if (decryptedURL) URL.revokeObjectURL(decryptedURL);
    decryptedURL = null;
    if (passwordInput) passwordInput.value = '';
    if (unlockStatus) unlockStatus.textContent = '';
    if (unlockForm) unlockForm.querySelector('button').disabled = false;
  }
  dialog.querySelector('.viewer-download').addEventListener('click', () => {
    if (!current?.dataset.download) return;
    unlockForm.hidden = false;
    passwordInput.focus();
    unlockForm.scrollIntoView({block:'nearest',behavior:'auto'});
  });
  unlockForm?.addEventListener('submit', async event => {
    event.preventDefault();
    const version = ++unlockVersion;
    const selected = current;
    const password = passwordInput.value;
    passwordInput.value = '';
    const button = unlockForm.querySelector('button');
    button.disabled = true;
    unlockStatus.textContent = lang === 'de' ? 'Dokument wird entschlüsselt…' : 'Decrypting document…';
    try {
      if (!window.isSecureContext || !crypto.subtle) throw Error('WebCrypto unavailable');
      const response = await fetch(selected.dataset.download, {credentials:'omit',cache:'no-store'});
      if (!response.ok) throw Error('Package unavailable');
      const packageText = await response.text();
      if (packageText.length > 16000000) throw Error('Package too large');
      const packet = JSON.parse(packageText);
      if (packet.format !== 'SK-EVIDENCE-v1' || packet.iterations !== 600000 ||
          !/^[a-z0-9-]+\.(webp|svg)$/.test(packet.filename)) throw Error('Invalid package');
      const decode = value => Uint8Array.from(atob(value), c => c.charCodeAt(0));
      const salt = decode(packet.salt), iv = decode(packet.iv);
      if (salt.length !== 16 || iv.length !== 12) throw Error('Invalid parameters');
      const material = await crypto.subtle.importKey('raw', new TextEncoder().encode(password), 'PBKDF2', false, ['deriveKey']);
      const key = await crypto.subtle.deriveKey({name:'PBKDF2',salt,iterations:600000,hash:'SHA-256'},material,{name:'AES-GCM',length:256},false,['decrypt']);
      const data = await crypto.subtle.decrypt({name:'AES-GCM',iv,additionalData:new TextEncoder().encode('SK-EVIDENCE-v1:'+packet.filename),tagLength:128},key,decode(packet.ciphertext));
      if (version !== unlockVersion || !dialog.open || current !== selected) return;
      decryptedURL = URL.createObjectURL(new Blob([data], {type:packet.filename.endsWith('.svg')?'image/svg+xml':'image/webp'}));
      const download = dialog.querySelector('.viewer-original-download');
      download.href = decryptedURL; download.download = packet.filename; download.hidden = false;
      imageStage.hidden = false; unlockForm.hidden = true;
      dialog.querySelector('.viewer-download').hidden = true;
      dialog.querySelector('.viewer-close').focus();
    } catch {
      if (version === unlockVersion) {
        unlockStatus.textContent = lang === 'de' ? 'Entsperren nicht möglich. Passwort prüfen oder Zugang per E-Mail anfragen.' : 'Unable to unlock. Check the password or request access by email.';
        passwordInput.focus();
      }
    } finally { if (version === unlockVersion) button.disabled = false; }
  });
  dialog.addEventListener('close', clearDocument);
  function setZoom(level) { zoomLevel=Math.max(1,Math.min(4,level));const img=dialog.querySelector('.viewer-image');img.style.width=(zoomLevel*100)+'%';img.style.maxWidth='none';img.style.maxHeight=zoomLevel===1?'68dvh':'none';img.style.objectFit='contain'; }
  dialog.querySelector('.viewer-zoom-in').addEventListener('click',()=>setZoom(zoomLevel+.5));
  dialog.querySelector('.viewer-zoom-out').addEventListener('click',()=>setZoom(zoomLevel-.5));
  dialog.querySelector('.viewer-fit').addEventListener('click',()=>setZoom(1));
  function show(link) {
    clearDocument();
    current = link;
    setZoom(1);
    const caption = link.dataset.caption || link.querySelector('img')?.alt || '';
    if (unlockForm) unlockForm.hidden = true;
    imageStage.hidden = false;
    dialog.querySelector('.viewer-image').src = link.href;
    dialog.querySelector('.viewer-image').alt = caption;
    dialog.querySelector('#viewer-caption').textContent = caption;
    dialog.querySelector('.viewer-download').hidden = !link.dataset.download;
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
    if (event.target.matches('input')) return;
    if (event.key === '+') { event.preventDefault(); setZoom(zoomLevel+.5); }
    if (event.key === '-') { event.preventDefault(); setZoom(zoomLevel-.5); }
    if (event.key === '0') { event.preventDefault(); setZoom(1); }
    if (event.key === 'ArrowRight') { event.preventDefault(); step(1); }
    if (event.key === 'ArrowLeft') { event.preventDefault(); step(-1); }
  });
  dialog.addEventListener('click', event => { if (event.target === dialog) dialog.close(); });
})();
