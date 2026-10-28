/* Targeted regression coverage for the final UX review. No test dependencies added. */
const {chromium}=require(process.env.PLAYWRIGHT_MODULE || 'playwright');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const base=process.env.PORTFOLIO_PREVIEW || 'http://127.0.0.1:4174';
const widths=[320,375,390,430,768,1024,1440];
(async()=>{
 fs.mkdirSync('qa',{recursive:true});
 const browser=await chromium.launch({headless:true});
 const context=await browser.newContext({reducedMotion:'reduce',colorScheme:'light'});
 const page=await context.newPage();const errors=[],externalRequests=[];let samples=0;
 page.on('pageerror',e=>errors.push(String(e)));
 page.on('response',r=>{if(r.status()>=400)errors.push(`${r.status()} ${r.url()}`)});
 page.on('request',r=>{if(new URL(r.url()).origin!==new URL(base).origin)externalRequests.push(r.url())});
 for(const lang of ['en','de']){
  for(const width of widths){
   await page.setViewportSize({width,height:900});
   for(const route of ['', 'cv/','legal/','privacy/','evidence/','gallery/','cad/']){
    await page.goto(`${base}/${lang}/${route}`);await page.evaluate(()=>document.fonts.ready);
    assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth),false,`${lang}/${route} overflow at ${width}`);
    assert.equal(await page.locator('h1').count(),1);
    assert.equal(await page.locator('.footer a[href$="/privacy/"]').innerText(),lang==='en'?'Privacy Policy':'Datenschutz');
    assert.equal(await page.locator('.footer a[href$="/legal/"]').innerText(),lang==='en'?'Legal Notice':'Impressum');
    assert.equal(await page.locator('.portrait-index').count(),0);
    assert.equal(await page.locator('a,button,summary').evaluateAll(nodes=>nodes.some(n=>/[↗←→↑↓↘]/u.test(n.textContent))),false,'Unicode directional control remains');
    assert.equal(await page.locator('script[src^="https:"],iframe,video').count(),0);
    samples++;
   }
   await page.goto(`${base}/${lang}/#education`);await page.evaluate(()=>document.fonts.ready);
   const header=await page.locator('.header').boundingBox();const education=await page.locator('#education').boundingBox();
   assert.ok(header.y<0,'Header should scroll out of view');
   assert.ok(education.y>=0,'Education anchor should remain visible');
   assert.equal(await page.locator('.education-step').count(),3);
   const dates=await page.locator('.education-step>.date').evaluateAll(nodes=>nodes.map(n=>n.getBoundingClientRect().x));
   assert.ok(dates.every(x=>Math.abs(x-dates[0])<1),'Education dates misaligned');
   if(width<=900){
    await page.evaluate(()=>scrollTo(0,0));
    await page.locator('.menu-toggle').click();assert.equal(await page.locator('#mobile-nav').isVisible(),true);
    const box=await page.locator('.menu-toggle').boundingBox();assert.ok(box.width>=44&&box.height>=44);
    await page.keyboard.press('Escape');assert.equal(await page.locator('#mobile-nav').isVisible(),false);
    assert.equal(await page.locator('.menu-toggle').evaluate(e=>e===document.activeElement),true);
   }
   assert.ok(parseFloat(await page.locator('.tags span').first().evaluate(e=>getComputedStyle(e).fontSize))>=10);
   await page.locator('#education').screenshot({path:`qa/ux-education-${lang}-${width}.png`});
  }
  // Switching languages keeps the route and current section; filters retain keyboard behavior.
  await page.goto(`${base}/${lang}/#experience`);
  await page.locator('.language').click();
  assert.equal(new URL(page.url()).hash,'#experience');
  await page.goto(`${base}/${lang}/`);
  for(const [filter,count] of [['machine',2],['thermal',3],['academic',3],['all',8]]){
   await page.locator(`[data-filter="${filter}"]`).focus();await page.keyboard.press('Enter');
   assert.equal(await page.locator('[data-category]:visible').count(),count);
   assert.equal(await page.locator(`[data-filter="${filter}"]`).getAttribute('aria-pressed'),'true');
  }
  await page.evaluate(()=>scrollTo(0,1600));
  await page.waitForFunction(()=>!document.querySelector('.back-to-top').hidden);
  await page.locator('.back-to-top').click();await page.waitForFunction(()=>window.scrollY<1);
  await page.locator('.footer').scrollIntoViewIfNeeded();
  await page.waitForFunction(()=>document.body.classList.contains('footer-visible'));
  assert.equal(await page.locator('.back-to-top').isVisible(),false);
  await page.goto(`${base}/${lang}/privacy/`);await page.locator('.theme').click();
  assert.ok(await page.evaluate(()=>localStorage.getItem('portfolio-theme')));
  await page.locator('.reset-theme').click();assert.equal(await page.evaluate(()=>localStorage.getItem('portfolio-theme')),null);
  assert.ok((await page.locator('.theme-reset-status').innerText()).length>0);
  assert.equal(await page.evaluate(()=>getComputedStyle(document.documentElement).scrollBehavior),'auto');
  await page.goto(`${base}/${lang}/evidence/`);
  await page.locator('#evidence-search').fill('no-match-ux-review');
  assert.equal(await page.locator('.evidence-empty').isVisible(),true);
  await page.locator('#evidence-search').fill('');await page.locator('[data-viewer]').first().click();
  assert.equal(await page.locator('.viewer-zoom-in').getAttribute('aria-label'),lang==='en'?'Zoom in':'Vergrößern');
  assert.equal(await page.locator('.viewer-fit').innerText(),lang==='en'?'Fit':'Einpassen');
  await page.keyboard.press('Escape');assert.equal(await page.locator('dialog').isVisible(),false);
 }
 for(const width of [390,1440]){
  await page.setViewportSize({width,height:900});await page.goto(`${base}/en/`);await page.evaluate(()=>document.fonts.ready);
  await page.screenshot({path:`qa/review-after-${width}.png`});
 }
 const nojs=await browser.newContext({javaScriptEnabled:false,viewport:{width:320,height:900}});
 const fallback=await nojs.newPage();await fallback.goto(`${base}/de/`);
 assert.equal(await fallback.locator('.no-js-nav a').count(),5);
 assert.equal(await fallback.locator('.no-js-nav').isVisible(),true);
 assert.equal(await fallback.evaluate(()=>document.documentElement.scrollWidth>innerWidth),false,'No-JS overflow');
 assert.equal(await fallback.locator('.back-to-top').isVisible(),false);
 await page.goto(`${base}/en/cv/`);await page.emulateMedia({media:'print'});
 assert.equal(await page.locator('.header').isVisible(),false);
 assert.equal((await context.cookies()).length,0);
 assert.deepEqual(externalRequests,[],'Unexpected third-party network requests');assert.deepEqual(errors,[]);
 fs.writeFileSync('qa/ux-results.json',JSON.stringify({passed:true,browser:'Playwright Chromium',widths,routeSamples:samples,externalRequests,cookies:0,errors,checks:['scrolling header','anchor clearance','SVG controls','localized footer and viewer','mobile menu and Escape focus','no-JS navigation','language section preservation','keyboard project filters','empty evidence results','back-to-top','theme reset','reduced motion','education alignment','print controls']},null,2));
 await browser.close();console.log(`PASS: ${samples} responsive route checks, bilingual controls, storage/network/privacy and accessibility regressions.`);
})().catch(e=>{console.error(e);process.exit(1)});
