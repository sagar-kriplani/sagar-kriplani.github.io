"""Public viewable previews with separately encrypted original-image downloads.
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
from evidence import RECORDS

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--rotate',action='store_true',help='Re-encrypt every original with the current local password')
args=parser.parse_args()
ROOT=Path(__file__).resolve().parent.parent
PRIVATE=ROOT.parent/'private-portfolio-access'
assert PRIVATE.resolve().parent==ROOT.parent.resolve() and PRIVATE.resolve()!=ROOT.resolve()
PRIVATE.mkdir(exist_ok=True)
PASSWORD=PRIVATE/'evidence-password.txt'
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
    items.append((key,ROOT/'assets/evidence'/name,PRIVATE/'evidence'/name))
for source in sorted((ROOT/'assets/gallery').glob('*.webp')):
    items.append(('gallery-'+source.stem,source,PRIVATE/'originals/gallery'/source.name))
for source in sorted((ROOT/'assets/evidence').glob('*')):
    if source.suffix in ('.webp','.svg') and source.stem not in {r['key'] for r in RECORDS}:
        items.append(('project-'+source.stem,source,PRIVATE/'originals/evidence'/source.name))
portrait=ROOT/'assets/images/sagar-kriplani.webp'
items.append(('portrait',portrait,PRIVATE/'originals/images'/portrait.name))
manifest=[]
for index,(key,preview,backup) in enumerate(items):
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
    if preview.suffix=='.webp':
        with Image.open(backup) as image:
            # Public derivative for browsing; the byte-exact source is a separate encrypted download.
            image.thumbnail((1200,1400),Image.Resampling.LANCZOS)
            image.save(preview,format='WEBP',quality=72,method=6)
    else:
        # A public diagram is inherently saveable; its official source-file download uses the same password flow.
        preview.write_bytes(data)
    manifest.append(dict(key=key,preview='/'+preview.relative_to(ROOT).as_posix(),source_sha256=digest,encrypted_sha256=hashlib.sha256(target.read_bytes()).hexdigest()))
    if (index+1)%25==0:print('Prepared',index+1,'public previews and encrypted originals',flush=True)
(OUT/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
(PRIVATE/'README.md').write_text('Private portfolio access\n\nThe password is in evidence-password.txt. Keep it in your password manager and share it privately with approved recipients. Never commit this directory. The evidence/originals folders contain original images. Public previews are intentionally visible and can be saved or captured. Passwords protect only separately encrypted original-file downloads, not the information visible in those previews. Public Git history also contains earlier originals. Previously shared passwords/packages cannot be revoked by a static website.\n',encoding='utf-8')
print('Prepared',len(manifest),'visible previews and encrypted original downloads. No credential was published.')
