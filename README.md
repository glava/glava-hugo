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