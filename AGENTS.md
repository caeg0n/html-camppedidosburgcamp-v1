# Repository Guidelines

## Project Structure & Module Organization
This repository is a static web app for Big Brasa with three entry points:
- `index.html`, `styles.css`, `script.js`: public menu page.
- `compras/` (`index.html`, `compras.css`, `compras.js`): shopping/cart flow with WhatsApp checkout.
- `admin/` (`index.html`, `admin.css`, `admin.js`): browser editor for `menu-data.js` with GitHub save.

Shared data lives in `menu-data.js`. Visual assets are in the repo root (`logo*.png`, `cardapio.*`, `bg_extracted.jpg`). Utility scripts include `deploy.bat` (Windows deploy), `admin/encrypt-token.mjs` (token encryption), and small Python helpers.

## Build, Test, and Development Commands
No build step is required for local usage.
- `python3 -m http.server 5500` (run in repo root): serve locally and open `http://localhost:5500`.
- `node admin/encrypt-token.mjs "TOKEN" "PASSPHRASE"`: generate encrypted token blob for `admin/admin.js`.
- `python3 read_pdf.py`: extract text from `cardapio.pdf` (requires `pypdf`).
- `deploy.bat [owner] [repo] [domain|--provisorio]`: automated GitHub/GitHub Pages deploy on Windows.

## Coding Style & Naming Conventions
- Use 2-space indentation in HTML/CSS/JS, matching existing files.
- Keep JavaScript in plain ES modules/scripts with semicolons and small helper functions.
- Use descriptive lowercase file names (`menu-data.js`, `compras.js`); keep section IDs and keys stable because UI logic depends on them.
- Preserve Portuguese user-facing copy unless the change explicitly updates content language.

## Testing Guidelines
There is currently no automated test suite. Validate changes manually before PR:
- Open `index.html`, `compras/`, and `admin/` in a local server.
- Confirm menu rendering from `menu-data.js`, price formatting, cart totals, and WhatsApp message output.
- In admin, verify save flow and error handling when token/passphrase is missing.

## Commit & Pull Request Guidelines
Current history uses short deploy-style subjects (example: `Deploy cardapio web`). Prefer concise imperative subjects, optionally with scope, e.g. `compras: corrigir total do carrinho`.

For PRs, include:
- What changed and why.
- Affected pages/files (for example `compras/compras.js`).
- Manual test evidence (steps + result, screenshots for UI changes).
- Any deployment/security impact (`deploy.bat`, token handling, `.secrets`).
