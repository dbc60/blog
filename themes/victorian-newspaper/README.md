# Victorian Newspaper Theme for Hugo

A Hugo theme inspired by Victorian-era illustrated newspapers (1860s-1910s), featuring elegant typography, decorative ornaments, drop caps, and warm aged newsprint colors.

## Features

- **Victorian Masthead**: Ornamental newspaper-style header with decorative rules and publication metadata
- **Ornamental Drop Caps**: Five decorative initial capital letter styles (Goudy, Cheshire, Deutsche Zierschrift, Kanzlei, Yinit)
- **Decorative Dividers**: Victorian-style section separators with ornamental centerpieces
- **Sidebar Sections**: Newspaper column-style sidebar with Contents, Latest Posts, and Collections
- **Backlinks**: Automatic backlink detection showing which pages reference the current page
- **Year-based Taxonomies**: Organize content by publication year with Victorian-styled index pages
- **Custom Shortcodes**: Table of contents, admonitions, content inclusion, YouTube embeds, and more
- **Syntax Highlighting**: Code blocks with Tango and Monokai themes
- **Responsive Design**: Mobile-friendly layout with responsive typography
- **Print Styles**: Optimized for printing with clean, readable output
- **KaTeX Support**: Mathematical notation rendering

## Requirements

- Hugo v0.151.0 or higher
- Extended Hugo version (for SCSS processing if customizing styles)

## Installation

### As a Git Submodule (Recommended)

```bash
cd your-hugo-site
git submodule add https://github.com/yourusername/victorian-newspaper.git themes/victorian-newspaper
```

### Manual Installation

1. Download or clone this repository
2. Copy the entire `victorian-newspaper` folder to your site's `themes/` directory

## Configuration

Add the theme to your `hugo.toml`:

```toml
theme = "victorian-newspaper"
```

### Essential Configuration

```toml
baseURL = "https://example.com"
languageCode = "en-us"
title = "Your Site Title"
theme = "victorian-newspaper"

[params]
  subtitle = "Your site tagline or motto"
  description = "Description of your site"
  dateFormat = "Monday Jan 2, 2006"

  # Drop caps font selection
  # Options: "goudy", "cheshire", "de-zs", "kanzlei", "yinit"
  dropCapsFont = "goudy"

  # Main content sections (for "Latest Posts" sidebar)
  mainSections = ["post", "blog"]

[params.author]
  name = "Your Name"
  email = "you@example.com"
```

### Optional Configuration

```toml
[params]
  # Featured/title images
  titleImage = "images/banners/your-image.jpg"
  titleImageDescription = "Image description"
  titleCopyright = "copyright © 2024 Your Name"

  # Math rendering
  katex = true  # Enable KaTeX for math notation
  mathjax = false  # Alternative to KaTeX

  # Comments
  disable_comments = true

  # List limits
  list_limit = 50
```

### Taxonomies

The theme supports year-based taxonomies. Add to your `hugo.toml`:

```toml
[taxonomies]
  tag = "tags"
  year = "years"
```

In your content front matter:

```yaml
---
title: "My Post"
date: 2024-01-15
2024: ["01"]
tags: [technology, hugo]
---
```

### Menu Configuration

```toml
[menu]
  [[menu.nav]]
    name = "Home"
    url = "/"
    weight = 50
  [[menu.nav]]
    name = "Posts"
    url = "/post/"
    weight = 100
  [[menu.nav]]
    name = "About"
    url = "/about/"
    weight = 300
```

## Customization

### CSS Architecture

The theme uses a carefully ordered CSS cascade to eliminate the need for `!important` declarations:

1. **front.css** - CSS reset and foundational styles
2. **base.css** - Core styles with CSS custom properties
3. **layout-grid.css** - Grid layout structure
4. **fonts.css** - Typography base with icon fonts
5. **font-system-stack.css** - System font fallbacks
6. **victorian-theme.css** - Unified theme with Victorian components (masthead, navigation, sidebar, front page, post metadata, taxonomy indexes)
7. **drop-caps-*.css** - Drop cap decorative initials
8. **font-drop-caps-*.css** - Drop cap font definitions
9. **syntax-highlighting/*.css** - Code syntax themes
10. **overrides.css** - User customizations (create in root `assets/style/`)
11. **print.css** - Print-specific styles (always last)

### CSS Custom Properties

Override theme colors by creating `assets/style/overrides.css` in your site root:

```css
:root {
  /* Background colors */
  --gray100: #ebe8e0;              /* Main background (warm cream) */
  --gray150: #ebe8e0;              /* Alternate background */
  --background-main-default: #ebe8e0;
  --background-main-content: #f5f5f0;  /* Content area background */

  /* Link colors */
  --color500: #2f75cc;             /* Primary links */
  --color-anchor: var(--color600);
  --color-anchor-hover: var(--color500-shade1-complement);

  /* Typography */
  --font-family-body-default: "Source Serif Pro", "Helvetica Neue", Helvetica, Arial, sans-serif;
  --line-height-default: 1.5;
}
```

### Drop Caps Configuration

Change the drop caps font in `hugo.toml`:

```toml
[params]
  dropCapsFont = "goudy"  # Options: goudy, cheshire, de-zs, kanzlei, yinit
```

Apply drop caps to content by adding the class in front matter:

```yaml
---
title: "My Post"
dropcaps: true
---
```

Or manually add to your content:

```html
<div class="c-drop-caps drop-caps_goudy">

Your first paragraph here...

</div>
```

### Victorian Components

#### Masthead

The masthead automatically displays your site title and subtitle from `hugo.toml`. The publication metadata bar shows:
- Left: Volume information (optional, customize in `layouts/partials/siteHeader.html`)
- Center: Current date
- Right: Price or edition (optional)

#### Sidebar Sections

The sidebar includes three Victorian-styled sections:
- **Table of Contents**: Site sections with decorative header
- **Latest Intelligence**: Recent posts from `mainSections`
- **Departments**: Taxonomies (tags, years) with decorative header

Customize sidebar content in `layouts/partials/items-*.html`.

#### Taxonomy Index Pages

Year and tag taxonomy index pages use Victorian newspaper styling with:
- Decorative section headers with ornaments
- Multi-column grid layout
- Dotted separator lines between entries
- Article counts for each taxonomy term

#### Decorative Dividers

Add Victorian dividers to your content:

```html
<div class="victorian-divider">
  <div class="divider-line divider-double"></div>
  <div class="divider-ornament">❦</div>
  <div class="divider-line divider-double"></div>
</div>
```

## Shortcodes

### Table of Contents

```markdown
{{< table_of_contents >}}
```

### Admonition (Callout Boxes)

```markdown
{{< admonition type="note" title="Important" >}}
Your note content here.
{{< /admonition >}}
```

### YouTube Embed

```markdown
{{< yt video_id="dQw4w9WgXcQ" >}}
```

### Content Inclusion

```markdown
{{< content path="partials/my-content.md" >}}
```

### Evergreen Notes

```markdown
{{< evergreen note="note-basename" >}}
```

## Content Organization

### Post Front Matter Template

```yaml
---
title: "Post Title"
date: 2024-01-15
2024: ["01"]
tags: [tag1, tag2]
dropcaps: true
math: false
---

<!--more-->

{{< table_of_contents >}}

Your content here...
```

### Page Types

- **Posts**: `content/post/*.md` - Blog posts with full features
- **Pages**: `content/about.md`, `content/now.md` - Static pages
- **Garden**: `content/garden/*.md` - Evergreen notes/wiki-style content

## Advanced Features

### Backlinks

The theme automatically generates backlinks showing which pages reference the current page. Backlinks appear at the bottom of posts.

**Performance Note**: Backlinks search all pages on every build, which can be slow for large sites (100+ pages).

### Git Integration

Enable git-based last modified dates:

```toml
enableGitInfo = true

[frontmatter]
  lastmod = ['lastmod', ':git', 'date', 'publishDate']
```

### Math Rendering

Enable KaTeX in `hugo.toml`:

```toml
[params]
  katex = true
```

Use math in content:

```markdown
Inline math: $E = mc^2$

Display math:
$$
\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
$$
```

## Theme Structure

```
victorian-newspaper/
├── archetypes/          # Content templates
├── assets/
│   └── style/          # CSS files (processed by Hugo)
├── layouts/
│   ├── _default/       # Base templates
│   ├── partials/       # Reusable components
│   ├── shortcodes/     # Custom shortcodes
│   └── taxonomy/       # Taxonomy templates
├── static/
│   └── font/          # Web fonts
├── LICENSE.md
├── README.md
└── theme.toml
```

## Performance Considerations

- **Backlinks**: Can be slow on large sites. Consider disabling by editing `layouts/_default/single.html`.
- **Drop Caps**: Uses unicode-range font loading for efficient delivery.
- **CSS**: Single concatenated, minified CSS file for fast loading.
- **Fonts**: Only loads Source Serif Pro and drop caps fonts as needed.

## Browser Support

- Modern browsers (Chrome, Firefox, Safari, Edge)
- Responsive design for mobile devices
- Graceful degradation for older browsers
- Print styles for all browsers

## Troubleshooting

### Build Errors

**Error**: `expected slice of Resource objects`

**Solution**: Ensure all CSS files referenced in `layouts/partials/head.html` exist in `assets/style/`.

### Styles Not Applying

1. Clear Hugo's cache: `hugo --gc`
2. Check CSS load order in `layouts/partials/head.html`
3. Verify `theme = "victorian-newspaper"` in `hugo.toml`
4. Check browser console for CSS loading errors

### Drop Caps Not Showing

1. Verify `dropCapsFont` is set in `hugo.toml`
2. Check that content has `dropcaps: true` in front matter or uses drop caps classes
3. Ensure drop caps fonts are in `static/font/`

## License

This theme is licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0).

See [LICENSE.md](LICENSE.md) for details.

## Credits

- Inspired by Victorian-era illustrated newspapers (1860s-1910s)
- Drop caps fonts: Goudy Initialen, Cheshire Initials, Deutsche Zierschrift, Kanzlei Initials, Yinit
- Body font: Source Serif Pro (SIL Open Font License)
- Icon font: Custom dbc60 font
- Layout inspired by historical newspaper design

## Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly with Hugo v0.151.0+
5. Submit a pull request

## Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Check existing documentation
- Review Hugo documentation for template questions

## Changelog

### Version 1.0.0 (2024)
- Initial release
- Victorian newspaper styling
- Drop caps support (5 fonts)
- Responsive layout
- Sidebar with collapsible sections
- Backlinks
- Year-based taxonomies
- Custom shortcodes
- KaTeX support
- Print styles
