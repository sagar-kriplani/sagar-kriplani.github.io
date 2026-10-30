/* Apply an explicit visitor choice before styles paint. New visitors start in light. */
(() => {
  let theme = 'light';
  try {
    const saved = localStorage.getItem('portfolio-theme');
    if (saved === 'light' || saved === 'dark') theme = saved;
  } catch { /* Light remains the default when browser storage is unavailable. */ }
  document.documentElement.dataset.theme = theme;
})();
