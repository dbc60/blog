# Content Strategy

Purpose and intent for each section of the blog. Use this to decide where new content belongs and to track open questions about the site's structure.

---

## Sections

### Posts (`/post/`)
Full, finished blog posts. The primary content of the site. Topics include programming, project planning, sketching, drawing, kempo, and whatever else suits the moment.

### Wander (`/wander/`)
Not a content section — infrastructure. Wander is a small, decentralised, self-hosted web console that lets visitors explore random pages from a community of personal websites. Each console loads pages recommended by the Wander community and can link to other Wander consoles, forming a lightweight decentralised network for browsing the small web. Think self-hosted web-ring or decentralized StumbleUpon. The nav entry surfaces the console to visitors.

### Seedlings (`/garden/`)
Draft posts made public. A seedling is a thought in progress — rough, incomplete, or exploratory. Showing work-in-progress is intentional. Inspired by the digital garden model: tend ideas in public rather than only publishing finished things.

Two kinds of seedlings naturally emerge:

- **Notes-to-self** — reference material that's useful as-is and doesn't need to graduate anywhere. Examples: blog internals notes (Partials, Shortcodes, CSS, HTML Layout). These live in the garden indefinitely.
- **Incubating posts** — drafts that happen to be public while they're forming. These eventually move to `content/post/` when ready.

**Graduating a seedling:** When an incubating post is done, move it to `content/post/`. That gives it a permanent dated URL (`/:year/:month/:slug/`) and puts it in the main post feed. Set `draft: false` if it isn't already.

**Draft posts in `content/post/`** (i.e. `draft: true`) are a separate thing — hidden until published. Use these for work you don't want seen until it's polished. The Faultline series posts, for example, should go straight to `content/post/` as drafts and be published when finished, not routed through the garden.

### Evergreen Notes
Removed. The section (`/evergreen-note/`) and its nav entry are gone.

The original intent was Andy Matuschak-style evergreen notes: atomic, concept-sized, densely interlinked notes. See: https://notes.andymatuschak.org/Evergreen_notes. The tension: that model works because of *density of links* between notes — a blog with relatively isolated pages is not the right substrate.

The one subsection that existed (`create-table`, documenting the `create_table` Hugo shortcode) was moved to `content/reference/create-table/` to preserve the links used by the "A Table Shortcode for Hugo" post. The `reference` section has no nav entry and is not intended to be browsed directly.

### Commentary (`/commentary/`)
Empty. Removed from nav. Section and `_index.md` exist but no content has been written. Intent unclear — remove or repurpose when direction is decided.

For commentary posts, run `hugo new --kind commentary content/commentary/your-post-title.md`

### Justice (`/justice/`)
Empty. Removed from nav. Same status as Commentary.

### About (`/about/`)
Standard about page.

### Now (`/now/`)
A /now page — what's happening at the moment, updated periodically. See: https://nownownow.com/about

### Blogroll (`/bookmark/`)
Links to other sites worth reading.

### RSS (`/index.xml`)
Feed. Not a content section.
