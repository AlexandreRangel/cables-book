# Screenshot Approach Guide

## Option 2: Real Cables.gl Screenshots

This approach uses actual screenshots from cables.gl for maximum authenticity.

### How to Create

1. **Open cables.gl** in your browser
2. **Create your patch** (e.g., MainLoop → BasicMaterial → Circle)
3. **Arrange ops cleanly** with good spacing
4. **Take screenshot** of the patch editor area
5. **Crop and optimize** the image
6. **Save as PNG** with transparent or dark background

### Advantages
- 100% authentic cables.gl appearance
- Exact fonts, colors, and styling
- Shows real UI elements
- Port colors are accurate
- Connection curves are perfect

### Disadvantages
- Requires manual screenshot process
- Not easily editable
- File size larger than SVG
- May include UI chrome (toolbars, etc.)
- Resolution dependent

### Best For
- Quick documentation
- Showing complex patches
- Tutorial steps that need exact UI reference
- When you need to show actual cables.gl interface

### Tools
- **Windows**: Snipping Tool, Win+Shift+S
- **Mac**: Cmd+Shift+4
- **Optimization**: TinyPNG, ImageOptim, Squoosh

### Example Workflow

```bash
1. Create patch in cables.gl
2. Press F11 for fullscreen (optional - cleaner look)
3. Take screenshot of patch area
4. Crop to just the ops and connections
5. Optimize with: npx @squoosh/cli --webp '{quality:85}' screenshot.png
6. Save to: chapters/images/basic-render-chain-screenshot.png
```

### Screenshot Tips
- Use dark theme for consistency
- Hide unnecessary UI panels
- Zoom to comfortable size
- Ensure good contrast
- Keep consistent framing across all screenshots

