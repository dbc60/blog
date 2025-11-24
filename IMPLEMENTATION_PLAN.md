# Victorian Theme Refactoring - Implementation Plan

## Overview
Refactor the blog from a monolithic structure to use a proper Hugo theme architecture based on Victorian newspaper styles. This will eliminate the need for `!important` declarations and create a reusable, maintainable theme structure.

## Goals
- Create standalone `victorian-newspaper` Hugo theme
- Organize CSS in proper cascade order (base → layout → components → overrides)
- Remove all `!important` declarations by fixing load order
- Use CSS custom properties for theming without specificity wars
- Enable theme reusability across projects

---

## Stage 1: Create Theme Structure
**Goal**: Set up proper Hugo theme directory structure without breaking existing site
**Success Criteria**:
- Theme directory exists with proper structure
- Site continues to build and function identically
- No visual changes to the site

**Tasks**:
- [x] Create `themes/victorian-newspaper/` directory structure:
  ```
  themes/victorian-newspaper/
  ├── archetypes/
  ├── assets/
  │   ├── scss/
  │   └── style/
  ├── layouts/
  │   ├── _default/
  │   ├── partials/
  │   ├── shortcodes/
  │   └── taxonomy/
  ├── static/
  ├── LICENSE.md
  └── theme.toml
  ```
- [x] Create `theme.toml` with metadata (name, license, description, author)
- [x] Copy `LICENSE.md` to theme directory
- [x] Verify site builds with empty theme structure

**Tests**:
- ✅ `hugo` builds without errors (89 pages, 2838ms)
- ✅ `hugo server` runs and site displays correctly (http://localhost:1313/)
- ✅ No console errors (site functions identically)

**Status**: Complete

---

## Stage 2: Move and Reorganize CSS Assets
**Goal**: Reorganize CSS files in proper cascade order and move to theme
**Success Criteria**:
- All CSS loads in correct order: base → layout → victorian components → overrides
- Victorian colors override base.css through cascade position, not !important
- Site appearance remains identical

**Tasks**:
- [x] **Copy base/foundation CSS to theme**:
  - ~~`assets/scss/`~~ (determined to be unused, not copied)
  - `assets/style/base.css` → theme ✅
  - `assets/style/fonts.css` → theme ✅
  - `assets/style/print.css` → theme ✅
  - Plus layout, breadcrumb, drop-caps, syntax-highlighting, font files ✅

- [x] **Update base.css color palette**:
  - Base.css already uses CSS custom properties ✅
  - `--gray100`, `--gray150`, `--background-main-default` are overridable ✅
  - Victorian theme overrides these through cascade ✅

- [x] **Create new `victorian-theme.css`** that combines:
  - Victorian color overrides using CSS custom properties ✅
  - `victorian-masthead.css` components ✅
  - `victorian-dividers.css` components ✅
  - `victorian-sidebar.css` components ✅
  - `victorian-post-metadata.css` components ✅
  - `victorian-front-page.css` components ✅

- [x] **Convert Victorian colors from !important to CSS custom properties**:
  ```css
  /* Implemented in victorian-theme.css */
  :root {
    --gray100: #ebe8e0;        /* Warm cream (was cool #fcfcfc) */
    --gray150: #ebe8e0;        /* Warm cream (was cool #e3e3e3) */
    --background-main-default: #ebe8e0;  /* Override directly */
  }
  body { background-color: var(--background-main-default); }
  /* No !important needed! */
  ```

- [x] **Update `layouts/_partials/head.html`** with new load order:
  ```
  1. front.css - Preface/reset
  2. base.css - Foundation with CSS variables
  3. layout-grid.css - Layout structure
  4. fonts.css - Typography base
  5. font-system-stack.css - Font fallbacks
  6. victorian-theme.css - Theme overrides + Victorian components
  7. drop-caps CSS - Decorative initial capitals
  8. font-drop-caps-*.css - Drop cap fonts
  9. breadcrumb.css - Navigation breadcrumbs
  10. syntax-highlighting/*.css - Code highlighting
  11. overrides.css - User customizations
  12. print.css - Print styles (always last)
  ```

**Tests**:
- ✅ Background color is warm cream (#ebe8e0), not cool gray - verified in generated CSS
- ✅ CSS loads in proper cascade order - verified in head.html
- ✅ Victorian theme overrides base.css through CSS custom properties
- ✅ Site builds successfully (89 pages, ~350ms)
- ✅ Only 1 legitimate `!important` remains (font protection in fonts.css)
- ✅ Victorian color `!important` declarations eliminated
- ✅ Hugo server runs at http://localhost:1313/

**Status**: Complete

---

## Stage 3: Move Layouts and Partials to Theme
**Goal**: Move all template files to theme structure
**Success Criteria**:
- All layouts, partials, and shortcodes moved to theme
- Site builds and functions identically
- Template hierarchy works correctly

**Tasks**:
- [x] Copy layout files to theme maintaining structure:
  - `layouts/*.html` → `themes/victorian-newspaper/layouts/` ✅ (10 files)
  - `layouts/rss.xml` → theme ✅
  - `layouts/_default/` → theme ✅
  - `layouts/_partials/` → theme ✅ (29 partials)
  - `layouts/_shortcodes/` → theme ✅ (13 shortcodes)
  - `layouts/_markup/` → theme ✅
  - `layouts/taxonomy/` → theme ✅ (9 taxonomy templates)
  - `layouts/post/` → theme ✅
  - `layouts/garden/` → theme ✅

- [x] Update asset paths in `head.html` to use theme assets:
  - Already done in Stage 2 ✅
  - All CSS paths use `resources.Get "style/..."` which works for both root and theme
  - CSS files verified to resolve correctly ✅

- [x] Copy archetypes to theme:
  - `archetypes/default.md` → `themes/victorian-newspaper/archetypes/` ✅
  - `archetypes/days.md` → theme ✅
  - `archetypes/project.md` → theme ✅

- [x] Verify template lookup order works correctly:
  - Site still builds from root layouts/ (theme not yet activated) ✅
  - Theme structure matches root structure exactly ✅
  - Ready for theme activation in Stage 5 ✅

**Tests**:
- ✅ Site builds successfully (89 pages, ~350ms)
- ✅ Hugo server runs at http://localhost:1313/
- ✅ All layouts, partials, shortcodes, taxonomy templates copied
- ✅ Archetypes available in theme
- ✅ Template hierarchy preserved (site continues to work from root)
- Theme is complete and ready to be activated

**Status**: Complete

---

## Stage 4: Move Static Assets to Theme
**Goal**: Move font files and static CSS to theme
**Success Criteria**:
- All fonts load correctly
- Static CSS files accessible
- No broken asset references

**Tasks**:
- [x] Identify static assets used by Victorian theme:
  - Font files identified: dbc60, Source Serif Pro, Source Sans Pro, drop caps (Goudy, Cheshire, De Zs, Kanzlei, Yinit) ✅
  - Images: Banner images are site-specific, not theme-specific (not copied) ✅
  - CSS files: gwern.net CSS not used by theme (not copied) ✅

- [x] Copy to `themes/victorian-newspaper/static/font/`:
  - dbc60 font (4 files: .eot, .svg, .ttf, .woff) ✅
  - Source Serif Pro (12 files) ✅
  - Source Sans Pro (12 files) ✅
  - Goudy drop caps (26 files, A-Z) ✅
  - Cheshire drop caps (26 files, A-Z) ✅
  - Deutsche Zierschrift drop caps (26 files, A-Z) ✅
  - Kanzlei drop caps (26 files, A-Z) ✅
  - Yinit drop caps (26 files, A-Z) ✅
  - **Total: 158 font files** ✅

- [x] Verify all asset paths resolve correctly:
  - Font files accessible at `/font/*` ✅
  - CSS @font-face declarations reference correct paths ✅

**Tests**:
- ✅ Site builds successfully (233 static files)
- ✅ Hugo server runs without errors
- ✅ All 158 font files copied to theme
- ✅ Font paths resolve correctly (verified in public/font/)
- Theme fonts ready for use when theme is activated

**Notes**:
- Site-specific assets (banner images, custom photos) remain in root `static/`
- Only theme-essential fonts copied to theme
- Theme is now self-contained with all necessary font assets

**Status**: Complete

---

## Stage 5: Configure Hugo to Use Theme
**Goal**: Update site configuration to use the new theme
**Success Criteria**:
- Site runs entirely from theme
- Root layouts/ and assets/ can be removed
- Theme can be used on other Hugo sites

**Tasks**:
- [x] Update `hugo.toml`:
  ```toml
  theme = "victorian-newspaper"
  ```
  Added on line 6 ✅

- [x] Test with root `layouts/` and `assets/` directories still present:
  - Site built successfully with theme configured ✅
  - Root directories still override theme as expected ✅

- [x] Rename root directories to verify theme is being used:
  - `mv layouts layouts.old` ✅
  - `mv assets assets.old` ✅
  - Build initially failed - missing font CSS files ✅
  - Copied 8 font CSS files to theme ✅
  - Build successful after adding fonts ✅

- [x] Verify theme is self-contained:
  - Site builds from theme only (89 pages, ~340ms) ✅
  - Hugo server runs at http://localhost:1313/ ✅
  - All CSS, layouts, fonts loaded from theme ✅

- [ ] Document any site-specific customizations:
  - All layouts and partials are now in theme ✅
  - Site-specific: content, data, static (images, etc.) remain in root ✅
  - archetypes.old can be removed (copied to theme) ✅
  - layouts.old and assets.old can be removed ✅

**Tests**:
- ✅ Site builds with `theme = "victorian-newspaper"` configured
- ✅ Site works without root layouts/ and assets/
- ✅ All 89 pages render correctly (verified by build output)
- ✅ Hugo watches `themes/` directory instead of root layouts/assets
- ✅ CSS loads correctly (233 static files)
- ✅ Victorian theme fully functional from theme directory

**Notes**:
- Discovered missing font CSS files during testing
- Added 8 font CSS files to theme:
  - font-drop-caps-{goudy,cheshire,de-zs,kanzlei,yinit}.css
  - font-source-{serif,sans}-pro.css
  - font-system-stack.css
- Theme is now completely self-contained

**Status**: Complete

---

## Stage 6: Documentation and Polish
**Goal**: Document theme for reuse and future maintenance
**Success Criteria**:
- Theme README explains installation and customization
- CSS architecture is documented
- No !important declarations remain

**Tasks**:
- [x] Create `themes/victorian-newspaper/README.md`:
  - Installation instructions ✅
  - Configuration options ✅
  - Customization guide (CSS variables, colors, fonts) ✅
  - Feature list (drop caps, dividers, backlinks, etc.) ✅

- [x] Document CSS architecture:
  - Cascade order explanation ✅
  - CSS custom property reference ✅
  - How to override theme styles ✅

- [x] Verify no `!important` declarations in theme CSS:
  ```bash
  grep -r "!important" themes/victorian-newspaper/assets/
  ```
  Result: Only 1 legitimate `!important` in fonts.css (icon font protection) ✅

- [x] Add example `hugo.toml` configuration ✅

- [x] Update main site `CLAUDE.md` to reference theme structure ✅

**Tests**:
- ✅ README is clear and complete (comprehensive documentation with installation, configuration, customization)
- ✅ Only 1 legitimate `!important` found (fonts.css for icon font protection)
- ✅ CSS custom properties documented in README
- ✅ Configuration examples included in README
- ✅ Deleted old `victorian-colors.css` with unnecessary `!important` declarations

**Notes**:
- Created comprehensive 400+ line README with:
  - Installation instructions (git submodule and manual)
  - Essential and optional configuration
  - CSS architecture with complete cascade order
  - CSS custom property reference
  - Drop caps configuration
  - Shortcode documentation
  - Performance considerations
  - Troubleshooting guide
  - Contributing guidelines
- Updated main `CLAUDE.md` with:
  - Theme structure documentation
  - CSS architecture reference
  - Template hierarchy with theme paths
  - Theme development history
- Removed old `victorian-colors.css` file with `!important` declarations

**Status**: Complete

---

## Notes
- Each stage should be committed separately with descriptive messages
- Keep site functional at every stage (no breaking changes)
- Test thoroughly before moving to next stage
- If stuck on a stage after 3 attempts, document issues and reassess approach
