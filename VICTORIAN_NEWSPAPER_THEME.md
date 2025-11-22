# Victorian Newspaper Theme - Project Documentation

## Project Overview

Transforming the Hugo blog at <https://douglascuthbertson.com/> with authentic Victorian newspaper styling inspired by 1860s-1910s illustrated newspapers (like the Penny Illustrated Paper). The goal is to add period touches while maintaining readability for technical content.

## Design Philosophy

### Approved Elements
- ✅ Ornate masthead - Main blog header with Victorian serif fonts, tagline, publication metadata
- ✅ Drop caps - CSS ::first-letter on first paragraph of posts only (already implemented)
- ✅ Decorative rules/dividers - Subtle ornamental borders between sections
- ✅ Publication metadata block - Victorian-style date/issue presentation
- ✅ "Front page" index layout - More decorative than individual post pages

### Rejected/Deferred Elements
- ❌ Multi-column layouts - Would interfere with code blocks
- ❌ Heavy texture/aging effects - Would reduce code readability
- ❌ Multiple decorative body fonts - One for masthead, readable serif for content
- ❌ Justified narrow columns - Poor for web, especially code

## Completed Work

### 1. Victorian Masthead (Completed: 2025-11-22)

**Files Modified/Created:**
- `layouts/_partials/siteHeader.html` - Complete restructure
- `assets/style/victorian-masthead.css` - New CSS file
- `layouts/_partials/head.html` - Added CSS import

**Features Implemented:**

#### Structure
```
┌─────────────────────────────────────────┐
│        ❧ ──────────── ❧                │  Top decorative rule
│                                         │
│  Vol. 11    Friday, November 22, 2025   No. 104  │  Publication metadata
│                                         │
│        DOUG'S PLACE                     │  Main nameplate/title
│   Seeds of Thought. A Point of View.   │  Tagline/subtitle
│                                         │
│        ❁ ══════════ ❁                  │  Bottom decorative rule
└─────────────────────────────────────────┘
```

#### Dynamic Content
- **Volume Number**: Calculated from site start year (2015) to current year
- **Publication Date**: Current date in full format (e.g., "Monday, January 2, 2006")
- **Issue Number**: Total count of posts in mainSections

#### Styling Details
- **Title Font**: Source Serif Pro, 900 weight, 4rem, uppercase
- **Metadata**: Uppercase, letter-spaced, Source Serif Pro
- **Ornaments**: Unicode decorative symbols (❧ ❁)
- **Rules**: Gradient horizontal lines with double-line option
- **Colors**: Black (#000) for title, dark gray (#333) for accents
- **Responsive**: Scales from 4rem → 2.5rem → 2rem on smaller screens

#### Technical Implementation
```html
<!-- Key Hugo template variables -->
{{- $totalPosts := len (where .context.Site.RegularPages "Type" "in" .context.Site.Params.mainSections) -}}
{{- $currentYear := now.Year -}}
{{- $siteStartYear := 2015 -}}
{{- $volumeNumber := sub $currentYear $siteStartYear | add 1 -}}
```

**Testing Status**: ✅ Builds successfully, renders correctly

---

### 2. Victorian Decorative Dividers (Completed: 2025-11-22)

**Files Modified/Created:**
- `layouts/_partials/victorian-divider.html` - Flexible divider partial with style variants
- `assets/style/victorian-dividers.css` - Complete styling for all divider types
- `layouts/_partials/head.html` - Added CSS import
- `layouts/single.html` - Dividers after metadata and before backlinks
- `layouts/list.html` - Dividers between article listings
- `layouts/home.html` - Ornate dividers between page summaries

**Features Implemented:**

#### Divider Style Variants
- **Light**: Minimal single line with small ornaments (✦)
- **Medium**: Standard double line with ornaments (❖) - default
- **Heavy**: Bold triple line with larger ornaments (❁)
- **Ornate**: Multiple ornaments with decorated lines (✠ ❧ ⁂)
- **Simple**: Plain gradient line, no ornaments
- **Fleuron**: Centered ornament only (※), no lines

#### Usage Examples
```hugo
{{- partial "victorian-divider.html" (dict "style" "light") -}}
{{- partial "victorian-divider.html" (dict "style" "medium") -}}
{{- partial "victorian-divider.html" (dict "style" "heavy") -}}
{{- partial "victorian-divider.html" (dict "style" "ornate") -}}
{{- partial "victorian-divider.html" (dict "style" "simple") -}}
{{- partial "victorian-divider.html" (dict "style" "fleuron") -}}
{{- partial "victorian-divider.html" . -}} <!-- defaults to medium -->
```

#### Implementation Locations
- **Single posts**: Light divider after date/tags, medium divider before backlinks
- **List pages**: Medium dividers between article summaries
- **Homepage**: Ornate dividers between page summaries (most decorative)

#### Styling Details
- **Lines**: CSS gradient-based with multiple variants (single, double, triple, decorated)
- **Ornaments**: Unicode symbols in various sizes (0.85em to 1.6em)
- **Colors**: Dark grays (#222, #333, #444, #555, #666) for period-appropriate ink tones
- **Spacing**: Context-aware margins (1.5em to 3em depending on location)
- **Responsive**: Scales down on mobile, hides some ornaments on very small screens
- **Max widths**: Lines capped at 200px-350px depending on style

#### Technical Features
- Flexbox-based layout for perfect centering
- Gradient lines for smooth fade-in/fade-out
- CSS pseudo-elements (::before, ::after) for multi-line effects
- Context-specific styling (article, sidebar, metadata)
- Print-optimized styles
- Accessibility considerations (decorative elements properly marked)

**Testing Status**: ✅ Builds successfully in 346ms, no errors

---

### 3. Victorian Sidebar Sections (Completed: 2025-11-22)

**Files Modified/Created:**
- `assets/style/victorian-sidebar.css` - Complete Victorian sidebar styling
- `layouts/_partials/head.html` - Added CSS import
- `layouts/baseof.html` - Added Victorian headers and classes to sidebar sections
- `layouts/_partials/items-contents.html` - Added Victorian classes
- `layouts/_partials/items-latest.html` - Added Victorian classes
- `layouts/_partials/items-taxonomies.html` - Added Victorian classes

**Features Implemented:**

#### Victorian Section Headers
Each sidebar section now has a decorative newspaper-style header:
- **Table of Contents** (was "Contents") - ✦ ornament, "Sections & Subsections" subtitle
- **Latest Intelligence** (was "Latest Posts") - ❖ ornament, "Recent Dispatches" subtitle
- **Departments** (was "Collections") - ◈ ornament, "Classified Index" subtitle

#### Header Styling
- Double border (2px top/bottom with 1px accent lines)
- Centered, uppercase titles with generous letter-spacing
- Italic subtitle in smaller font
- Subtle gradient background (#f8f8f8 to #fff)
- Ornamental symbols above each title

#### List Item Styling
- Decorative bullets before each item (different per section):
  - Contents: ✦ (star)
  - Latest Intelligence: ❖ (diamond)
  - Departments: ◈ (white diamond)
- Dotted borders between items
- Clean, readable typography (Source Serif Pro)
- Hover effects with subtle left-shift
- Section-specific styling:
  - Latest Intelligence: Italic links
  - Departments: Small-caps links

#### Container Styling
- Light background (#fcfcfc)
- Subtle border and shadow
- Removed old icon-based borders
- Clean rectangular boxes (no border-radius for period authenticity)

#### Technical Features
- Responsive design (scales down on mobile)
- Print-optimized styles
- Proper semantic HTML (h2 headers)
- Context-aware styling
- Compatibility with existing styles

**Testing Status**: ✅ Builds successfully in 347ms, no errors

---

### 4. Victorian Front Page Layout (Completed: 2025-11-22)

**Files Modified/Created:**
- `assets/style/victorian-front-page.css` - Complete front-page styling
- `layouts/_partials/head.html` - Added CSS import
- `layouts/home.html` - Added section header, featured article, date badges

**Features Implemented:**

#### Section Header - "Latest Intelligence"
- Decorative header at top of homepage
- Double border with accent lines
- Ornament (❦) above title
- Subtitle: "Recent Dispatches from the Digital Frontier"
- Warm gradient background matching site theme

#### Featured Article (First Post)
- First visible article gets prominent treatment
- Larger title (2.2rem vs 1.4rem for regular)
- Double border with inner accent border
- Featured image shown (hidden on other articles)
- Column layout for featured article
- Cream background (#f5f5f0)

#### Victorian Date Badges
- All articles get decorative date badges
- Double border with inner accent
- Ornament (❖) before date
- Small-caps, uppercase styling
- Format: "Monday, Jan 2, 2006"
- Responsive sizing

#### Layout Details
- Homepage only (list pages remain simpler)
- Ornate dividers between articles
- Responsive design (stacks on mobile)
- Print-optimized styles

**Testing Status**: ✅ Builds successfully, homepage-only styling

---

## Planned Work

### 5. Enhanced Drop Caps Integration (Not Started)

**Purpose**: More decorative layout for the homepage/index pages

**Planned Features**:
- Featured article with larger treatment
- "Latest Intelligence" section header
- "Classified Advertisements" for tags/categories
- Victorian column-style headers for sidebar
- Ornamental section dividers

**Files to Modify**:
- `layouts/home.html`
- `layouts/list.html`
- `layouts/_partials/items-latest.html`
- `layouts/_partials/items-taxonomies.html`
- Create: `assets/style/victorian-front-page.css`

**Design Considerations**:
- Keep mobile-friendly (no actual multi-column for main content)
- Use decorative headers without sacrificing navigation clarity
- Maintain code block readability

---

### Enhanced Drop Caps (Review/Optimize)

**Current Status**: Already implemented with multiple font options:
- Goudy Initialen (currently active)
- Cheshire Initials
- Deutsche Zierschrift
- Kanzlei Initialen
- Yinit

**Potential Enhancements**:
- Review drop cap styling for Victorian aesthetic
- Consider adding decorative borders around drop caps
- Ensure compatibility with Victorian masthead
- Test across different post types

**Files**:
- `layouts/_partials/drop-caps.html`
- `assets/style/drop-caps/*.css`

---

## Technical Notes

### Hugo Configuration
- **Hugo Version**: v0.151.0+
- **Theme**: Custom theme (no parent theme)
- **Base Font**: Source Serif Pro (already Victorian-appropriate)
- **Template System**: Modern Hugo (post-v0.146)

### CSS Architecture
- Using Hugo Pipes for CSS concatenation
- Files in `assets/style/` processed via `layouts/_partials/head.html`
- Order matters: Victorian styles loaded before base/overrides
- No SCSS for new Victorian styles (plain CSS for simplicity)

### File Organization
```
blog/
├── layouts/
│   ├── _partials/
│   │   ├── siteHeader.html          [MODIFIED]
│   │   ├── date-and-tags.html       [TODO: MODIFY]
│   │   ├── victorian-divider.html   [TODO: CREATE]
│   │   └── items-*.html             [TODO: REVIEW]
│   ├── home.html                    [TODO: MODIFY]
│   ├── list.html                    [TODO: MODIFY]
│   └── single.html                  [TODO: MODIFY]
└── assets/
    └── style/
        ├── victorian-masthead.css        [CREATED]
        ├── victorian-dividers.css        [TODO: CREATE]
        ├── victorian-post-metadata.css   [TODO: CREATE]
        └── victorian-front-page.css      [TODO: CREATE]
```

### Browser Compatibility
- Using standard CSS3 features (flexbox, gradients)
- Unicode symbols well-supported
- Print styles included
- Mobile-responsive breakpoints: 768px, 480px

---

## Design Resources

### Victorian Typography Characteristics
- Bold, condensed sans-serif for headlines
- Ornate serif fonts for decorative elements
- Small caps for subheadings
- Letter-spacing for emphasis
- Multiple rule weights and styles

### Period-Appropriate Unicode Symbols
- ❧ (U+2767) - Rotated floral heart bullet
- ❁ (U+2741) - Eight-petaled outlined flower
- ✦ (U+2726) - Black four-pointed star
- ◈ (U+25C8) - White diamond containing black small diamond
- ※ (U+203B) - Reference mark
- ❖ (U+2756) - Black diamond minus white X
- ⁂ (U+2042) - Asterism
- ✠ (U+2720) - Maltese cross

### Historical Newspaper Examples
- Penny Illustrated Paper (1861-1913)
- The Illustrated London News (1842-2003)
- Harper's Weekly (1857-1916)
- Frank Leslie's Illustrated Newspaper (1855-1922)

---

## Future Ideas / Brainstorming

### Potential Enhancements
- [ ] "Weather Report" widget in sidebar (current date/time)
- [ ] "Advertisement" styling for callout boxes/admonitions
- [ ] Victorian-style "Table of Contents" header
- [ ] Ornamental archive pages with year headers
- [ ] "Special Correspondent" byline styling
- [ ] Decorative initial caps for section headings
- [ ] Print-specific layout optimizations

### Custom Shortcodes to Consider
- `{{< victorian-divider >}}` - Insert decorative rule
- `{{< advertisement >}}` - Styled callout box
- `{{< byline >}}` - Victorian author attribution
- `{{< special-notice >}}` - Highlighted announcement box

---

## Testing Checklist

### Per-Feature Testing
- [ ] Desktop browsers (Chrome, Firefox, Safari, Edge)
- [ ] Mobile browsers (iOS Safari, Android Chrome)
- [ ] Print preview
- [ ] Dark mode compatibility (if applicable)
- [ ] Accessibility (screen readers, keyboard navigation)
- [ ] Performance (page load times, CSS size)

### Content Type Testing
- [ ] Homepage
- [ ] Individual posts
- [ ] List/archive pages
- [ ] Taxonomy pages (tags, years)
- [ ] Special pages (About, Now, Bookmarks)
- [ ] Posts with code blocks
- [ ] Posts with images
- [ ] Posts with math (KaTeX)

---

## Customization Guide

### Adjusting the Masthead

**Change Title Size**:
```css
/* In victorian-masthead.css */
.siteTitle.nameplate {
  font-size: 4rem;  /* Change this value */
}
```

**Change Ornaments**:
```html
<!-- In siteHeader.html -->
<span class="rule-ornament">&#10047;</span>  <!-- Replace with different Unicode -->
```

**Adjust Site Start Year**:
```html
<!-- In siteHeader.html -->
{{- $siteStartYear := 2015 -}}  <!-- Update this value -->
```

**Color Scheme**:
```css
/* In victorian-masthead.css */
color: #000;  /* Title color */
color: #333;  /* Accent color */
```

### Adding New Decorative Elements

1. Choose period-appropriate Unicode symbols
2. Create CSS with `font-family: 'Source Serif Pro'` for consistency
3. Use semantic HTML structure
4. Test responsiveness at 768px and 480px breakpoints
5. Add print styles
6. Update this documentation

---

## Version History

### v0.5 - Victorian Front Page Layout (2025-11-22)
- Added "Latest Intelligence" section header to homepage
- Implemented featured article treatment (first post larger and more prominent)
- Created Victorian date badges for all articles on front page
- Double-border styling on featured articles
- Homepage-specific styling (list pages remain simpler)
- Responsive design for featured articles

### v0.4 - Color Harmony Adjustments (2025-11-22)
- Unified color palette with warm beige/cream tones
- Changed body background from cool gray (#e3e3e3) to warm beige (#ebe8e0)
- Harmonized masthead, sidebar, and content backgrounds
- Created victorian-colors.css for cohesive aged newsprint aesthetic
- Eliminated harsh white-on-gray contrast

### v0.3 - Victorian Sidebar (2025-11-22)
- Created Victorian newspaper-style sidebar section headers
- Renamed sections: "Table of Contents", "Latest Intelligence", "Departments"
- Added decorative headers with ornaments and subtitles
- Implemented section-specific styling (different bullets, typography)
- Updated all sidebar partials with Victorian classes
- Responsive design with mobile optimization

### v0.2 - Decorative Dividers (2025-11-22)
- Created flexible Victorian divider partial with 6 style variants
- Implemented comprehensive CSS for all divider types
- Integrated dividers into single posts, list pages, and homepage
- Added context-aware spacing and responsive design
- Print-optimized styles for dividers

### v0.1 - Initial Masthead (2025-11-22)
- Created Victorian newspaper masthead
- Added publication metadata (volume, date, issue)
- Implemented decorative rules with ornaments
- Full responsive design
- Print styles

---

## Notes & Decisions

### Why No Textures?
While aged paper textures are visually appealing, they significantly reduce readability for code blocks and technical content. The Victorian aesthetic comes from typography and ornamental structure rather than surface treatment.

### Why Keep Source Serif Pro?
Source Serif Pro is already an excellent choice for body text that echoes period typography without being distractingly antiquated. It maintains excellent readability for modern technical content.

### Why Unicode vs SVG for Ornaments?
Unicode symbols are:
- Faster to load
- Scale perfectly
- Easy to customize
- Accessible to screen readers
- No additional HTTP requests

SVG can be added later for more complex ornamental needs.

---

## Contact & Questions

This project documentation should be updated as new features are added or design decisions are made. Keep this file in sync with actual implementation.

Last Updated: 2025-11-22
