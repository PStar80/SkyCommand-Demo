# Maintaining This Showcase

This is a documentation-only repository. It is separate from the private SkyCommand implementation and does not need a local clone or a recurring build pipeline.

## Layout

- `README.md`: public landing page, with capabilities, screenshots, product architecture and documentation links.
- `assets/brand/hero*.svg`: full-width animated banner and explicit desktop/mobile static alternatives.
- `assets/brand/capabilities*.svg`: six capability cards and their desktop/mobile static alternatives.
- `assets/brand/architecture*.svg`: conceptual product architecture and its desktop/mobile static alternatives.
- `assets/screenshots/`: reviewed application captures only.
- `docs/features.md`: feature tour.
- `docs/architecture.md`: product architecture, agent capabilities and the separate development method.
- `docs/walkthrough.md`: proposed demonstration sequence.
- `docs/gallery.md`: published screenshot captions and links.

## Updating Presentation Assets

Retain the blue palette, square metallic frames and readable text. The banner labels are **Reusable Tools**, **Durable Workflows**, **AI Agents** and **Observable Execution**.

For each changed animated asset, update its `-static.svg` counterpart and mobile variant. Static alternatives must contain no animation styles or SVG animation elements. Keep SVG text descriptions and README alternative text aligned with the visible content.

The shared UI/API box is a conceptual grouping: the UI still calls platform services. The product architecture is distinct from the Cloud Agent / Operator / Dropbox / Local Agent development flow shown on the profile. Native work-order integration remains a Phase 20 plan until supported by delivery evidence.

## Adding Media

Upload reviewed captures into `assets/screenshots`, then link to the files from the gallery. On a Markdown page in `docs`, the relative path begins with `../assets/screenshots/`. On the root README, it begins with `./assets/screenshots/`.

Place a small selection in the README's **See the Platform** section before the architecture discussion. Keep the complete captioned sequence in the gallery. Replace pending-screenshot wording only after actual captures are published.

Check each image at ordinary desktop and phone widths. Add useful alt text and describe what is visible without claiming more than the capture shows.

## Keeping the Public Boundary Clear

Copy only individually reviewed presentation material. Do not fork, mirror, import, or change the visibility of the private application repository to create this showcase. Do not add runtime configuration, account authentication files, original logs, or private implementation history.

## Profile Link

The profile already links to this repository. Preserve that link and the walkthrough email contact when changing the landing page.

## Content Basis

The initial documentation was derived from the public profile and the owner's plan for a documentation-and-screenshots showcase. The refreshed presentation uses the current showcase documentation and the owner's clarified development process, shared access routes and automation endpoints. It is not a fresh audit of the private application source. Verify new claims against a current demonstration before adding them.

The embedded header artwork is retained from the approved blue-metallic profile asset package. Decorative artwork and conceptual diagrams are not application screenshots or live telemetry. This repository does not add or change a software licence for the private SkyCommand application.
