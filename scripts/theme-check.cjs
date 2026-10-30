/* Shared palette and explicit light-first preference across the complete built site. */
const {chromium}=require(process.env.PLAYWRIGHT_MODULE || 'playwright');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const base=process.env.PORTFOLIO_PREVIEW || 'http://127.0.0.1:4174';
const routes=['/','/404.html',...['en','de'].flatMap(lang=>['','mechanical/','research/','cv/','legal/','privacy/','evidence/','gallery/','cad/'].map(sub=>`/${lang}/${sub}`))];
const tokens=['--bg','--surface','--ink','--muted','--line','--accent','--dark','--on-dark','--paper','--media-surface'];
const rgb=hex=>[1,3,5].map(i=>parseInt(hex.slice(i,i+2),16)/255);
const luminance=color=>(color.startsWith('#')?rgb(color):color.match(/[\d.]+/g).slice(0,3).map(v=>Number(v)/255)).map(v=>v<=.04045?v/12.92:((v+.055)/1.055)**2.4).reduce((sum,v,i)=>sum+v*[.2126,.7152,.0722][i],0);
const contrast=(a,b)=>{const x=luminance(a),y=luminance(b);return (Math.max(x,y)+.05)/(Math.min(x,y)+.05)};

(async()=>{
  fs.mkdirSync('qa',{recursive:true});
  const browser=await chromium.launch({headless:true,args:['--use-angle=swiftshader','--enable-unsafe-swiftshader']});
  try {
    const context=await browser.newContext({colorScheme:'dark',reducedMotion:'reduce',viewport:{width:1440,height:1000}});
    const page=await context.newPage();const errors=[],samples=[];
    page.on('pageerror',e=>errors.push(e.message));
    page.on('response',r=>{if(r.status()>=400 && !r.url().endsWith('/404.html')) errors.push(`${r.status()} ${r.url()}`)});
    await page.goto(base);
    assert.equal(await page.locator('html').getAttribute('data-theme'),'light','Fresh visit ignores dark OS preference');
    assert.equal(await page.evaluate(()=>localStorage.getItem('portfolio-theme')),null,'Default is not saved as a visitor choice');
    await page.emulateMedia({colorScheme:'light'});await page.emulateMedia({colorScheme:'dark'});
    assert.equal(await page.locator('html').getAttribute('data-theme'),'light','OS changes never override the light-first default');
    for(const theme of ['light','dark']) {
      await page.goto(base);await page.evaluate(value=>localStorage.setItem('portfolio-theme',value),theme);await page.reload();
      const reference=await page.locator('body').evaluate((e,names)=>Object.fromEntries(names.map(n=>[n,getComputedStyle(e).getPropertyValue(n).trim()])),tokens);
      assert.equal(reference['--bg'],theme==='light'?'#f3f6f8':'#111820');
      for(const width of [375,782,1440]) for(const route of routes) {
        await page.setViewportSize({width,height:1000});await page.goto(base+route);await page.evaluate(()=>document.fonts.ready);
        assert.equal(await page.locator('html').getAttribute('data-theme'),theme,route);
        const actual=await page.locator('body').evaluate((e,names)=>Object.fromEntries(names.map(n=>[n,getComputedStyle(e).getPropertyValue(n).trim()])),tokens);
        assert.deepEqual(actual,reference,`${route}: all colours match homepage in ${theme}`);
        assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth),false,`${route}/${width}: horizontal overflow`);
        assert.ok(contrast(actual['--ink'],actual['--bg'])>=4.5);
        assert.ok(contrast(actual['--muted'],actual['--bg'])>=4.5);
        assert.ok(contrast(actual['--accent'],actual['--bg'])>=4.5);
        if(await page.locator('.theme').count()) assert.equal(await page.locator('.theme').getAttribute('aria-pressed'),String(theme==='dark'));
        const startup=await page.evaluate(()=>{const scripts=[...document.scripts];const boot=scripts.find(s=>s.src.endsWith('/theme.js'));const css=document.querySelector('link[href="/assets/site.css"]');return !!boot && !!(boot.compareDocumentPosition(css)&Node.DOCUMENT_POSITION_FOLLOWING)});
        assert.ok(startup,'Preference restoration precedes stylesheet to avoid wrong-theme flash');
        if(route.endsWith('/gallery/')) {
          const frame=page.locator('.gallery-card').first();
          const colours=await frame.evaluate(e=>({card:getComputedStyle(e).backgroundColor,label:getComputedStyle(e.querySelector('h2')).color,stage:getComputedStyle(e.querySelector('a')).backgroundColor}));
          assert.ok(contrast(colours.label,colours.card)>=4.5,'Gallery caption contrast');
          assert.notEqual(colours.stage,theme==='dark'?'rgb(236, 238, 232)':'rgb(238, 239, 233)','No legacy green image frame');
          assert.ok((await frame.locator('img').getAttribute('src')).endsWith('.webp'),'Original project figure remains intact');
        }
        if(route.endsWith('/cad/')) {
          await page.waitForFunction(()=>document.getElementById('cad-status').textContent.includes('12'));
          const rendered=await page.locator('#cad-canvas').evaluate(c=>{const gl=c.getContext('webgl');const program=gl.getParameter(gl.CURRENT_PROGRAM);return {background:Array.from(gl.getParameter(gl.COLOR_CLEAR_VALUE)).slice(0,3),mesh:Array.from(gl.getUniform(program,gl.getUniformLocation(program,'meshColour')))}});
          for(let i=0;i<3;i++){assert.ok(Math.abs(rendered.background[i]-rgb(reference['--media-surface'])[i])<.001);assert.ok(Math.abs(rendered.mesh[i]-rgb(reference['--accent'])[i])<.001);}
        }
        if(route.startsWith('/en/') && ['gallery','cad','evidence','mechanical'].some(s=>route===`/en/${s}/`) && [375,1440].includes(width)) {
          await page.screenshot({path:`qa/theme-${theme}-${route.split('/')[2]}-${width}.png`});
          if(route==='/en/gallery/') {await page.locator('#handling-07').evaluate(e=>{e.hidden=false;e.scrollIntoView({block:'center'})});await page.screenshot({path:`qa/theme-${theme}-gallery-card-${width}.png`});}
        }
        samples.push({theme,width,route});
      }
    }
    // Explicit choice, navigation, language switching and reset under dark OS settings.
    await page.goto(base+'/en/gallery/');await page.locator('.theme').click();
    assert.equal(await page.locator('html').getAttribute('data-theme'),'light');
    await page.locator('.theme').click();assert.equal(await page.evaluate(()=>localStorage.getItem('portfolio-theme')),'dark');
    await page.reload();assert.equal(await page.locator('html').getAttribute('data-theme'),'dark');
    await page.locator('.language').click();assert.equal(await page.locator('html').getAttribute('data-theme'),'dark');
    await page.goto(base+'/de/privacy/');await page.locator('.reset-theme').click();
    assert.equal(await page.locator('html').getAttribute('data-theme'),'light');
    assert.equal(await page.evaluate(()=>localStorage.getItem('portfolio-theme')),null);
    await page.reload();assert.equal(await page.locator('html').getAttribute('data-theme'),'light');
    await page.evaluate(()=>localStorage.setItem('portfolio-theme','invalid'));await page.reload();
    assert.equal(await page.locator('html').getAttribute('data-theme'),'light');
    // Live CAD theme changes repaint without dropping the model or requiring a reload.
    await page.goto(base+'/en/cad/');await page.waitForFunction(()=>document.getElementById('cad-status').textContent.includes('12'));
    const before=await page.locator('#cad-status').textContent();await page.locator('.theme').click();
    await page.waitForFunction(()=>{const c=document.getElementById('cad-canvas'),gl=c.getContext('webgl');return Math.abs(gl.getParameter(gl.COLOR_CLEAR_VALUE)[0]-20/255)<.001});
    assert.equal(await page.locator('#cad-status').textContent(),before);
    const blocked=await browser.newContext({colorScheme:'dark'});await blocked.addInitScript(()=>Object.defineProperty(window,'localStorage',{get(){throw new DOMException('Blocked','SecurityError')}}));
    const blockedPage=await blocked.newPage();await blockedPage.goto(base+'/en/gallery/');assert.equal(await blockedPage.locator('html').getAttribute('data-theme'),'light');await blockedPage.locator('.theme').click();assert.equal(await blockedPage.locator('html').getAttribute('data-theme'),'dark');await blocked.close();
    const nojs=await browser.newContext({javaScriptEnabled:false,colorScheme:'dark'});const staticPage=await nojs.newPage();
    for(const route of ['/en/','/de/gallery/','/en/cad/','/de/evidence/']) {await staticPage.goto(base+route);assert.equal(await staticPage.locator('body').evaluate(e=>getComputedStyle(e).backgroundColor),'rgb(243, 246, 248)');}
    await nojs.close();assert.deepEqual(errors,[]);
    fs.writeFileSync('qa/theme-results.json',JSON.stringify({passed:true,routes:routes.length,samples,errors,checks:['shared homepage palette across all routes/profiles','light-first with dark OS','saved theme before first paint','explicit toggle/persistence','OS changes ignored','reset to light','storage blocked/invalid','no-JS light default','gallery frames and caption contrast','CAD background/mesh colours','live CAD repaint','responsive layouts']},null,2));
    console.log(`PASS: ${samples.length} route/theme/viewport combinations; light-first under dark OS, shared palette, persistence/reset/storage fallback, gallery frames, live CAD colours; no console/HTTP errors.`);
  } finally {await browser.close();}
})().catch(error=>{console.error(error);process.exitCode=1});
