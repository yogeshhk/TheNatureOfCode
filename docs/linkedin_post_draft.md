# LinkedIn Post Draft

Status: draft, not yet published. See the "Publish LinkedIn post" item in
`TODO.md` for when to use this.

Suggested images: `banner_wide.svg` (link-preview / cover format, 1200x630) or
`banner_square.svg` (square image-post format, 1200x1200), both in this folder.
LinkedIn doesn't accept SVG uploads directly, so export whichever one you use to
PNG first (open it in a browser and screenshot it, or run it through any
SVG-to-PNG converter) before attaching it to the post.

---

## Post text (copy everything below the line)

---

I've been chipping away at a personal project: porting Daniel Shiffman's *The
Nature of Code* from Processing to Python, following along with his YouTube
series.

Just wrapped a cleanup pass on the repo. A few things were quietly broken:

- One example called a method that doesn't actually exist in the py5 API, so
  it crashed the moment you ran it
- The setup docs still told people to install the old, unmaintained "p5"
  library, even though every script actually imports "py5" (a different,
  actively maintained one)
- requirements.txt was a leftover dump from an unrelated environment, full of
  macOS-only packages that wouldn't even install on Windows

All fixed now, plus some smaller consistency cleanups across the examples.

Where things stand: the repo currently covers the book's Introduction /
Randomness, Vectors, Forces, and Oscillation chapters (through Springs).
Roughly the first third of the book.

I also added a CONTRIBUTING.md for anyone who wants to help extend it. It
walks through getting the existing code running, then a table mapping what's
implemented against the book's own chapter list, so you can see exactly where
coverage stops. Right now that's Chapter 4, Particle Systems: the first
chapter with nothing built yet.

If you've been meaning to work through Nature of Code yourself, or want a
low-stakes way to practice porting Processing sketches to Python, this could
be a fun place to start.

Repo: https://github.com/yogeshkulkarni/TheNatureOfCode

#Python #Processing #py5 #CreativeCoding #GenerativeArt #NatureOfCode #OpenSource

---

## Notes for whoever publishes this
- Swap in the actual repo URL if the slug ever changes.
- If more chapters get implemented before this is posted, update the "where
  things stand" paragraph and the CONTRIBUTING.md pointer accordingly.
- Consider attaching a short screen-recording GIF of one sketch (e.g. the
  springs or gravitational-attraction example) instead of a static banner if
  one exists by the time this goes out; motion tends to perform better on
  LinkedIn for this kind of content.
