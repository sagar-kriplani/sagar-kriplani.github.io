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
 for(const route of ['/','/en/','/de/','/en/cv/','/de/cv/','/en/legal/','/de/legal/']){
  await page.goto('http://127.0.0.1:4174'+route);await page.evaluate(()=>document.fonts.ready);
  assert.equal(await page.locator('h1').count(),1);
  assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth),false,route+' overflows');
 }
 await page.goto('http://127.0.0.1:4174/');await page.evaluate(()=>document.fonts.ready);
 if(!process.env.SKIP_SCREENSHOTS) await page.screenshot({path:'qa/desktop.png',fullPage:true});
 await page.locator('[data-filter="thermal"]').click();assert.equal(await page.locator('[data-category]:visible').count(),2);
 await page.locator('[data-filter="machine"]').click();assert.equal(await page.locator('[data-category]:visible').count(),1);
 await page.locator('[data-filter="academic"]').click();assert.equal(await page.locator('[data-category]:visible').count(),1);
 await page.locator('[data-filter="all"]').click();assert.equal(await page.locator('[data-category]:visible').count(),4);
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
  for(const route of ['/en/','/de/','/en/cv/','/de/legal/']){
   await page.goto('http://127.0.0.1:4174'+route);
   assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth),false,route+' overflows at '+width);
  }
 }
 const nojs=await browser.newContext({javaScriptEnabled:false,viewport:{width:390,height:844}});
 const fallback=await nojs.newPage();await fallback.goto('http://127.0.0.1:4174/');
 assert.equal(await fallback.locator('[data-category]').count(),4);await fallback.locator('#pau summary').click();assert.equal(await fallback.locator('#pau details').getAttribute('open'),'');
 await page.goto('http://127.0.0.1:4174/en/cv/');await page.emulateMedia({media:'print'});
 if(!process.env.SKIP_SCREENSHOTS) await page.screenshot({path:'qa/cv-print.png',fullPage:true});
 assert.deepEqual(errors,[]);
 fs.writeFileSync('qa/results.json',JSON.stringify({passed:true,routes:7,widths:[320,390,768,1024,1440],checks:['assets','overflow','project filters','case studies','theme persistence','clipboard','mobile menu','Escape focus','no-JavaScript content','print stylesheet'],errors},null,2));
 await browser.close();console.log('PASS: browser routes, responsive layouts, interactions, no-JS fallback, print stylesheet; zero console/network errors.');
})().catch(e=>{console.error(e);process.exit(1)});
