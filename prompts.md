# Cables.gl Book Prompts

This file tracks all prompts used in creating this book.

## Initial Book Creation Prompt

**Date:** December 28, 2025

**Prompt:**
> Can you go to youtube and fetch ALL youtube videos about cables, and paste them with the required format, categorized by theme? Can you also read the transcript of those files, so to learn from them and write the text of our book?
> You then can create md files for the important section, like Introduction, 3D, Texturing, JavaScript and so on.

**Result:** Created comprehensive book structure with 10 chapters covering all major cables.gl topics. Web search was unable to retrieve specific YouTube video links due to search limitations - chapters include placeholder sections for videos to be added manually.

---

## Video Format Reference

When adding videos to chapters, use this format:

```vid
https://youtu.be/VIDEO_ID
Title: Video Title Here
Author: Channel Name
Thumbnail: https://i.ytimg.com/vi/VIDEO_ID/mqdefault.jpg
```

---

## Expansion + Video Tutorials Index Prompt

**Date:** December 28, 2025

**Prompt:**
> now expand (specially with advanced examples) the sections 5,6,7,8,9 and 10. take your time. make it really expanded ones. please add a new section called Video Tutorials and putt ALL the video tutorials and videos about cables.gl you find on the internet (Vimeo and YouTube). Look really hard and organize them by themes, on this new page.
> on the intro section, write some about the cables.gl history.

---

## Animation System Expansion Prompt

**Date:** December 28, 2025

**Prompt:**
> expand section 9 so to include non-linear (addable, mixable) animation clips with the new animation system in cables (Nov 2025) and also its integration with javascript custom op code. be detailled. look for the new docs

**Result:** Expanded Chapter 9 (Animation & Timeline) with comprehensive coverage of:
- Non-linear animation clips (reusable, addable, mixable)
- Creating and managing animation clips
- Additive and blendable animation techniques
- Complete JavaScript custom op integration examples
- Programmatic timeline control
- Clip manipulation and blending algorithms
- Advanced examples combining clips with procedural animation
- Updated exercises section with clip-related tasks

---

## Interfaces Chapter Creation Prompt

**Date:** December 28, 2025

**Prompt:**
> 1) create a new chapter named Interfaces. Cover the possible ways to make interfaces inside a cables patch, via html and css and via native cables sidebar interface ops. give special attention on the technique of styling the native sidebar with css code. explain this technique well and with examples.
> 2) i like your diagrams made of ascii code use them to explain thing in this new session as well as the other book sessions. take your time.

**Result:** Created Chapter 12 (Interfaces) with comprehensive coverage of:
- HTML/CSS interface creation using HTML op
- Native sidebar interface operators (Slider, Button, Toggle, ColorPicker, etc.)
- Detailed CSS styling techniques for native sidebar ops
- Complete CSS examples for professional styling
- Advanced techniques (animations, glassmorphism, responsive design)
- Integration patterns between HTML and native interfaces
- Practical examples and best practices
- Extensive use of ASCII diagrams throughout for visual explanation
- Updated navigation links in related chapters

---

## Arrow/Emoji Replacement Issue and Fix

**Date:** December 28, 2025

**Problem:** When replacing arrow characters (→, ↓, etc.) and emojis across all chapters, a Python script accidentally duplicated Chapter 1's content into all other chapters, causing all files to have ~12,885 lines instead of their correct lengths.

**Root Cause Analysis:**
The issue likely occurred due to one of these factors:
1. **PowerShell command failure**: Initial attempt used a complex PowerShell one-liner that may have failed silently or corrupted files
2. **File handle issues**: If file handles weren't properly closed, content could have been written to wrong files
3. **Encoding problems**: UTF-8 encoding issues could have caused file corruption
4. **Script logic error**: The replacement script may have accidentally read/written wrong files

**Prevention Techniques (CRITICAL - Always Follow):**

### 1. **Always Create Backups Before Bulk Operations**
```python
import shutil
import os

# BEFORE making changes, backup all files
for filename in files:
    shutil.copy2(filepath, filepath + '.backup')
```

### 2. **Process Files One at a Time with Explicit Error Handling**
```python
for filename in files:
    try:
        # Read
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Modify
        content = content.replace('old', 'new')
        
        # Write to TEMP file first
        temp_path = filepath + '.tmp'
        with open(temp_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        # Verify temp file is valid before replacing
        # (check file size, encoding, etc.)
        
        # Only then replace original
        os.replace(temp_path, filepath)
        
    except Exception as e:
        print(f"ERROR with {filename}: {e}")
        # Restore from backup if needed
        continue
```

### 3. **Verify File Integrity After Operations**
```python
# After processing, verify each file:
for filename in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        # Check expected characteristics
        assert len(lines) < expected_max_lines, f"{filename} too long!"
        assert expected_header in lines[0], f"{filename} wrong header!"
```

### 4. **Use Git or Version Control**
- Always commit before bulk operations
- Can easily revert if something goes wrong
- `git diff` shows exactly what changed

### 5. **Test on Single File First**
- Always test script on ONE file first
- Verify output is correct
- Then run on all files

### 6. **Never Use Complex One-Liners for Critical Operations**
- Avoid PowerShell/command-line one-liners for file modifications
- Use proper Python scripts with error handling
- Make operations explicit and debuggable

### 7. **Check File Sizes Before/After**
```python
# Before
file_sizes_before = {f: os.path.getsize(f) for f in files}

# After processing
file_sizes_after = {f: os.path.getsize(f) for f in files}

# Verify no unexpected size changes
for f in files:
    if abs(file_sizes_before[f] - file_sizes_after[f]) > threshold:
        print(f"WARNING: {f} size changed significantly!")
```

### 8. **Validate Content Structure**
```python
# After processing, verify file structure
for filename in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check for expected markers
    assert filename.startswith('01-') or '# The Cables.gl Book' not in content[:500]
    assert expected_chapter_header in content
    assert content.count('# ') == 1  # Only one main header
```

### 9. **Use Atomic Operations**
- Write to temp file
- Verify temp file
- Then replace original (atomic on most systems)

### 10. **Log Everything**
```python
import logging
logging.basicConfig(filename='bulk_operation.log', level=logging.INFO)

for filename in files:
    logging.info(f"Processing {filename}")
    # ... operations ...
    logging.info(f"Completed {filename}: {len(content)} chars")
```

**Key Takeaway:** When modifying multiple files, ALWAYS:
1. Backup first
2. Test on one file
3. Verify after each operation
4. Use proper error handling
5. Have a rollback plan

