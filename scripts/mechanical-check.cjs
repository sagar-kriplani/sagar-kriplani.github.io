const {chromium}=require(process.env.PLAYWRIGHT_MODULE || 'playwright');
const assert=require('node:assert/strict');const fs=require('node:fs');
const base=process.env.PORTFOLIO_PREVIEW || 'http://127.0.0.1:4174';
(async()=>{
 const browser=await chromium.launch();const context=await browser.newContext({reducedMotion:'reduce',colorScheme:'light'});const page=await context.newPage();const errors=[],samples=[];
 page.on('pageerror',e=>errors.push(String(e)));page.on('response',r=>{if(r.status()>=400)errors.push(`${r.status()} ${r.url()}`)});
 for(const lang of ['de','en'])for(const width of [320,375,390,430,768,1024,1440]){
  await page.setViewportSize({width,height:1000});await page.goto(`${base}/${lang}/mechanical/`);await page.evaluate(()=>document.fonts.ready);
  assert.deepEqual(await page.locator('#featured-projects>[data-category]').evaluateAll(es=>es.map(e=>e.id)),['pau','thesis']);
  assert.equal(await page.locator('.project-archive [data-category]').count(),5);
  assert.equal(await page.locator('.project-archive').getAttribute('open'),null);
  assert.equal(await page.locator('[data-category]:visible').count(),2);
  assert.equal(await page.locator('.case-brief dt').count(),6);
  assert.equal(await page.locator('.case-source-link').count(),2);
  assert.equal(await page.locator('.evidence-groups>details').count(),5);
  assert.equal(await page.locator('.job-context').count(),2);
  assert.ok((await page.locator('.job-context').first().textContent()).includes('70'));
  assert.ok((await page.locator('.job-context').first().textContent()).includes(lang==='de'?'bestätigt':'established'));
  const cards=await page.locator('.evidence-intro .proof-card').evaluateAll(es=>es.map(e=>e.getAttribute('href')));
  assert.ok(cards[0].endsWith('#nest-reference')&&cards[1].endsWith('#brooks-reference-2'));
  const prominent=await page.locator('.industrial-case h3,.industrial-case .case-overview,.case-brief').allTextContents();
  assert.ok(!/Eigentümer|nach eigener Angabe|owner-confirmed|owner reports/i.test(prominent.join(' ')));
  assert.equal(await page.locator('[data-relevant-cv]').getAttribute('href'),`/assets/cv/mechanical-${lang}.pdf`);
  assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth),false);
  for(const id of ['pau','thesis']){
   assert.equal(await page.locator(`#${id} .case-details`).getAttribute('open'),null);
   assert.equal(await page.locator(`#${id} .case-brief`).isVisible(),true);
   assert.equal(await page.locator(`#${id} .project-art`).isVisible(),true);
  }
  samples.push({lang,width,height:await page.evaluate(()=>document.body.scrollHeight)});
 }
 await page.goto(`${base}/de/mechanical/`);
 await page.locator('#pau .case-source-link').focus();await page.keyboard.press('Enter');
 assert.equal(await page.locator('#pau .case-details').getAttribute('open'),'');
 assert.equal(await page.locator('#pau-sources').isVisible(),true);
 assert.ok(/Bericht/.test(await page.locator('#pau-sources').innerText()));
 assert.equal(await page.locator('#pau-sources').evaluate(e=>e===document.activeElement),true);
 await page.goto(`${base}/de/mechanical/#ai-cad`);
 assert.equal(await page.locator('.project-archive').getAttribute('open'),'');
 assert.equal(await page.locator('#ai-cad').isVisible(),true);
 await page.goto(`${base}/de/mechanical/`);await page.locator('.project-archive>summary').focus();await page.keyboard.press('Enter');
 assert.equal(await page.locator('.project-archive [data-category]:visible').count(),5);
 for(const [filter,count] of [['thermal',3],['machine',1],['academic',3],['all',7]]){
  await page.locator(`[data-filter="${filter}"]`).click();assert.equal(await page.locator('[data-category]:visible').count(),count);
 }
 await page.goto(`${base}/de/evidence/?category=references`);
 assert.equal(await page.locator('[data-evidence-category]:visible').count(),5);
 await page.locator('.language').click();assert.match(page.url(),/en\/evidence\/\?category=references/);
 assert.equal(await page.locator('[data-evidence-category]:visible').count(),5);
 await page.goto(`${base}/de/evidence/?category=certifications&q=NX`);
 assert.equal(await page.locator('[data-evidence-category]:visible').count(),3);
 await page.goto(`${base}/de/mechanical/#pau`);await page.locator('.language').click();
 assert.equal(new URL(page.url()).pathname,'/en/mechanical/');assert.equal(new URL(page.url()).hash,'#pau');
 await page.locator('[data-profile="research"]').click();assert.equal(new URL(page.url()).pathname,'/en/research/');assert.equal(new URL(page.url()).hash,'#pau');
 assert.equal(await page.locator('.project-archive').count(),0);
 assert.deepEqual(await page.locator('[data-category]').evaluateAll(es=>es.map(e=>e.id)),['thesis','pau','ansys','frost','handling','ai-cad','shoe']);
 const nojs=await browser.newContext({javaScriptEnabled:false,viewport:{width:390,height:1000}});const fallback=await nojs.newPage();
 await fallback.goto(`${base}/de/mechanical/`);await fallback.locator('.project-archive>summary').click();
 assert.equal(await fallback.locator('.project-archive [data-category]:visible').count(),5);
 await fallback.locator('#pau .case-details>summary').click();assert.equal(await fallback.locator('#pau-sources').isVisible(),true);
 assert.deepEqual(errors,[]);
 fs.writeFileSync('qa/mechanical-results.json',JSON.stringify({passed:true,browser:'Chromium',samples,checks:['two active major cases; NeSt temporarily paused','five archived projects preserved','visible challenge/decision/result and visual','five evidence groups','professional references first','provenance accessible by keyboard','archive deep links','all project filters','evidence category/search deep links','language/profile context','R&D order unchanged','no-JavaScript archive/evidence'],errors},null,2));
 await browser.close();console.log('PASS: 14 mechanical-profile viewport samples; hierarchy, archive, evidence, context and keyboard behavior.');
})().catch(e=>{console.error(e);process.exit(1)});
