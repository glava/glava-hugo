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

Use the image processing script to add new projects:

```bash
# Example: Process images from your photos directory
python process_images.py "/Users/goran/Documents/Photos/2025/Oct" \
  --project-name "Day Out - Tegeler Forst" \
  --year 2024 \
  --date 2024-10-15 \
  --description "A day exploring the autumn landscapes of Tegeler Forst"
```

This will:
- Resize and compress images for web
- Create thumbnails
- Generate Hugo markdown content file
- Organize files in the correct directory structure

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
python process_images.py <source_directory> --project-name "Project Name" [options]

Options:
  --year YEAR           Year for the project (default: current year)
  --date YYYY-MM-DD     Date for the project (default: today)
  --description TEXT    Project description
  --hugo-root PATH      Hugo project root (default: current directory)
```

### Example Usage

```bash
# Process October 2025 photos
python process_images.py "/Users/goran/Documents/Photos/2025/Oct" \
  --project-name "Autumn in Berlin" \
  --year 2025 \
  --date 2025-10-31 \
  --description "Capturing autumn colors around Berlin"
```

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