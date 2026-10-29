/* Feature behaviour and integration QA against the locally built portfolio. */
const {chromium} = require(process.env.PLAYWRIGHT_MODULE || 'playwright');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const base = process.env.PORTFOLIO_PREVIEW || 'http://127.0.0.1:4174';
const count = page => page.locator('[data-showcase-count]').textContent();
const current = page => page.locator('[data-showcase-slide].is-current');
const errors = [];
function contrast(a,b) {
  const luminance = color => (color.match(/[\d.]+/g)||[]).slice(0,3).map(Number).map(v=>v/255).map(v=>v<=.04045?v/12.92:((v+.055)/1.055)**2.4).reduce((sum,v,i)=>sum+v*[.2126,.7152,.0722][i],0);
  const x=luminance(a),y=luminance(b);
  return (Math.max(x,y)+.05)/(Math.min(x,y)+.05);
}

(async () => {
  fs.mkdirSync('qa', {recursive: true});
  const browser = await chromium.launch({headless: true});
  try {
    const context = await browser.newContext({reducedMotion: 'reduce', viewport: {width:1440, height:1000}});
    const page = await context.newPage();
    page.on('pageerror', e => errors.push(String(e)));
    page.on('response', r => { if (r.status() >= 400) errors.push(`${r.status()} ${r.url()}`); });
    const results = [];
    for (const theme of ['light','dark']) {
    await page.goto(base);
    await page.evaluate(value=>localStorage.setItem('portfolio-theme',value),theme);
    for (const lang of ['en', 'de']) for (const profile of ['mechanical', 'research']) {
      for (const width of [375, 768, 1440, 1920]) {
        await page.setViewportSize({width, height:1000});
        await page.goto(`${base}/${lang}/${profile}/`);
        const carousel = page.locator('[data-showcase]');
        await carousel.scrollIntoViewIfNeeded();
        await page.evaluate(() => document.fonts.ready);
        await page.waitForFunction(() => document.querySelector('[data-showcase]')?.classList.contains('is-enhanced'));
        assert.equal(await page.locator('[data-showcase-slide]').count(), profile === 'mechanical' ? 5 : 4);
        assert.equal(await carousel.getAttribute('data-playing'), 'false', 'Reduced motion defaults to paused');
        assert.equal(await page.locator('html').getAttribute('data-theme'),theme);
        const expectedScene = `${profile === 'mechanical' ? 'mechanical' : 'research'}-environment${width <= 760 ? '-mobile' : ''}.webp`;
        assert.ok((await carousel.evaluate(e=>getComputedStyle(e,'::before').backgroundImage)).includes(expectedScene),'Correct responsive profile backdrop');
        assert.ok((await page.locator('.hero').evaluate(e=>getComputedStyle(e,'::before').backgroundImage)).includes(expectedScene),'Hero background follows theme/profile/viewport');
        const colors = await current(page).locator('.showcase-caption>p').evaluate(e=>({ink:getComputedStyle(e).color,paper:getComputedStyle(e.closest('.showcase-slide')).backgroundColor}));
        assert.ok(contrast(colors.ink,colors.paper)>=4.5,`${theme} readable caption contrast`);
        assert.equal(await page.evaluate(() => document.documentElement.scrollWidth > innerWidth), false, `${lang}/${profile}/${width} overflow`);
        assert.equal(await page.locator('#work article.project').count(), 8, 'Existing projects preserved');
        const order = await page.evaluate(() => {
          const main = document.querySelector('main');
          return [...main.children].map(e => e.className);
        });
        assert.ok(order.indexOf('engineering-showcase is-enhanced') === order.indexOf('hero') + 1, 'Immediately after hero');
        const slideHeights = [];
        for (let i = 0; i < (profile === 'mechanical' ? 5 : 4); i++) {
          await page.locator(`[data-showcase-go="${i}"]`).click();
          assert.equal(await count(page), String(i + 1).padStart(2, '0'));
          const figure = current(page);
          const img = figure.locator('img');
          await img.evaluate(e => e.decode());
          assert.ok(await img.evaluate(e => e.complete && e.naturalWidth > 0));
          assert.equal(await img.evaluate(e => getComputedStyle(e).objectFit), 'contain');
          assert.ok(await img.getAttribute('alt'));
          assert.equal(await img.evaluate(e => e.naturalWidth === Number(e.getAttribute('width')) && e.naturalHeight === Number(e.getAttribute('height'))), true);
          const href = await figure.locator('[data-showcase-project]').first().getAttribute('href');
          assert.equal(await page.locator(href).count(), 1, 'Verified existing project');
          assert.equal(await figure.getAttribute('aria-hidden'), 'false');
          assert.equal(await page.locator('[data-showcase-slide]:not(.is-current)').evaluateAll(es => es.every(e => e.inert)), true);
          assert.equal(await figure.locator('.showcase-image').evaluate(e => e.clientHeight), width <= 600 ? 230 : Math.min(345, Math.max(260,width * .26)));
          if (width === 375) assert.equal(await page.locator('[data-showcase-slide]:visible').count(), 1);
          slideHeights.push(await carousel.evaluate(e => e.getBoundingClientRect().height));
        }
        assert.ok(Math.max(...slideHeights) - Math.min(...slideHeights) < 1, 'Stable layout when slides change');
        await page.locator('[data-showcase-next]').click();
        assert.equal(await count(page), '01', 'Wrap next');
        await page.locator('[data-showcase-prev]').click();
        assert.equal(await count(page), profile === 'mechanical' ? '05' : '04', 'Wrap previous');
        await carousel.focus();
        await page.keyboard.press('ArrowRight');
        assert.equal(await count(page), '01');
        await page.keyboard.press('ArrowLeft');
        assert.equal(await count(page), profile === 'mechanical' ? '05' : '04');
        assert.ok(await page.locator('.showcase-announcement').textContent());
        await page.locator('[data-showcase-go="0"]').click();
        await carousel.scrollIntoViewIfNeeded();
        if ([375,1440].includes(width)) await carousel.screenshot({path:`qa/showcase-${theme}-${lang}-${profile}-${width}.png`});
        results.push(`${theme}/${lang}/${profile}/${width}`);
      }
    }
    }
    // Separate enlarged-view link; the large image always goes to a case study.
    await page.goto(`${base}/en/mechanical/`);
    await current(page).locator('.showcase-zoom').click();
    assert.equal(await page.locator('.document-viewer').evaluate(e => e.open), true);
    assert.ok((await page.locator('.viewer-image').getAttribute('src')).endsWith('/handling-27.webp'));
    await page.keyboard.press('Escape');
    assert.equal(await page.locator('.document-viewer').evaluate(e => e.open), false);
    assert.equal(await current(page).locator('.showcase-zoom').evaluate(e => e === document.activeElement), true);

    // All image / caption click-throughs open the right existing, possibly filtered case.
    for (const profile of ['mechanical', 'research']) {
      await page.goto(`${base}/de/${profile}/`);
      const n = await page.locator('[data-showcase-go]').count();
      for (let i=0; i<n; i++) {
        await page.locator('[data-filter="machine"]').click();
        await page.locator(`[data-showcase-go="${i}"]`).click();
        const imageLink = current(page).locator('[data-showcase-project]').first();
        const href = await imageLink.getAttribute('href');
        await imageLink.click();
        assert.equal(new URL(page.url()).hash, href);
        assert.equal(await page.locator(href).isVisible(), true);
        assert.equal(await page.locator(`${href} .case-details`).evaluate(e=>e.open), true);
      }
    }

    // Native language/profile navigation retains the showcase anchor and changes the slide set.
    await page.goto(`${base}/en/research/#engineering-showcase`);
    await page.locator('.language').click();
    assert.equal(new URL(page.url()).pathname, '/de/research/');
    assert.equal(new URL(page.url()).hash, '#engineering-showcase');
    await page.locator('[data-profile="mechanical"]').click();
    assert.equal(new URL(page.url()).pathname, '/de/mechanical/');
    assert.equal(await page.locator('[data-showcase-slide]').count(), 5);
    assert.equal(new URL(page.url()).hash, '#engineering-showcase');

    // Without JS: a useful linked first figure, correct profile and no dead controls.
    const nojs = await browser.newContext({javaScriptEnabled:false});
    const staticPage = await nojs.newPage();
    for (const lang of ['de','en']) for (const profile of ['mechanical','research']) {
      await staticPage.goto(`${base}/${lang}/${profile}/`);
      assert.equal(await staticPage.locator('[data-showcase-slide]:visible').count(),1);
      assert.equal(await staticPage.locator('.showcase-controls').isVisible(),false);
      assert.equal(await staticPage.locator('.showcase-footer>a').isVisible(),true);
      await staticPage.locator('[data-showcase-slide]:visible [data-showcase-project]').first().click();
      assert.ok(new URL(staticPage.url()).hash);
    }
    await nojs.close();

    // Real touch input: swipe navigates without accidentally following the image link.
    const touchContext = await browser.newContext({hasTouch:true,isMobile:true,reducedMotion:'reduce',viewport:{width:375,height:900}});
    const touch = await touchContext.newPage();
    await touch.goto(`${base}/en/mechanical/`);
    await touch.locator('[data-showcase]').scrollIntoViewIfNeeded();
    const box = await current(touch).locator('.showcase-image').boundingBox();
    const cdp = await touchContext.newCDPSession(touch);
    for (const [type, x] of [['touchStart',280],['touchMove',220],['touchMove',150],['touchMove',75],['touchEnd',75]]) {
      await cdp.send('Input.dispatchTouchEvent',{type,touchPoints:type==='touchEnd'?[]:[{x,y:box.y+100}]});
    }
    assert.equal(await count(touch),'02');
    assert.equal(new URL(touch.url()).hash,'');
    await touchContext.close();

    // Real timer checks: 6 seconds, temporary hover pause, offscreen pause, tab handler,
    // persistent keyboard/manual pause and a live change to reduced-motion preferences.
    const motion = await browser.newContext({viewport:{width:1440,height:1000},reducedMotion:'no-preference'});
    const auto = await motion.newPage();
    auto.on('pageerror', e => errors.push(String(e)));
    await auto.goto(`${base}/en/mechanical/#engineering-showcase`);
    await auto.mouse.move(0,0);
    const carousel = auto.locator('[data-showcase]');
    await carousel.scrollIntoViewIfNeeded();
    await auto.waitForFunction(()=>document.querySelector('[data-showcase]').dataset.playing==='true');
    await auto.waitForFunction(()=>document.querySelector('[data-showcase-count]').textContent==='02',{},{timeout:8000});
    assert.equal(await auto.locator('.showcase-announcement').textContent(),'','No automatic live announcements');
    await current(auto).hover();
    assert.equal(await carousel.getAttribute('data-playing'),'false');
    const paused = await count(auto);
    await auto.waitForTimeout(6200);
    assert.equal(await count(auto),paused);
    await auto.mouse.move(0,0);
    await auto.waitForFunction(()=>document.querySelector('[data-showcase]').dataset.playing==='true');
    await auto.locator('#contact').scrollIntoViewIfNeeded();
    await auto.waitForFunction(()=>document.querySelector('[data-showcase]').dataset.playing==='false');
    await auto.waitForTimeout(6200);
    assert.equal(await count(auto),paused);
    await carousel.scrollIntoViewIfNeeded();
    await auto.waitForFunction(()=>document.querySelector('[data-showcase]').dataset.playing==='true');
    // Synthetic visibility event exercises the tab lifecycle in a single headless page.
    await auto.evaluate(()=>{Object.defineProperty(document,'hidden',{configurable:true,value:true});document.dispatchEvent(new Event('visibilitychange'));});
    assert.equal(await carousel.getAttribute('data-playing'),'false');
    await auto.waitForTimeout(6200);
    assert.equal(await count(auto),paused);
    await auto.evaluate(()=>{delete document.hidden;document.dispatchEvent(new Event('visibilitychange'));});
    assert.equal(await carousel.getAttribute('data-playing'),'true');
    await carousel.focus();
    assert.equal(await carousel.getAttribute('data-playing'),'true','Anchor/programmatic focus does not disable autoplay');
    await auto.keyboard.press('Tab');
    assert.equal(await carousel.getAttribute('data-playing'),'false');
    await auto.locator('.theme').focus();
    assert.equal(await carousel.getAttribute('data-playing'),'false','Focus exit does not restart rotation');
    await auto.locator('[data-showcase-play]').click();
    await auto.mouse.move(0,0);
    assert.equal(await carousel.getAttribute('data-playing'),'true');
    await auto.locator('[data-showcase-play]').click();
    await auto.mouse.move(0,0);
    assert.equal(await carousel.getAttribute('data-playing'),'false');
    await auto.locator('[data-showcase-play]').click();
    await auto.mouse.move(0,0);
    await auto.emulateMedia({reducedMotion:'reduce'});
    await auto.waitForFunction(()=>document.querySelector('[data-showcase]').dataset.playing==='false');
    assert.equal(await current(auto).evaluate(e=>getComputedStyle(e).transitionDuration),'0s');
    // Mobile auto-start and resume after a swipe without requiring the play control.
    const mobileAuto = await browser.newContext({hasTouch:true,isMobile:true,viewport:{width:375,height:900},reducedMotion:'no-preference'});
    const mobile = await mobileAuto.newPage();
    await mobile.goto(`${base}/en/research/#engineering-showcase`);
    await mobile.waitForFunction(()=>document.querySelector('[data-showcase]').dataset.playing==='true');
    await mobile.waitForFunction(()=>document.querySelector('[data-showcase-count]').textContent==='02',{},{timeout:8000});
    const mobileBox = await current(mobile).locator('.showcase-image').boundingBox();
    const mobileCdp = await mobileAuto.newCDPSession(mobile);
    for(const [type,x] of [['touchStart',280],['touchMove',200],['touchMove',130],['touchMove',75],['touchEnd',75]]) await mobileCdp.send('Input.dispatchTouchEvent',{type,touchPoints:type==='touchEnd'?[]:[{x,y:mobileBox.y+100}]});
    assert.equal(await count(mobile),'03');
    assert.equal(await mobile.locator('[data-showcase]').getAttribute('data-playing'),'true');
    await mobile.waitForFunction(()=>document.querySelector('[data-showcase-count]').textContent==='04',{},{timeout:8000});
    await mobileAuto.close();
    await motion.close();
    assert.deepEqual(errors,[],'No browser errors or HTTP failures');
    fs.writeFileSync('qa/showcase-results.json',JSON.stringify({passed:true,layouts:results,errors,checks:['all slide indicators','wrapping arrows','scoped keyboard','real touch swipe','all project click-throughs','filtered cases','enlarged viewer and focus return','language/profile anchor retention','no JavaScript','6-second autoplay','hover pause','offscreen pause','synthetic tab visibility','persistent focus pause','play/pause','live reduced-motion change']},null,2));
    console.log('PASS: 32 light/dark × DE/EN × profile × width layouts; correct responsive backgrounds, caption contrast, stable layout, all links, desktop/mobile autoplay, swipe-resume, keyboard protection, reduced motion and no-JS; zero browser/HTTP errors.');
  } finally { await browser.close(); }
})().catch(error=>{console.error(error);process.exitCode=1;});
