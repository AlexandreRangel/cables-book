# How to Manually Fix Inline Bold Labels in Markdown

## Pattern to Look For

When you see text like this in a markdown file:
```markdown
**Label1:** Description1 **Label2:** Description2 **Label3:** Description3
```

You need to split it into separate list items with line breaks.

## Manual Fix Steps

### Step 1: Identify the Pattern
Look for lines that have:
- Multiple `**Bold Text:**` patterns on the same line
- Text between them that should be descriptions

### Step 2: Split Each Label and Description

For each `**Label:** Description` pair:

1. **Put the label on its own line:**
   ```markdown
   **Label:**
   ```

2. **Add a blank line after the label**

3. **Convert the description to a list item:**
   ```markdown
   - Description
   ```

4. **Add a blank line before the next label** (if there is one)

### Example Transformation

**Before:**
```markdown
**Key Light:** Main illumination (brightest) **Fill Light:** Reduces harsh shadows (ambient or weak directional) **Rim Light:** Creates edge highlights (back/side lighting)
```

**After:**
```markdown
**Key Light:**

- Main illumination (brightest)

**Fill Light:**

- Reduces harsh shadows (ambient or weak directional)

**Rim Light:**

- Creates edge highlights (back/side lighting)
```

## Quick Find Pattern

In your editor, search for:
- Pattern: `\*\*[^*]+\*\*:\s+[^*]+\s+\*\*[^*]+\*\*:`
- This finds bold labels followed by text, then another bold label on the same line

## Using the Script

Run the script to automatically find and fix these:
```bash
python scripts/fix_bold_label_lists.py
```

This will show you what it finds and can optionally fix them automatically.
