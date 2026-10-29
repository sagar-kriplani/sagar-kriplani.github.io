const {chromium}=require(process.env.PLAYWRIGHT_MODULE || 'playwright');
const assert=require('node:assert/strict');const fs=require('node:fs');
const base=process.env.PORTFOLIO_PREVIEW || 'http://127.0.0.1:4174';
(async()=>{
 const browser=await chromium.launch();const context=await browser.newContext({reducedMotion:'reduce',colorScheme:'light'});const page=await context.newPage();const errors=[],samples=[];
 page.on('pageerror',e=>errors.push(String(e)));page.on('response',r=>{if(r.status()>=400)errors.push(`${r.status()} ${r.url()}`)});
 for(const lang of ['de','en'])for(const width of [320,375,390,430,768,1024,1440]){
  await page.setViewportSize({width,height:1000});await page.goto(`${base}/${lang}/mechanical/`);await page.evaluate(()=>document.fonts.ready);
  assert.deepEqual(await page.locator('#featured-projects>[data-category]').evaluateAll(es=>es.map(e=>e.id)),['machine','pau','thesis','handling','ansys','frost','shoe','ai-cad']);
  assert.equal(await page.locator('.project-archive').count(),0);
  assert.equal(await page.locator('[data-category]:visible').count(),8);
  assert.equal(await page.locator('.case-brief').count(),0);
  assert.equal(await page.locator('.project-jumps').count(),0);
  assert.equal(await page.locator('.evidence-groups>details').count(),5);
  assert.equal(await page.locator('.job-context').count(),2);
  assert.ok((await page.locator('.job-context').first().textContent()).includes('70'));
  assert.ok((await page.locator('.job-context').first().textContent()).includes(lang==='de'?'bestätigt':'established'));
  const cards=await page.locator('.evidence-intro .proof-card').evaluateAll(es=>es.map(e=>e.getAttribute('href')));
  assert.ok(cards[0].endsWith('#nest-reference')&&cards[1].endsWith('#brooks-reference-2'));
  const prominent=await page.locator('.project h3,.project-content>p:not(.eyebrow)').allTextContents();
  assert.ok(!/Eigentümer|nach eigener Angabe|owner-confirmed|owner reports/i.test(prominent.join(' ')));
  assert.equal(await page.locator('[data-relevant-cv]').getAttribute('href'),`/assets/cv/mechanical-${lang}.pdf`);
  assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth),false);
  for(const id of ['machine','pau','thesis']){
   assert.equal(await page.locator(`#${id} .case-details`).getAttribute('open'),null);
   assert.equal(await page.locator(`#${id} .engineering-steps`).isVisible(),false);
   assert.equal(await page.locator(`#${id} .project-art`).isVisible(),true);
  }
  samples.push({lang,width,height:await page.evaluate(()=>document.body.scrollHeight)});
 }
 await page.goto(`${base}/de/mechanical/`);
 await page.locator('#machine .case-details>summary').focus();await page.keyboard.press('Enter');
 assert.equal(await page.locator('#machine .case-details').getAttribute('open'),'');
 assert.equal(await page.locator('#machine-sources').isVisible(),true);
 assert.ok(/NeSt-Arbeitszeugnis/.test(await page.locator('#machine-sources').innerText()));
 assert.ok(!/8.mm|Biegefreistellung|repair welding/i.test(await page.locator('#machine').textContent()));
 assert.ok(/Maschinenverkleidungen/.test(await page.locator('#machine h3').innerText()));
 assert.equal(await page.locator('#machine .project-art svg').count(),1);
 assert.equal(await page.locator('#machine .case-details>summary').evaluate(e=>e===document.activeElement),true);
 await page.goto(`${base}/de/mechanical/#ai-cad`);
 assert.equal(await page.locator('#ai-cad').isVisible(),true);
 assert.equal(await page.locator('#ai-cad').isVisible(),true);
 await page.goto(`${base}/de/mechanical/`);
 assert.equal(await page.locator('[data-category]:visible').count(),8);
 for(const [filter,count] of [['thermal',3],['machine',2],['academic',3],['all',8]]){
  await page.locator(`[data-filter="${filter}"]`).click();assert.equal(await page.locator('[data-category]:visible').count(),count);
 }
 await page.goto(`${base}/de/evidence/?category=references`);
 assert.equal(await page.locator('[data-evidence-category]:visible').count(),5);
 await page.locator('.language').click();assert.match(page.url(),/en\/evidence\/\?category=references/);
 assert.equal(await page.locator('[data-evidence-category]:visible').count(),5);
 await page.goto(`${base}/de/evidence/?category=certifications&q=NX`);
 await page.waitForFunction(()=>[...document.querySelectorAll('[data-evidence-category]')].filter(e=>!e.hidden).length===3);
 assert.equal(await page.locator('[data-evidence-category]:visible').count(),3);
 await page.goto(`${base}/de/mechanical/#pau`);await page.locator('.language').click();
 assert.equal(new URL(page.url()).pathname,'/en/mechanical/');assert.equal(new URL(page.url()).hash,'#pau');
 await page.locator('[data-profile="research"]').click();assert.equal(new URL(page.url()).pathname,'/en/research/');assert.equal(new URL(page.url()).hash,'#pau');
 assert.equal(await page.locator('.project-archive').count(),0);
 assert.deepEqual(await page.locator('[data-category]').evaluateAll(es=>es.map(e=>e.id)),['thesis','pau','ansys','frost','machine','handling','ai-cad','shoe']);
 const nojs=await browser.newContext({javaScriptEnabled:false,viewport:{width:390,height:1000}});const fallback=await nojs.newPage();
 await fallback.goto(`${base}/de/mechanical/`);
 assert.equal(await fallback.locator('[data-category]:visible').count(),8);
 await fallback.locator('#machine .case-details>summary').click();assert.equal(await fallback.locator('#machine-sources').isVisible(),true);
 assert.deepEqual(errors,[]);
 fs.writeFileSync('qa/mechanical-results.json',JSON.stringify({passed:true,browser:'Chromium',samples,checks:['eight continuously visible projects','no project archive','consistent cards with collapsed methodology','five evidence groups','professional references first','provenance accessible by keyboard','project deep links','all project filters','evidence category/search deep links','language/profile context','R&D order unchanged','no-JavaScript projects/evidence'],errors},null,2));
 await browser.close();console.log('PASS: 14 mechanical-profile viewport samples; hierarchy, continuous projects, evidence, context and keyboard behavior.');
})().catch(e=>{console.error(e);process.exit(1)});
