# Export 3D Files Custom Op for Cables.gl

This custom op allows you to export 3D geometry from Cables.gl as OBJ or GLTF files, with optional noise texture-based distortion.

## Features

- **Export Formats**: OBJ and GLTF
- **Noise Distortion**: Apply distortion to geometry based on noise texture values
- **Channel Selection**: Choose which texture channel to use for distortion (R, G, B, A, or Luminance)
- **Automatic Download**: Downloads the exported file automatically
- **Error Handling**: Provides error messages if export fails

## Installation

1. Open your Cables.gl patch
2. Click the "+" button to add a new op
3. Select "Create Op"
4. Name it: `Ops.User.Export3D.Export3DFile`
5. Copy and paste the code from `export_3d_op.js` into the op editor
6. Save the op

## Usage

### Basic Export (No Distortion)

1. Connect a **Geometry** object to the `Geometry` input port
2. Set the `Export Format` to "OBJ" or "GLTF"
3. Set the `Filename` (without extension)
4. Click the `Export` button
5. The file will automatically download

### Export with Noise Distortion

1. Create a **NoiseTexture** op (or use any texture)
2. Connect the noise texture to the `Noise Texture` input
3. Connect your geometry to the `Geometry` input
4. Adjust `Distortion Strength` (0 = no distortion, higher values = more distortion)
5. Select which `Distortion Channel` to use (R, G, B, A, or Luminance)
6. Click `Export`

### Example Patch Setup

```
NoiseTexture -> [Noise Texture input]
Plane -> [Geometry input]
[Export3DFile op] -> Downloads OBJ file
```

## Input Ports

- **Geometry** (Object): The 3D geometry/mesh to export
- **Noise Texture** (Texture): Optional texture for distortion (leave empty for no distortion)
- **Distortion Strength** (Float): How much to distort the geometry (0.0 = no distortion)
- **Distortion Channel** (Switch): Which channel to sample from the noise texture
  - R: Red channel
  - G: Green channel
  - B: Blue channel
  - A: Alpha channel
  - Luminance: Grayscale value
- **Export Format** (Switch): File format to export
  - OBJ: Wavefront OBJ format (text-based, widely supported)
  - GLTF: GLTF JSON format (simplified version)
- **Filename** (String): Name of the exported file (without extension)
- **Export** (Trigger Button): Click to export and download

## Output Ports

- **File String** (String): The exported file content as a string (useful for preview)
- **Downloaded** (Trigger): Fires when download completes
- **Error** (String): Error message if export fails

## How It Works

1. **Geometry Input**: Takes any Cables.gl geometry object
2. **Distortion**: If a noise texture is provided:
   - Reads the texture data using WebGL
   - Samples the texture at each vertex's UV coordinates
   - Applies distortion along the Z-axis based on the sampled value
3. **Export**: Converts the geometry to the requested format:
   - **OBJ**: Standard Wavefront OBJ format with vertices, UVs, normals, and faces
   - **GLTF**: Simplified GLTF JSON format (full binary GLTF would require additional libraries)

## Limitations

- **Texture Reading**: The texture reading function may need adjustment depending on how Cables.gl structures texture objects. If distortion doesn't work, check the browser console for warnings.
- **GLTF Export**: The GLTF export is simplified. For full GLTF binary support, consider using a library like `gltf-transform` or `gltf-jsx`.
- **Large Geometries**: Very large geometries may take time to process. The op processes everything synchronously.

## Troubleshooting

### Distortion Not Working

If the noise texture distortion isn't working:

1. Check the browser console for warnings
2. The texture object structure in Cables.gl might be different than expected
3. Try using a different texture or creating a simple test texture
4. You can still export without distortion by leaving the noise texture input empty

### Export Fails

1. Check the `Error` output port for error messages
2. Ensure the geometry input is valid
3. Make sure the geometry has vertex positions
4. Check browser console for detailed error logs

### File Not Downloading

1. Check browser download settings (some browsers block automatic downloads)
2. Check the browser console for errors
3. Try a different filename

## Advanced Usage

### Using with Procedural Geometry

You can use this op with procedurally generated geometry:

```
CustomGeometry -> [Geometry input]
NoiseTexture -> [Noise Texture input]
[Export3DFile op] -> Exports distorted procedural mesh
```

### Combining with Other Ops

You can chain this with other geometry ops:

```
Plane -> Subdivide -> Displace -> [Geometry input]
NoiseTexture -> [Noise Texture input]
[Export3DFile op]
```

## Notes

- The op clones the geometry before applying distortion, so the original geometry is not modified
- UV coordinates are required for texture-based distortion. If the geometry doesn't have UVs, they're generated from vertex positions
- The distortion is applied along the Z-axis by default. You can modify the code to apply distortion along normals or other directions

## Future Improvements

Possible enhancements:
- Support for STL format
- Distortion along normals instead of Z-axis
- Multiple distortion modes
- Binary GLTF export
- Export with materials/textures
- Batch export multiple geometries

