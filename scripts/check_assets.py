from pathlib import Path
from PIL import Image

root = Path(__file__).resolve().parents[1]
assets = root / 'input' / 'assets'

print('Asset inventory')
for path in sorted(assets.rglob('*')):
    if path.is_file():
        rel = path.relative_to(root)
        try:
            im = Image.open(path)
            print(f'{rel}\t{im.width}x{im.height}\t{path.stat().st_size/1024:.1f} KB')
        except Exception:
            print(f'{rel}\t{path.stat().st_size/1024:.1f} KB')
