/* Verify real encrypted delivery without printing or persisting the access password. */
const {chromium}=require(process.env.PLAYWRIGHT_MODULE || 'playwright');
const fs=require('node:fs');const path=require('node:path');const assert=require('node:assert/strict');
const {createHash}=require('node:crypto');
const originals=new Map(JSON.parse(fs.readFileSync('assets/protected/manifest.json','utf8')).map(record=>[record.key,record.source_sha256]));
const digest=bytes=>createHash('sha256').update(bytes).digest('hex');
(async()=>{
 const privateRoot=path.resolve('..','private-portfolio-access');
 const password=fs.readFileSync(path.join(privateRoot,'evidence-password.txt'),'utf8').trim();
 const browser=await chromium.launch({headless:true});
 try{
  const context=await browser.newContext({acceptDownloads:true,reducedMotion:'reduce'});
  const page=await context.newPage();const errors=[];const requests=[];
  page.on('pageerror',e=>errors.push(String(e)));
  page.on('request',r=>{if(r.url().startsWith('http'))requests.push({url:r.url(),body:r.postData()||''})});
  for(const lang of ['en','de']){
   await page.goto(`http://127.0.0.1:4174/${lang}/evidence/`);
   assert.equal(await page.locator('[data-download]').count(),33);
   assert.equal(await page.locator('img[src*="/assets/evidence/"]').count(),31);
   const plaintext=await page.request.get('http://127.0.0.1:4174/assets/evidence/nest-reference.webp');
   assert.equal(plaintext.status(),200);
   assert.notEqual(digest(await plaintext.body()),originals.get('nest-reference'),'Preview must be a separate derivative');
   await page.locator('#nest-reference [data-download]').click();
   assert.equal(await page.locator('.document-unlock').isVisible(),false);
   await page.waitForFunction(()=>document.querySelector('.viewer-image').complete&&document.querySelector('.viewer-image').naturalWidth>0);
   assert.equal(await page.locator('.viewer-image-stage').isVisible(),true);
   await page.locator('.viewer-download').click();
   assert.equal(await page.locator('.document-unlock').isVisible(),true);
   assert.equal(await page.locator('.viewer-original-download').isVisible(),false);
   await page.locator('#document-password').fill('incorrect-access-password');
   await page.locator('.document-unlock button').click();
   await page.waitForFunction(()=>!document.querySelector('.document-unlock button').disabled);
   assert.equal(await page.locator('.document-unlock').isVisible(),true);
   assert.equal(await page.locator('.viewer-original-download').isVisible(),false);
   assert.ok((await page.locator('.unlock-status').innerText()).length>0);
   await page.locator('#document-password').fill(password);
   await page.keyboard.press('ArrowLeft');
   assert.ok((await page.locator('#viewer-caption').innerText()).includes('NeSt'),'Editing password should not navigate documents');
   await page.locator('.document-unlock button').click();
   await page.waitForFunction(()=>document.querySelector('.document-unlock').hidden);
   assert.equal(await page.locator('#document-password').inputValue(),'');
   assert.equal(await page.locator('.viewer-image').evaluate(img=>img.complete&&img.naturalWidth>0),true);
   const downloadEvent=page.waitForEvent('download');await page.locator('.viewer-original-download').click();
   const download=await downloadEvent;
   assert.equal(download.suggestedFilename(),'nest-reference.webp');
   const recovered=fs.readFileSync(await download.path());
   assert.equal(digest(recovered),originals.get('nest-reference'),'Decrypted download must match the private original');
   await page.keyboard.press('Escape');
   assert.equal(await page.locator('.viewer-image').getAttribute('src'),null);
   assert.equal(await page.locator('.viewer-original-download').getAttribute('href'),null);
   await page.locator('#nest-reference [data-download]').click();
   assert.equal(await page.locator('.document-unlock').isVisible(),false,'Reopening preview must not require a password');
   await page.locator('.viewer-download').click();
   assert.equal(await page.locator('.document-unlock').isVisible(),true,'Original download must require password again');
   await page.keyboard.press('Escape');
   for(const [key,pages] of [['brooks-thesis-reference',3],['nest-recommendation',1]]) {
    const reference=page.locator('#'+key);
    assert.equal(await reference.locator('[data-viewer]').count(),pages);
    assert.deepEqual(await reference.locator('[data-viewer]').evaluateAll(links=>[...new Set(links.map(a=>a.dataset.download))]),['/assets/protected/'+key+'.skvault']);
    for(let i=0;i<pages;i++) {
     await reference.locator('[data-viewer]').nth(i).click();
     assert.equal(await page.locator('.document-unlock').isVisible(),false);
     await page.waitForFunction(()=>document.querySelector('.viewer-image').complete&&document.querySelector('.viewer-image').naturalWidth>0);
     if(pages>1)assert.ok((await page.locator('#viewer-caption').textContent()).includes(lang==='de'?`Seite ${i+1} von ${pages}`:`Page ${i+1} of ${pages}`));
     await page.locator('.viewer-download').click();
     await page.locator('#document-password').fill('incorrect-pdf-password');await page.locator('.document-unlock button').click();
     await page.waitForFunction(()=>!document.querySelector('.document-unlock button').disabled);
     assert.equal(await page.locator('.viewer-original-download').isVisible(),false);
     await page.locator('#document-password').fill(password);await page.locator('.document-unlock button').click();
     await page.waitForFunction(()=>!document.querySelector('.viewer-original-download').hidden);
     assert.equal(await page.evaluate(async()=>{const response=await fetch(document.querySelector('.viewer-original-download').href);return response.headers.get('content-type')}),'application/pdf');
     const pdfEvent=page.waitForEvent('download');await page.locator('.viewer-original-download').click();
     const pdf=await pdfEvent;
     assert.equal(pdf.suggestedFilename(),key+'.pdf');
     assert.equal(digest(fs.readFileSync(await pdf.path())),originals.get(key),'Recovered PDF must match the private original exactly');
     await pdf.delete();
     await page.keyboard.press('Escape');
     assert.equal(await page.locator('.viewer-original-download').getAttribute('href'),null);
    }
   }
   for(const profile of ['mechanical','research']) {
    await page.goto(`http://127.0.0.1:4174/${lang}/${profile}/`);
    assert.equal(await page.locator(`.proof-card[href="/${lang}/evidence/#brooks-thesis-reference"]`).count(),1);
    if(profile==='mechanical')assert.equal(await page.locator(`.evidence-groups a[href="/${lang}/evidence/#nest-recommendation"]`).count(),1);
   }
  }
  // Project gallery, diagram and portrait use the same download-only password flow.
  for(const sample of [
   {route:'en/gallery/',selector:'.gallery-card:visible [data-viewer]'},
   {route:'en/',selector:'#pau .project-source-image [data-viewer]'},
   {route:'en/',selector:'.portrait-preview'}
  ]){
   await page.goto('http://127.0.0.1:4174/'+sample.route);
   const link=page.locator(sample.selector).first();
   const encrypted=await link.getAttribute('data-download');
   assert.ok(encrypted,'Every image viewer must have a protected original download');
   const preview=await link.getAttribute('href');
   await link.click();
   assert.equal(await page.locator('.document-unlock').isVisible(),false);
   await page.locator('.viewer-download').click();
   await page.locator('#document-password').fill(password);
   await page.locator('.document-unlock button').click();
   await page.waitForFunction(()=>!document.querySelector('.viewer-original-download').hidden);
   assert.ok((await page.locator('.viewer-image').getAttribute('src')).endsWith(preview),'Unlocking a download must not replace the public preview');
   const event=page.waitForEvent('download');await page.locator('.viewer-original-download').click();
   const downloaded=await event;
   assert.equal(digest(fs.readFileSync(await downloaded.path())),originals.get(path.basename(encrypted,'.skvault')),'Project original must download byte-exactly');
   await page.keyboard.press('Escape');
  }
  await page.goto('http://127.0.0.1:4174/de/evidence/');
  // AES-GCM must reject a modified encrypted package, even with the correct password.
  await page.route('**/assets/protected/nest-reference.skvault',async route=>{
   const packet=JSON.parse(fs.readFileSync('assets/protected/nest-reference.skvault','utf8'));
   packet.ciphertext=(packet.ciphertext[0]==='A'?'B':'A')+packet.ciphertext.slice(1);
   await route.fulfill({contentType:'application/json',body:JSON.stringify(packet)});
  });
  await page.locator('#nest-reference [data-download]').click();
  await page.locator('.viewer-download').click();
  await page.locator('#document-password').fill(password);await page.locator('.document-unlock button').click();
  await page.waitForFunction(()=>!document.querySelector('.document-unlock button').disabled);
  assert.equal(await page.locator('.document-unlock').isVisible(),true);
  assert.equal(await page.locator('.viewer-original-download').isVisible(),false);
  await page.screenshot({path:'qa/protected-access.png'});
  assert.ok(requests.every(r=>!r.url.includes(password)&&!r.body.includes(password)),'Password must never enter a network request');
  assert.ok(requests.every(r=>new URL(r.url).hostname==='127.0.0.1'),'No third-party request');
  assert.equal(await page.evaluate(()=>Object.keys(localStorage).some(k=>k!=='portfolio-theme')),false);
  assert.equal((await context.cookies()).length,0);assert.deepEqual(errors,[]);
  fs.writeFileSync('qa/security-results.json',JSON.stringify({passed:true,protectedRecords:31,protectedOriginals:originals.size,publicDocumentPages:33,tests:['public previews visible without password','separate encrypted original downloads','Brooks reference and NeSt recommendation in both languages','original PDF MIME type and byte-exact download from every page','gallery/diagram/portrait originals','wrong password rejected','correct password decrypts','download byte-identical','tampering rejected','password editing preserves selection','password not transmitted','password not persisted','close revokes image/download','reopening requires password'],errors},null,2));
  console.log(`PASS: 31 records / 33 public document pages / ${originals.size} protected originals; byte-exact PDF downloads, wrong-password/tamper rejection, profiles/languages and no password transmission/storage.`);
 }finally{await browser.close()}
})().catch(e=>{console.error(e);process.exit(1)});
