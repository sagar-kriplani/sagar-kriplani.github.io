/* Dependency-free, progressively enhanced engineering carousel. */
(() => {
  'use strict';
  document.querySelectorAll('[data-showcase]').forEach(carousel => {
    const slides = [...carousel.querySelectorAll('[data-showcase-slide]')];
    if (slides.length < 2) return;
    const indicators = [...carousel.querySelectorAll('[data-showcase-go]')];
    const play = carousel.querySelector('[data-showcase-play]');
    const reduced = matchMedia('(prefers-reduced-motion: reduce)');
    const viewer = document.querySelector('.document-viewer');
    let index = 0;
    let userPaused = reduced.matches;
    let keyboardPaused = false;
    let keyboardInput = false;
    let ignoreHover = false;
    let hovered = false;
    let visible = false;
    let timer;
    let playPointerIntent;
    const interval = 6000;
    const announcement = carousel.querySelector('.showcase-announcement');

    function updatePlayback() {
      clearTimeout(timer);
      let reason = 'playing';
      if (userPaused) reason = reduced.matches ? 'reduced' : 'paused';
      else if (keyboardPaused || viewer?.open) reason = 'focus';
      else if (document.hidden) reason = 'hidden';
      else if (!visible) reason = 'ready';
      else if (hovered && !ignoreHover) reason = 'hover';
      const playing = reason === 'playing';
      carousel.dataset.playing = String(playing);
      carousel.dataset.playbackReason = reason;
      play.setAttribute('aria-label', playing ? carousel.dataset.pauseLabel : carousel.dataset.playLabel);
      play.querySelector('[data-showcase-play-icon]').textContent = playing ? 'Ⅱ' : '▷';
      carousel.querySelector('[data-showcase-state]').textContent = carousel.dataset[reason + 'Label'] || carousel.dataset.pausedLabel;
      // A full reading interval restarts after a temporary pause.
      if (playing) timer = setTimeout(() => show(index + 1, false), interval);
    }

    function show(next, manual = true) {
      index = (next + slides.length) % slides.length;
      // Pointer controls and swipes restart the full reading interval, without permanently
      // turning off autoplay. Keyboard exploration stays paused until explicitly resumed.
      if (manual && keyboardInput) keyboardPaused = true;
      slides.forEach((slide, i) => {
        const active = i === index;
        const previous = i === (index - 1 + slides.length) % slides.length;
        const following = i === (index + 1) % slides.length;
        slide.hidden = !(active || previous || following);
        slide.inert = !active;
        slide.setAttribute('aria-hidden', String(!active));
        slide.classList.toggle('is-current', active);
        slide.classList.toggle('is-previous', previous);
        slide.classList.toggle('is-next', following);
        // Keep the shared document viewer's navigation limited to visible slide controls.
        slide.querySelector('.showcase-zoom').hidden = !active;
        indicators[i].setAttribute('aria-pressed', String(active));
      });
      carousel.querySelector('[data-showcase-count]').textContent = String(index + 1).padStart(2, '0');
      // Autoplay never writes to the live region or moves keyboard focus.
      if (manual) announcement.textContent = slides[index].getAttribute('aria-label');
      updatePlayback();
    }

    carousel.querySelector('.showcase-controls').hidden = false;
    carousel.querySelector('.showcase-help').hidden = false;
    carousel.classList.add('is-enhanced');
    carousel.querySelector('[data-showcase-prev]').addEventListener('click', () => show(index - 1));
    carousel.querySelector('[data-showcase-next]').addEventListener('click', () => show(index + 1));
    indicators.forEach(button => button.addEventListener('click', () => show(Number(button.dataset.showcaseGo))));
    play.addEventListener('pointerdown', () => { playPointerIntent = carousel.dataset.playing !== 'true'; });
    play.addEventListener('click', () => {
      const wantsPlay = playPointerIntent ?? (carousel.dataset.playing !== 'true');
      userPaused = !wantsPlay;
      if (wantsPlay) { keyboardPaused = false; ignoreHover = true; }
      playPointerIntent = undefined;
      updatePlayback();
    });
    document.addEventListener('keydown', event => {
      if (event.key === 'Tab') keyboardInput = true;
    }, true);
    document.addEventListener('pointerdown', () => { keyboardInput = false; }, true);
    carousel.addEventListener('keydown', event => {
      if (event.altKey || event.ctrlKey || event.metaKey || event.shiftKey || !['ArrowLeft', 'ArrowRight'].includes(event.key)) return;
      event.preventDefault();
      keyboardInput = true;
      show(index + (event.key === 'ArrowRight' ? 1 : -1));
    });
    // Keyboard/screen-reader exploration stops rotation until the visitor explicitly restarts it.
    carousel.addEventListener('focusin', () => {
      if (keyboardInput) { keyboardPaused = true; updatePlayback(); }
    });
    // Only the figure/caption pauses on hover. Merely scrolling to the section, its
    // heading or its controls must not make an automatic slideshow look stopped.
    const viewport = carousel.querySelector('.showcase-viewport');
    viewport.addEventListener('pointerenter', event => {
      if (event.pointerType === 'mouse' || event.pointerType === 'pen') { hovered = true; updatePlayback(); }
    });
    viewport.addEventListener('pointerleave', () => { hovered = false; ignoreHover = false; updatePlayback(); });
    const pointers = new Map();
    let gesture;
    let swipeEnded = -Infinity;
    viewport.addEventListener('click', event => {
      if (performance.now() - swipeEnded < 400) {
        event.preventDefault();
        event.stopImmediatePropagation();
      }
    }, true);
    viewport.addEventListener('pointerdown', event => {
      if (event.pointerType === 'mouse') return;
      pointers.set(event.pointerId, true);
      if (pointers.size > 1) { gesture = null; return; }
      gesture = {id: event.pointerId, x: event.clientX, y: event.clientY};
      clearTimeout(timer);
    });
    viewport.addEventListener('pointerup', event => {
      pointers.delete(event.pointerId);
      if (!gesture || event.pointerId !== gesture.id) { updatePlayback(); return; }
      const dx = event.clientX - gesture.x;
      const dy = event.clientY - gesture.y;
      gesture = null;
      if (Math.abs(dx) > 45 && Math.abs(dx) > Math.abs(dy) * 1.5) {
        // Suppress the pointer's ensuing click, so a swipe cannot open a project/viewer.
        swipeEnded = performance.now();
        show(index + (dx < 0 ? 1 : -1));
      } else updatePlayback();
    });
    viewport.addEventListener('pointercancel', event => { pointers.delete(event.pointerId); gesture = null; updatePlayback(); });
    carousel.querySelectorAll('[data-showcase-project]').forEach(link => link.addEventListener('click', () => {
      clearTimeout(timer);
      const target = document.getElementById(link.hash.slice(1));
      if (target?.hidden) document.querySelector('[data-filter="all"]')?.click();
      const details = target?.querySelector('.case-details');
      if (details) details.open = true;
    }));
    viewer?.addEventListener('close', updatePlayback);
    carousel.querySelectorAll('.showcase-zoom').forEach(link => link.addEventListener('click', () => {
      // The shared viewer takes focus; pause until it closes, then resume normally.
      updatePlayback();
    }));
    document.addEventListener('visibilitychange', updatePlayback);
    reduced.addEventListener('change', event => { if (event.matches) userPaused = true; updatePlayback(); });
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(entries => { visible = entries[0].isIntersecting; updatePlayback(); }, {threshold: 0.25}).observe(carousel);
    }
    // No IntersectionObserver means manual playback only, avoiding offscreen rotation.
    show(0, false);
    window.addEventListener('pagehide', () => clearTimeout(timer));
    window.addEventListener('pageshow', updatePlayback);
  });
})();
