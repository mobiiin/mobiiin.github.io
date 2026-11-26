#!/usr/bin/env python3
"""Generate the static slideshow manifest from files in slideshow/."""
import json
from pathlib import Path
from urllib.parse import quote

root = Path(__file__).resolve().parent.parent
folder = root / 'slideshow'
image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.webp', '.avif'}
video_extensions = {'.mp4', '.webm', '.ogg', '.mov'}
items = []
for path in sorted(folder.iterdir(), key=lambda p: p.name.casefold()):
    extension = path.suffix.lower()
    if not path.is_file() or extension not in image_extensions | video_extensions:
        continue
    optimized = folder / 'optimized' / (path.name + '.webp')
    source = 'optimized/' + quote(optimized.name) if optimized.is_file() and extension in image_extensions else quote(path.name)
    items.append({
        'src': 'slideshow/' + source,
        'type': 'video' if extension in video_extensions else 'image',
        'label': path.stem.replace('_', ' ').replace('-', ' '),
    })
(folder / 'media.js').write_text('window.slideshowMedia = ' + json.dumps(items, ensure_ascii=True, indent=2) + ';\n', encoding='utf-8')
