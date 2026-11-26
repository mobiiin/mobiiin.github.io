# Mobin Habibpour — Portfolio

A responsive, single-page research portfolio for computer vision, robotics, and autonomous wildfire intelligence.

## Publish with GitHub Pages

This site is in [`mobiiin/personal_website`](https://github.com/mobiiin/personal_website).

1. In the repository, open **Settings → Pages** and choose **GitHub Actions** as the build and deployment source.
2. Open **Actions** and rerun **Deploy portfolio to GitHub Pages**. The initial run happened before Pages was enabled and stopped during setup.
3. After a successful run, the site will be available at `https://mobiiin.github.io/`.

The site is plain HTML, CSS, and JavaScript. No build step or package installation is required.

## Before publishing

- Confirm the contact email and profile links in `index.html`.
- Check publication metadata and paper links against the latest CV.
- Replace or remove any project card that is not ready to be public.


## Homepage slideshow

Add images and video clips to the `slideshow/` folder. Supported image formats are JPG, PNG, GIF, WebP, and AVIF; supported video formats are MP4, WebM, OGG, and MOV (browser support varies, so MP4 is recommended). Files appear in alphabetical order; use names such as `01-robot.jpg` and `02-flight.mp4` to control their order. Each slide appears for one second, and videos play muted. Use descriptive filenames, which also serve as accessible labels.

The GitHub Pages workflow generates the media list automatically when you push to `main`. To preview new files locally before pushing, run `python3 scripts/generate-slideshow.py` from the repository root, then open `index.html`. The slideshow is hidden until at least one supported file is present. Visitors can pause it, and it starts paused when reduced motion is requested.

### Optimize slideshow images

To create smaller, high-quality WebP copies for local previews, install Pillow (`python3 -m pip install Pillow`), then run `python3 scripts/optimize-slideshow.py` followed by `python3 scripts/generate-slideshow.py`. Originals remain in `slideshow/`; generated copies are stored in `slideshow/optimized/` and are not committed. GitHub Actions performs these steps automatically when the site is deployed. Animated images and videos keep their original files.
