# Ops.Gl.GLTF


```{=latex}
\OpsSubsubNoSubsectionNumbering\setcounter{subsubsection}{0}
```
### GltfAnimationArray
![GltfAnimationArray op](images/ops/Ops_Gl_GLTF_GltfAnimationArray.svg)

**Full Name:** `Ops.Gl.GLTF.GltfAnimationArray`

Convert an animation into an array of coordinates.

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **Node Name** (String)
- **Steps** (Number: Integer)
- **Full Animation** (Number: Boolean)
- **Start** (Number)
- **Length** (Number)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)
- **Found** (booleanNumber)
- **Positions** (Array)

**Example:** [cables.gl/edit/py-JK0](https://cables.gl/edit/py-JK0)

**Doc:** [cables.gl/op/Ops.Gl.GLTF.GltfAnimationArray](https://cables.gl/op/Ops.Gl.GLTF.GltfAnimationArray)

### GltfCameraViewMatrix
![GltfCameraViewMatrix op](images/ops/Ops_Gl_GLTF_GltfCameraViewMatrix.svg)

**Full Name:** `Ops.Gl.GLTF.GltfCameraViewMatrix`

get view matrix from a gltf camera.

**`\inputsymbol`{=latex} Inputs**

- **Update** (Trigger)
- **Node Name** (String)

**`\outputsymbol`{=latex} Output**

- **Matrix** (Array)
- **Found** (booleanNumber)

**Example:** [cables.gl/edit/klpdcI](https://cables.gl/edit/klpdcI)

**Doc:** [cables.gl/op/Ops.Gl.GLTF.GltfCameraViewMatrix](https://cables.gl/op/Ops.Gl.GLTF.GltfCameraViewMatrix)

### GltfDracoCompression
![GltfDracoCompression op](images/ops/Ops_Gl_GLTF_GltfDracoCompression.svg)

**Full Name:** `Ops.Gl.GLTF.GltfDracoCompression`

gltf draco compression library.

**Example:** [cables.gl/edit/WFva2K](https://cables.gl/edit/WFva2K)

**Doc:** [cables.gl/op/Ops.Gl.GLTF.GltfDracoCompression](https://cables.gl/op/Ops.Gl.GLTF.GltfDracoCompression)

### GltfGeometry
![GltfGeometry op](images/ops/Ops_Gl_GLTF_GltfGeometry.svg)

**Full Name:** `Ops.Gl.GLTF.GltfGeometry`

expose geometry from gltf meshes, also possible to expose submaterial geometries.

**`\inputsymbol`{=latex} Inputs**

- **Update** (Trigger)
- **Name** (String)
- **Submesh** (Number: Integer)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)
- **Geometry** (Object)
- **Found** (booleanNumber)

**Example:** [cables.gl/edit/XKXmf6](https://cables.gl/edit/XKXmf6)

**Doc:** [cables.gl/op/Ops.Gl.GLTF.GltfGeometry](https://cables.gl/op/Ops.Gl.GLTF.GltfGeometry)

### GltfHierarchy
![GltfHierarchy op](images/ops/Ops_Gl_GLTF_GltfHierarchy.svg)

**Full Name:** `Ops.Gl.GLTF.GltfHierarchy`

export array of positions from a hierarchy of a branch structure in a gltf, e.g. a skeleton bones.

**`\inputsymbol`{=latex} Inputs**

- **Trigger** (Trigger)
- **Node Name** (String)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)
- **Bones Lines** (Array)

**Example:** [cables.gl/edit/3t_mJR](https://cables.gl/edit/3t_mJR)

**Doc:** [cables.gl/op/Ops.Gl.GLTF.GltfHierarchy](https://cables.gl/op/Ops.Gl.GLTF.GltfHierarchy)

### GltfInfo
![GltfInfo op](images/ops/Ops_Gl_GLTF_GltfInfo.svg)

**Full Name:** `Ops.Gl.GLTF.GltfInfo`

output some infos about the current parent GLTF scene.

**`\inputsymbol`{=latex} Inputs**

- **Exec** (Trigger)

**`\outputsymbol`{=latex} Output**

- **Num Nodes** (Number)
- **Num Cams** (Number)
- **FileUrl** (String)
- **FileName** (String)
- **Camera Names** (Array)

**Example:** [cables.gl/edit/Z7tacy](https://cables.gl/edit/Z7tacy)

**Doc:** [cables.gl/op/Ops.Gl.GLTF.GltfInfo](https://cables.gl/op/Ops.Gl.GLTF.GltfInfo)

### GltfMeshSequence_v2
![GltfMeshSequence_v2 op](images/ops/Ops_Gl_GLTF_GltfMeshSequence_v2.svg)

**Full Name:** `Ops.Gl.GLTF.GltfMeshSequence_v2`

switch between meshes e.g. like a stop motion animation.

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **Index** (Number: Integer)
- **Node Name** (String)
- **Transformation** (Number: Boolean)
- **Ignore Material** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)
- **Found** (Number)
- **Current Index** (Number)

**Example:** [cables.gl/edit/FiJsxn](https://cables.gl/edit/FiJsxn)

**Doc:** [cables.gl/op/Ops.Gl.GLTF.GltfMeshSequence_v2](https://cables.gl/op/Ops.Gl.GLTF.GltfMeshSequence_v2)

### GltfMorphTargets
![GltfMorphTargets op](images/ops/Ops_Gl_GLTF_GltfMorphTargets.svg)

**Full Name:** `Ops.Gl.GLTF.GltfMorphTargets`

render weighted morph targets/shape keys from a gltf file.

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **Node Name** (String)
- **Scene Time** (Number: Boolean)
- **Time** (Number)
- **Submesh** (Number: Integer)
- **Target Weights** (Array)

**`\outputsymbol`{=latex} Output**

- **Found Node** (booleanNumber)
- **Found Skin** (booleanNumber)
- **Target Names** (Array)
- **MorphTargets Tex** (Object)
- **Next** (Trigger)

**Example:** [cables.gl/edit/zon4xF](https://cables.gl/edit/zon4xF)

**Doc:** [cables.gl/op/Ops.Gl.GLTF.GltfMorphTargets](https://cables.gl/op/Ops.Gl.GLTF.GltfMorphTargets)

### GltfNode_v2
![GltfNode_v2 op](images/ops/Ops_Gl_GLTF_GltfNode_v2.svg)

**Full Name:** `Ops.Gl.GLTF.GltfNode_v2`

Control a single node from the GLTFscene op.

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **Node Name** (String)
- **Transformation** (Number: Boolean)
- **Draw Mesh** (Number: Boolean)
- **Draw Childs** (Number: Boolean)
- **Ignore Material** (Number: Boolean)
- **Use Scene Time** (Number: Boolean)
- **Time** (Number)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)
- **Geometry** (Object)
- **Found** (booleanNumber)

**Example:** [cables.gl/op/Ops.Gl.GLTF.GltfNode_v2#example](https://cables.gl/op/Ops.Gl.GLTF.GltfNode_v2#example)

**Doc:** [cables.gl/op/Ops.Gl.GLTF.GltfNode_v2](https://cables.gl/op/Ops.Gl.GLTF.GltfNode_v2)

### GltfNodeSineAnim
![GltfNodeSineAnim op](images/ops/Ops_Gl_GLTF_GltfNodeSineAnim.svg)

**Full Name:** `Ops.Gl.GLTF.GltfNodeSineAnim`

sine animate gltf nodes by a filter.

**`\inputsymbol`{=latex} Inputs**

- **Update** (Trigger)
- **Filter** (String)
- **Time** (Number)
- **Offset** (Number)
- **Amplitude** (Number)
- **Axis X** (Number)
- **Axis Y** (Number)
- **Axis Z** (Number)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)
- **Found** (Number)

**Example:** [cables.gl/edit/w1SPcI](https://cables.gl/edit/w1SPcI)

**Doc:** [cables.gl/op/Ops.Gl.GLTF.GltfNodeSineAnim](https://cables.gl/op/Ops.Gl.GLTF.GltfNodeSineAnim)

### GltfNodeTransform_v2
![GltfNodeTransform_v2 op](images/ops/Ops_Gl_GLTF_GltfNodeTransform_v2.svg)

**Full Name:** `Ops.Gl.GLTF.GltfNodeTransform_v2`

Get the transform from the GLTFscene op.

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **Node Name** (String)
- **Set Matrix** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)
- **Found** (booleanNumber)
- **Matrix** (Array)

**Example:** [cables.gl/edit/yrOJve](https://cables.gl/edit/yrOJve)

**Doc:** [cables.gl/op/Ops.Gl.GLTF.GltfNodeTransform_v2](https://cables.gl/op/Ops.Gl.GLTF.GltfNodeTransform_v2)

### GltfNodeTransforms_v3
![GltfNodeTransforms_v3 op](images/ops/Ops_Gl_GLTF_GltfNodeTransforms_v3.svg)

**Full Name:** `Ops.Gl.GLTF.GltfNodeTransforms_v3`

output all transformations of nodes starting with [search].

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **Search** (String)
- **Order Index** (Number: Integer)
- **Space Index** (Number: Integer)
- **Time** (Number)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)
- **Positions** (Array)
- **Scale** (Array)
- **Rotation** (Array)
- **Names** (Array)

**Example:** [cables.gl/op/Ops.Gl.GLTF.GltfNodeTransforms_v3#example](https://cables.gl/op/Ops.Gl.GLTF.GltfNodeTransforms_v3#example)

**Doc:** [cables.gl/op/Ops.Gl.GLTF.GltfNodeTransforms_v3](https://cables.gl/op/Ops.Gl.GLTF.GltfNodeTransforms_v3)

### GltfScene_v4
![GltfScene_v4 op](images/ops/Ops_Gl_GLTF_GltfScene_v4.svg)

**Full Name:** `Ops.Gl.GLTF.GltfScene_v4`

Load GLTF/GLB 3d files.

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **Glb File** (String)
- **Draw** (Number: Boolean)
- **Camera Index** (Number: Integer)
- **Animation** (String)
- **Show Structure** (Trigger)
- **Rescale** (Number: Boolean)
- **Rescale Size** (Number)
- **Time** (Number)
- **Sync To Timeline** (Number: Boolean)
- **Loop** (Number: Boolean)
- **Materials** (Object)
- **Hide Nodes** (Array)
- **Use Material Properties** (Number: Boolean)
- **Active** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Render Before** (Trigger)
- **Next** (Trigger)
- **Generator** (String)
- **GLTF Version** (Number)
- **GLTF Extensions Used** (Array)
- **Anim Length** (Number)
- **Anim Time** (Number)
- **Json** (Object)
- **Anims** (Array)
- **BoundingPoints** (Array)
- **Bounds** (Object)
- **Finished** (Trigger)
- **Loading** (booleanNumber)

**Example:** [cables.gl/edit/XmL8GY](https://cables.gl/edit/XmL8GY)

**Doc:** [cables.gl/op/Ops.Gl.GLTF.GltfScene_v4](https://cables.gl/op/Ops.Gl.GLTF.GltfScene_v4)

### GltfSetMaterial
![GltfSetMaterial op](images/ops/Ops_Gl_GLTF_GltfSetMaterial.svg)

**Full Name:** `Ops.Gl.GLTF.GltfSetMaterial`

Assigns a material to a node inside of the gltfScene op.

**`\inputsymbol`{=latex} Inputs**

- **Shader** (Object:Shader)
- **Material Name** (String)

**`\outputsymbol`{=latex} Output**

- **Material** (Object)

**Example:** [cables.gl/edit/Mk3Dv2](https://cables.gl/edit/Mk3Dv2)

**Doc:** [cables.gl/op/Ops.Gl.GLTF.GltfSetMaterial](https://cables.gl/op/Ops.Gl.GLTF.GltfSetMaterial)

### GltfSkin
![GltfSkin op](images/ops/Ops_Gl_GLTF_GltfSkin.svg)

**Full Name:** `Ops.Gl.GLTF.GltfSkin`

render a skinned mesh (bone/rigging/rigged animation).

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **Node Name** (String)
- **Scene Time** (Number: Boolean)
- **Time** (Number)
- **Blend Anims** (Array)

**`\outputsymbol`{=latex} Output**

- **Found Node** (booleanNumber)
- **Found Skin** (booleanNumber)
- **Next** (Trigger)

**Example:** [cables.gl/edit/TWBC-N](https://cables.gl/edit/TWBC-N)

**Doc:** [cables.gl/op/Ops.Gl.GLTF.GltfSkin](https://cables.gl/op/Ops.Gl.GLTF.GltfSkin)

### GltfTexture
![GltfTexture op](images/ops/Ops_Gl_GLTF_GltfTexture.svg)

**Full Name:** `Ops.Gl.GLTF.GltfTexture`

Load textures from inside a .glb file.

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **Name** (String)
- **Filter Index** (Number: Integer)
- **Wrap Index** (Number: Integer)
- **Anisotropic Index** (Number: Integer)
- **Flip** (Number: Boolean)
- **Pre Multiplied Alpha** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Texture** (Object)
- **Width** (Number)
- **Height** (Number)
- **Type** (String)
- **Found** (booleanNumber)

**Example:** [cables.gl/edit/PBGKve](https://cables.gl/edit/PBGKve)

**Doc:** [cables.gl/op/Ops.Gl.GLTF.GltfTexture](https://cables.gl/op/Ops.Gl.GLTF.GltfTexture)

### GltfTransformNode
![GltfTransformNode op](images/ops/Ops_Gl_GLTF_GltfTransformNode.svg)

**Full Name:** `Ops.Gl.GLTF.GltfTransformNode`

set transformation of a gltf node.

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **Node Name** (String)
- **Translate X** (Number)
- **Translate Y** (Number)
- **Translate Z** (Number)
- **Rotation X** (Number)
- **Rotation Y** (Number)
- **Rotation Z** (Number)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)
- **Found** (booleanNumber)

**Example:** [cables.gl/op/Ops.Gl.GLTF.GltfTransformNode#example](https://cables.gl/op/Ops.Gl.GLTF.GltfTransformNode#example)

**Doc:** [cables.gl/op/Ops.Gl.GLTF.GltfTransformNode](https://cables.gl/op/Ops.Gl.GLTF.GltfTransformNode)

### GltfVertexAnim
![GltfVertexAnim op](images/ops/Ops_Gl_GLTF_GltfVertexAnim.svg)

**Full Name:** `Ops.Gl.GLTF.GltfVertexAnim`

play gltf vertex anim directly with its own timing.

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **Node Name** (String)
- **Scene Time** (Number: Boolean)
- **Time** (Number)

**`\outputsymbol`{=latex} Output**

- **Found Node** (Number)
- **Next** (Trigger)

**Example:** [cables.gl/op/Ops.Gl.GLTF.GltfVertexAnim#example](https://cables.gl/op/Ops.Gl.GLTF.GltfVertexAnim#example)

**Doc:** [cables.gl/op/Ops.Gl.GLTF.GltfVertexAnim](https://cables.gl/op/Ops.Gl.GLTF.GltfVertexAnim)


