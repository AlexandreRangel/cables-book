#!/usr/bin/env python3
"""
Analyze and create renaming plan for section 13 files based on grouping
"""

# Current files in order (from the index)
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

def create_grouping_plan():
    """Create intelligent grouping based on namespace hierarchy"""
    
    # Define major groups (first letter)
    groups = []
    
    # Group A: Anim (standalone)
    groups.append({
        'letter': 'a',
        'namespaces': ['Ops.Anim']
    })
    
    # Group B: Array + Array.*
    groups.append({
        'letter': 'b',
        'namespaces': ['Ops.Array', 'Ops.Array.PointArray']
    })
    
    # Group C: Audio
    groups.append({
        'letter': 'c',
        'namespaces': ['Ops.Audio']
    })
    
    # Group C: Boolean
    groups.append({
        'letter': 'c',
        'namespaces': ['Ops.Boolean']
    })
    
    # Group C: Cables
    groups.append({
        'letter': 'c',
        'namespaces': ['Ops.Cables']
    })
    
    # Group C: Color
    groups.append({
        'letter': 'c',
        'namespaces': ['Ops.Color']
    })
    
    # Group D: Data + Data.*
    groups.append({
        'letter': 'd',
        'namespaces': ['Ops.Data', 'Ops.Data.Compose.Array', 'Ops.Data.Compose.Object', 
                      'Ops.Data.Compose.String', 'Ops.Data.JsonPath', 'Ops.Data.StackValues']
    })
    
    # Group E: Date, Debug
    groups.append({
        'letter': 'e',
        'namespaces': ['Ops.Date', 'Ops.Debug']
    })
    
    # Group F: Devices + Devices.*
    groups.append({
        'letter': 'f',
        'namespaces': ['Ops.Devices', 'Ops.Devices.Browser', 'Ops.Devices.GamePad',
                      'Ops.Devices.Keyboard', 'Ops.Devices.Midi', 'Ops.Devices.Mobile',
                      'Ops.Devices.Mouse', 'Ops.Devices.WebXr.Vr']
    })
    
    # Group G: Extension + Extension.* (all Extension namespaces)
    groups.append({
        'letter': 'g',
        'namespaces': ['Ops.Extension.Ai', 'Ops.Extension.AmmoPhysics', 'Ops.Extension.DetectGpu',
                      'Ops.Extension.ECharts', 'Ops.Extension.FxHash', 'Ops.Extension.GlParticles',
                      'Ops.Extension.HtmlElementArray', 'Ops.Extension.HtmlToTexture', 'Ops.Extension.LSystem',
                      'Ops.Extension.Lottie', 'Ops.Extension.Mediapipe', 'Ops.Extension.OpenType',
                      'Ops.Extension.Osc2Ws', 'Ops.Extension.ReactionDiffusion', 'Ops.Extension.SocketCluster',
                      'Ops.Extension.SocketCluster.Deprecated', 'Ops.Extension.Standalone',
                      'Ops.Extension.Standalone.Files', 'Ops.Extension.Standalone.Net',
                      'Ops.Extension.SuperShapes', 'Ops.Extension.TeachableMachines',
                      'Ops.Extension.Trackingjs', 'Ops.Extension.Voice', 'Ops.Extension.WebGpu']
    })
    
    # Group H: Gl + Gl.*
    groups.append({
        'letter': 'h',
        'namespaces': ['Ops.Gl', 'Ops.Gl.CubeMap', 'Ops.Gl.GLTF', 'Ops.Gl.Geometry',
                      'Ops.Gl.ImageCompose', 'Ops.Gl.ImageCompose.Math', 'Ops.Gl.ImageCompose.Noise',
                      'Ops.Gl.Matrix', 'Ops.Gl.Meshes', 'Ops.Gl.Pbr', 'Ops.Gl.Phong',
                      'Ops.Gl.Shader', 'Ops.Gl.ShaderEffects', 'Ops.Gl.Textures']
    })
    
    # Group I: Graphics + Graphics.*
    groups.append({
        'letter': 'i',
        'namespaces': ['Ops.Graphics', 'Ops.Graphics.Geometry', 'Ops.Graphics.Intersection',
                      'Ops.Graphics.Meshes']
    })
    
    # Group J: Html + Html.*
    groups.append({
        'letter': 'j',
        'namespaces': ['Ops.Html', 'Ops.Html.Attributes', 'Ops.Html.CSS', 'Ops.Html.Css',
                      'Ops.Html.Elements', 'Ops.Html.Event', 'Ops.Html.Utils']
    })
    
    # Group K: Json
    groups.append({
        'letter': 'k',
        'namespaces': ['Ops.Json']
    })
    
    # Group L: Math + Math.*
    groups.append({
        'letter': 'l',
        'namespaces': ['Ops.Math', 'Ops.Math.Compare']
    })
    
    # Group M: Net + Net.*
    groups.append({
        'letter': 'm',
        'namespaces': ['Ops.Net', 'Ops.Net.WebSocket']
    })
    
    # Group N: Number
    groups.append({
        'letter': 'n',
        'namespaces': ['Ops.Number']
    })
    
    # Group O: Sidebar
    groups.append({
        'letter': 'o',
        'namespaces': ['Ops.Sidebar']
    })
    
    # Group P: String + String.*
    groups.append({
        'letter': 'p',
        'namespaces': ['Ops.String', 'Ops.String.Base64', 'Ops.String.File']
    })
    
    # Group Q: Templates
    groups.append({
        'letter': 'q',
        'namespaces': ['Ops.Templates']
    })
    
    # Group R: TimeLine + TimeLine.*
    groups.append({
        'letter': 'r',
        'namespaces': ['Ops.TimeLine', 'Ops.TimeLine.Viz']
    })
    
    # Group S: Trigger
    groups.append({
        'letter': 's',
        'namespaces': ['Ops.Trigger']
    })
    
    # Group T: Ui + Ui.*
    groups.append({
        'letter': 't',
        'namespaces': ['Ops.Ui', 'Ops.Ui.Debug', 'Ops.Ui.Routing']
    })
    
    # Group U: Vars
    groups.append({
        'letter': 'u',
        'namespaces': ['Ops.Vars']
    })
    
    # Group V: WebAudio
    groups.append({
        'letter': 'v',
        'namespaces': ['Ops.WebAudio']
    })
    
    # Group W: Website
    groups.append({
        'letter': 'w',
        'namespaces': ['Ops.Website']
    })
    
    return groups

def generate_new_names(groups):
    """Generate new filenames based on grouping"""
    rename_map = []
    
    # Track which first letters we've used for single-item groups
    used_first_letters = set()
    
    for group in groups:
        letter = group['letter']
        namespaces = group['namespaces']
        
        # Check if this letter was already used for a single-item group
        if letter in used_first_letters:
            # This means we have multiple groups with same first letter
            # They should all use two-letter format (letter + 'a', 'b', etc.)
            # But we need to track which subgroup index this is
            pass
        
        for idx, namespace in enumerate(namespaces):
            base_name = get_base_name(namespace)
            
            # Based on user's pattern: single-item groups use single letter (13a)
            # Multi-item groups use two letters (13ba, 13bb, 13ca, 13cb, etc.)
            if len(namespaces) == 1 and letter not in used_first_letters:
                # Single namespace, use single letter
                suffix = letter
                used_first_letters.add(letter)
            else:
                # Multiple namespaces in group, use two letters
                # First item uses letter + 'a', subsequent use letter + 'b', 'c', etc.
                if len(namespaces) > 1 or letter in used_first_letters:
                    second_letter = chr(ord('a') + idx)
                    suffix = letter + second_letter
                else:
                    suffix = letter
            
            new_name = f"13{suffix}-Ops{base_name}.md"
            rename_map.append((namespace, new_name, suffix))
    
    return rename_map

def main():
    groups = create_grouping_plan()
    rename_map = generate_new_names(groups)
    
    # Find current files
    current_map = {ns: old for old, ns in current_files}
    
    print("=" * 80)
    print("RENAMING PLAN FOR SECTION 13 FILES")
    print("=" * 80)
    print()
    print("Pattern: First letter = major group, Second letter = subsections within group")
    print()
    
    # Group by first letter for display
    grouped_renames = {}
    for namespace, new_name, suffix in rename_map:
        first_letter = suffix[0]
        if first_letter not in grouped_renames:
            grouped_renames[first_letter] = []
        old_name = current_map[namespace]
        grouped_renames[first_letter].append((old_name, new_name, namespace))
    
    for letter in sorted(grouped_renames.keys()):
        group_num = ord(letter) - ord('a') + 1
        print(f"\nGroup {letter.upper()} (#{group_num}):")
        print("-" * 80)
        for old_name, new_name, namespace in sorted(grouped_renames[letter], key=lambda x: x[1]):
            print(f"  {old_name:40} -> {new_name:40}  ({namespace})")
    
    print()
    print("=" * 80)
    print(f"Total files to rename: {len(rename_map)}")
    print("=" * 80)

if __name__ == "__main__":
    main()

