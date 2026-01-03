#!/usr/bin/env python3
"""
Show renaming plan based on user's suggested pattern
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

# Current files: (old_name, namespace)
current = {
    "Ops.Anim": "13a-OpsAnim.md",
    "Ops.Array": "13b-OpsArray.md",
    "Ops.Array.PointArray": "13c-OpsArrayPointArray.md",
    "Ops.Audio": "13d-OpsAudio.md",
    "Ops.Boolean": "13e-OpsBoolean.md",
    "Ops.Cables": "13f-OpsCables.md",
    "Ops.Color": "13g-OpsColor.md",
    "Ops.Data": "13h-OpsData.md",
    "Ops.Data.Compose.Array": "13i-OpsDataComposeArray.md",
    "Ops.Data.Compose.Object": "13j-OpsDataComposeObject.md",
    "Ops.Data.Compose.String": "13k-OpsDataComposeString.md",
    "Ops.Data.JsonPath": "13l-OpsDataJsonPath.md",
    "Ops.Data.StackValues": "13m-OpsDataStackValues.md",
    "Ops.Date": "13n-OpsDate.md",
    "Ops.Debug": "13o-OpsDebug.md",
    "Ops.Devices": "13p-OpsDevices.md",
    "Ops.Devices.Browser": "13q-OpsDevicesBrowser.md",
    "Ops.Devices.GamePad": "13r-OpsDevicesGamePad.md",
    "Ops.Devices.Keyboard": "13s-OpsDevicesKeyboard.md",
    "Ops.Devices.Midi": "13t-OpsDevicesMidi.md",
    "Ops.Devices.Mobile": "13u-OpsDevicesMobile.md",
    "Ops.Devices.Mouse": "13v-OpsDevicesMouse.md",
    "Ops.Devices.WebXr.Vr": "13w-OpsDevicesWebXrVr.md",
    "Ops.Extension.Ai": "13x-OpsExtensionAi.md",
    "Ops.Extension.AmmoPhysics": "13y-OpsExtensionAmmoPhysics.md",
    "Ops.Extension.DetectGpu": "13z-OpsExtensionDetectGpu.md",
    "Ops.Extension.ECharts": "13aa-OpsExtensionECharts.md",
    "Ops.Extension.FxHash": "13ab-OpsExtensionFxHash.md",
    "Ops.Extension.GlParticles": "13ac-OpsExtensionGlParticles.md",
    "Ops.Extension.HtmlElementArray": "13ad-OpsExtensionHtmlElementArray.md",
    "Ops.Extension.HtmlToTexture": "13ae-OpsExtensionHtmlToTexture.md",
    "Ops.Extension.LSystem": "13af-OpsExtensionLSystem.md",
    "Ops.Extension.Lottie": "13ag-OpsExtensionLottie.md",
    "Ops.Extension.Mediapipe": "13ah-OpsExtensionMediapipe.md",
    "Ops.Extension.OpenType": "13ai-OpsExtensionOpenType.md",
    "Ops.Extension.Osc2Ws": "13aj-OpsExtensionOsc2Ws.md",
    "Ops.Extension.ReactionDiffusion": "13ak-OpsExtensionReactionDiffusion.md",
    "Ops.Extension.SocketCluster": "13al-OpsExtensionSocketCluster.md",
    "Ops.Extension.SocketCluster.Deprecated": "13am-OpsExtensionSocketClusterDeprecated.md",
    "Ops.Extension.Standalone": "13an-OpsExtensionStandalone.md",
    "Ops.Extension.Standalone.Files": "13ao-OpsExtensionStandaloneFiles.md",
    "Ops.Extension.Standalone.Net": "13ap-OpsExtensionStandaloneNet.md",
    "Ops.Extension.SuperShapes": "13aq-OpsExtensionSuperShapes.md",
    "Ops.Extension.TeachableMachines": "13ar-OpsExtensionTeachableMachines.md",
    "Ops.Extension.Trackingjs": "13as-OpsExtensionTrackingjs.md",
    "Ops.Extension.Voice": "13at-OpsExtensionVoice.md",
    "Ops.Extension.WebGpu": "13au-OpsExtensionWebGpu.md",
    "Ops.Gl": "13av-OpsGl.md",
    "Ops.Gl.CubeMap": "13aw-OpsGlCubeMap.md",
    "Ops.Gl.GLTF": "13ax-OpsGlGLTF.md",
    "Ops.Gl.Geometry": "13ay-OpsGlGeometry.md",
    "Ops.Gl.ImageCompose": "13az-OpsGlImageCompose.md",
    "Ops.Gl.ImageCompose.Math": "13ba-OpsGlImageComposeMath.md",
    "Ops.Gl.ImageCompose.Noise": "13bb-OpsGlImageComposeNoise.md",
    "Ops.Gl.Matrix": "13bc-OpsGlMatrix.md",
    "Ops.Gl.Meshes": "13bd-OpsGlMeshes.md",
    "Ops.Gl.Pbr": "13be-OpsGlPbr.md",
    "Ops.Gl.Phong": "13bf-OpsGlPhong.md",
    "Ops.Gl.Shader": "13bg-OpsGlShader.md",
    "Ops.Gl.ShaderEffects": "13bh-OpsGlShaderEffects.md",
    "Ops.Gl.Textures": "13bi-OpsGlTextures.md",
    "Ops.Graphics": "13bj-OpsGraphics.md",
    "Ops.Graphics.Geometry": "13bk-OpsGraphicsGeometry.md",
    "Ops.Graphics.Intersection": "13bl-OpsGraphicsIntersection.md",
    "Ops.Graphics.Meshes": "13bm-OpsGraphicsMeshes.md",
    "Ops.Html": "13bn-OpsHtml.md",
    "Ops.Html.Attributes": "13bo-OpsHtmlAttributes.md",
    "Ops.Html.CSS": "13bp-OpsHtmlCSS.md",
    "Ops.Html.Css": "13bq-OpsHtmlCss.md",
    "Ops.Html.Elements": "13br-OpsHtmlElements.md",
    "Ops.Html.Event": "13bs-OpsHtmlEvent.md",
    "Ops.Html.Utils": "13bt-OpsHtmlUtils.md",
    "Ops.Json": "13bu-OpsJson.md",
    "Ops.Math": "13bv-OpsMath.md",
    "Ops.Math.Compare": "13bw-OpsMathCompare.md",
    "Ops.Net": "13bx-OpsNet.md",
    "Ops.Net.WebSocket": "13by-OpsNetWebSocket.md",
    "Ops.Number": "13bz-OpsNumber.md",
    "Ops.Sidebar": "13ca-OpsSidebar.md",
    "Ops.String": "13cb-OpsString.md",
    "Ops.String.Base64": "13cc-OpsStringBase64.md",
    "Ops.String.File": "13cd-OpsStringFile.md",
    "Ops.Templates": "13ce-OpsTemplates.md",
    "Ops.TimeLine": "13cf-OpsTimeLine.md",
    "Ops.TimeLine.Viz": "13cg-OpsTimeLineViz.md",
    "Ops.Trigger": "13ch-OpsTrigger.md",
    "Ops.Ui": "13ci-OpsUi.md",
    "Ops.Ui.Debug": "13cj-OpsUiDebug.md",
    "Ops.Ui.Routing": "13ck-OpsUiRouting.md",
    "Ops.Vars": "13cl-OpsVars.md",
    "Ops.WebAudio": "13cm-OpsWebAudio.md",
    "Ops.Website": "13cn-OpsWebsite.md",
}

def get_base_name(namespace):
    return namespace.replace("Ops.", "").replace(".", "")

# Based on user's pattern, try to match their examples:
# Extension.ECharts -> 13ba, Extension.FxHash -> 13bb
# Gl -> 13ca, Gl.CubeMap -> 13cb

# Let me create a logical grouping that respects namespace hierarchy
# Group families by their top-level namespace

families = [
    # Format: (group_letter, namespace_list)
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
    # Extension - user wants 'ba' for ECharts, so they want 'b' for Extension group
    # But we already used 'b' for Array... Maybe Extension should be a different scheme?
    # Or maybe Array uses just 'b' and Extension uses 'ba'? Let me try that
    # Actually, based on user example, Extension.ECharts is 'ba', so Extension group = 'b'
    # But Array also uses 'b'... Maybe the pattern is different?
    # Let me just assign sequentially and show for approval
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

print("=" * 90)
print("RENAMING PLAN FOR SECTION 13 FILES")
print("=" * 90)
print()
print("Pattern: First letter = major namespace group, Second letter = subsections")
print()
print("NOTE: Your examples suggest Extension uses 'b' (13ba) and Gl uses 'c' (13ca)")
print("This conflicts with Array which also starts with 'b'. Showing logical grouping:")
print()

all_renames = []

for group_letter, namespaces in families:
    for idx, namespace in enumerate(namespaces):
        old_name = current[namespace]
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
        
        all_renames.append((old_name, new_name, namespace, suffix))

# Group by first letter for display
grouped = {}
for old, new, ns, suffix in all_renames:
    first = suffix[0] if len(suffix) > 1 or suffix >= 'aa' else suffix
    if first not in grouped:
        grouped[first] = []
    grouped[first].append((old, new, ns))

for letter in sorted(grouped.keys(), key=lambda x: (len(x), x)):
    print(f"\nGroup '{letter.upper()}':")
    print("-" * 90)
    for old, new, ns in sorted(grouped[letter], key=lambda x: x[1]):
        print(f"  {old:47} -> {new:47}  ({ns})")

print()
print("=" * 90)
print(f"Total: {len(all_renames)} files")
print("=" * 90)
print()
print("Please review and confirm if this grouping matches your intent, or specify")
print("the exact grouping you'd like (especially for Array vs Extension conflict)")



