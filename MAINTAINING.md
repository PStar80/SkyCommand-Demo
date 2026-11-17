# Maintaining this showcase

This is a documentation-only repository. It is separate from the private SkyCommand implementation and does not need a local clone or a build pipeline.

## Layout

- `README.md`: public landing page.
- `assets/brand/`: blue-metallic SVG header and explicit static/mobile alternatives.
- `assets/screenshots/`: reviewed application captures only.
- `docs/features.md`: feature tour.
- `docs/architecture.md`: conceptual architecture.
- `docs/walkthrough.md`: proposed demonstration sequence.
- `docs/gallery.md`: published screenshot captions and links.

## Adding media

Upload reviewed captures into `assets/screenshots`, then link to the files from the gallery. On a Markdown page in `docs`, the relative path begins with `../assets/screenshots/`. On the root README, it begins with `./assets/screenshots/`.

Check the image at ordinary desktop and phone widths. Add useful alt text and describe what is visible without claiming more than the capture shows.

## Keeping the public boundary clear

Copy only individually reviewed presentation material. Do not fork, mirror, import, or change the visibility of the private application repository to create this showcase. Do not add runtime configuration, account authentication files, original logs, or private implementation history.

## Updating the profile link

After the repository exists and its landing page is published, replace the profile's planned-showcase wording with a link to this repository. Keep the walkthrough email link as an additional contact option. Do not publish a link to a repository that has not been created.

## Content basis

The initial documentation is derived from the public `PStar80/PStar80` profile README as inspected at blob `2b23751cc5c4aa723ada3af6fb58b1d5f68255f9`, plus the owner's stated plan for a documentation-and-screenshots showcase. It is not a fresh audit of the private application source. Verify new claims against a current demonstration before adding them.

The header artwork is adapted from the user-approved blue-metallic profile asset package. This repository does not add or change a software licence for the private SkyCommand application.
