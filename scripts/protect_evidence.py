"""Public viewable previews with separately encrypted original-file downloads.
Passwords and original backups stay outside the repository. Public previews can be saved.
"""
from pathlib import Path
import base64
import hashlib
import json
import secrets
import argparse
from PIL import Image
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from evidence import RECORDS, preview_paths

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--rotate',action='store_true',help='Re-encrypt every original with the current local password')
parser.add_argument('--only',help='Prepare one selected record, preserving every unrelated preview and package')
args=parser.parse_args()
ROOT=Path(__file__).resolve().parent.parent
PRIVATE=ROOT.parent/'private-portfolio-access'
assert PRIVATE.resolve().parent==ROOT.parent.resolve() and PRIVATE.resolve()!=ROOT.resolve()
PRIVATE.mkdir(exist_ok=True)
PASSWORD=PRIVATE/'evidence-password.txt'
assert not args.only or PASSWORD.exists(), 'Selected-record updates require the existing access password'
if not PASSWORD.exists():PASSWORD.write_text(secrets.token_urlsafe(30),encoding='utf-8')
password=PASSWORD.read_text(encoding='utf-8').strip()
assert len(password)>=20,'Use a long, unique password'
OUT=ROOT/'assets/protected'
OUT.mkdir(exist_ok=True)
old_manifest=json.loads((OUT/'manifest.json').read_text()) if (OUT/'manifest.json').exists() else []
old={r['key']:r for r in old_manifest}
items=[]
for record in RECORDS:
    key=record['key'];name=key+'.webp'
    previews=[ROOT/path.lstrip('/') for path in preview_paths(record)]
    if record.get('original'):
        original=record['original']
        assert Path(original).name==original and original.endswith('.pdf'), 'Expected a local PDF basename'
        backup=PRIVATE/'originals/documents'/original
        assert backup.exists() and all(path.exists() for path in previews), 'Prepare private original and redacted pages first'
    else:backup=PRIVATE/'evidence'/name
    items.append((key,previews[0],backup,previews[1:]))
for source in sorted((ROOT/'assets/gallery').glob('*.webp')):
    items.append(('gallery-'+source.stem,source,PRIVATE/'originals/gallery'/source.name,[]))
document_previews={Path(path).stem for record in RECORDS for path in preview_paths(record)}
for source in sorted((ROOT/'assets/evidence').glob('*')):
    if source.suffix in ('.webp','.svg') and source.stem not in document_previews:
        items.append(('project-'+source.stem,source,PRIVATE/'originals/evidence'/source.name,[]))
portrait=ROOT/'assets/images/sagar-kriplani.webp'
items.append(('portrait',portrait,PRIVATE/'originals/images'/portrait.name,[]))
if args.only:
    items=[item for item in items if item[0]==args.only]
    assert len(items)==1, 'Unknown or duplicate record key'
selected_keys={item[0] for item in items}
manifest=[record for record in old_manifest if record['key'] not in selected_keys] if args.only else []
for index,(key,preview,backup,extra_previews) in enumerate(items):
    backup.parent.mkdir(parents=True,exist_ok=True)
    if not backup.exists():
        assert preview.exists(),'Original missing: '+key
        backup.write_bytes(preview.read_bytes())
    data=backup.read_bytes();name=backup.name
    digest=hashlib.sha256(data).hexdigest()
    target=OUT/(key+'.skvault')
    if args.rotate or key not in old or old[key]['source_sha256']!=digest or not target.exists():
        salt=secrets.token_bytes(16);iv=secrets.token_bytes(12)
        derived=PBKDF2HMAC(algorithm=hashes.SHA256(),length=32,salt=salt,iterations=600000).derive(password.encode('utf-8'))
        aad=('SK-EVIDENCE-v1:'+name).encode('utf-8')
        ciphertext=AESGCM(derived).encrypt(iv,data,aad)
        assert AESGCM(derived).decrypt(iv,ciphertext,aad)==data
        encode=lambda value:base64.b64encode(value).decode('ascii')
        packet=dict(format='SK-EVIDENCE-v1',iterations=600000,salt=encode(salt),iv=encode(iv),filename=name,ciphertext=encode(ciphertext))
        target.write_text(json.dumps(packet,separators=(',',':')),encoding='utf-8')
    if backup.suffix=='.pdf':
        # A PDF-backed record uses separately reviewed raster redactions. Never
        # recreate these public pages from the unredacted original automatically.
        assert data.startswith(b'%PDF-') and preview.exists()
    elif preview.suffix=='.webp':
        with Image.open(backup) as image:
            # Public derivative for browsing; the byte-exact source is a separate encrypted download.
            image.thumbnail((1200,1400),Image.Resampling.LANCZOS)
            image.save(preview,format='WEBP',quality=72,method=6)
    else:
        # A public diagram is inherently saveable; its official source-file download uses the same password flow.
        preview.write_bytes(data)
    entry=dict(key=key,preview='/'+preview.relative_to(ROOT).as_posix(),source_sha256=digest,encrypted_sha256=hashlib.sha256(target.read_bytes()).hexdigest())
    if extra_previews:entry['previews']=['/'+path.relative_to(ROOT).as_posix() for path in extra_previews]
    manifest.append(entry)
    if (index+1)%25==0:print('Prepared',index+1,'public previews and encrypted originals',flush=True)
(OUT/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
(PRIVATE/'README.md').write_text('Private portfolio access\n\nThe password is in evidence-password.txt. Keep it in your password manager and share it privately with approved recipients. Never commit this directory. The evidence/originals folders contain original images. Public previews are intentionally visible and can be saved or captured. Passwords protect only separately encrypted original-file downloads, not the information visible in those previews. Public Git history also contains earlier originals. Previously shared passwords/packages cannot be revoked by a static website.\n',encoding='utf-8')
print('Prepared',len(items),'selected records;',len(manifest),'protected originals in manifest. No credential was published.')
