# Claude Code Prompt: Hugo Photography Portfolio Setup

## Context
I'm migrating from Adobe Portfolio to a self-hosted Hugo site on GitHub Pages. I have a minimal, clean aesthetic photography portfolio (see reference design). The site is a personal photography diary with archive navigation by date. Traffic is minimal (~10 visits/month). I'm comfortable with technical setup.

**Key constraints:**
- Minimal, clean aesthetic (white space, black & white images)
- Mobile responsive
- Archive-organized by date/project
- Static site (Hugo)
- Hosted on GitHub Pages
- Images stored locally: `/Users/goran/Documents/Photos/2025/Oct`


## Task: Build a complete Hugo portfolio project with image processing pipeline

### Part 1: Hugo Project Structure
Create a Hugo project with the following structure:

```
hugo-portfolio/
├── config.toml                    # Hugo config
├── content/
│   └── posts/                     # Each project as a post
│       ├── 2024-day-out-tegeler-forst.md
│       └── ... (other projects)
├── static/
│   └── images/                    # Processed images go here
│       ├── 2024/
│       │   └── day-out-tegeler-forst/
│       │       ├── hero.jpg
│       │       ├── thumb-1.jpg
│       │       └── ...
├── layouts/
│   ├── _default/
│   │   ├── single.html           # Individual project page
│   │   └── list.html             # Archive/index page
│   └── partials/
│       └── header.html
├── assets/
│   └── css/
│       └── style.css             # Minimal CSS
└── .gitignore
```

### Part 2: Hugo Configuration
- Clean, minimal theme (no heavy frameworks)
- SEO-friendly URLs
- Mobile-responsive design
- Simple navigation with archive listing
- Sidebar navigation similar to the reference (dated entries)

### Part 3: Image Processing Pipeline
Create a Python or Bash script that:
1. Reads images from `/Users/goran/Documents/Photos/2025/Oct` (and future dates)
2. For each image:
   - Resize to web-friendly sizes (max 2000px width)
   - Compress to 70-80% JPG quality
   - Create thumbnails (500px width for gallery)
   - Output to `static/images/[YYYY]/[project-name]/`
3. Generate a Hugo markdown file structure from the organized images

### Part 4: Content Organization
- Create a template/example markdown file for a photo project
- Show how to organize images by date and project
- Include front matter with title, date, description

### Part 5: Styling & Templates
- HTML templates using semantic HTML
- Minimal CSS (no frameworks like Bootstrap)
- Mobile-first responsive design
- Clean typography
- Image gallery layout (similar to reference: hero + grid of smaller images)
- The look I am going for /Users/goran/Desktop/Screenshot\ 2025-10-31\ at\ 09.23.23.png

### Part 6: Deployment to GitHub Pages
- `.github/workflows/deploy.yml` - GitHub Actions workflow to:
  - Build Hugo site
  - Deploy to GitHub Pages
- `.gitignore` - exclude large original images, only commit processed versions
- Instructions for GitHub Pages setup

## Output Deliverables

1. **Complete Hugo project** with all files
2. **Image processing script** (Python/Bash) that's easy to run regularly
3. **Example content** with one sample project (Tegeler Forst) with real image organization
4. **CSS** - minimal, clean, responsive design matching your aesthetic
5. **GitHub Actions workflow** for automatic deployment
6. **README.md** with:
   - How to add new projects
   - How to run the image processing script
   - How to deploy
   - Directory structure explanation

## Design Requirements

- **Typography**: Clean, readable sans-serif (system fonts fine)
- **Color scheme**: Minimal (white, black, grays)
- **Layout**:
  - Left sidebar navigation (dated archive list)
  - Main content area for images
  - Hero image (large, full-width or near-full)
  - Gallery grid below (4 images in 2x2 or flexible grid)
  - Mobile: stacked layout, sidebar becomes hamburger menu or collapses
- **Image display**: Full-width or near full-width, with proper spacing
- **"Back to Top" link**: Simple footer link
- **No clutter**: No analytics, comments, share buttons, ads

## Technical Notes

- Use Hugo's built-in features (no heavy plugins)
- Image processing: ImageMagick, Pillow (Python), or similar
- Static file serving from GitHub Pages
- Custom domain support (already purchased)
- Git-based workflow

## Image Paths & Organization

- Source images: `/Users/goran/Documents/Photos/2025/Oct`
- Processed images will go to: `static/images/2025/oct-day-out-tegeler-forst/`
- Hugo will reference them as: `/images/2025/oct-day-out-tegeler-forst/image.jpg`

## Questions to Clarify During Build

- Preferred slug/naming convention for projects? (e.g., `2024-day-out-tegeler-forst` or `tegeler-forst-2024`)
- Should sidebar show all past projects or just current year?
- Preferred grid layout for smaller images? (e.g., 2 columns, 4 columns)
- Any specific fonts you prefer, or system fonts fine?

---

**Start by creating the full project structure and configuration, then build the image processing script, then create example templates and styling.**
