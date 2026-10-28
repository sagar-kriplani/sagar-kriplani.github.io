/* Local-only STL/OBJ mesh viewer. No uploads, dependencies, telemetry or storage. */
(() => {
  'use strict';
  const canvas = document.getElementById('cad-canvas');
  if (!canvas) return;
  const de = document.documentElement.lang === 'de';
  const status = document.getElementById('cad-status');
  const input = document.getElementById('cad-file');
  const gl = canvas.getContext('webgl', {antialias:true, preserveDrawingBuffer:false});
  if (!gl) { status.textContent = de ? 'WebGL ist nicht verfügbar. Bitte einen Browser mit 3D-Unterstützung verwenden.' : 'WebGL is unavailable. Use a browser with 3D support.'; return; }
  const MAX_TRIANGLES = 500000;
  function shader(type, code) {
    const s = gl.createShader(type); gl.shaderSource(s, code); gl.compileShader(s);
    if (!gl.getShaderParameter(s, gl.COMPILE_STATUS)) throw Error('Shader compilation failed');
    return s;
  }
  const program = gl.createProgram();
  gl.attachShader(program, shader(gl.VERTEX_SHADER, `attribute vec3 p;attribute vec3 n;uniform vec2 angles;uniform vec2 pan;uniform float zoom;uniform float aspect;varying vec3 normal;vec3 rot(vec3 v){float a=angles.x,b=angles.y;vec3 q=vec3(cos(a)*v.x+sin(a)*v.z,v.y,-sin(a)*v.x+cos(a)*v.z);return vec3(q.x,cos(b)*q.y-sin(b)*q.z,sin(b)*q.y+cos(b)*q.z);}void main(){vec3 q=rot(p);gl_Position=vec4((q.x*zoom+pan.x)/aspect,q.y*zoom+pan.y,-q.z*.2,1.);normal=rot(n);}`));
  gl.attachShader(program, shader(gl.FRAGMENT_SHADER, `precision mediump float;varying vec3 normal;void main(){float l=.35+.65*abs(dot(normalize(normal),normalize(vec3(.4,.8,1.))));gl_FragColor=vec4(vec3(.25,.55,.59)*l,1.);}`));
  gl.linkProgram(program); if (!gl.getProgramParameter(program,gl.LINK_STATUS)) return;
  gl.useProgram(program);
  const positions = gl.createBuffer(), normals = gl.createBuffer();
  let count=0, yaw=.65, pitch=.4, zoom=.52, pan=[0,0];
  let dragging=null;
  function setBuffer(buffer,name,data) {
    gl.bindBuffer(gl.ARRAY_BUFFER,buffer);gl.bufferData(gl.ARRAY_BUFFER,data,gl.STATIC_DRAW);
    const loc=gl.getAttribLocation(program,name);gl.enableVertexAttribArray(loc);gl.vertexAttribPointer(loc,3,gl.FLOAT,false,0,0);
  }
  function draw() {
    const r=canvas.getBoundingClientRect(), ratio=Math.min(devicePixelRatio||1,2);
    canvas.width=Math.max(1,Math.floor(r.width*ratio));canvas.height=Math.max(1,Math.floor(r.height*ratio));
    gl.viewport(0,0,canvas.width,canvas.height);gl.clearColor(.91,.93,.91,1);gl.clear(gl.COLOR_BUFFER_BIT|gl.DEPTH_BUFFER_BIT);gl.enable(gl.DEPTH_TEST);
    gl.uniform2f(gl.getUniformLocation(program,'angles'),yaw,pitch);
    gl.uniform2fv(gl.getUniformLocation(program,'pan'),pan);
    gl.uniform1f(gl.getUniformLocation(program,'zoom'),zoom);
    gl.uniform1f(gl.getUniformLocation(program,'aspect'),canvas.width/canvas.height);
    gl.drawArrays(gl.TRIANGLES,0,count);
  }
  function reset(){yaw=.65;pitch=.4;zoom=.52;pan=[0,0];draw();}
  function loadMesh(vertices,label) {
    if (!vertices.length || vertices.length%9 || vertices.length/9>MAX_TRIANGLES) throw Error(de?'Ungültiges oder zu großes Netz.':'Invalid or oversized mesh.');
    const min=[Infinity,Infinity,Infinity],max=[-Infinity,-Infinity,-Infinity];
    for(let i=0;i<vertices.length;i++){const v=vertices[i];if(!Number.isFinite(v))throw Error(de?'Ungültige Koordinaten.':'Invalid coordinates.');const a=i%3;min[a]=Math.min(min[a],v);max[a]=Math.max(max[a],v);}
    const centre=min.map((v,i)=>(v+max[i])/2),extent=Math.max(...max.map((v,i)=>v-min[i]));
    if(!Number.isFinite(extent)||extent<=0)throw Error(de?'Das Netz hat keine räumliche Ausdehnung.':'Mesh has no spatial extent.');
    const p=new Float32Array(vertices.length),n=new Float32Array(vertices.length);
    for(let i=0;i<vertices.length;i++)p[i]=(vertices[i]-centre[i%3])*2/extent;
    for(let i=0;i<p.length;i+=9){const a=[p[i+3]-p[i],p[i+4]-p[i+1],p[i+5]-p[i+2]],b=[p[i+6]-p[i],p[i+7]-p[i+1],p[i+8]-p[i+2]];const v=[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]],len=Math.hypot(...v)||1;for(let j=0;j<9;j++)n[i+j]=v[j%3]/len;}
    setBuffer(positions,'p',p);setBuffer(normals,'n',n);count=p.length/3;reset();
    status.textContent=`${label} · ${(count/3).toLocaleString()} ${de?'Dreiecke · lokal geöffnet':'triangles · opened locally'}`;
  }
  function stl(buffer) {
    const view=new DataView(buffer),vertices=[];
    if(buffer.byteLength>=84){const faces=view.getUint32(80,true);if(faces>0&&84+faces*50<=buffer.byteLength){if(faces>MAX_TRIANGLES)throw Error(de?'Maximal 500.000 Dreiecke.':'Maximum 500,000 triangles.');for(let f=0;f<faces;f++)for(let j=0;j<9;j++)vertices.push(view.getFloat32(84+f*50+12+j*4,true));return vertices;}}
    const text=new TextDecoder().decode(buffer),re=/\bvertex\s+([-+\d.eE]+)\s+([-+\d.eE]+)\s+([-+\d.eE]+)/g;let match;
    while((match=re.exec(text))){vertices.push(Number(match[1]),Number(match[2]),Number(match[3]));if(vertices.length>MAX_TRIANGLES*9)throw Error('Mesh limit exceeded');}return vertices;
  }
  function obj(buffer) {
    const points=[],vertices=[];
    for(const line of new TextDecoder().decode(buffer).split(/\r?\n/)){
      const parts=line.trim().split(/\s+/);
      if(parts[0]==='v'){if(points.length>MAX_TRIANGLES*3)throw Error('Mesh limit exceeded');points.push(parts.slice(1,4).map(Number));}
      if(parts[0]==='f'){
        const face=parts.slice(1).map(t=>{const i=Number(t.split('/')[0]);if(!Number.isInteger(i)||!i)throw Error('Invalid OBJ index');const p=points[i<0?points.length+i:i-1];if(!p||p.length!==3)throw Error('Invalid OBJ vertex');return p;});
        for(let i=1;i<face.length-1;i++){vertices.push(...face[0],...face[i],...face[i+1]);if(vertices.length>MAX_TRIANGLES*9)throw Error('Mesh limit exceeded');}
      }
    }return vertices;
  }
  async function open(file) {
    if(!file)return;
    try {
      if(file.size>50*1024*1024)throw Error(de?'Dateigrenze: 50 MB.':'File limit: 50 MB.');
      const ext=file.name.split('.').pop().toLowerCase();if(!['stl','obj'].includes(ext))throw Error(de?'Bitte zuerst aus Inventor/FreeCAD als STL oder OBJ exportieren.':'Export from Inventor/FreeCAD as STL or OBJ first.');
      const data=await file.arrayBuffer();loadMesh(ext==='stl'?stl(data):obj(data),file.name);
    }catch(e){status.textContent=(de?'Datei konnte nicht geöffnet werden: ':'Could not open file: ')+e.message;}
    input.value='';
  }
  input.addEventListener('change',()=>open(input.files[0]));
  const drop=document.querySelector('.cad-stage');
  drop.addEventListener('dragover',e=>{e.preventDefault();drop.classList.add('drag-over');});
  drop.addEventListener('dragleave',()=>drop.classList.remove('drag-over'));
  drop.addEventListener('drop',e=>{e.preventDefault();drop.classList.remove('drag-over');open(e.dataTransfer.files[0]);});
  canvas.addEventListener('contextmenu',e=>e.preventDefault());
  canvas.addEventListener('pointerdown',e=>{dragging={x:e.clientX,y:e.clientY,pan:e.button===2||e.shiftKey};canvas.setPointerCapture(e.pointerId);canvas.focus();});
  canvas.addEventListener('pointermove',e=>{if(!dragging)return;const dx=e.clientX-dragging.x,dy=e.clientY-dragging.y;if(dragging.pan){pan[0]+=dx/canvas.clientHeight*2;pan[1]-=dy/canvas.clientHeight*2;}else{yaw+=dx*.01;pitch+=dy*.01;}dragging.x=e.clientX;dragging.y=e.clientY;draw();});
  canvas.addEventListener('pointerup',()=>{dragging=null;});canvas.addEventListener('pointercancel',()=>{dragging=null;});
  canvas.addEventListener('wheel',e=>{e.preventDefault();zoom=Math.max(.1,Math.min(8,zoom*Math.exp(-e.deltaY*.001)));draw();},{passive:false});
  document.querySelectorAll('[data-cad-action]').forEach(b=>b.addEventListener('click',()=>{const a=b.dataset.cadAction;if(a==='reset')return reset();if(a==='zoom-in')zoom=Math.min(8,zoom*1.2);if(a==='zoom-out')zoom=Math.max(.1,zoom/1.2);if(a==='front'){yaw=0;pitch=0;}if(a==='top'){yaw=0;pitch=Math.PI/2;}draw();}));
  canvas.addEventListener('keydown',e=>{if(!['ArrowLeft','ArrowRight','ArrowUp','ArrowDown','+','-','0'].includes(e.key))return;e.preventDefault();if(e.key==='0')return reset();if(e.key==='ArrowLeft')yaw-=.12;if(e.key==='ArrowRight')yaw+=.12;if(e.key==='ArrowUp')pitch-=.12;if(e.key==='ArrowDown')pitch+=.12;if(e.key==='+')zoom=Math.min(8,zoom*1.2);if(e.key==='-')zoom=Math.max(.1,zoom/1.2);draw();});
  new ResizeObserver(draw).observe(canvas);
  const corners=[[-1,-1,-1],[1,-1,-1],[1,1,-1],[-1,1,-1],[-1,-1,1],[1,-1,1],[1,1,1],[-1,1,1]],triangles=[[0,1,2],[0,2,3],[4,6,5],[4,7,6],[0,4,5],[0,5,1],[3,2,6],[3,6,7],[0,3,7],[0,7,4],[1,5,6],[1,6,2]];
  loadMesh(triangles.flatMap(t=>t.flatMap(i=>corners[i])),de?'Demo-Würfel, kein Projektmodell':'Demo cube, not a project model');
})();
