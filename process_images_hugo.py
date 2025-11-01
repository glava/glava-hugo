#!/usr/bin/env python3
"""
Hugo-integrated image processing script for photography portfolio
Uses Hugo's image processing instead of manual resizing
"""

import os
import sys
import shutil
from pathlib import Path
import argparse
import re
from datetime import datetime
from PIL import Image, ImageOps

def slugify(text):
    """Convert text to URL-friendly slug"""
    text = re.sub(r'[^\w\s-]', '', text.lower())
    return re.sub(r'[-\s]+', '-', text).strip('-')

def copy_and_fix_rotation(source_file, dest_file):
    """Copy image and fix EXIF rotation"""
    try:
        with Image.open(source_file) as img:
            # Apply EXIF orientation and save
            img = ImageOps.exif_transpose(img)
            img.save(dest_file, quality=95, optimize=True)
        return True
    except Exception as e:
        print(f"Error processing {source_file}: {e}")
        # Fallback to regular copy
        shutil.copy2(source_file, dest_file)
        return False

def copy_images_to_hugo(source_dir, project_slug, hugo_root):
    """Copy images to Hugo's page bundle structure with EXIF rotation fixed"""
    source_path = Path(source_dir)
    if not source_path.exists():
        print(f"Source directory does not exist: {source_dir}")
        return False
    
    # Create page bundle directory in content/posts
    bundle_dir = Path(hugo_root) / "content" / "posts" / project_slug
    bundle_dir.mkdir(parents=True, exist_ok=True)
    
    # Get all image files
    image_extensions = {'.jpg', '.jpeg', '.png', '.tiff', '.bmp'}
    image_files = [f for f in source_path.iterdir() 
                  if f.suffix.lower() in image_extensions and f.is_file()]
    
    if not image_files:
        print(f"No image files found in {source_dir}")
        return False
    
    # Sort files for consistent ordering
    image_files.sort()
    
    copied_images = []
    
    for i, image_file in enumerate(image_files):
        # Copy all images for gallery (with rotation fixed)
        gallery_filename = f"gallery-{i+1:02d}{image_file.suffix}"
        gallery_path = bundle_dir / gallery_filename
        copy_and_fix_rotation(image_file, gallery_path)
        copied_images.append(gallery_filename)
        print(f"✓ Copied and fixed rotation for gallery image: {gallery_filename}")
    
    return {
        'gallery': copied_images,
        'count': len(copied_images),
        'bundle_dir': bundle_dir
    }

def create_hugo_page_bundle(project_name, year, date, description, image_data, hugo_root):
    """Create Hugo page bundle with index.md"""
    bundle_dir = image_data['bundle_dir']
    
    # Create index.md in the bundle directory
    index_path = bundle_dir / "index.md"
    
    # Create front matter
    frontmatter = f"""---
title: "{project_name}"
date: {date}T12:00:00Z
description: "{description}"
gallery:
"""
    
    # Add gallery images
    for img in image_data['gallery']:
        frontmatter += f'  - "{img}"\n'
    
    frontmatter += "---\n\n"
    
    # Add basic content with flexible structure for multiple galleries
    content = f"""A collection of {image_data['count']} photographs from {project_name}.

Captured with attention to light, composition, and the quiet moments that define each scene.

You can add more text here and create additional galleries by editing this file.
"""
    
    # Write the file
    with open(index_path, 'w') as f:
        f.write(frontmatter + content)
    
    print(f"✓ Created page bundle: {bundle_dir.name}/index.md")
    return index_path

def main():
    parser = argparse.ArgumentParser(description='Process images for Hugo photography portfolio using Hugo image processing')
    parser.add_argument('source_dir', help='Source directory containing images')
    parser.add_argument('--project-name', required=True, help='Name of the photography project')
    parser.add_argument('--year', help='Year for the project (default: current year)')
    parser.add_argument('--date', help='Date for the project (YYYY-MM-DD format)')
    parser.add_argument('--description', default='', help='Project description')
    parser.add_argument('--hugo-root', default='.', help='Hugo project root directory')
    
    args = parser.parse_args()
    
    # Set defaults
    if not args.year:
        args.year = str(datetime.now().year)
    
    if not args.date:
        args.date = datetime.now().strftime('%Y-%m-%d')
    
    print(f"Processing project: {args.project_name}")
    print(f"Source directory: {args.source_dir}")
    print(f"Year: {args.year}")
    print(f"Date: {args.date}")
    
    # Create project slug
    slug = f"{args.year}-{slugify(args.project_name)}"
    
    # Copy images to Hugo page bundle
    image_data = copy_images_to_hugo(
        args.source_dir, 
        slug, 
        args.hugo_root
    )
    
    if not image_data:
        print("Failed to process images")
        sys.exit(1)
    
    # Create Hugo page bundle
    create_hugo_page_bundle(
        args.project_name,
        args.year,
        args.date,
        args.description,
        image_data,
        args.hugo_root
    )
    
    print(f"\n✅ Successfully processed {image_data['count']} images for '{args.project_name}'")
    print(f"Page bundle created: content/posts/{slug}/")
    print(f"Hugo will automatically process images at different sizes")
    print(f"\nNext: Run 'hugo server' to see your new project!")

if __name__ == "__main__":
    main()