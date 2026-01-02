#!/usr/bin/env python3
"""
Create renaming plan based on user's pattern:
- 13a-OpsAnim
- 13ba-OpsExtensionsECharts, 13bb-OpsExtensionFxHash (Extension group uses 'b')
- 13ca-OpsGl, 13cb-OpsGlCubeMap (Gl group uses 'c')
"""

# Current files mapping: (old_name, namespace)
current_files = [
    ("13a-OpsAnim.md", "Ops.Anim"),
    ("13b-OpsArray.md", "Ops.Array"),
    ("13c-OpsArrayPointArray.md", "Ops.Array.PointArray"),
    ("13d-OpsAudio.md", "Ops.Audio"),
    ("13e-OpsBoolean.md", "Ops.Boolean"),
    ("13f-OpsCables.md", "Ops.Cables"),
    ("13g-OpsColor.md", "Ops.Color"),
    ("13h-OpsData.md", "Ops.Data"),
    ("13i-OpsDataComposeArray.md", "Ops.Data.Compose.Array"),
    ("13j-OpsDataComposeObject.md", "Ops.Data.Compose.Object"),
    ("13k-OpsDataComposeString.md", "Ops.Data.Compose.String"),
    ("13l-OpsDataJsonPath.md", "Ops.Data.JsonPath"),
    ("13m-OpsDataStackValues.md", "Ops.Data.StackValues"),
    ("13n-OpsDate.md", "Ops.Date"),
    ("13o-OpsDebug.md", "Ops.Debug"),
    ("13p-OpsDevices.md", "Ops.Devices"),
    ("13q-OpsDevicesBrowser.md", "Ops.Devices.Browser"),
    ("13r-OpsDevicesGamePad.md", "Ops.Devices.GamePad"),
    ("13s-OpsDevicesKeyboard.md", "Ops.Devices.Keyboard"),
    ("13t-OpsDevicesMidi.md", "Ops.Devices.Midi"),
    ("13u-OpsDevicesMobile.md", "Ops.Devices.Mobile"),
    ("13v-OpsDevicesMouse.md", "Ops.Devices.Mouse"),
    ("13w-OpsDevicesWebXrVr.md", "Ops.Devices.WebXr.Vr"),
    ("13x-OpsExtensionAi.md", "Ops.Extension.Ai"),
    ("13y-OpsExtensionAmmoPhysics.md", "Ops.Extension.AmmoPhysics"),
    ("13z-OpsExtensionDetectGpu.md", "Ops.Extension.DetectGpu"),
    ("13aa-OpsExtensionECharts.md", "Ops.Extension.ECharts"),
    ("13ab-OpsExtensionFxHash.md", "Ops.Extension.FxHash"),
    ("13ac-OpsExtensionGlParticles.md", "Ops.Extension.GlParticles"),
    ("13ad-OpsExtensionHtmlElementArray.md", "Ops.Extension.HtmlElementArray"),
    ("13ae-OpsExtensionHtmlToTexture.md", "Ops.Extension.HtmlToTexture"),
    ("13af-OpsExtensionLSystem.md", "Ops.Extension.LSystem"),
    ("13ag-OpsExtensionLottie.md", "Ops.Extension.Lottie"),
    ("13ah-OpsExtensionMediapipe.md", "Ops.Extension.Mediapipe"),
    ("13ai-OpsExtensionOpenType.md", "Ops.Extension.OpenType"),
    ("13aj-OpsExtensionOsc2Ws.md", "Ops.Extension.Osc2Ws"),
    ("13ak-OpsExtensionReactionDiffusion.md", "Ops.Extension.ReactionDiffusion"),
    ("13al-OpsExtensionSocketCluster.md", "Ops.Extension.SocketCluster"),
    ("13am-OpsExtensionSocketClusterDeprecated.md", "Ops.Extension.SocketCluster.Deprecated"),
    ("13an-OpsExtensionStandalone.md", "Ops.Extension.Standalone"),
    ("13ao-OpsExtensionStandaloneFiles.md", "Ops.Extension.Standalone.Files"),
    ("13ap-OpsExtensionStandaloneNet.md", "Ops.Extension.Standalone.Net"),
    ("13aq-OpsExtensionSuperShapes.md", "Ops.Extension.SuperShapes"),
    ("13ar-OpsExtensionTeachableMachines.md", "Ops.Extension.TeachableMachines"),
    ("13as-OpsExtensionTrackingjs.md", "Ops.Extension.Trackingjs"),
    ("13at-OpsExtensionVoice.md", "Ops.Extension.Voice"),
    ("13au-OpsExtensionWebGpu.md", "Ops.Extension.WebGpu"),
    ("13av-OpsGl.md", "Ops.Gl"),
    ("13aw-OpsGlCubeMap.md", "Ops.Gl.CubeMap"),
    ("13ax-OpsGlGLTF.md", "Ops.Gl.GLTF"),
    ("13ay-OpsGlGeometry.md", "Ops.Gl.Geometry"),
    ("13az-OpsGlImageCompose.md", "Ops.Gl.ImageCompose"),
    ("13ba-OpsGlImageComposeMath.md", "Ops.Gl.ImageCompose.Math"),
    ("13bb-OpsGlImageComposeNoise.md", "Ops.Gl.ImageCompose.Noise"),
    ("13bc-OpsGlMatrix.md", "Ops.Gl.Matrix"),
    ("13bd-OpsGlMeshes.md", "Ops.Gl.Meshes"),
    ("13be-OpsGlPbr.md", "Ops.Gl.Pbr"),
    ("13bf-OpsGlPhong.md", "Ops.Gl.Phong"),
    ("13bg-OpsGlShader.md", "Ops.Gl.Shader"),
    ("13bh-OpsGlShaderEffects.md", "Ops.Gl.ShaderEffects"),
    ("13bi-OpsGlTextures.md", "Ops.Gl.Textures"),
    ("13bj-OpsGraphics.md", "Ops.Graphics"),
    ("13bk-OpsGraphicsGeometry.md", "Ops.Graphics.Geometry"),
    ("13bl-OpsGraphicsIntersection.md", "Ops.Graphics.Intersection"),
    ("13bm-OpsGraphicsMeshes.md", "Ops.Graphics.Meshes"),
    ("13bn-OpsHtml.md", "Ops.Html"),
    ("13bo-OpsHtmlAttributes.md", "Ops.Html.Attributes"),
    ("13bp-OpsHtmlCSS.md", "Ops.Html.CSS"),
    ("13bq-OpsHtmlCss.md", "Ops.Html.Css"),
    ("13br-OpsHtmlElements.md", "Ops.Html.Elements"),
    ("13bs-OpsHtmlEvent.md", "Ops.Html.Event"),
    ("13bt-OpsHtmlUtils.md", "Ops.Html.Utils"),
    ("13bu-OpsJson.md", "Ops.Json"),
    ("13bv-OpsMath.md", "Ops.Math"),
    ("13bw-OpsMathCompare.md", "Ops.Math.Compare"),
    ("13bx-OpsNet.md", "Ops.Net"),
    ("13by-OpsNetWebSocket.md", "Ops.Net.WebSocket"),
    ("13bz-OpsNumber.md", "Ops.Number"),
    ("13ca-OpsSidebar.md", "Ops.Sidebar"),
    ("13cb-OpsString.md", "Ops.String"),
    ("13cc-OpsStringBase64.md", "Ops.String.Base64"),
    ("13cd-OpsStringFile.md", "Ops.String.File"),
    ("13ce-OpsTemplates.md", "Ops.Templates"),
    ("13cf-OpsTimeLine.md", "Ops.TimeLine"),
    ("13cg-OpsTimeLineViz.md", "Ops.TimeLine.Viz"),
    ("13ch-OpsTrigger.md", "Ops.Trigger"),
    ("13ci-OpsUi.md", "Ops.Ui"),
    ("13cj-OpsUiDebug.md", "Ops.Ui.Debug"),
    ("13ck-OpsUiRouting.md", "Ops.Ui.Routing"),
    ("13cl-OpsVars.md", "Ops.Vars"),
    ("13cm-OpsWebAudio.md", "Ops.WebAudio"),
    ("13cn-OpsWebsite.md", "Ops.Website"),
]

def get_base_name(namespace):
    """Get base filename part from namespace"""
    name = namespace.replace("Ops.", "")
    return name.replace(".", "")

# Based on user's pattern, define grouping:
# - Each namespace family gets a letter
# - First namespace in family uses letter + 'a', subsequent use letter + 'b', 'c', etc.
# - Single-item families can use just the letter (like 13a for Anim)

# Define namespace families (sorted alphabetically by first namespace in family)
namespace_families = [
    ('a', ['Ops.Anim']),  # Single item, use 'a'
    ('b', ['Ops.Array', 'Ops.Array.PointArray']),  # Array family
    ('c', ['Ops.Audio']),  # Single
    ('d', ['Ops.Boolean']),  # Single
    ('e', ['Ops.Cables']),  # Single
    ('f', ['Ops.Color']),  # Single
    ('g', ['Ops.Data', 'Ops.Data.Compose.Array', 'Ops.Data.Compose.Object', 
           'Ops.Data.Compose.String', 'Ops.Data.JsonPath', 'Ops.Data.StackValues']),  # Data family
    ('h', ['Ops.Date']),  # Single
    ('i', ['Ops.Debug']),  # Single
    ('j', ['Ops.Devices', 'Ops.Devices.Browser', 'Ops.Devices.GamePad',
           'Ops.Devices.Keyboard', 'Ops.Devices.Midi', 'Ops.Devices.Mobile',
           'Ops.Devices.Mouse', 'Ops.Devices.WebXr.Vr']),  # Devices family
    ('k', ['Ops.Extension.Ai', 'Ops.Extension.AmmoPhysics', 'Ops.Extension.DetectGpu',
           'Ops.Extension.ECharts', 'Ops.Extension.FxHash', 'Ops.Extension.GlParticles',
           'Ops.Extension.HtmlElementArray', 'Ops.Extension.HtmlToTexture', 'Ops.Extension.LSystem',
           'Ops.Extension.Lottie', 'Ops.Extension.Mediapipe', 'Ops.Extension.OpenType',
           'Ops.Extension.Osc2Ws', 'Ops.Extension.ReactionDiffusion', 'Ops.Extension.SocketCluster',
           'Ops.Extension.SocketCluster.Deprecated', 'Ops.Extension.Standalone',
           'Ops.Extension.Standalone.Files', 'Ops.Extension.Standalone.Net',
           'Ops.Extension.SuperShapes', 'Ops.Extension.TeachableMachines',
           'Ops.Extension.Trackingjs', 'Ops.Extension.Voice', 'Ops.Extension.WebGpu']),  # Extension family - but user said 'ba' for ECharts, so maybe 'b'?
    ('l', ['Ops.Gl', 'Ops.Gl.CubeMap', 'Ops.Gl.GLTF', 'Ops.Gl.Geometry',
           'Ops.Gl.ImageCompose', 'Ops.Gl.ImageCompose.Math', 'Ops.Gl.ImageCompose.Noise',
           'Ops.Gl.Matrix', 'Ops.Gl.Meshes', 'Ops.Gl.Pbr', 'Ops.Gl.Phong',
           'Ops.Gl.Shader', 'Ops.Gl.ShaderEffects', 'Ops.Gl.Textures']),  # Gl family - but user said 'ca', so maybe 'c'?
    ('m', ['Ops.Graphics', 'Ops.Graphics.Geometry', 'Ops.Graphics.Intersection',
           'Ops.Graphics.Meshes']),  # Graphics family
    ('n', ['Ops.Html', 'Ops.Html.Attributes', 'Ops.Html.CSS', 'Ops.Html.Css',
           'Ops.Html.Elements', 'Ops.Html.Event', 'Ops.Html.Utils']),  # Html family
    ('o', ['Ops.Json']),  # Single
    ('p', ['Ops.Math', 'Ops.Math.Compare']),  # Math family
    ('q', ['Ops.Net', 'Ops.Net.WebSocket']),  # Net family
    ('r', ['Ops.Number']),  # Single
    ('s', ['Ops.Sidebar']),  # Single
    ('t', ['Ops.String', 'Ops.String.Base64', 'Ops.String.File']),  # String family
    ('u', ['Ops.Templates']),  # Single
    ('v', ['Ops.TimeLine', 'Ops.TimeLine.Viz']),  # TimeLine family
    ('w', ['Ops.Trigger']),  # Single
    ('x', ['Ops.Ui', 'Ops.Ui.Debug', 'Ops.Ui.Routing']),  # Ui family
    ('y', ['Ops.Vars']),  # Single
    ('z', ['Ops.WebAudio']),  # Single
]

# Wait, the user's example suggests Extension uses 'b' and Gl uses 'c'
# Let me re-read: "13ba-OpsExtensionsECharts, 13bb-OpsExtensionFxHash (...) 13ca-OpsGl,13cb-OpsGlCubeMap"
# So Extension -> 'b', Gl -> 'c'
# But Array also needs 'b'... Unless Array uses 'b' and Extension uses something else?
# Actually, I think the user wants us to figure out a logical grouping.

# Let me try a different approach: Based on their example, I think they want:
# - Extension.* to use letter 'b' (starting with 13ba for first Extension)
# - Gl.* to use letter 'c' (starting with 13ca for Gl)
# But we also have Array which starts with 'b'...

# Actually, maybe Array gets 'b' (13b, 13ba) and Extension gets a different approach?
# Or maybe the user's grouping is different than alphabetical?

# For now, let me create a plan based on logical grouping and show it to the user for approval.
# I'll use their examples as guidance: Extension uses 'b', Gl uses 'c'

def create_rename_plan():
    """Create rename plan - need to figure out exact grouping from user examples"""
    
    # Based on user examples:
    # Extension.ECharts -> 13ba (so Extension group uses 'b', first is 'ba')
    # Extension.FxHash -> 13bb
    # Gl -> 13ca (so Gl group uses 'c', first is 'ca')
    # Gl.CubeMap -> 13cb
    
    # This suggests that:
    # - Groups with multiple items always use two letters (letter + 'a', 'b', etc.)
    # - The first letter indicates the group
    # - But we need to assign groups logically
    
    # Let me assign groups based on namespace hierarchy and user hints:
    groups = {}
    
    # Group assignments (trying to match user's pattern):
    groups['Ops.Anim'] = ('a', 0)  # Single item, use 'a'
    groups['Ops.Array'] = ('b', 0)  # Array family - but user said Extension uses 'b', so conflict?
    groups['Ops.Array.PointArray'] = ('b', 1)
    
    # Hmm, I think I need to ask the user or make an educated guess.
    # Let me create a logical grouping and show it for approval:
    
    rename_map = []
    
    # Create mapping based on logical grouping
    # I'll assign letters sequentially but group related namespaces
    current_letter = 'a'
    
    families = [
        # (family_letter, namespaces_list)
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
        # Extension - user said starts with 'ba', so maybe they want 'b' for Extension?
        # But we already used 'b' for Array... Maybe Extension should be after Array?
        # Actually wait - if Extension.ECharts is 'ba', that means first letter is 'b'
        # So maybe the grouping is: b=Extension, and Array gets moved or uses a different scheme?
        # For now, let me put Extension after Devices and see what letter that would be
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
        # Need one more for Website
    ]
    
    # We've used a-z, need 'aa' for Website
    families.append(('aa', ['Ops.Website']))
    
    current_map = {ns: old for old, ns in current_files}
    
    print("=" * 80)
    print("PROPOSED RENAMING PLAN")
    print("=" * 80)
    print()
    print("NOTE: Based on your examples, Extension uses 'b' and Gl uses 'c'")
    print("This creates a conflict with Array which also starts with 'b'")
    print("Please review and let me know the correct grouping!")
    print()
    
    all_renames = []
    
    for family_letter, namespaces in families:
        for idx, namespace in enumerate(namespaces):
            base_name = get_base_name(namespace)
            old_name = current_map[namespace]
            
            if len(namespaces) == 1:
                # Single item - use single letter
                suffix = family_letter
                new_name = f"13{suffix}-Ops{base_name}.md"
            else:
                # Multiple items - use two letters
                second_letter = chr(ord('a') + idx)
                suffix = family_letter + second_letter
                new_name = f"13{suffix}-Ops{base_name}.md"
            
            all_renames.append((old_name, new_name, namespace, suffix))
    
    # Group by first letter for display
    grouped = {}
    for old_name, new_name, namespace, suffix in all_renames:
        first_letter = suffix[0] if len(suffix) > 0 else suffix
        if first_letter not in grouped:
            grouped[first_letter] = []
        grouped[first_letter].append((old_name, new_name, namespace))
    
    for letter in sorted(grouped.keys(), key=lambda x: (len(x), x)):
        print(f"\nGroup {letter.upper()}:")
        print("-" * 80)
        for old_name, new_name, namespace in sorted(grouped[letter], key=lambda x: x[1]):
            print(f"  {old_name:45} -> {new_name:45}  ({namespace})")
    
    print()
    print("=" * 80)
    print(f"Total: {len(all_renames)} files")
    print("=" * 80)

if __name__ == "__main__":
    create_rename_plan()


