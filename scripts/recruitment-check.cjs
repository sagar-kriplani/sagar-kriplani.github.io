const {chromium}=require(process.env.PLAYWRIGHT_MODULE || 'playwright');
const fs=require('node:fs');const assert=require('node:assert/strict');
const base=process.env.PORTFOLIO_PREVIEW || 'http://127.0.0.1:4174';const widths=[320,375,390,430,768,1024,1440];
function luminance(rgb){return rgb.slice(0,3).map(v=>v/255).map(v=>v<=.04045?v/12.92:((v+.055)/1.055)**2.4).reduce((a,v,i)=>a+v*[.2126,.7152,.0722][i],0)}
function contrast(a,b){const x=luminance(a),y=luminance(b);return(Math.max(x,y)+.05)/(Math.min(x,y)+.05)}
(async()=>{
 const browser=await chromium.launch();const context=await browser.newContext({reducedMotion:'reduce',colorScheme:'light'});const page=await context.newPage();const errors=[],observations=[];
 page.on('pageerror',e=>errors.push(String(e)));page.on('response',r=>{if(r.status()>=400)errors.push(`${r.status()} ${r.url()}`)});
 for(const lang of ['en','de'])for(const profile of ['mechanical','research'])for(const width of widths){
  await page.setViewportSize({width,height:1000});await page.goto(`${base}/${lang}/${profile}/`);await page.evaluate(()=>document.fonts.ready);
  assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth),false,`${lang}/${profile} ${width} overflow`);
  assert.equal(await page.locator('h1').count(),1);assert.equal(await page.locator('.profile-switch [aria-current="page"]').getAttribute('data-profile'),profile);
  assert.ok(!(await page.locator('main').innerText()).includes('R&D;'),'Malformed ampersand entity');
  const expected=`/assets/cv/${profile==='research'?'rd':'mechanical'}-${lang}.pdf`;
  assert.equal(await page.locator('[data-relevant-cv]').getAttribute('href'),expected);assert.equal((await page.request.get(base+expected)).status(),200);
  assert.equal(await page.locator('[data-category]').first().getAttribute('id'),profile==='research'?'thesis':'machine');
  assert.equal(await page.locator('.skill').count(),4);
  for(const id of ['machine','pau','thesis'])assert.equal(await page.locator(`#${id} .engineering-steps>li`).count(),6);
  const title=await page.locator('h1').innerText();assert.ok(lang==='de'?/ingenieur/i.test(title):/Engineer/.test(title));
  for(const theme of ['light','dark']){
   await page.evaluate(value=>document.documentElement.dataset.theme=value,theme);
   const colours=await page.locator('.intro').evaluate(el=>{const rgb=v=>v.match(/[\d.]+/g).map(Number);return {text:rgb(getComputedStyle(el).color),background:rgb(getComputedStyle(document.body).backgroundColor)}});
   assert.ok(contrast(colours.text,colours.background)>=4.5,'Body contrast '+lang+'/'+profile+'/'+theme);
   const accent=await page.locator('.profile-industries').evaluate(el=>getComputedStyle(el).color.match(/[\d.]+/g).map(Number));
   assert.ok(contrast(accent,colours.background)>=4.5,'Accent contrast '+lang+'/'+profile+'/'+theme);
  }
  await page.evaluate(()=>document.documentElement.dataset.theme='light');
  observations.push({lang,profile,width,title,cv:expected});
 }
 // Context survives profile and language changes; native disclosure remains keyboard accessible.
 await page.goto(`${base}/en/mechanical/#thesis`);await page.locator('[data-profile="research"]').click();
 assert.equal(new URL(page.url()).pathname,'/en/research/');assert.equal(new URL(page.url()).hash,'#thesis');
 await page.locator('.language').click();assert.equal(new URL(page.url()).pathname,'/de/research/');assert.equal(new URL(page.url()).hash,'#thesis');
 await page.locator('.header>nav').first().locator('a[href$="#experience"]').click();assert.equal(new URL(page.url()).pathname,'/de/research/');
 await page.goto(`${base}/en/research/`);await page.locator('#thesis summary').focus();await page.keyboard.press('Enter');
 assert.equal(await page.locator('#thesis details').getAttribute('open'),'');
 assert.equal(await page.locator('#thesis .case-table tbody tr').count(),4);
 assert.equal(await page.locator('#thesis .research-plots img').count(),2);
 await page.locator('#thesis .research-plots [data-viewer]').first().click();assert.equal(await page.locator('.document-unlock').isVisible(),false);
 assert.equal(await page.locator('.viewer-download').isVisible(),true);await page.keyboard.press('Escape');
 await page.goto(`${base}/en/mechanical/`);await page.locator('#machine summary').click();await page.locator('#machine .engineering-steps').screenshot({path:'qa/recruitment-nest-case.png'});
 await page.goto(`${base}/en/research/`);await page.locator('#thesis summary').click();await page.locator('#thesis .case-table').screenshot({path:'qa/recruitment-thesis-table.png'});
 const nojs=await browser.newContext({javaScriptEnabled:false,viewport:{width:390,height:1000}});const fallback=await nojs.newPage();
 await fallback.goto(`${base}/de/research/`);assert.equal(await fallback.locator('.profile-switch a').count(),2);await fallback.locator('#thesis summary').click();
 assert.equal(await fallback.locator('#thesis .engineering-steps').isVisible(),true);assert.equal(await fallback.locator('[data-relevant-cv]').count(),1);
 assert.deepEqual(errors,[]);fs.writeFileSync('qa/recruitment-results.json',JSON.stringify({passed:true,browser:'Chromium',widths,profileSamples:observations.length,checks:['role/CV match','all four language/profile paths','three six-step cases','project priority','four skills groups','profile/language/anchor context','keyboard and no-JavaScript disclosure','body and accent contrast >=4.5:1 in both themes','public research plots and protected-original control'],errors,observations},null,2));
 await browser.close();console.log('PASS: 28 role/language/viewport samples; role-specific CVs, cases, skills, context and contrast.');
})().catch(e=>{console.error(e);process.exit(1)});
