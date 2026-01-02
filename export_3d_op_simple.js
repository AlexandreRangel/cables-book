// Simplified Export 3D Op - Uses existing GeometryToObj pattern
// Name: Ops.User.Export3D.Export3DSimple
// Description: Simple 3D export that works with GeometryToObj op

// Input Ports
const inGeometry = op.inObject("Geometry");
const inFormat = op.inSwitch("Format", ["OBJ", "STL"], "OBJ");
const inFilename = op.inString("Filename", "exported_mesh");
const inExport = op.inTriggerButton("Export");

// Output Ports
const outFileString = op.outString("File String");
const outDownloaded = op.outTrigger("Downloaded");
const outError = op.outString("Error");

// Group ports
op.setPortGroup("Export", [inFormat, inFilename, inExport]);

// Helper: Convert geometry to OBJ string
function geometryToOBJ(geometry) {
    if (!geometry) return "";
    
    let obj = "# Exported from Cables.gl\n";
    obj += `# Generated: ${new Date().toISOString()}\n\n`;
    
    // Try to access geometry data
    // Cables.gl geometry objects may have different structures
    let positions = [];
    let normals = [];
    let uvs = [];
    let indices = [];
    
    // Try common geometry property names
    if (geometry.attributes) {
        positions = geometry.attributes.position?.array || geometry.attributes.POSITION?.array || [];
        normals = geometry.attributes.normal?.array || geometry.attributes.NORMAL?.array || [];
        uvs = geometry.attributes.uv?.array || geometry.attributes.UV?.array || geometry.attributes.TEXCOORD_0?.array || [];
    }
    
    if (geometry.index) {
        indices = geometry.index.array || [];
    }
    
    // If no positions found, try direct access
    if (positions.length === 0 && geometry.positions) {
        positions = geometry.positions;
    }
    if (normals.length === 0 && geometry.normals) {
        normals = geometry.normals;
    }
    if (uvs.length === 0 && geometry.uvs) {
        uvs = geometry.uvs;
    }
    if (indices.length === 0 && geometry.indices) {
        indices = geometry.indices;
    }
    
    if (positions.length === 0) {
        throw new Error("Geometry has no vertex positions");
    }
    
    // Write vertices
    for (let i = 0; i < positions.length; i += 3) {
        const x = positions[i] || 0;
        const y = positions[i + 1] || 0;
        const z = positions[i + 2] || 0;
        obj += `v ${x.toFixed(6)} ${y.toFixed(6)} ${z.toFixed(6)}\n`;
    }
    
    // Write texture coordinates
    if (uvs && uvs.length > 0) {
        for (let i = 0; i < uvs.length; i += 2) {
            const u = uvs[i] || 0;
            const v = uvs[i + 1] || 0;
            obj += `vt ${u.toFixed(6)} ${v.toFixed(6)}\n`;
        }
    }
    
    // Write normals
    if (normals && normals.length > 0) {
        for (let i = 0; i < normals.length; i += 3) {
            const nx = normals[i] || 0;
            const ny = normals[i + 1] || 0;
            const nz = normals[i + 2] || 0;
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
            
            if (uvs.length > 0 && normals.length > 0) {
                obj += `f ${i1}/${i1}/${i1} ${i2}/${i2}/${i2} ${i3}/${i3}/${i3}\n`;
            } else if (uvs.length > 0) {
                obj += `f ${i1}/${i1} ${i2}/${i2} ${i3}/${i3}\n`;
            } else if (normals.length > 0) {
                obj += `f ${i1}//${i1} ${i2}//${i2} ${i3}//${i3}\n`;
            } else {
                obj += `f ${i1} ${i2} ${i3}\n`;
            }
        }
    } else if (positions.length > 0) {
        // No indices, assume triangles
        obj += "\n";
        const vertexCount = positions.length / 3;
        for (let i = 0; i < vertexCount; i += 3) {
            if (i + 2 < vertexCount) {
                const i1 = i + 1;
                const i2 = i + 2;
                const i3 = i + 3;
                obj += `f ${i1} ${i2} ${i3}\n`;
            }
        }
    }
    
    return obj;
}

// Helper: Convert geometry to STL string (ASCII)
function geometryToSTL(geometry) {
    if (!geometry) return "";
    
    let stl = "solid exported_from_cables\n";
    
    // Get positions and indices (same as OBJ)
    let positions = [];
    let indices = [];
    
    if (geometry.attributes) {
        positions = geometry.attributes.position?.array || geometry.attributes.POSITION?.array || [];
    }
    if (geometry.index) {
        indices = geometry.index.array || [];
    }
    
    if (positions.length === 0 && geometry.positions) {
        positions = geometry.positions;
    }
    if (indices.length === 0 && geometry.indices) {
        indices = geometry.indices;
    }
    
    if (positions.length === 0) {
        throw new Error("Geometry has no vertex positions");
    }
    
    // Calculate normals if not provided
    function calculateNormal(v1, v2, v3) {
        const a = [v2[0] - v1[0], v2[1] - v1[1], v2[2] - v1[2]];
        const b = [v3[0] - v1[0], v3[1] - v1[1], v3[2] - v1[2]];
        const cross = [
            a[1] * b[2] - a[2] * b[1],
            a[2] * b[0] - a[0] * b[2],
            a[0] * b[1] - a[1] * b[0]
        ];
        const len = Math.sqrt(cross[0] * cross[0] + cross[1] * cross[1] + cross[2] * cross[2]);
        if (len > 0) {
            return [cross[0] / len, cross[1] / len, cross[2] / len];
        }
        return [0, 0, 1];
    }
    
    // Write triangles
    if (indices && indices.length > 0) {
        for (let i = 0; i < indices.length; i += 3) {
            const i1 = indices[i];
            const i2 = indices[i + 1];
            const i3 = indices[i + 2];
            
            const v1 = [
                positions[i1 * 3],
                positions[i1 * 3 + 1],
                positions[i1 * 3 + 2]
            ];
            const v2 = [
                positions[i2 * 3],
                positions[i2 * 3 + 1],
                positions[i2 * 3 + 2]
            ];
            const v3 = [
                positions[i3 * 3],
                positions[i3 * 3 + 1],
                positions[i3 * 3 + 2]
            ];
            
            const normal = calculateNormal(v1, v2, v3);
            
            stl += `  facet normal ${normal[0].toFixed(6)} ${normal[1].toFixed(6)} ${normal[2].toFixed(6)}\n`;
            stl += `    outer loop\n`;
            stl += `      vertex ${v1[0].toFixed(6)} ${v1[1].toFixed(6)} ${v1[2].toFixed(6)}\n`;
            stl += `      vertex ${v2[0].toFixed(6)} ${v2[1].toFixed(6)} ${v2[2].toFixed(6)}\n`;
            stl += `      vertex ${v3[0].toFixed(6)} ${v3[1].toFixed(6)} ${v3[2].toFixed(6)}\n`;
            stl += `    endloop\n`;
            stl += `  endfacet\n`;
        }
    } else {
        // No indices, assume triangles
        for (let i = 0; i < positions.length; i += 9) {
            if (i + 8 < positions.length) {
                const v1 = [positions[i], positions[i + 1], positions[i + 2]];
                const v2 = [positions[i + 3], positions[i + 4], positions[i + 5]];
                const v3 = [positions[i + 6], positions[i + 7], positions[i + 8]];
                
                const normal = calculateNormal(v1, v2, v3);
                
                stl += `  facet normal ${normal[0].toFixed(6)} ${normal[1].toFixed(6)} ${normal[2].toFixed(6)}\n`;
                stl += `    outer loop\n`;
                stl += `      vertex ${v1[0].toFixed(6)} ${v1[1].toFixed(6)} ${v1[2].toFixed(6)}\n`;
                stl += `      vertex ${v2[0].toFixed(6)} ${v2[1].toFixed(6)} ${v2[2].toFixed(6)}\n`;
                stl += `      vertex ${v3[0].toFixed(6)} ${v3[1].toFixed(6)} ${v3[2].toFixed(6)}\n`;
                stl += `    endloop\n`;
                stl += `  endfacet\n`;
            }
        }
    }
    
    stl += "endsolid exported_from_cables\n";
    return stl;
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
        
        const format = inFormat.get();
        let fileContent = "";
        let extension = "";
        let mimeType = "";
        
        if (format === "OBJ") {
            fileContent = geometryToOBJ(geometry);
            extension = ".obj";
            mimeType = "text/plain";
        } else if (format === "STL") {
            fileContent = geometryToSTL(geometry);
            extension = ".stl";
            mimeType = "application/octet-stream";
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

