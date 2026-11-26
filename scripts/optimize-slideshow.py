#!/usr/bin/env python3
"""Create smaller slideshow images while keeping the originals untouched."""
from pathlib import Path
from PIL import Image, ImageOps, UnidentifiedImageError

folder = Path(__file__).resolve().parent.parent / 'slideshow'
output = folder / 'optimized'
output.mkdir(exist_ok=True)
formats = {'.jpg', '.jpeg', '.png', '.webp', '.avif'}
expected = set()
original_bytes = optimized_bytes = count = 0
for path in sorted(folder.iterdir()):
    if not path.is_file() or path.suffix.lower() not in formats:
        continue
    target = output / (path.name + '.webp')
    try:
        with Image.open(path) as image:
            # Preserve animated files by using their originals in the manifest.
            if getattr(image, 'is_animated', False):
                continue
            image = ImageOps.exif_transpose(image)
            image.thumbnail((1600, 1600), Image.Resampling.LANCZOS)
            if image.mode not in ('RGB', 'RGBA'):
                image = image.convert('RGBA' if 'transparency' in image.info else 'RGB')
            options = {'format': 'WEBP', 'quality': 85, 'method': 6}
            if image.info.get('icc_profile'):
                options['icc_profile'] = image.info['icc_profile']
            image.save(target, **options)
    except (OSError, UnidentifiedImageError) as error:
        target.unlink(missing_ok=True)
        print(f'Skipping {path.name}: {error}')
        continue
    expected.add(target.name)
    count += 1
    original_bytes += path.stat().st_size
    optimized_bytes += target.stat().st_size
for path in output.glob('*.webp'):
    if path.name not in expected:
        path.unlink()
print(f'Optimized {count} images: {original_bytes / 1_000_000:.1f} MB → {optimized_bytes / 1_000_000:.1f} MB')
