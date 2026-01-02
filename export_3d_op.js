// Custom Cables.gl Op: Export 3D Files with Noise Distortion
// Name: Ops.User.Export3D.Export3DFile
// Description: Export geometry as 3D file (OBJ/GLTF) with optional noise texture distortion

// Input Ports
const inGeometry = op.inObject("Geometry");
const inNoiseTexture = op.inTexture("Noise Texture", null);
const inDistortionStrength = op.inFloat("Distortion Strength", 0.0);
const inDistortionChannel = op.inSwitch("Distortion Channel", ["R", "G", "B", "A", "Luminance"], "Luminance");
const inFormat = op.inSwitch("Export Format", ["OBJ", "GLTF"], "OBJ");
const inFilename = op.inString("Filename", "exported_mesh");
const inExport = op.inTriggerButton("Export");

// Output Ports
const outFileString = op.outString("File String");
const outDownloaded = op.outTrigger("Downloaded");
const outError = op.outString("Error");

// Group ports for better UI
op.setPortGroup("Geometry", [inGeometry]);
op.setPortGroup("Distortion", [inNoiseTexture, inDistortionStrength, inDistortionChannel]);
op.setPortGroup("Export", [inFormat, inFilename, inExport]);

// Helper: Read texture data to canvas
// Note: This function attempts to read texture data from WebGL
// If the texture object structure is different in cables.gl, you may need to adjust
function textureToCanvas(texture, width, height) {
    if (!texture) return null;
    
    const canvas = document.createElement('canvas');
    const targetWidth = width || 256;
    const targetHeight = height || 256;
    canvas.width = targetWidth;
    canvas.height = targetHeight;
    const ctx = canvas.getContext('2d');
    
    // Try to get texture from WebGL context
    const gl = op.patch.cgl.gl;
    if (!gl) {
        op.logWarn("WebGL context not available");
        return null;
    }
    
    // Try different ways to access the texture
    let glTexture = null;
    
    // Method 1: Direct texture object (if it's a WebGL texture)
    if (texture instanceof WebGLTexture) {
        glTexture = texture;
    }
    // Method 2: Texture object with .texture property
    else if (texture.texture) {
        glTexture = texture.texture;
    }
    // Method 3: Texture object with .glTexture property
    else if (texture.glTexture) {
        glTexture = texture.glTexture;
    }
    // Method 4: Try to use the object directly
    else {
        glTexture = texture;
    }
    
    if (!glTexture) {
        op.logWarn("Could not extract WebGL texture from texture object");
        return null;
    }
    
    // Create a framebuffer to read texture
    const framebuffer = gl.createFramebuffer();
    gl.bindFramebuffer(gl.FRAMEBUFFER, framebuffer);
    
    try {
        gl.framebufferTexture2D(gl.FRAMEBUFFER, gl.COLOR_ATTACHMENT0, gl.TEXTURE_2D, glTexture, 0);
        
        if (gl.checkFramebufferStatus(gl.FRAMEBUFFER) === gl.FRAMEBUFFER_COMPLETE) {
            const pixels = new Uint8Array(targetWidth * targetHeight * 4);
            gl.readPixels(0, 0, targetWidth, targetHeight, gl.RGBA, gl.UNSIGNED_BYTE, pixels);
            
            // Convert to ImageData (flip Y because readPixels reads bottom-to-top)
            const imageData = ctx.createImageData(targetWidth, targetHeight);
            for (let y = 0; y < targetHeight; y++) {
                for (let x = 0; x < targetWidth; x++) {
                    const srcIndex = (y * targetWidth + x) * 4;
                    const dstIndex = ((targetHeight - 1 - y) * targetWidth + x) * 4;
                    imageData.data[dstIndex] = pixels[srcIndex];     // R
                    imageData.data[dstIndex + 1] = pixels[srcIndex + 1]; // G
                    imageData.data[dstIndex + 2] = pixels[srcIndex + 2]; // B
                    imageData.data[dstIndex + 3] = pixels[srcIndex + 3]; // A
                }
            }
            ctx.putImageData(imageData, 0, 0);
        } else {
            op.logWarn("Framebuffer incomplete, cannot read texture");
            gl.bindFramebuffer(gl.FRAMEBUFFER, null);
            gl.deleteFramebuffer(framebuffer);
            return null;
        }
    } catch (e) {
        op.logWarn("Error reading texture:", e);
        gl.bindFramebuffer(gl.FRAMEBUFFER, null);
        gl.deleteFramebuffer(framebuffer);
        return null;
    } finally {
        gl.bindFramebuffer(gl.FRAMEBUFFER, null);
        gl.deleteFramebuffer(framebuffer);
    }
    
    return canvas;
}

// Helper: Sample texture at UV coordinates
function sampleTexture(canvas, u, v) {
    if (!canvas) return 0;
    
    const x = Math.floor(u * canvas.width) % canvas.width;
    const y = Math.floor((1 - v) * canvas.height) % canvas.height; // Flip V
    
    const ctx = canvas.getContext('2d');
    const imageData = ctx.getImageData(x, y, 1, 1);
    const [r, g, b, a] = imageData.data;
    
    const channel = inDistortionChannel.get();
    switch (channel) {
        case "R": return r / 255.0;
        case "G": return g / 255.0;
        case "B": return b / 255.0;
        case "A": return a / 255.0;
        case "Luminance": return (r * 0.299 + g * 0.587 + b * 0.114) / 255.0;
        default: return r / 255.0;
    }
}

// Helper: Apply distortion to geometry
function applyDistortion(geometry, noiseCanvas) {
    if (!geometry || !noiseCanvas || inDistortionStrength.get() === 0) {
        return geometry;
    }
    
    // Clone geometry to avoid modifying original
    const distortedGeometry = JSON.parse(JSON.stringify(geometry));
    
    // Get vertex positions and UVs
    const positions = distortedGeometry.attributes?.position?.array || [];
    const uvs = distortedGeometry.attributes?.uv?.array || [];
    const strength = inDistortionStrength.get();
    
    if (!positions || positions.length === 0) {
        return geometry;
    }
    
    // Apply distortion along Z-axis (or normal direction)
    for (let i = 0; i < positions.length; i += 3) {
        const x = positions[i];
        const y = positions[i + 1];
        const z = positions[i + 2];
        
        // Get UV coordinates
        let u = 0.5, v = 0.5;
        if (uvs && uvs.length > 0) {
            const uvIndex = Math.floor((i / 3) * 2);
            if (uvIndex < uvs.length - 1) {
                u = uvs[uvIndex];
                v = uvs[uvIndex + 1];
            }
        } else {
            // Generate UVs from position if not available
            u = (x + 1) / 2;
            v = (y + 1) / 2;
        }
        
        // Sample noise texture
        const noiseValue = sampleTexture(noiseCanvas, u, v);
        
        // Apply distortion (along Z-axis by default)
        positions[i + 2] = z + (noiseValue - 0.5) * strength;
    }
    
    return distortedGeometry;
}

// Helper: Convert geometry to OBJ string
function geometryToOBJ(geometry) {
    if (!geometry) return "";
    
    let obj = "# Exported from Cables.gl\n";
    obj += `# Generated: ${new Date().toISOString()}\n\n`;
    
    const positions = geometry.attributes?.position?.array || [];
    const normals = geometry.attributes?.normal?.array || [];
    const uvs = geometry.attributes?.uv?.array || [];
    const indices = geometry.index?.array || [];
    
    // Write vertices
    if (positions && positions.length > 0) {
        for (let i = 0; i < positions.length; i += 3) {
            const x = positions[i];
            const y = positions[i + 1];
            const z = positions[i + 2];
            obj += `v ${x.toFixed(6)} ${y.toFixed(6)} ${z.toFixed(6)}\n`;
        }
    }
    
    // Write texture coordinates
    if (uvs && uvs.length > 0) {
        for (let i = 0; i < uvs.length; i += 2) {
            const u = uvs[i];
            const v = uvs[i + 1];
            obj += `vt ${u.toFixed(6)} ${v.toFixed(6)}\n`;
        }
    }
    
    // Write normals
    if (normals && normals.length > 0) {
        for (let i = 0; i < normals.length; i += 3) {
            const nx = normals[i];
            const ny = normals[i + 1];
            const nz = normals[i + 2];
            obj += `vn ${nx.toFixed(6)} ${ny.toFixed(6)} ${nz.toFixed(6)}\n`;
        }
    }
    
    // Write faces
    if (indices && indices.length > 0) {
        obj += "\n";
        for (let i = 0; i < indices.length; i += 3) {
            const i1 = indices[i] + 1; // OBJ uses 1-based indexing
            const i2 = indices[i + 1] + 1;
            const i3 = indices[i + 2] + 1;
            
            if (uvs && normals) {
                obj += `f ${i1}/${i1}/${i1} ${i2}/${i2}/${i2} ${i3}/${i3}/${i3}\n`;
            } else if (uvs) {
                obj += `f ${i1}/${i1} ${i2}/${i2} ${i3}/${i3}\n`;
            } else if (normals) {
                obj += `f ${i1}//${i1} ${i2}//${i2} ${i3}//${i3}\n`;
            } else {
                obj += `f ${i1} ${i2} ${i3}\n`;
            }
        }
    } else if (positions && positions.length > 0) {
        // No indices, assume triangles
        obj += "\n";
        for (let i = 0; i < positions.length / 3; i += 3) {
            const i1 = i + 1;
            const i2 = i + 2;
            const i3 = i + 3;
            obj += `f ${i1} ${i2} ${i3}\n`;
        }
    }
    
    return obj;
}

// Helper: Convert geometry to GLTF (simplified JSON)
function geometryToGLTF(geometry) {
    if (!geometry) return "";
    
    const positions = geometry.attributes?.position?.array || [];
    const normals = geometry.attributes?.normal?.array || [];
    const uvs = geometry.attributes?.uv?.array || [];
    const indices = geometry.index?.array || [];
    
    // Convert arrays to base64
    function arrayToBase64(arr, componentType, type) {
        const buffer = new ArrayBuffer(arr.length * 4);
        const view = new Float32Array(buffer);
        for (let i = 0; i < arr.length; i++) {
            view[i] = arr[i];
        }
        const base64 = btoa(String.fromCharCode(...new Uint8Array(buffer)));
        return base64;
    }
    
    // For simplicity, we'll create a minimal GLTF JSON
    // Note: Full GLTF export would require proper binary encoding
    const gltf = {
        asset: {
            version: "2.0",
            generator: "Cables.gl Custom Export Op"
        },
        scenes: [{
            nodes: [0]
        }],
        nodes: [{
            mesh: 0
        }],
        meshes: [{
            primitives: [{
                attributes: {
                    POSITION: 0,
                    NORMAL: normals.length > 0 ? 1 : undefined,
                    TEXCOORD_0: uvs.length > 0 ? 2 : undefined
                },
                indices: 3
            }]
        }],
        accessors: [
            {
                bufferView: 0,
                componentType: 5126, // FLOAT
                count: positions.length / 3,
                type: "VEC3",
                min: [0, 0, 0], // Should calculate actual min
                max: [1, 1, 1]  // Should calculate actual max
            }
        ],
        bufferViews: [
            {
                buffer: 0,
                byteOffset: 0,
                byteLength: positions.length * 4
            }
        ],
        buffers: [{
            uri: "data:application/octet-stream;base64," + arrayToBase64(positions, 5126, "VEC3")
        }]
    };
    
    // Clean up undefined values
    return JSON.stringify(gltf, null, 2);
}

// Helper: Trigger file download
function downloadFile(content, filename, mimeType) {
    const blob = new Blob([content], { type: mimeType });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = filename;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    URL.revokeObjectURL(url);
}

// Main export function
inExport.onTriggered = function() {
    try {
        outError.set("");
        
        const geometry = inGeometry.get();
        if (!geometry) {
            outError.set("No geometry provided");
            return;
        }
        
        // Get noise texture if provided
        let noiseCanvas = null;
        const noiseTexture = inNoiseTexture.get();
        if (noiseTexture && inDistortionStrength.get() !== 0) {
            // Try to read texture to canvas
            // Get texture dimensions if available
            let texWidth = 256;
            let texHeight = 256;
            
            if (noiseTexture.width) texWidth = noiseTexture.width;
            if (noiseTexture.height) texHeight = noiseTexture.height;
            
            noiseCanvas = textureToCanvas(noiseTexture, texWidth, texHeight);
            
            if (!noiseCanvas) {
                op.logWarn("Could not read noise texture, proceeding without distortion");
            }
        }
        
        // Apply distortion if noise texture is provided
        let processedGeometry = geometry;
        if (noiseCanvas && inDistortionStrength.get() !== 0) {
            processedGeometry = applyDistortion(geometry, noiseCanvas);
        }
        
        // Convert to requested format
        const format = inFormat.get();
        let fileContent = "";
        let extension = "";
        let mimeType = "";
        
        if (format === "OBJ") {
            fileContent = geometryToOBJ(processedGeometry);
            extension = ".obj";
            mimeType = "text/plain";
        } else if (format === "GLTF") {
            fileContent = geometryToGLTF(processedGeometry);
            extension = ".gltf";
            mimeType = "application/json";
        }
        
        if (!fileContent) {
            outError.set("Failed to generate file content");
            return;
        }
        
        // Output file string
        outFileString.set(fileContent);
        
        // Trigger download
        const filename = inFilename.get() || "exported_mesh";
        const fullFilename = filename + extension;
        downloadFile(fileContent, fullFilename, mimeType);
        
        outDownloaded.trigger();
        
    } catch (error) {
        const errorMsg = error.message || String(error);
        outError.set(errorMsg);
        op.logError("Export failed:", error);
    }
};

// Also update file string when geometry changes (without exporting)
inGeometry.onChange = function() {
    const geometry = inGeometry.get();
    if (geometry) {
        // Optionally update preview without exporting
        // This allows users to see the OBJ string before downloading
    }
};

