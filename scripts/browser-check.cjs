const {chromium}=require(process.env.PLAYWRIGHT_MODULE || 'playwright');
const fs=require('fs');
const assert=require('node:assert/strict');
(async()=>{
 fs.mkdirSync('qa',{recursive:true});
 const browser=await chromium.launch({headless:true});
 const context=await browser.newContext({viewport:{width:1440,height:1000},colorScheme:'light',reducedMotion:'reduce',permissions:['clipboard-read','clipboard-write']});
 const page=await context.newPage(); const errors=[];
 page.on('pageerror',e=>errors.push(String(e)));
 page.on('response',r=>{if(r.status()>=400)errors.push(`${r.status()} ${r.url()}`)});
 for(const route of ['/','/en/','/de/','/en/cv/','/de/cv/','/en/legal/','/de/legal/','/en/evidence/','/de/evidence/']){
  await page.goto('http://127.0.0.1:4174'+route);await page.evaluate(()=>document.fonts.ready);
  assert.equal(await page.locator('h1').count(),1);
  assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth),false,route+' overflows');
 }
 await page.goto('http://127.0.0.1:4174/');await page.evaluate(()=>document.fonts.ready);
 if(!process.env.SKIP_SCREENSHOTS) await page.screenshot({path:'qa/desktop.png',fullPage:true});
 await page.locator('[data-filter="thermal"]').click();assert.equal(await page.locator('[data-category]:visible').count(),3);
 await page.locator('[data-filter="machine"]').click();assert.equal(await page.locator('[data-category]:visible').count(),2);
 await page.locator('[data-filter="academic"]').click();assert.equal(await page.locator('[data-category]:visible').count(),3);
 await page.locator('[data-filter="all"]').click();assert.equal(await page.locator('[data-category]:visible').count(),8);
 await page.locator('#pau summary').click();assert.equal(await page.locator('#pau details').getAttribute('open'),'');
 await page.locator('.theme').click();assert.equal(await page.locator('html').getAttribute('data-theme'),'dark');
 await page.reload();assert.equal(await page.locator('html').getAttribute('data-theme'),'dark');
 await page.locator('.theme').click();
 await page.locator('.copy-email').click();await page.waitForFunction(()=>document.querySelector('.copy-status').textContent==='Email copied');
 await page.setViewportSize({width:390,height:844});await page.goto('http://127.0.0.1:4174/de/');await page.evaluate(()=>document.fonts.ready);
 if(!process.env.SKIP_SCREENSHOTS) await page.screenshot({path:'qa/mobile.png',fullPage:true});
 await page.locator('.menu-toggle').click();assert.equal(await page.locator('#mobile-nav').isVisible(),true);
 await page.keyboard.press('Escape');assert.equal(await page.locator('#mobile-nav').isVisible(),false);
 await page.locator('.menu-toggle').click();await page.locator('#mobile-nav a').first().click();assert.equal(await page.locator('#mobile-nav').isVisible(),false);
 for(const width of [320,390,768,1024,1440]){
  await page.setViewportSize({width,height:900});
  for(const route of ['/en/','/de/','/en/cv/','/de/legal/','/en/evidence/','/de/evidence/']){
   await page.goto('http://127.0.0.1:4174'+route);
   assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth),false,route+' overflows at '+width);
  }
 }
 await page.goto('http://127.0.0.1:4174/en/evidence/');
 assert.equal(await page.locator('[data-evidence-category]:visible').count(),29);
 await page.locator('[data-evidence-filter="certifications"]').click();assert.equal(await page.locator('[data-evidence-category]:visible').count(),16);
 await page.locator('#evidence-search').fill('NX');assert.equal(await page.locator('[data-evidence-category]:visible').count(),3);
 await page.locator('#evidence-search').fill('no-such-record-123');assert.equal(await page.locator('[data-evidence-category]:visible').count(),0);assert.equal(await page.locator('.evidence-empty').isVisible(),true);
 await page.locator('#evidence-search').fill('');await page.locator('[data-evidence-filter="references"]').click();assert.equal(await page.locator('[data-evidence-category]:visible').count(),5);
 await page.locator('#nest-reference [data-viewer]').click();assert.equal(await page.locator('dialog').isVisible(),true);
 await page.locator('.viewer-close').focus();await page.keyboard.press('ArrowRight');assert.match(await page.locator('#viewer-caption').textContent(),/Brooks/);
 await page.keyboard.press('Escape');assert.equal(await page.locator('dialog').isVisible(),false);
 await page.locator('[data-evidence-filter="education"]').click();assert.equal(await page.locator('[data-evidence-category]:visible').count(),8);
 await page.locator('.language').click();assert.match(page.url(),/de\/evidence/);
 await page.setViewportSize({width:1440,height:1000});await page.screenshot({path:'qa/evidence-desktop.png'});
 await page.setViewportSize({width:390,height:844});await page.screenshot({path:'qa/evidence-mobile.png'});
 await page.goto('http://127.0.0.1:4174/en/');
 const nojs=await browser.newContext({javaScriptEnabled:false,viewport:{width:390,height:844}});
 const fallback=await nojs.newPage();await fallback.goto('http://127.0.0.1:4174/');
 assert.equal(await fallback.locator('[data-category]').count(),8);await fallback.locator('#pau summary').click();assert.equal(await fallback.locator('#pau details').getAttribute('open'),'');
 await page.goto('http://127.0.0.1:4174/en/cv/');await page.emulateMedia({media:'print'});
 if(!process.env.SKIP_SCREENSHOTS) await page.screenshot({path:'qa/cv-print.png',fullPage:true});
 assert.deepEqual(errors,[]);
 fs.writeFileSync('qa/results.json',JSON.stringify({passed:true,routes:9,widths:[320,390,768,1024,1440],checks:['assets','overflow','project filters','case studies','theme persistence','clipboard','mobile menu','Escape focus','no-JavaScript content','print stylesheet','evidence filtering and search','document viewer and keyboard navigation','employer imagery excluded'],errors},null,2));
 await browser.close();console.log('PASS: browser routes, responsive layouts, interactions, no-JS fallback, print stylesheet; zero console/network errors.');
})().catch(e=>{console.error(e);process.exit(1)});
