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
