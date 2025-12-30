# Ops.Gl.GLTF

*Part of the [All Operators Reference](13-_AllOps.md)*

---

## Ops.Gl.GLTF

### GltfAnimationArray
![GltfAnimationArray op](images/ops/Ops_Gl_GLTF_GltfAnimationArray.svg)

**Full Name:** `Ops.Gl.GLTF.GltfAnimationArray`
**Description:** Convert an animation into an array of coordinates

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Node Name** (String): *See documentation*
- **Steps** (Number: Integer): *See documentation*
- **Full Animation** (Number: Boolean): *See documentation*
- **Start** (Number): *See documentation*
- **Length** (Number): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Found** (booleanNumber): *See documentation*
- **Positions** (Array): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/py-JK0)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GltfAnimationArray"*
**Docs:** [https://cables.gl/op/Ops.Gl.GLTF.GltfAnimationArray](https://cables.gl/op/Ops.Gl.GLTF.GltfAnimationArray)

---

### GltfCameraViewMatrix
![GltfCameraViewMatrix op](images/ops/Ops_Gl_GLTF_GltfCameraViewMatrix.svg)

**Full Name:** `Ops.Gl.GLTF.GltfCameraViewMatrix`
**Description:** get view matrix from a gltf camera

**> Input Ports:**
- **Update** (Trigger): *See documentation*
- **Node Name** (String): *See documentation*

**< Output Ports:**
- **Matrix** (Array): *See documentation*
- **Found** (booleanNumber): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/klpdcI)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GltfCameraViewMatrix"*
**Docs:** [https://cables.gl/op/Ops.Gl.GLTF.GltfCameraViewMatrix](https://cables.gl/op/Ops.Gl.GLTF.GltfCameraViewMatrix)

---

### GltfDracoCompression
![GltfDracoCompression op](images/ops/Ops_Gl_GLTF_GltfDracoCompression.svg)

**Full Name:** `Ops.Gl.GLTF.GltfDracoCompression`
**Description:** gltf draco compression library

**> Input Ports:**
- *Visit [Ops.Gl.GLTF.GltfDracoCompression documentation](https://cables.gl/op/Ops.Gl.GLTF.GltfDracoCompression) for input port details*

**< Output Ports:**
- *Visit [Ops.Gl.GLTF.GltfDracoCompression documentation](https://cables.gl/op/Ops.Gl.GLTF.GltfDracoCompression) for output port details*

**Example Patch:** [Open in Editor](https://cables.gl/edit/WFva2K)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GltfDracoCompression"*
**Docs:** [https://cables.gl/op/Ops.Gl.GLTF.GltfDracoCompression](https://cables.gl/op/Ops.Gl.GLTF.GltfDracoCompression)

---

### GltfGeometry
![GltfGeometry op](images/ops/Ops_Gl_GLTF_GltfGeometry.svg)

**Full Name:** `Ops.Gl.GLTF.GltfGeometry`
**Description:** expose geometry from gltf meshes, also possible to expose submaterial geometries

**> Input Ports:**
- **Update** (Trigger): *See documentation*
- **Name** (String): *See documentation*
- **Submesh** (Number: Integer): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Geometry** (Object): *See documentation*
- **Found** (booleanNumber): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/XKXmf6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GltfGeometry"*
**Docs:** [https://cables.gl/op/Ops.Gl.GLTF.GltfGeometry](https://cables.gl/op/Ops.Gl.GLTF.GltfGeometry)

---

### GltfHierarchy
![GltfHierarchy op](images/ops/Ops_Gl_GLTF_GltfHierarchy.svg)

**Full Name:** `Ops.Gl.GLTF.GltfHierarchy`
**Description:** export array of positions from a hierarchy of a branch structure in a gltf, e.g. a skeleton bones

**> Input Ports:**
- **Trigger** (Trigger): *See documentation*
- **Node Name** (String): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Bones Lines** (Array): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/3t_mJR)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GltfHierarchy"*
**Docs:** [https://cables.gl/op/Ops.Gl.GLTF.GltfHierarchy](https://cables.gl/op/Ops.Gl.GLTF.GltfHierarchy)

---

### GltfInfo
![GltfInfo op](images/ops/Ops_Gl_GLTF_GltfInfo.svg)

**Full Name:** `Ops.Gl.GLTF.GltfInfo`
**Description:** output some infos about the current parent GLTF scene

**> Input Ports:**
- **Exec** (Trigger): *See documentation*

**< Output Ports:**
- **Num Nodes** (Number): *See documentation*
- **Num Cams** (Number): *See documentation*
- **FileUrl** (String): *See documentation*
- **FileName** (String): *See documentation*
- **Camera Names** (Array): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/Z7tacy)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GltfInfo"*
**Docs:** [https://cables.gl/op/Ops.Gl.GLTF.GltfInfo](https://cables.gl/op/Ops.Gl.GLTF.GltfInfo)

---

### GltfMeshSequence_v2
![GltfMeshSequence_v2 op](images/ops/Ops_Gl_GLTF_GltfMeshSequence_v2.svg)

**Full Name:** `Ops.Gl.GLTF.GltfMeshSequence_v2`
**Description:** switch between meshes e.g. like a stop motion animation

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Index** (Number: Integer): *See documentation*
- **Node Name** (String): *See documentation*
- **Transformation** (Number: Boolean): *See documentation*
- **Ignore Material** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Found** (Number): *See documentation*
- **Current Index** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/FiJsxn)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GltfMeshSequence_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.GLTF.GltfMeshSequence_v2](https://cables.gl/op/Ops.Gl.GLTF.GltfMeshSequence_v2)

---

### GltfMorphTargets
![GltfMorphTargets op](images/ops/Ops_Gl_GLTF_GltfMorphTargets.svg)

**Full Name:** `Ops.Gl.GLTF.GltfMorphTargets`
**Description:** render weighted morph targets/shape keys from a gltf file

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Node Name** (String): *See documentation*
- **Scene Time** (Number: Boolean): *See documentation*
- **Time** (Number): *See documentation*
- **Submesh** (Number: Integer): *See documentation*
- **Target Weights** (Array): *See documentation*

**< Output Ports:**
- **Found Node** (booleanNumber): *See documentation*
- **Found Skin** (booleanNumber): *See documentation*
- **Target Names** (Array): *See documentation*
- **MorphTargets Tex** (Object): *See documentation*
- **Next** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/zon4xF)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GltfMorphTargets"*
**Docs:** [https://cables.gl/op/Ops.Gl.GLTF.GltfMorphTargets](https://cables.gl/op/Ops.Gl.GLTF.GltfMorphTargets)

---

### GltfNode_v2
![GltfNode_v2 op](images/ops/Ops_Gl_GLTF_GltfNode_v2.svg)

**Full Name:** `Ops.Gl.GLTF.GltfNode_v2`
**Description:** Control a single node from the GLTFscene op

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Node Name** (String): *See documentation*
- **Transformation** (Number: Boolean): *See documentation*
- **Draw Mesh** (Number: Boolean): *See documentation*
- **Draw Childs** (Number: Boolean): *See documentation*
- **Ignore Material** (Number: Boolean): *See documentation*
- **Use Scene Time** (Number: Boolean): *See documentation*
- **Time** (Number): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Geometry** (Object): *See documentation*
- **Found** (booleanNumber): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.GLTF.GltfNode_v2#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GltfNode_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.GLTF.GltfNode_v2](https://cables.gl/op/Ops.Gl.GLTF.GltfNode_v2)

---

### GltfNodeSineAnim
![GltfNodeSineAnim op](images/ops/Ops_Gl_GLTF_GltfNodeSineAnim.svg)

**Full Name:** `Ops.Gl.GLTF.GltfNodeSineAnim`
**Description:** sine animate gltf nodes by a filter

**> Input Ports:**
- **Update** (Trigger): *See documentation*
- **Filter** (String): *See documentation*
- **Time** (Number): *See documentation*
- **Offset** (Number): *See documentation*
- **Amplitude** (Number): *See documentation*
- **Axis X** (Number): *See documentation*
- **Axis Y** (Number): *See documentation*
- **Axis Z** (Number): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Found** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/w1SPcI)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GltfNodeSineAnim"*
**Docs:** [https://cables.gl/op/Ops.Gl.GLTF.GltfNodeSineAnim](https://cables.gl/op/Ops.Gl.GLTF.GltfNodeSineAnim)

---

### GltfNodeTransform_v2
![GltfNodeTransform_v2 op](images/ops/Ops_Gl_GLTF_GltfNodeTransform_v2.svg)

**Full Name:** `Ops.Gl.GLTF.GltfNodeTransform_v2`
**Description:** Get the transform from the GLTFscene op

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Node Name** (String): *See documentation*
- **Set Matrix** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Found** (booleanNumber): *See documentation*
- **Matrix** (Array): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/yrOJve)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GltfNodeTransform_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.GLTF.GltfNodeTransform_v2](https://cables.gl/op/Ops.Gl.GLTF.GltfNodeTransform_v2)

---

### GltfNodeTransforms_v3
![GltfNodeTransforms_v3 op](images/ops/Ops_Gl_GLTF_GltfNodeTransforms_v3.svg)

**Full Name:** `Ops.Gl.GLTF.GltfNodeTransforms_v3`
**Description:** output all transformations of nodes starting with [search]

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Search** (String): *See documentation*
- **Order Index** (Number: Integer): *See documentation*
- **Space Index** (Number: Integer): *See documentation*
- **Time** (Number): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Positions** (Array): *See documentation*
- **Scale** (Array): *See documentation*
- **Rotation** (Array): *See documentation*
- **Names** (Array): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.GLTF.GltfNodeTransforms_v3#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GltfNodeTransforms_v3"*
**Docs:** [https://cables.gl/op/Ops.Gl.GLTF.GltfNodeTransforms_v3](https://cables.gl/op/Ops.Gl.GLTF.GltfNodeTransforms_v3)

---

### GltfScene_v4
![GltfScene_v4 op](images/ops/Ops_Gl_GLTF_GltfScene_v4.svg)

**Full Name:** `Ops.Gl.GLTF.GltfScene_v4`
**Description:** Load GLTF/GLB 3d files

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Glb File** (String): *See documentation*
- **Draw** (Number: Boolean): *See documentation*
- **Camera Index** (Number: Integer): *See documentation*
- **Animation** (String): *See documentation*
- **Show Structure** (Trigger): *See documentation*
- **Rescale** (Number: Boolean): *See documentation*
- **Rescale Size** (Number): *See documentation*
- **Time** (Number): *See documentation*
- **Sync To Timeline** (Number: Boolean): *See documentation*
- **Loop** (Number: Boolean): *See documentation*
- **Materials** (Object): *See documentation*
- **Hide Nodes** (Array): *See documentation*
- **Use Material Properties** (Number: Boolean): *See documentation*
- **Active** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Render Before** (Trigger): *See documentation*
- **Next** (Trigger): *See documentation*
- **Generator** (String): *See documentation*
- **GLTF Version** (Number): *See documentation*
- **GLTF Extensions Used** (Array): *See documentation*
- **Anim Length** (Number): *See documentation*
- **Anim Time** (Number): *See documentation*
- **Json** (Object): *See documentation*
- **Anims** (Array): *See documentation*
- **BoundingPoints** (Array): *See documentation*
- **Bounds** (Object): *See documentation*
- **Finished** (Trigger): *See documentation*
- **Loading** (booleanNumber): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/XmL8GY)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GltfScene_v4"*
**Docs:** [https://cables.gl/op/Ops.Gl.GLTF.GltfScene_v4](https://cables.gl/op/Ops.Gl.GLTF.GltfScene_v4)

---

### GltfSetMaterial
![GltfSetMaterial op](images/ops/Ops_Gl_GLTF_GltfSetMaterial.svg)

**Full Name:** `Ops.Gl.GLTF.GltfSetMaterial`
**Description:** Assigns a material to a node inside of the gltfScene op

**> Input Ports:**
- **Shader** (Object:Shader): *See documentation*
- **Material Name** (String): *See documentation*

**< Output Ports:**
- **Material** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/Mk3Dv2)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GltfSetMaterial"*
**Docs:** [https://cables.gl/op/Ops.Gl.GLTF.GltfSetMaterial](https://cables.gl/op/Ops.Gl.GLTF.GltfSetMaterial)

---

### GltfSkin
![GltfSkin op](images/ops/Ops_Gl_GLTF_GltfSkin.svg)

**Full Name:** `Ops.Gl.GLTF.GltfSkin`
**Description:** render a skinned mesh (bone/rigging/rigged animation)

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Node Name** (String): *See documentation*
- **Scene Time** (Number: Boolean): *See documentation*
- **Time** (Number): *See documentation*
- **Blend Anims** (Array): *See documentation*

**< Output Ports:**
- **Found Node** (booleanNumber): *See documentation*
- **Found Skin** (booleanNumber): *See documentation*
- **Next** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/TWBC-N)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GltfSkin"*
**Docs:** [https://cables.gl/op/Ops.Gl.GLTF.GltfSkin](https://cables.gl/op/Ops.Gl.GLTF.GltfSkin)

---

### GltfTexture
![GltfTexture op](images/ops/Ops_Gl_GLTF_GltfTexture.svg)

**Full Name:** `Ops.Gl.GLTF.GltfTexture`
**Description:** Load textures from inside a .glb file

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Name** (String): *See documentation*
- **Filter Index** (Number: Integer): *See documentation*
- **Wrap Index** (Number: Integer): *See documentation*
- **Anisotropic Index** (Number: Integer): *See documentation*
- **Flip** (Number: Boolean): *See documentation*
- **Pre Multiplied Alpha** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Texture** (Object): *See documentation*
- **Width** (Number): *See documentation*
- **Height** (Number): *See documentation*
- **Type** (String): *See documentation*
- **Found** (booleanNumber): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/PBGKve)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GltfTexture"*
**Docs:** [https://cables.gl/op/Ops.Gl.GLTF.GltfTexture](https://cables.gl/op/Ops.Gl.GLTF.GltfTexture)

---

### GltfTransformNode
![GltfTransformNode op](images/ops/Ops_Gl_GLTF_GltfTransformNode.svg)

**Full Name:** `Ops.Gl.GLTF.GltfTransformNode`
**Description:** set transformation of a gltf node

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Node Name** (String): *See documentation*
- **Translate X** (Number): *See documentation*
- **Translate Y** (Number): *See documentation*
- **Translate Z** (Number): *See documentation*
- **Rotation X** (Number): *See documentation*
- **Rotation Y** (Number): *See documentation*
- **Rotation Z** (Number): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Found** (booleanNumber): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.GLTF.GltfTransformNode#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GltfTransformNode"*
**Docs:** [https://cables.gl/op/Ops.Gl.GLTF.GltfTransformNode](https://cables.gl/op/Ops.Gl.GLTF.GltfTransformNode)

---

### GltfVertexAnim
![GltfVertexAnim op](images/ops/Ops_Gl_GLTF_GltfVertexAnim.svg)

**Full Name:** `Ops.Gl.GLTF.GltfVertexAnim`
**Description:** play gltf vertex anim directly with its own timing

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Node Name** (String): *See documentation*
- **Scene Time** (Number: Boolean): *See documentation*
- **Time** (Number): *See documentation*

**< Output Ports:**
- **Found Node** (Number): *See documentation*
- **Next** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.GLTF.GltfVertexAnim#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GltfVertexAnim"*
**Docs:** [https://cables.gl/op/Ops.Gl.GLTF.GltfVertexAnim](https://cables.gl/op/Ops.Gl.GLTF.GltfVertexAnim)

---

