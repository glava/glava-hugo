# Photography Portfolio - Hugo Static Site

A minimal, clean photography portfolio built with Hugo and designed for GitHub Pages deployment.

## Project Structure

```
hugo-glava/
├── config.toml                 # Hugo configuration
├── content/posts/              # Photography projects (markdown files)
├── static/images/              # Processed web-ready images
├── layouts/                    # HTML templates
├── assets/css/                 # Stylesheets
├── process_images.py           # Image processing script
└── .github/workflows/          # GitHub Actions for deployment
```

## Quick Start

### 1. Install Dependencies

```bash
# Install Hugo (extended version)
brew install hugo

# Install Python dependencies for image processing
pip install Pillow
```

### 2. Add New Photography Project

Use the Hugo-integrated image processing script:

```bash
# Process images from your source directory
python3 process_images_hugo.py "./source" \
  --project-name "Day Out - Tegeler Forst" \
  --year 2024 \
  --description "Autumn forest photography"
```

This will:
- Copy images to Hugo page bundle structure
- Fix EXIF rotation automatically
- Generate Hugo markdown content file
- Let Hugo handle all image resizing and optimization

### 2.1. Update/Replace Existing Project

**Common workflow when you change your mind:**

1. **Update source images**: Replace/add/remove photos in your `source/` directory
2. **Re-run processing script**: Use the same command as above
3. **Hugo auto-rebuilds**: Site updates automatically with new images

```bash
# Example: You changed one photo in source/ and want to republish
python3 process_images_hugo.py "./source" \
  --project-name "Day Out - Tegeler Forst" \
  --year 2024 \
  --description "Autumn forest photography"
```

**What happens:**
- ✅ Overwrites existing project with updated images
- ✅ Fixes EXIF rotation for any new/changed photos
- ✅ Hugo automatically processes new image sizes
- ✅ Live reload updates your browser instantly

### 3. Preview Locally

```bash
hugo server -D
```

Visit `http://localhost:1313` to preview your site.

### 4. Deploy to GitHub Pages

1. Push your changes to the `main` branch
2. GitHub Actions will automatically build and deploy your site
3. Your site will be available at `https://yourusername.github.io/repository-name`

## Image Processing Script Usage

```bash
python3 process_images_hugo.py <source_directory> --project-name "Project Name" [options]

Options:
  --year YEAR           Year for the project (default: current year)
  --date YYYY-MM-DD     Date for the project (default: today)
  --description TEXT    Project description
  --hugo-root PATH      Hugo project root (default: current directory)
```

### Example Usage

```bash
# Process photos from source directory
python3 process_images_hugo.py "./source" \
  --project-name "Autumn in Berlin" \
  --year 2025 \
  --description "Capturing autumn colors around Berlin"
```

### Workflow for Managing Projects

**Initial Setup:**
1. Place your photos in `source/` directory
2. Run the processing script
3. Preview with `hugo server`

**When You Want to Change Something:**
1. **Replace photos**: Update files in `source/` directory
2. **Re-run script**: Same command as initial setup
3. **Auto-update**: Hugo live reload shows changes instantly

**Multiple Projects:**
- Each run creates/updates one project
- Different project names create separate blog posts
- Use descriptive project names for better organization

## Gallery Layout Options

Your portfolio supports multiple flexible gallery layouts for different storytelling needs:

### Single Gallery Layouts

Add `gallery_layout` to your front matter to control the layout:

```yaml
---
title: "Your Project"
gallery_layout: "gallery-mixed"  # Choose layout type
gallery:
  - "gallery-01.JPG"
  - "gallery-02.JPG"
  - "gallery-03.JPG"
---
```

**Available layouts:**

1. **`gallery` (default)** - 2x2 grid:
   ```
   [ img ] [ img ]
   [ img ] [ img ]
   ```

2. **`gallery-mixed`** - 1 large + smaller images:
   ```
   [   LARGE    ] [ small ]
   [   IMAGE    ] [ small ]
   [            ] [ small ]
   ```
   - Perfect for hero shot + supporting images
   - No wasted space, flexible height

3. **`gallery-three`** - 3 equal columns:
   ```
   [ img ] [ img ] [ img ]
   [ img ] [ img ] [ img ]
   ```

4. **`gallery-compact`** - Wide format with small images:
   ```
   [     LARGE      ] [ sm ] [ sm ]
   [     IMAGE      ] [ sm ] [ sm ]
   ```

5. **`gallery-single`** - Full width images:
   ```
   [    FULL WIDTH IMAGE    ]
   [    FULL WIDTH IMAGE    ]
   ```

### Multiple Galleries on One Page

Create rich storytelling by mixing galleries with text:

```yaml
---
title: "Day Out - Tegeler Forst"
gallery_layout: "gallery-mixed"
gallery:
  - "gallery-01.JPG"
  - "gallery-02.JPG"
  - "gallery-03.JPG"
gallery2_layout: "gallery-three"
gallery2:
  - "gallery-04.JPG"
  - "gallery-05.JPG"
  - "gallery-06.JPG"
gallery3_layout: "gallery-single"
gallery3:
  - "gallery-07.JPG"
---

## Morning Walk
First part of our day exploring the forest...

<!-- First gallery appears here -->

## Afternoon Discovery
Later we found this amazing spot...

<!-- Second gallery appears here -->

## Evening Light
As the sun set, we captured these final moments...

<!-- Third gallery appears here -->
```

**Features:**
- ✅ **Up to 3 galleries** per page (`gallery`, `gallery2`, `gallery3`)
- ✅ **Different layouts** for each gallery
- ✅ **Text between galleries** for storytelling
- ✅ **Continuous lightbox** navigation across all images
- ✅ **Flexible ordering** and combinations

### Layout Selection Guide

**Use `gallery-mixed` when:**
- You have one standout hero image
- Want to emphasize one photo over others
- Need efficient space usage

**Use `gallery-three` when:**
- All images have equal importance
- Want clean, organized presentation
- Have 3, 6, 9+ images

**Use `gallery-compact` when:**
- You have landscape-oriented hero image
- Want more horizontal emphasis
- Need to fit many small images

**Use `gallery-single` when:**
- Images deserve full attention
- Creating dramatic impact
- Showing detailed work

**Use `gallery` (default) when:**
- Simple, balanced presentation
- Classic 2x2 grid works well
- No specific layout requirements

## Text Alignment Options

Control how text content appears on your project pages by adding a CSS class to your content:

```yaml
---
title: "Your Project"
# ... other front matter
---

<!-- Default: centered text -->
Your project description and content will be centered by default.

<!-- For justified text, add the class in your markdown -->
<div class="project-content text-justified">

Long paragraphs work better with justified alignment. This spreads text evenly across the line width, creating clean edges on both sides. Perfect for detailed project descriptions, artist statements, or longer storytelling content.

</div>

<!-- For left-aligned text -->
<div class="project-content text-left">

Left alignment provides a more traditional reading experience.
Good for technical details, lists, or casual descriptions.

</div>
```

**Available text alignment options:**
- **Default (centered)**: Clean, artistic look that matches the minimal design
- **`text-justified`**: Even text distribution for longer paragraphs
- **`text-left`**: Traditional left alignment for readability

## Adding Projects Manually

If you prefer to add projects manually:

1. Create a new markdown file in `content/posts/`
2. Use this front matter template:

```yaml
---
title: "Project Title"
date: 2024-10-15T12:00:00Z
description: "Project description"
hero_image: "/images/2024/project-slug/hero.jpg"
gallery:
  - "/images/2024/project-slug/thumb-01.jpg"
  - "/images/2024/project-slug/thumb-02.jpg"
---

Project content goes here.
```

3. Add your processed images to `static/images/YEAR/project-slug/`

## GitHub Pages Setup

1. Go to your repository Settings > Pages
2. Set Source to "GitHub Actions"
3. The workflow will automatically deploy on every push to `main`

## Customization

### Styling
- Edit `assets/css/style.css` for visual customizations
- The design is mobile-first and responsive

### Layout
- Modify templates in `layouts/` directory
- `layouts/_default/single.html` - Individual project pages
- `layouts/_default/list.html` - Archive/index page
- `layouts/partials/sidebar.html` - Navigation sidebar

### Configuration
- Edit `config.toml` for site settings
- Update site title, description, and other metadata

## File Organization

### Source Images
- Keep original photos in `/Users/goran/Documents/Photos/YYYY/MMM/`
- Use the processing script to create web versions

### Processed Images
- Web-ready images go in `static/images/YYYY/project-name/`
- Only processed images are committed to git
- Original large files are ignored via `.gitignore`

## Tips

- Use descriptive project names for better organization
- Keep image file sizes reasonable for web performance
- The processing script handles EXIF orientation and compression automatically
- Sidebar navigation automatically updates when you add new projects