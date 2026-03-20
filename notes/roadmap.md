# Content Roadmap

Planned posts and series. Update status as work progresses.

Status values: `planned` · `drafting` · `ready` · `published`

---

## Before Next Publish

- [x] Update the Now page
- [ ] Update the Blogroll page
- [ ] Update `wander.js` (review for any needed changes before going live)
- [ ] Audit existing draft posts — decide which to promote to Seedlings, which to keep hidden, which to discard
- [ ] Start drafting Faultline Post 1 (push Faultline repo to GitHub before the second article)
  - The first article will be about BUT
  - The second article is about why Faultline was created

## Current Draft Posts
As of Thursday, March 19, 2026, there are 10 drafts across two sections:

Posts (content/post/)
- "Unit Test" — unit-test.md
- "Testing With Permutations" — testing-with-permutations.md
- "A Templating Journey" — a-templating-journey.md
- "Software-Development Workshop" — software-development-workshop.md

Garden/Seedlings (content/garden/)
- "Memory Allocator" — mem-allocator/_index.md (the section itself is a draft)
- "A Deep Look at a Memory Allocator" — mem-allocator/a-deep-look-at-a-memory-allocator.md
- "Partials" — blog/partials.md
- "Shortcodes" — blog/shortcodes.md
- "CSS" — blog/css.md
- "HTML Layout" — blog/html-layout.md

The garden ones already live in the right section for in-progress work. The question is mainly whether to flip `draft: false` on them so they appear publicly. The four post drafts are the ones that need a decision: finish and publish, demote to Seedlings, or discard. See `content-strategy.md` for the full policy on drafts vs. seedlings.

## Future Posts

- I built a TrueNAS server. Do more with it and write about it.
  - make it a local backup server.
  - make it a [Plex](https://www.plex.tv/) or [Jellyfin](https://jellyfin.org/) media server.
- I made a [rain gardens](https://www.epa.gov/soakuptherain/soak-rain-rain-gardens) in 2024. Write about it. Previously, I said: I'm looking into building a couple of [rain gardens](https://www.epa.gov/soakuptherain/soak-rain-rain-gardens) next spring, one in the front yard and one in the back. Rain gardens have a lot of environmental benefits, but that's not the _real_ purpose. I want something pretty that will guide water away from the house and cut down on the amount of lawn I have to mow.

## Site Operations

### Building and Publishing

```bash
# Build the site (outputs to public/)
hugo

# Preview locally with TLS
hugo server --tlsAuto
```

### Managing the `public/` Git Submodule

`public/` is a git submodule tracking `git@github.com:dbc60/dbc60.github.io` on branch `master`.

**After every `hugo` build:**

1. Check for stale hashed CSS files and delete them before committing:

   ```bash
   ls public/css/
   # Delete any style.min.<oldhash>.css files that are no longer referenced.
   # Keep only the current hashed file and style.css.
   rm public/css/style.min.<oldhash>.css
   ```

2. Commit and push the submodule:

   ```bash
   cd public
   git add -A
   git commit -m "publish: <brief description>"
   git push origin master
   cd ..
   ```

3. Update the submodule pointer in the parent repo:

   ```bash
   git add public
   git commit -m "chore: update public submodule"
   git push
   ```

**Why delete old CSS files?** Hugo generates content-hashed CSS filenames (e.g. `style.min.<hash>.css`). Each build with changed CSS produces a new hash. The old file is no longer referenced by any page but stays on disk — and in the deployed repo — until manually removed. Leaving stale files bloats the repo and the deployed site.

---

## Series: Faultline — A C Unit-Test Framework with Fault Injection

Faultline is a unit-test framework for C that includes fault injection. This series introduces the project and the journey of building it.

Recommended reading order: posts 1–4 in sequence.

**Pre-series prerequisite:** Push the Faultline repo to GitHub before publishing Post 1 — all posts link to the source.

---

### Post 1 — The Original Implementation
**Status:** `planned`

**Core idea:** Present the simplest C unit-test framework you could conceive, and explain the thinking behind it.

**Narrative engine:** "Here's the simplest possible thing" — developers are drawn to minimal implementations.

**Key points:**
- The basic unit-test framework as the starting point
- Why `setjmp`/`longjmp` was the right primitive for test escape mechanics (an unusual choice worth explaining — signals deliberate design, not defaults)
- How Faultline grew out of that foundation

**Goal:** Reader walks away understanding the original design and the reasoning behind its core mechanism.

---

### Post 2 — Where the Design Fell Short, and the Services Model
**Status:** `planned`

**Core idea:** The gap between "first working design" and "design that survives real use."

**Narrative engine:** Classic problem/solution structure grounded in specific, real failure modes.

**Key points:**
- Concrete ways the original design fell short (be specific — vague shortcomings are less compelling than "here's exactly where it broke down")
- The services model as the response to those failures
- How the reorganization was loosely inspired by Casey Muratori's structure in Handmade Hero (mention as an influence, not a dependency — readers unfamiliar with HH shouldn't feel lost)
- What the new model solved

**Goal:** Reader walks away with a concrete example of design iteration and the thinking that drives it.

**Note:** Probably the most broadly useful post of the series.

---

### Post 3 — The Clang Release-Build Bug
**Status:** `planned`

**Core idea:** A subtle bug invisible to MSVC that only surfaced in Clang release builds, and how you tracked it down.

**Narrative engine:** Natural tension — worked fine in VS2022, broke in Clang release mode, here's why. Readers burned by similar bugs will feel recognition; readers who haven't will come away with something genuinely useful.

**Key points:**
- Context: the bug was dormant until build scripts were added for Clang
- What the bug was and why release-mode optimization exposed it
- The investigation — prioritize how-you-found-it over the fix itself
- The fix, and what it implies about the original code

**Goal:** Reader walks away understanding both the specific bug and the broader lesson about compiler-specific behavior and optimization assumptions.

**Note:** The gem of the series. Resist the urge to lead with the fix — the investigation is the story.

---

### Post 4 — CI/CD Integration: JUnit XML Output
**Status:** `planned`

**Core idea:** How Faultline ended up with JUnit XML output, told as a chain of discoveries.

**Narrative engine:** One thing led to another — the development story is the post.

**Key points / discovery chain:**
1. Visualizing Ukkonen's Suffix Tree Algorithm on HN → offline visualization on GitHub
2. That repo led to BATS (Bash Automated Test System), whose README described it as "a TAP-compliant testing framework for Bash"
3. What's TAP? The Test Anything Protocol. Almost stopped there with the idea of adding TAP to Faultline
4. Asked a better question: what other test output protocols exist, and are any more appropriate for a C unit-test framework?
5. Claude listed several; JUnit XML emerged as the de facto standard
6. GitLab CI has native, first-party JUnit support — JUnit XML is required
7. GitHub Actions has no native equivalent, but the major test reporter actions (dorny/test-reporter, EnricoMi/publish-unit-test-result-action, mikepenz/action-junit-report) all list JUnit XML as primary or sole XML format; only test-summary/action listed TAP support
8. Decision: JUnit XML

**Goal:** Reader understands why JUnit XML was the right choice, and gets a model for how to evaluate output format decisions for developer tooling.
