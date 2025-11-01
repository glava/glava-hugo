#!/usr/bin/env python3
"""
Image processing script for Hugo photography portfolio
Processes images from source directory and creates web-ready versions
"""

import os
import sys
from PIL import Image, ImageOps
import argparse
from pathlib import Path
import re
from datetime import datetime

def slugify(text):
    """Convert text to URL-friendly slug"""
    text = re.sub(r'[^\w\s-]', '', text.lower())
    return re.sub(r'[-\s]+', '-', text).strip('-')

def process_image(input_path, output_dir, max_width=2000, quality=75):
    """Process a single image: resize and compress"""
    try:
        with Image.open(input_path) as img:
            # Convert to RGB if necessary
            if img.mode in ('RGBA', 'P'):
                img = img.convert('RGB')
            
            # Auto-orient based on EXIF
            img = ImageOps.exif_transpose(img)
            
            # Resize if needed
            if img.width > max_width:
                ratio = max_width / img.width
                new_height = int(img.height * ratio)
                img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
            
            # Save compressed image
            img.save(output_dir, 'JPEG', quality=quality, optimize=True)
            return True
    except Exception as e:
        print(f"Error processing {input_path}: {e}")
        return False

def create_thumbnail(input_path, output_path, width=500):
    """Create thumbnail version of image"""
    try:
        with Image.open(input_path) as img:
            if img.mode in ('RGBA', 'P'):
                img = img.convert('RGB')
            
            img = ImageOps.exif_transpose(img)
            
            # Calculate new height maintaining aspect ratio
            ratio = width / img.width
            new_height = int(img.height * ratio)
            img = img.resize((width, new_height), Image.Resampling.LANCZOS)
            
            img.save(output_path, 'JPEG', quality=80, optimize=True)
            return True
    except Exception as e:
        print(f"Error creating thumbnail for {input_path}: {e}")
        return False

def process_project_directory(source_dir, project_name, year, hugo_root):
    """Process all images in a project directory"""
    source_path = Path(source_dir)
    if not source_path.exists():
        print(f"Source directory does not exist: {source_dir}")
        return False
    
    # Create output directory structure
    output_dir = Path(hugo_root) / "static" / "images" / year / project_name
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Get all image files
    image_extensions = {'.jpg', '.jpeg', '.png', '.tiff', '.bmp'}
    image_files = [f for f in source_path.iterdir() 
                  if f.suffix.lower() in image_extensions and f.is_file()]
    
    if not image_files:
        print(f"No image files found in {source_dir}")
        return False
    
    # Sort files for consistent ordering
    image_files.sort()
    
    processed_images = []
    hero_image = None
    
    for i, image_file in enumerate(image_files):
        # First image becomes hero
        if i == 0:
            hero_filename = "hero.jpg"
            hero_path = output_dir / hero_filename
            if process_image(image_file, hero_path, max_width=2000, quality=80):
                hero_image = f"/images/{year}/{project_name}/{hero_filename}"
                print(f"✓ Processed hero image: {hero_filename}")
        
        # Create gallery thumbnails for all images
        thumb_filename = f"thumb-{i+1:02d}.jpg"
        thumb_path = output_dir / thumb_filename
        if create_thumbnail(image_file, thumb_path, width=500):
            processed_images.append(f"/images/{year}/{project_name}/{thumb_filename}")
            print(f"✓ Created thumbnail: {thumb_filename}")
    
    return {
        'hero_image': hero_image,
        'gallery': processed_images,
        'count': len(processed_images)
    }

def create_hugo_content(project_name, year, date, description, image_data, hugo_root):
    """Create Hugo markdown content file"""
    content_dir = Path(hugo_root) / "content" / "posts"
    content_dir.mkdir(parents=True, exist_ok=True)
    
    # Create filename
    slug = slugify(project_name)
    filename = f"{year}-{slug}.md"
    content_path = content_dir / filename
    
    # Create front matter
    frontmatter = f"""---
title: "{project_name}"
date: {date}T12:00:00Z
description: "{description}"
hero_image: "{image_data['hero_image']}"
gallery:
"""
    
    # Add gallery images
    for img in image_data['gallery']:
        frontmatter += f'  - "{img}"\n'
    
    frontmatter += "---\n\n"
    
    # Add basic content
    content = f"""A collection of {image_data['count']} photographs from {project_name}.

{{{{< gallery >}}}}
"""
    
    # Write the file
    with open(content_path, 'w') as f:
        f.write(frontmatter + content)
    
    print(f"✓ Created content file: {filename}")
    return content_path

def main():
    parser = argparse.ArgumentParser(description='Process images for Hugo photography portfolio')
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
    
    # Process images
    slug = slugify(args.project_name)
    image_data = process_project_directory(
        args.source_dir, 
        slug, 
        args.year, 
        args.hugo_root
    )
    
    if not image_data:
        print("Failed to process images")
        sys.exit(1)
    
    # Create Hugo content
    create_hugo_content(
        args.project_name,
        args.year,
        args.date,
        args.description,
        image_data,
        args.hugo_root
    )
    
    print(f"\n✅ Successfully processed {image_data['count']} images for '{args.project_name}'")
    print(f"Images saved to: static/images/{args.year}/{slug}/")
    print(f"Content created: content/posts/{args.year}-{slug}.md")

if __name__ == "__main__":
    main()