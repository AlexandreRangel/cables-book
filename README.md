# The Cables.gl Book

A comprehensive guide to cables.gl - the visual programming platform for creating interactive WebGL experiences.

## About This Book

This book is designed to take you from beginner to advanced cables.gl user. Each chapter focuses on a specific topic and includes tutorials, examples, and curated YouTube video resources.

## Dependencies & Installation

### Quick Install (Recommended)

Run the automated installer:

```bash
./install-requirements.bat
```

This will install all Python packages and check for system dependencies.

### System Requirements (Windows) - Manual Install

Before running `install.bat`, you need these system dependencies:

#### 1. Python 3.x
- Download from: https://www.python.org/downloads/
- **Important:** Check "Add Python to PATH" during installation

#### 2. Pandoc (Document Converter)
- Download from: https://pandoc.org/installing.html
- Or install via Chocolatey: `choco install pandoc`

#### 3. MiKTeX or TeX Live (LaTeX Distribution)
- **MiKTeX** (recommended for Windows): https://miktex.org/download
  - During installation, select "Install missing packages on-the-fly: Yes"
- Or **TeX Live**: https://tug.org/texlive/
- Provides XeLaTeX engine for PDF generation

#### 4. Ubuntu Fonts
- Download from: https://fonts.google.com/specimen/Ubuntu
- Install both **Ubuntu** and **Ubuntu Mono** font families
- Required for the book's typography

### Quick Install with Chocolatey

```powershell
# Install Chocolatey if not installed (see https://chocolatey.org/install)

# Install system dependencies
choco install python pandoc miktex -y

# Then run the installer
./install-requirements.bat
```

### Python Packages (Reference)

These are installed automatically by `install-requirements.bat`:

| Package | Purpose |
|---------|---------|
| `requests` | HTTP requests for web scraping |
| `beautifulsoup4` | HTML parsing for scraping cables.gl ops |
| `playwright` | Headless browser automation for scraping dynamic content |
| `svglib` | SVG file parsing |
| `reportlab` | PDF generation from SVG (required for XeLaTeX) |

### Generating the Book

Run the batch script to generate the PDF:

```bash
./makebook.bat
```

This will:
1. Convert SVG images to PDF format (XeLaTeX compatibility)
2. Combine all chapter markdown files
3. Generate `cables-gl-book.pdf` using Pandoc + XeLaTeX

---

## Chapters

1. **[Introduction](chapters/01-introduction.md)** - What is cables.gl and why use it
2. **[Getting Started](chapters/02-getting-started.md)** - Interface, navigation, and your first patch
3. **[2D Graphics](chapters/03-2d-graphics.md)** - Shapes, colors, and 2D transformations
4. **[3D Graphics](chapters/04-3d-graphics.md)** - Meshes, cameras, lighting, and 3D scenes
5. **[Texturing](chapters/05-texturing.md)** - Images, videos, and texture mapping
6. **[Shaders & GLSL](chapters/06-shaders-glsl.md)** - Custom shaders and visual effects
7. **[JavaScript & Custom Ops](chapters/07-javascript-ops.md)** - Writing custom operators
8. **[Audio & Sound](chapters/08-audio-sound.md)** - Audio reactive visuals and sound
9. **[Animation & Timeline](chapters/09-animation-timeline.md)** - Keyframes and time-based animation
10. **[Interfaces](chapters/10-interfaces.md)** - User interfaces and interactions
11. **[Export & Deployment](chapters/11-export-deployment.md)** - Standalone builds and embedding
12. **[Video Tutorials](chapters/12-video-tutorials.md)** - A heavily searched index of cables.gl videos, organized by theme
13. **[All Ops Reference](chapters/13-AllOps.md)** - Complete reference of all cables.gl operators

## Video Format Guide

When adding YouTube videos to chapters, use this format:

```vid
https://youtu.be/VIDEO_ID
Title: Video Title Here
Author: Channel Name
Thumbnail: https://i.ytimg.com/vi/VIDEO_ID/mqdefault.jpg
```

## Contributing

Feel free to add more videos, examples, and content to each chapter!

---

*Last updated: December 29, 2025*
