# Cables.gl Ops Scraper Scripts

This folder contains all scripts related to scraping, validating, and generating the **All Operators Reference** (Chapter 13) for the cables.gl book.

## Current Issues with AllOps.md

Many ops have incomplete or incorrect data:
- **Missing port descriptions** - Shows "Visit documentation for details" instead of actual info
- **Wrong images** - Some SVG images may not match the op
- **Missing descriptions** - Op descriptions are empty or placeholders
- **Incorrect URLs** - Some URLs may be malformed

## IMPORTANT: cables.gl Uses JavaScript Rendering

cables.gl op pages are **JavaScript-rendered**, meaning the port information is loaded dynamically. This requires:

1. **Browser-based scraping** (recommended) - Uses Playwright to render pages fully
2. OR **API access** (if available) - Direct API calls for structured data

The simple `requests`-based scrapers will miss most port information because the HTML doesn't contain the rendered content.

## Script Overview

### Main Scripts (Use These)

| Script | Purpose | Usage |
|--------|---------|-------|
| `browser_op_scraper.py` | **RECOMMENDED** - Uses headless browser for accurate scraping | `python browser_op_scraper.py` |
| `thorough_op_scraper.py` | Requests-based scraper (faster but less accurate) | `python thorough_op_scraper.py` |
| `validate_allops.py` | Validates and audits AllOps.md for completeness | `python validate_allops.py` |
| `regenerate_allops.py` | Regenerates 13-AllOps.md from scraped JSON data | `python regenerate_allops.py` |

### Supporting/Legacy Scripts

| Script | Purpose | Notes |
|--------|---------|-------|
| `comprehensive_scraper.py` | Earlier attempt at comprehensive scraping | Uses requests only, limited JS support |
| `scrape_ops_with_browser.py` | Browser-based scraping with Playwright | Requires Playwright installation |
| `full_scraper.py` | Full namespace scraping | Legacy approach |
| `scrape_correct_ops.py` | Attempt to get correct op info | Basic requests approach |
| `scrape_cables_ops.py` | Original basic scraper | Very limited |
| `get_all_correct_ops.py` | Get all correct op names | Helper script |
| `regenerate_allops_correct.py` | Earlier regeneration attempt | Legacy |
| `generate_allops.py` | Earlier generation script | Legacy |
| `generate_allops_complete.py` | Earlier complete generation | Legacy |
| `generate_all_ops_complete.py` | Earlier complete generation | Legacy |
| `generate_complete_allops.py` | Earlier complete generation | Legacy |
| `upgrade_all_ops.py` | Upgrade script | Legacy |
| `upgrade_all_ops_to_detailed.py` | Upgrade to detailed format | Legacy |
| `scrape_allops.py` | Original AllOps scraper | Legacy |
| `scrape_allops_improved.py` | Improved version | Legacy |
| `test_scrape.py` | Test scraping functions | Development |
| `test_scraper.py` | Test scraper functionality | Development |

## How cables.gl Op Pages Work

Each op has its own page at: `https://cables.gl/op/Ops.Namespace.OpName`

The page structure includes:
1. **Op name/title** - The short name of the op
2. **Full Name** - Complete namespace path (e.g., `Ops.Anim.SimpleAnim`)
3. **Summary** - One-liner description
4. **INPUT PORTS section** - List of input ports with:
   - Port name
   - Port type (Number, String, Trigger, Object, Array, etc.)
   - Description
5. **OUTPUT PORTS section** - Same structure as inputs
6. **Examples** - Links to example patches
7. **Changelog** - Version history

### Port Types in cables.gl

- `Number` - Numeric value (can be boolean: 0/1)
- `String` - Text value
- `Trigger` - Execution trigger (like an event)
- `Object` - JavaScript object
- `Array` - Array of values
- `Texture` - WebGL texture
- `Function` - JavaScript function

## API Endpoints

cables.gl provides an SVG layout API:
```
https://cables.gl/api/op/layout/Ops.Namespace.OpName
```

This returns an SVG diagram of the op showing:
- Op name
- All input ports (left side)
- All output ports (right side)
- Port types (color coded)

## JSON Data Files

| File | Description |
|------|-------------|
| `../all_ops_list.json` | List of all ops by namespace (basic info) |
| `../all_ops_complete.json` | More complete op data |
| `../detailed_ops_data.json` | Detailed scraped data |
| `../correct_ops_data.json` | Corrected op data |
| `../scraped_ops_data.json` | Raw scraped data |

## Recommended Workflow

### To Re-scrape All Ops Thoroughly:

1. **First, install dependencies:**
   ```bash
   pip install requests beautifulsoup4 playwright
   playwright install chromium
   ```

2. **Run the browser-based scraper (recommended for accuracy):**
   ```bash
   cd scripts
   python browser_op_scraper.py
   ```
   This will:
   - Use a headless browser to render each page
   - Extract description, input ports, output ports
   - Download fresh SVG images
   - Save progress to JSON (can resume if interrupted)
   - Takes 4-8 hours for all ~1340 ops

   **Alternative (faster but less complete):**
   ```bash
   python thorough_op_scraper.py
   ```
   Uses simple HTTP requests - faster but gets less port info.

3. **Validate the results:**
   ```bash
   python validate_allops.py
   ```
   This shows:
   - How many ops have complete data
   - Which ops are still missing ports
   - Which ops have placeholder descriptions

4. **Regenerate the markdown:**
   ```bash
   python regenerate_allops.py
   ```

### To Update a Specific Namespace:

```bash
python browser_op_scraper.py --namespace Ops.Gl
```

### To Resume an Interrupted Scrape:

The scraper saves progress to JSON periodically. Just run it again with --resume:
```bash
python browser_op_scraper.py --resume
```

### Options for browser_op_scraper.py:

```
--namespace NAMESPACE  Only scrape ops in this namespace
--resume               Resume from last saved progress
--test                 Test mode - only scrape 10 ops
--slow                 Slower but more reliable scraping
--skip-images          Don't download SVG images
```

## Troubleshooting

### "Rate limited" or 429 errors
The scraper includes automatic delays. If you still get rate limited, increase the delay in the script.

### Empty port information
Some ops genuinely have no ports. Others may require JavaScript rendering. Try:
- Using the Playwright-based scraper
- Checking the op page manually

### Images not downloading
The SVG API endpoint may have changed. Check if `https://cables.gl/api/op/layout/Ops.Anim.SimpleAnim` returns valid SVG.

## Contributing

When improving these scripts:
1. Always test on a small subset first
2. Add delays between requests (be nice to cables.gl servers!)
3. Save progress incrementally
4. Document any changes to the data format

## License

These scripts are for educational purposes as part of the cables.gl book project.

