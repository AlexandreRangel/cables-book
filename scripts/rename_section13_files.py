#!/usr/bin/env python3
"""
Rename section 13 files based on logical hierarchical grouping
"""

import os
import shutil
import sys
sys.stdout.reconfigure(encoding='utf-8')

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHAPTERS_DIR = os.path.join(PROJECT_ROOT, "chapters")

def get_base_name(namespace):
    return namespace.replace("Ops.", "").replace(".", "")

# Define the grouping plan (logical hierarchical grouping)
families = [
    ('a', ['Ops.Anim']),
    ('b', ['Ops.Array', 'Ops.Array.PointArray']),
    ('c', ['Ops.Audio']),
    ('d', ['Ops.Boolean']),
    ('e', ['Ops.Cables']),
    ('f', ['Ops.Color']),
    ('g', ['Ops.Data', 'Ops.Data.Compose.Array', 'Ops.Data.Compose.Object',
           'Ops.Data.Compose.String', 'Ops.Data.JsonPath', 'Ops.Data.StackValues']),
    ('h', ['Ops.Date']),
    ('i', ['Ops.Debug']),
    ('j', ['Ops.Devices', 'Ops.Devices.Browser', 'Ops.Devices.GamePad',
           'Ops.Devices.Keyboard', 'Ops.Devices.Midi', 'Ops.Devices.Mobile',
           'Ops.Devices.Mouse', 'Ops.Devices.WebXr.Vr']),
    ('k', ['Ops.Extension.Ai', 'Ops.Extension.AmmoPhysics', 'Ops.Extension.DetectGpu',
           'Ops.Extension.ECharts', 'Ops.Extension.FxHash', 'Ops.Extension.GlParticles',
           'Ops.Extension.HtmlElementArray', 'Ops.Extension.HtmlToTexture', 'Ops.Extension.LSystem',
           'Ops.Extension.Lottie', 'Ops.Extension.Mediapipe', 'Ops.Extension.OpenType',
           'Ops.Extension.Osc2Ws', 'Ops.Extension.ReactionDiffusion', 'Ops.Extension.SocketCluster',
           'Ops.Extension.SocketCluster.Deprecated', 'Ops.Extension.Standalone',
           'Ops.Extension.Standalone.Files', 'Ops.Extension.Standalone.Net',
           'Ops.Extension.SuperShapes', 'Ops.Extension.TeachableMachines',
           'Ops.Extension.Trackingjs', 'Ops.Extension.Voice', 'Ops.Extension.WebGpu']),
    ('l', ['Ops.Gl', 'Ops.Gl.CubeMap', 'Ops.Gl.GLTF', 'Ops.Gl.Geometry',
           'Ops.Gl.ImageCompose', 'Ops.Gl.ImageCompose.Math', 'Ops.Gl.ImageCompose.Noise',
           'Ops.Gl.Matrix', 'Ops.Gl.Meshes', 'Ops.Gl.Pbr', 'Ops.Gl.Phong',
           'Ops.Gl.Shader', 'Ops.Gl.ShaderEffects', 'Ops.Gl.Textures']),
    ('m', ['Ops.Graphics', 'Ops.Graphics.Geometry', 'Ops.Graphics.Intersection',
           'Ops.Graphics.Meshes']),
    ('n', ['Ops.Html', 'Ops.Html.Attributes', 'Ops.Html.CSS', 'Ops.Html.Css',
           'Ops.Html.Elements', 'Ops.Html.Event', 'Ops.Html.Utils']),
    ('o', ['Ops.Json']),
    ('p', ['Ops.Math', 'Ops.Math.Compare']),
    ('q', ['Ops.Net', 'Ops.Net.WebSocket']),
    ('r', ['Ops.Number']),
    ('s', ['Ops.Sidebar']),
    ('t', ['Ops.String', 'Ops.String.Base64', 'Ops.String.File']),
    ('u', ['Ops.Templates']),
    ('v', ['Ops.TimeLine', 'Ops.TimeLine.Viz']),
    ('w', ['Ops.Trigger']),
    ('x', ['Ops.Ui', 'Ops.Ui.Debug', 'Ops.Ui.Routing']),
    ('y', ['Ops.Vars']),
    ('z', ['Ops.WebAudio']),
    ('aa', ['Ops.Website']),
]

# Current file mapping (from the index file - we'll read it)
def read_current_mapping():
    """Read current mapping from 13-AllOps.md"""
    index_file = os.path.join(CHAPTERS_DIR, "13-AllOps.md")
    mapping = {}
    
    if os.path.exists(index_file):
        with open(index_file, 'r', encoding='utf-8') as f:
            content = f.read()
            # Parse lines like: - [Ops.Anim](13a-OpsAnim.md)
            import re
            pattern = r'- \[([^\]]+)\]\(([^\)]+)\)'
            for match in re.finditer(pattern, content):
                namespace = match.group(1)
                filename = match.group(2)
                mapping[namespace] = filename
    
    return mapping

def generate_new_filenames():
    """Generate new filename mapping"""
    rename_map = {}
    
    for group_letter, namespaces in families:
        for idx, namespace in enumerate(namespaces):
            base_name = get_base_name(namespace)
            
            if len(namespaces) == 1:
                # Single item uses single letter
                suffix = group_letter
                new_name = f"13{suffix}-Ops{base_name}.md"
            else:
                # Multi-item uses two letters: group_letter + 'a', 'b', 'c'...
                second_letter = chr(ord('a') + idx)
                suffix = group_letter + second_letter
                new_name = f"13{suffix}-Ops{base_name}.md"
            
            rename_map[namespace] = new_name
    
    return rename_map

def rename_files(old_to_new):
    """Rename files and return mapping of old -> new"""
    renamed = []
    errors = []
    
    for old_name, new_name in old_to_new.items():
        old_path = os.path.join(CHAPTERS_DIR, old_name)
        new_path = os.path.join(CHAPTERS_DIR, new_name)
        
        if not os.path.exists(old_path):
            errors.append(f"Source file not found: {old_name}")
            continue
        
        if os.path.exists(new_path) and old_path != new_path:
            errors.append(f"Target file already exists: {new_name}")
            continue
        
        try:
            if old_path != new_path:
                os.rename(old_path, new_path)
                renamed.append((old_name, new_name))
                print(f"  Renamed: {old_name} -> {new_name}")
            else:
                print(f"  No change: {old_name}")
        except Exception as e:
            errors.append(f"Error renaming {old_name}: {e}")
    
    return renamed, errors

def update_index_file(rename_map):
    """Update 13-AllOps.md with new filenames"""
    index_file = os.path.join(CHAPTERS_DIR, "13-AllOps.md")
    
    if not os.path.exists(index_file):
        print(f"WARNING: Index file not found: {index_file}")
        return
    
    with open(index_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace old filenames with new ones
    import re
    for namespace, new_filename in rename_map.items():
        # Find line like: - [Ops.Anim](13a-OpsAnim.md)
        pattern = rf'- \[{re.escape(namespace)}\]\([^\)]+\)'
        replacement = f'- [{namespace}]({new_filename})'
        content = re.sub(pattern, replacement, content)
    
    # Write updated content
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  Updated index file: {index_file}")

def main():
    print("=" * 80)
    print("RENAMING SECTION 13 FILES")
    print("=" * 80)
    print()
    
    # Read current mapping
    print("Reading current file mapping...")
    current_mapping = read_current_mapping()
    
    # Generate new filenames
    print("Generating new filename mapping...")
    new_filenames = generate_new_filenames()
    
    # Create old -> new mapping
    old_to_new = {}
    for namespace, new_name in new_filenames.items():
        if namespace in current_mapping:
            old_name = current_mapping[namespace]
            if old_name != new_name:
                old_to_new[old_name] = new_name
    
    if not old_to_new:
        print("No files need renaming!")
        return
    
    print(f"\nFound {len(old_to_new)} files to rename")
    print()
    
    # Show what will be renamed (first 10 and last 10)
    print("Files to rename (showing first and last 10):")
    sorted_renames = sorted(old_to_new.items())
    for old, new in sorted_renames[:10]:
        print(f"  {old} -> {new}")
    if len(sorted_renames) > 20:
        print(f"  ... ({len(sorted_renames) - 20} more) ...")
    for old, new in sorted_renames[-10:]:
        print(f"  {old} -> {new}")
    
    print()
    print("Proceeding with renaming...")
    print()
    print("Renaming files...")
    renamed, errors = rename_files(old_to_new)
    
    if errors:
        print()
        print("ERRORS:")
        for error in errors:
            print(f"  {error}")
    
    print()
    print(f"Successfully renamed {len(renamed)} files")
    
    # Update index file
    print()
    print("Updating index file...")
    update_index_file(new_filenames)
    
    print()
    print("=" * 80)
    print("DONE!")
    print("=" * 80)

if __name__ == "__main__":
    main()

