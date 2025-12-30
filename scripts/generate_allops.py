#!/usr/bin/env python3
"""
Generate the AllOps chapter by scraping information from cables.gl/ops/
This script helps maintain the AllOps reference chapter.
"""

import re
import urllib.parse

# Op names organized by namespace from cables.gl/ops/
OPS_BY_NAMESPACE = {
    "Ops.Anim": [
        "AnimNumber", "Bang", "BoolAnim", "Crossfade", "FrameRangeAnim", 
        "FrameRangeAnimSwitcher", "InOutInAnim", "LFO", "RandomAnim", 
        "SimpleAnim", "SineAnim", "Smooth", "Snap", "Spring", 
        "StringTypeAnimation", "TimeDelta", "Timer"
    ],
    "Ops.Array": [
        "AnglesBetweenPoints", "AnimArray", "Array", "Array1toX", "Array2To3",
        "Array3", "Array3GetAverage", "Array3GetNumbers", "Array3InterpolateDistributed",
        "Array3Iterator", "Array3Multiply", "Array3PushNumbers", "Array3RandomSelection",
        "Array3SetNumber", "Array3Sum", "Array3To2", "Array3To4", "Array3VectorLength",
        "Array4", "Array4GetNumbers", "Array4SetNumber", "Array4toArray3", "ArrayAbs",
        "ArrayAppendArray", "ArrayBuffer", "ArrayBuffer3", "ArrayCeil", "ArrayChunk",
        "ArrayChunkDuplicate", "ArrayClamp", "ArrayContains", "ArrayDivide", "ArrayFindStrings",
        "ArrayFloor", "ArrayFract", "ArrayFromNumbers", "ArrayGetArray", "ArrayGetNumber",
        "ArrayGetObject", "ArrayGetString", "ArrayGetTexture", "ArrayGetValuesByIndexArray",
        "ArrayIndexBetween", "ArrayIndexMinMax", "ArrayIteratorArray", "ArrayIteratorNumbers",
        "ArrayIteratorObjects", "ArrayIteratorStrings", "ArrayIteratorTextures", "ArrayLength",
        "ArrayLogic", "ArrayLogicArray", "ArrayLogicBetween", "ArrayLookup", "ArrayMath",
        "ArrayMathArray", "ArrayMathExpression", "ArrayMathExpressionTrigger", "ArrayMax",
        "ArrayMerge", "ArrayMergeTrigger", "ArrayMin", "ArrayModulo", "ArrayMultiply",
        "ArrayNumberRamp", "ArrayOfArrays", "ArrayOfObjectsFilterByKeyValue",
        "ArrayOfObjectsFilterKeys", "ArrayOfObjectsToString", "ArrayPack", "ArrayPack2",
        "ArrayPack2Simple", "ArrayPack3", "ArrayPack3Simple", "ArrayPack4", "ArrayPack4Simple",
        "ArrayPow", "ArrayPushString", "ArrayQuantizer", "ArrayRandomSelection", "ArrayRemoveFalsy",
        "ArrayReverse", "ArrayRound", "ArraySetNumber", "ArraySetString", "ArraySin",
        "ArraySmoothStep", "ArraySort", "ArraySplit", "ArraySubtract", "ArraySum",
        "ArrayToObject", "ArrayToString", "ArrayUnique", "ArrayUnpack", "ArrayUnpack2",
        "ArrayUnpack3", "ArrayUnpack4", "ArrayZip"
    ],
    # Add more namespaces as needed
}

DESCRIPTIONS = {
    "Ops.Anim.AnimNumber": "Always animates to the current value",
    "Ops.Anim.Bang": "Trigger a simple bang animation going from 1 to 0",
    "Ops.Anim.BoolAnim": "Animate between two numbers based on a boolean value",
    "Ops.Anim.Crossfade": "Crossfade between 2 values",
    "Ops.Anim.FrameRangeAnim": "Parses string containing ranges of frames and play as coherent animation",
    "Ops.Anim.FrameRangeAnimSwitcher": "Switch between multiple anim ranges of a keyframed 3d scene",
    "Ops.Anim.InOutInAnim": "Animates after a trigger from 1 to 0 to 1",
    "Ops.Anim.LFO": "Low-frequency oscillation for animations",
    "Ops.Anim.RandomAnim": "Animates between random values defined by a min and max value",
    "Ops.Anim.SimpleAnim": "Simple animation between two values",
    "Ops.Anim.SineAnim": "Animation in the form of a sine/cosine curve (sinus/cos)",
    "Ops.Anim.Smooth": "Smooths out jumps in values (AverageInterpolation)",
    "Ops.Anim.Snap": "Snap at certain points (e.g. while scrolling)",
    "Ops.Anim.Spring": "Spring simulation based on input target value.",
    "Ops.Anim.StringTypeAnimation": "Animates a text/string, like it is being typed out by a person",
    "Ops.Anim.TimeDelta": "Measure the time difference between two triggers",
    "Ops.Anim.Timer": "A timer that can be started, paused and reset by triggering",
}

def generate_op_section(namespace, op_name, description=""):
    """Generate markdown section for a single op"""
    full_name = f"{namespace}.{op_name}"
    op_url = f"https://cables.gl/ops/{full_name}"
    editor_url = f"https://cables.gl/editor?patch=example_{op_name}"
    
    section = f"""### {op_name}

**Description:** {description or f"*See [documentation]({op_url})*"}

**Input Ports:**
- *Visit [{full_name} documentation]({op_url}) for complete input port details*

**Output Ports:**
- *Visit [{full_name} documentation]({op_url}) for complete output port details*

**Example Patch:** [Open in Editor]({editor_url})

**Patches Using This Op:**
- *Search [cables.gl patches](https://cables.gl/ops) for "{op_name}"*

**Documentation:** [{op_url}]({op_url})

---

"""
    return section

def generate_namespace_section(namespace, ops_list, namespace_description=""):
    """Generate markdown section for a namespace"""
    section = f"""## {namespace}

{namespace_description}

"""
    for op_name in ops_list:
        full_key = f"{namespace}.{op_name}"
        description = DESCRIPTIONS.get(full_key, "")
        section += generate_op_section(namespace, op_name, description)
    
    return section

if __name__ == "__main__":
    # This script can be extended to actually scrape cables.gl
    # For now, it provides the structure
    print("This script helps generate the AllOps chapter.")
    print("To fully populate it, visit each op's page at cables.gl/ops/")

