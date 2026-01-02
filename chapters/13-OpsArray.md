# Ops.Array

*Part of the [All Operators Reference](13-_AllOps.md)*

---

## Ops.Array

### AnglesBetweenPoints
![AnglesBetweenPoints op](images/ops/Ops_Array_AnglesBetweenPoints.svg)

**Full Name:** `Ops.Array.AnglesBetweenPoints`
**Description:** Outputs the angle between points in 3D space (degree)

**> Input Ports:**

- **Points** (Array)
- **Theta** (Number)
- **Phi** (Number)

**< Output Ports:**

- **Rotations** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/Y2_BIR)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "AnglesBetweenPoints"*
**Docs:** [https://cables.gl/op/Ops.Array.AnglesBetweenPoints](https://cables.gl/op/Ops.Array.AnglesBetweenPoints)

---

### AnimArray_v2
![AnimArray_v2 op](images/ops/Ops_Array_AnimArray_v2.svg)

**Full Name:** `Ops.Array.AnimArray_v2`
**Description:** Animate values in an array to another array

**> Input Ports:**

- **Update** (Trigger)
- **Next Array** (Array)
- **Duration** (Number)
- **Easing Index** (Number: Integer)

**< Output Ports:**

- **Next** (Trigger)
- **Matrix** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/OwvgkJ)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "AnimArray_v2"*
**Docs:** [https://cables.gl/op/Ops.Array.AnimArray_v2](https://cables.gl/op/Ops.Array.AnimArray_v2)

---

### Array1toX_v2
![Array1toX_v2 op](images/ops/Ops_Array_Array1toX_v2.svg)

**Full Name:** `Ops.Array.Array1toX_v2`
**Description:** convert an array1 to array2,3,4 by choosing content for new axis

**> Input Ports:**

- **Array1x** (Array)

**< Output Ports:**

- **Array3x** (Array)
- **Total Points** (Number)
- **Array Length** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/omZrLu)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Array1toX_v2"*
**Docs:** [https://cables.gl/op/Ops.Array.Array1toX_v2](https://cables.gl/op/Ops.Array.Array1toX_v2)

---

### Array2To3
![Array2To3 op](images/ops/Ops_Array_Array2To3.svg)

**Full Name:** `Ops.Array.Array2To3`
**Description:** Inserts zeroes every third item

**> Input Ports:**

- **Array2x** (Array)

**< Output Ports:**

- **Array3x** (Array)
- **Total Points** (Number)
- **Array Length** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/xAg8P6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Array2To3"*
**Docs:** [https://cables.gl/op/Ops.Array.Array2To3](https://cables.gl/op/Ops.Array.Array2To3)

---

### Array3
![Array3 op](images/ops/Ops_Array_Array3.svg)

**Full Name:** `Ops.Array.Array3`
**Description:** Create an array of num triplets set to default values xyz

**> Input Ports:**

- **Num Triplets** (Number: Integer)
- **X** (Number)
- **Y** (Number)
- **Z** (Number)

**< Output Ports:**

- **Array** (Array)
- **Total Points** (Number)
- **Array Length** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/lmn5Og)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Array3"*
**Docs:** [https://cables.gl/op/Ops.Array.Array3](https://cables.gl/op/Ops.Array.Array3)

---

### Array3GetAverage
![Array3GetAverage op](images/ops/Ops_Array_Array3GetAverage.svg)

**Full Name:** `Ops.Array.Array3GetAverage`
**Description:** Average x,y,z values of an array3x

**> Input Ports:**

- **Array** (Array)

**< Output Ports:**

- **Average X** (Number)
- **Average Y** (Number)
- **Average Z** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/lmn5Og)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Array3GetAverage"*
**Docs:** [https://cables.gl/op/Ops.Array.Array3GetAverage](https://cables.gl/op/Ops.Array.Array3GetAverage)

---

### Array3GetNumbers
![Array3GetNumbers op](images/ops/Ops_Array_Array3GetNumbers.svg)

**Full Name:** `Ops.Array.Array3GetNumbers`
**Description:** Get 3 values XYZ from an array

**> Input Ports:**

- **Array** (Array)
- **Index** (Number: Integer)

**< Output Ports:**

- **X** (Number)
- **Y** (Number)
- **Z** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/5LhTLJ)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Array3GetNumbers"*
**Docs:** [https://cables.gl/op/Ops.Array.Array3GetNumbers](https://cables.gl/op/Ops.Array.Array3GetNumbers)

---

### Array3InterpolateDistributed
![Array3InterpolateDistributed op](images/ops/Ops_Array_Array3InterpolateDistributed.svg)

**Full Name:** `Ops.Array.Array3InterpolateDistributed`
**Description:** Interpolate between two arrays

**> Input Ports:**

- **Update** (Trigger)
- **Array 1** (Array)
- **Array 2** (Array)
- **Progress** (Number)

**< Output Ports:**

- **Result** (Array)
- **Array Length** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/2UuCa6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Array3InterpolateDistributed"*
**Docs:** [https://cables.gl/op/Ops.Array.Array3InterpolateDistributed](https://cables.gl/op/Ops.Array.Array3InterpolateDistributed)

---

### Array3Iterator
![Array3Iterator op](images/ops/Ops_Array_Array3Iterator.svg)

**Full Name:** `Ops.Array.Array3Iterator`
**Description:** Iterate over an array in steps of three and outputs three values

**> Input Ports:**

- **Execute** (Trigger)
- **Array** (Array)
- **Step** (Number)

**< Output Ports:**

- **Trigger** (Trigger)
- **Triggers for every iteration step** (triplet in the array)
- **Index** (Number)
- **Value 1** (Number)
- **First value of the current triplet** (e.g. x)
- **Value 2** (Number)
- **Second value of the current triplet** (e.g. y)
- **Value 3** (Number)
- **Third value of the current triplet** (e.g. z)

**Example Patch:** [Open in Editor](https://cables.gl/edit/Ubwk3u)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Array3Iterator"*
**Docs:** [https://cables.gl/op/Ops.Array.Array3Iterator](https://cables.gl/op/Ops.Array.Array3Iterator)

---

### Array3Multiply
![Array3Multiply op](images/ops/Ops_Array_Array3Multiply.svg)

**Full Name:** `Ops.Array.Array3Multiply`
**Description:** Multiply every XYZ member of array3x

**> Input Ports:**

- **Array3x** (Array)
- **Mul X** (Number)
- **Mul Y** (Number)
- **Mul Z** (Number)

**< Output Ports:**

- **Result** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/8FxmVJ)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Array3Multiply"*
**Docs:** [https://cables.gl/op/Ops.Array.Array3Multiply](https://cables.gl/op/Ops.Array.Array3Multiply)

---

### Array3PushNumbers_v2
![Array3PushNumbers_v2 op](images/ops/Ops_Array_Array3PushNumbers_v2.svg)

**Full Name:** `Ops.Array.Array3PushNumbers_v2`
**Description:** Push three numbers to the end of an array (was ArrayPushValue3x)

**> Input Ports:**

- **Execute** (Trigger)
- **Array** (Array)
- **Value 1** (Number)
- **Value 2** (Number)
- **Value 3** (Number)
- **Reset** (Trigger)

**< Output Ports:**

- **Next** (Trigger)
- **Result Array** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/uOzMH7)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Array3PushNumbers_v2"*
**Docs:** [https://cables.gl/op/Ops.Array.Array3PushNumbers_v2](https://cables.gl/op/Ops.Array.Array3PushNumbers_v2)

---

### Array3RandomSelection
![Array3RandomSelection op](images/ops/Ops_Array_Array3RandomSelection.svg)

**Full Name:** `Ops.Array.Array3RandomSelection`
**Description:** Extract definable amount of random xyz points from an array

**> Input Ports:**

- **Array** (Array)
- **Elements** (Number: Integer)
- **Seed** (Number)

**< Output Ports:**

- **Result** (Array)
- **Total Points** (Number)
- **Array Length** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/1qNz98)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Array3RandomSelection"*
**Docs:** [https://cables.gl/op/Ops.Array.Array3RandomSelection](https://cables.gl/op/Ops.Array.Array3RandomSelection)

---

### Array3SetNumber
![Array3SetNumber op](images/ops/Ops_Array_Array3SetNumber.svg)

**Full Name:** `Ops.Array.Array3SetNumber`
**Description:** Set three numbers at index in an array

**> Input Ports:**

- **Array** (Array)
- **Index** (Number: Integer)
- **Value X** (Number)
- **Value Y** (Number)
- **Value Z** (Number)

**< Output Ports:**

- **Result** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/t44fQc)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Array3SetNumber"*
**Docs:** [https://cables.gl/op/Ops.Array.Array3SetNumber](https://cables.gl/op/Ops.Array.Array3SetNumber)

---

### Array3Sum
![Array3Sum op](images/ops/Ops_Array_Array3Sum.svg)

**Full Name:** `Ops.Array.Array3Sum`
**Description:** Add number to every XYZ member of array3x

**> Input Ports:**

- **Array3x** (Array)
- **Add X** (Number)
- **Add Y** (Number)
- **Add Z** (Number)

**< Output Ports:**

- **Result** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/D-pQHj)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Array3Sum"*
**Docs:** [https://cables.gl/op/Ops.Array.Array3Sum](https://cables.gl/op/Ops.Array.Array3Sum)

---

### Array3To2
![Array3To2 op](images/ops/Ops_Array_Array3To2.svg)

**Full Name:** `Ops.Array.Array3To2`
**Description:** Remove every 3rd item of an array - changes array length

**> Input Ports:**

- **Array3x** (Array)

**< Output Ports:**

- **Array2x** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/lmn5Og)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Array3To2"*
**Docs:** [https://cables.gl/op/Ops.Array.Array3To2](https://cables.gl/op/Ops.Array.Array3To2)

---

### Array3To4
![Array3To4 op](images/ops/Ops_Array_Array3To4.svg)

**Full Name:** `Ops.Array.Array3To4`
**Description:** Convert an array3 to an array4 by filling it up with 1

**> Input Ports:**

- **Array3x** (Array)

**< Output Ports:**

- **Array4x** (Array)
- **Total Points** (Number)
- **Array Length** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/h_Dbm4)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Array3To4"*
**Docs:** [https://cables.gl/op/Ops.Array.Array3To4](https://cables.gl/op/Ops.Array.Array3To4)

---

### Array3VectorLength
![Array3VectorLength op](images/ops/Ops_Array_Array3VectorLength.svg)

**Full Name:** `Ops.Array.Array3VectorLength`
**Description:** Return the length of a vector from an array 3

**> Input Ports:**

- **Array In** (Array)

**< Output Ports:**

- **Array Out** (Array)
- **Array Lengths** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/L9tsRJ)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Array3VectorLength"*
**Docs:** [https://cables.gl/op/Ops.Array.Array3VectorLength](https://cables.gl/op/Ops.Array.Array3VectorLength)

---

### Array4
![Array4 op](images/ops/Ops_Array_Array4.svg)

**Full Name:** `Ops.Array.Array4`
**Description:** Create an array of num quadruples set to default values xyz

**> Input Ports:**

- **Num Quadruplets** (Number: Integer)
- **X** (Number)
- **Y** (Number)
- **Z** (Number)
- **W** (Number)

**< Output Ports:**

- **Array** (Array)
- **Total Quadruplets** (Number)
- **Array Length** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/HjHdQc)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Array4"*
**Docs:** [https://cables.gl/op/Ops.Array.Array4](https://cables.gl/op/Ops.Array.Array4)

---

### Array4GetNumbers
![Array4GetNumbers op](images/ops/Ops_Array_Array4GetNumbers.svg)

**Full Name:** `Ops.Array.Array4GetNumbers`
**Description:** Get 4 values from an array

**> Input Ports:**

- **Array** (Array)
- **Index** (Number: Integer)

**< Output Ports:**

- **X** (Number)
- **Y** (Number)
- **Z** (Number)
- **W** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/tI0COg)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Array4GetNumbers"*
**Docs:** [https://cables.gl/op/Ops.Array.Array4GetNumbers](https://cables.gl/op/Ops.Array.Array4GetNumbers)

---

### Array4SetNumber
![Array4SetNumber op](images/ops/Ops_Array_Array4SetNumber.svg)

**Full Name:** `Ops.Array.Array4SetNumber`
**Description:** Set four numbers at index in an array

**> Input Ports:**

- **Array** (Array)
- **Index** (Number: Integer)
- **Value X** (Number)
- **Value Y** (Number)
- **Value Z** (Number)
- **Value W** (Number)

**< Output Ports:**

- **Result** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/HjHdQc)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Array4SetNumber"*
**Docs:** [https://cables.gl/op/Ops.Array.Array4SetNumber](https://cables.gl/op/Ops.Array.Array4SetNumber)

---

### Array4toArray3
![Array4toArray3 op](images/ops/Ops_Array_Array4toArray3.svg)

**Full Name:** `Ops.Array.Array4toArray3`
**Description:** Convert an array4 to array3 by dropping every 4th number

**> Input Ports:**

- **Array** (Array)

**< Output Ports:**

- **Result** (Array)
- **Array Length** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/SZdOet)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Array4toArray3"*
**Docs:** [https://cables.gl/op/Ops.Array.Array4toArray3](https://cables.gl/op/Ops.Array.Array4toArray3)

---

### Array_v3
![Array_v3 op](images/ops/Ops_Array_Array_v3.svg)

**Full Name:** `Ops.Array.Array_v3`
**Description:** Can generate 3 kinds of arrays: Number - 1,2,3,4 - Normalized - (ContinuousNumberArray)

**> Input Ports:**

- **Array Length** (Number: Integer)
- **Mode Select Index** (Number: Integer)
- **Default Value** (Number)
- **Reverse** (Number: Boolean)

**< Output Ports:**

- **Array** (Array)
- **Array Length Out** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/P4qAz6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Array_v3"*
**Docs:** [https://cables.gl/op/Ops.Array.Array_v3](https://cables.gl/op/Ops.Array.Array_v3)

---

### ArrayAbs
![ArrayAbs op](images/ops/Ops_Array_ArrayAbs.svg)

**Full Name:** `Ops.Array.ArrayAbs`
**Description:** Converts array contents to absolute values - converts all negative numbers to positive numbers

**> Input Ports:**

- **In** (Array)

**< Output Ports:**

- **Result** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/Jdij7z)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayAbs"*
**Docs:** [https://cables.gl/op/Ops.Array.ArrayAbs](https://cables.gl/op/Ops.Array.ArrayAbs)

---

### ArrayAppendArray
![ArrayAppendArray op](images/ops/Ops_Array_ArrayAppendArray.svg)

**Full Name:** `Ops.Array.ArrayAppendArray`
**Description:** Append an array to an existing array

**> Input Ports:**

- **Join** (Trigger)
- **Array** (Array)
- **Reset** (Trigger)

**< Output Ports:**

- **Result** (Array)
- **Array Length** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/quYUvH)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayAppendArray"*
**Docs:** [https://cables.gl/op/Ops.Array.ArrayAppendArray](https://cables.gl/op/Ops.Array.ArrayAppendArray)

---

### ArrayBuffer
![ArrayBuffer op](images/ops/Ops_Array_ArrayBuffer.svg)

**Full Name:** `Ops.Array.ArrayBuffer`
**Description:** Store values in an array / fifo array buffer

**> Input Ports:**

- **Exec** (Trigger)
- **Value** (Number)
- **Max Length** (Number: Integer)
- **Reset** (Trigger)

**< Output Ports:**

- **Trigger Out** (Trigger)
- **Result** (Array)
- **Array Length** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/_ZPEnB)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayBuffer"*
**Docs:** [https://cables.gl/op/Ops.Array.ArrayBuffer](https://cables.gl/op/Ops.Array.ArrayBuffer)

---

### ArrayBuffer3
![ArrayBuffer3 op](images/ops/Ops_Array_ArrayBuffer3.svg)

**Full Name:** `Ops.Array.ArrayBuffer3`
**Description:** Circular buffer for xyz values

**> Input Ports:**

- **Exec** (Trigger)
- **Max Num Elements** (Number)
- **Value X** (Number)
- **Value Y** (Number)
- **Value Z** (Number)
- **Reset** (Trigger)

**< Output Ports:**

- **Trigger Out** (Trigger)
- **Result** (Array)
- **Array Length** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/TNwIZC)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayBuffer3"*
**Docs:** [https://cables.gl/op/Ops.Array.ArrayBuffer3](https://cables.gl/op/Ops.Array.ArrayBuffer3)

---

### ArrayCeil
![ArrayCeil op](images/ops/Ops_Array_ArrayCeil.svg)

**Full Name:** `Ops.Array.ArrayCeil`
**Description:** Round numbers up

**> Input Ports:**

- **In** (Array)

**< Output Ports:**

- **Result** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/7xdJrG)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayCeil"*
**Docs:** [https://cables.gl/op/Ops.Array.ArrayCeil](https://cables.gl/op/Ops.Array.ArrayCeil)

---

### ArrayChunk
![ArrayChunk op](images/ops/Ops_Array_ArrayChunk.svg)

**Full Name:** `Ops.Array.ArrayChunk`
**Description:** Extracts x elements from an array

**> Input Ports:**

- **Input Array** (Array)
- **Begin Index** (Number: Integer)
- **Chunk Size** (Number: Integer)
- **Circular** (Number: Boolean)

**< Output Ports:**

- **Output Array** (Array)
- **Array Length** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/yGR5GA)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayChunk"*
**Docs:** [https://cables.gl/op/Ops.Array.ArrayChunk](https://cables.gl/op/Ops.Array.ArrayChunk)

---

### ArrayChunkDuplicate
![ArrayChunkDuplicate op](images/ops/Ops_Array_ArrayChunkDuplicate.svg)

**Full Name:** `Ops.Array.ArrayChunkDuplicate`
**Description:** Repeat chunks of an array multiple times

**> Input Ports:**

- **Array** (Array)
- **Chunk Size** (Number: Integer)
- **Repeats** (Number: Integer)

**< Output Ports:**

- **Result** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/Vu22bf)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayChunkDuplicate"*
**Docs:** [https://cables.gl/op/Ops.Array.ArrayChunkDuplicate](https://cables.gl/op/Ops.Array.ArrayChunkDuplicate)

---

### ArrayClamp
![ArrayClamp op](images/ops/Ops_Array_ArrayClamp.svg)

**Full Name:** `Ops.Array.ArrayClamp`
**Description:** Clamp the values of an array to a min and max value

**> Input Ports:**

- **Array In** (Array)
- **Min** (Number)
- **Max** (Number)

**< Output Ports:**

- **Array Out** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/tyxvSP)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayClamp"*
**Docs:** [https://cables.gl/op/Ops.Array.ArrayClamp](https://cables.gl/op/Ops.Array.ArrayClamp)

---

### ArrayContains_v2
![ArrayContains_v2 op](images/ops/Ops_Array_ArrayContains_v2.svg)

**Full Name:** `Ops.Array.ArrayContains_v2`
**Description:** Check if an array contains a number (find,search,indexOf)

**> Input Ports:**

- **Array** (Array)
- **SearchValue** (Number)

**< Output Ports:**

- **Found** (booleanNumber)
- **Index** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/8pZ8GA)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayContains_v2"*
**Docs:** [https://cables.gl/op/Ops.Array.ArrayContains_v2](https://cables.gl/op/Ops.Array.ArrayContains_v2)

---

### ArrayDivide
![ArrayDivide op](images/ops/Ops_Array_ArrayDivide.svg)

**Full Name:** `Ops.Array.ArrayDivide`
**Description:** Divide all values in an array by one number

**> Input Ports:**

- **Array In** (Array)
- **Value** (Number)

**< Output Ports:**

- **Array Out** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/uIYNcn)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayDivide"*
**Docs:** [https://cables.gl/op/Ops.Array.ArrayDivide](https://cables.gl/op/Ops.Array.ArrayDivide)

---

### ArrayFindStrings
![ArrayFindStrings op](images/ops/Ops_Array_ArrayFindStrings.svg)

**Full Name:** `Ops.Array.ArrayFindStrings`
**Description:** Return all the indexes of a string in an array

**> Input Ports:**

- **Array** (Array)
- **SearchValue** (String)

**< Output Ports:**

- **Index** (Array)
- **Found** (booleanNumber)

**Example Patch:** [Open in Editor](https://cables.gl/edit/p9sBjH)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayFindStrings"*
**Docs:** [https://cables.gl/op/Ops.Array.ArrayFindStrings](https://cables.gl/op/Ops.Array.ArrayFindStrings)

---

### ArrayFloor
![ArrayFloor op](images/ops/Ops_Array_ArrayFloor.svg)

**Full Name:** `Ops.Array.ArrayFloor`
**Description:** Round numbers down

**> Input Ports:**

- **In** (Array)

**< Output Ports:**

- **Result** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/7xdJrG)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayFloor"*
**Docs:** [https://cables.gl/op/Ops.Array.ArrayFloor](https://cables.gl/op/Ops.Array.ArrayFloor)

---

### ArrayFract
![ArrayFract op](images/ops/Ops_Array_ArrayFract.svg)

**Full Name:** `Ops.Array.ArrayFract`
**Description:** Return the fractional remainder of all values in an array

**> Input Ports:**

- **In** (Array)

**< Output Ports:**

- **Result** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/uVzImG)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayFract"*
**Docs:** [https://cables.gl/op/Ops.Array.ArrayFract](https://cables.gl/op/Ops.Array.ArrayFract)

---

### ArrayFromNumbers
![ArrayFromNumbers op](images/ops/Ops_Array_ArrayFromNumbers.svg)

**Full Name:** `Ops.Array.ArrayFromNumbers`
**Description:** Simple way to create small arrays of numbers

**> Input Ports:**

- **Update** (Trigger)
- **Limit** (Number: Integer)
- **Slider** (Number: Boolean)
- **Index 0** (Number)
- **Index 1** (Number)
- **Index 2** (Number)
- **Index 3** (Number)
- **Index 4** (Number)
- **Index 5** (Number)
- **Index 6** (Number)
- **Index 7** (Number)
- **Index 8** (Number)
- **Index 9** (Number)
- **Index 10** (Number)
- **Index 11** (Number)
- **Index 12** (Number)
- **Index 13** (Number)
- **Index 14** (Number)
- **Index 15** (Number)
- **Index 16** (Number)
- **Index 17** (Number)
- **Index 18** (Number)
- **Index 19** (Number)
- **Index 20** (Number)
- **Index 21** (Number)
- **Index 22** (Number)
- **Index 23** (Number)
- **Index 24** (Number)
- **Index 25** (Number)
- **Index 26** (Number)
- **Index 27** (Number)
- **Index 28** (Number)
- **Index 29** (Number)

**< Output Ports:**

- **Next** (Trigger)
- **Array** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/ZNPh2B)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayFromNumbers"*
**Docs:** [https://cables.gl/op/Ops.Array.ArrayFromNumbers](https://cables.gl/op/Ops.Array.ArrayFromNumbers)

---

### ArrayGetArray
![ArrayGetArray op](images/ops/Ops_Array_ArrayGetArray.svg)

**Full Name:** `Ops.Array.ArrayGetArray`
**Description:** Get an array from an array of arrays

**> Input Ports:**

- **Array Of Arrays** (Array)
- **Index** (Number: Integer)

**< Output Ports:**

- **Result Array** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/yU2Pet)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayGetArray"*
**Docs:** [https://cables.gl/op/Ops.Array.ArrayGetArray](https://cables.gl/op/Ops.Array.ArrayGetArray)

---

### ArrayGetNumber
![ArrayGetNumber op](images/ops/Ops_Array_ArrayGetNumber.svg)

**Full Name:** `Ops.Array.ArrayGetNumber`
**Description:** Return a value from an array

**> Input Ports:**

- **Array** (Array)
- **Index** (Number: Integer)
- **Value Invalid Index** (Number)

**< Output Ports:**

- **Value** (Number)
- **Valid Index** (booleanNumber)

**Example Patch:** [Open in Editor](https://cables.gl/edit/38AIji)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayGetNumber"*
**Docs:** [https://cables.gl/op/Ops.Array.ArrayGetNumber](https://cables.gl/op/Ops.Array.ArrayGetNumber)

---

### ArrayGetObject
![ArrayGetObject op](images/ops/Ops_Array_ArrayGetObject.svg)

**Full Name:** `Ops.Array.ArrayGetObject`
**Description:** Get an object from an array

**> Input Ports:**

- **Array** (Array)
- **Index** (Number: Integer)

**< Output Ports:**

- **Value** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/7npL_M)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayGetObject"*
**Docs:** [https://cables.gl/op/Ops.Array.ArrayGetObject](https://cables.gl/op/Ops.Array.ArrayGetObject)

---

### ArrayGetString_v2
![ArrayGetString_v2 op](images/ops/Ops_Array_ArrayGetString_v2.svg)

**Full Name:** `Ops.Array.ArrayGetString_v2`
**Description:** Get a string from an array at [index]

**> Input Ports:**

- **Array** (Array)
- **Index** (Number: Integer)

**< Output Ports:**

- **Result** (String)
- **Found** (booleanNumber)

**Example Patch:** [Open in Editor](https://cables.gl/edit/aHNk8i)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayGetString_v2"*
**Docs:** [https://cables.gl/op/Ops.Array.ArrayGetString_v2](https://cables.gl/op/Ops.Array.ArrayGetString_v2)

---

### ArrayGetTexture
![ArrayGetTexture op](images/ops/Ops_Array_ArrayGetTexture.svg)

**Full Name:** `Ops.Array.ArrayGetTexture`
**Description:** Get texture from array at index

**> Input Ports:**

- **Array** (Array)
- **Index** (Number: Integer)

**< Output Ports:**

- **Value** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/jFv097)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayGetTexture"*
**Docs:** [https://cables.gl/op/Ops.Array.ArrayGetTexture](https://cables.gl/op/Ops.Array.ArrayGetTexture)

---

### ArrayGetValuesByIndexArray
![ArrayGetValuesByIndexArray op](images/ops/Ops_Array_ArrayGetValuesByIndexArray.svg)

**Full Name:** `Ops.Array.ArrayGetValuesByIndexArray`
**Description:** Pick values from input array at given indices and stride

**> Input Ports:**

- **Array** (Array)
- **Array Stride Index** (Number: Integer)
- **Indices** (Array)

**< Output Ports:**

- **Results** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/bOBgTq)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayGetValuesByIndexArray"*
**Docs:** [https://cables.gl/op/Ops.Array.ArrayGetValuesByIndexArray](https://cables.gl/op/Ops.Array.ArrayGetValuesByIndexArray)

---

### ArrayIndexBetween
![ArrayIndexBetween op](images/ops/Ops_Array_ArrayIndexBetween.svg)

**Full Name:** `Ops.Array.ArrayIndexBetween`
**Description:** Output index where value is greater than number and smaller then next number

**> Input Ports:**

- **Array** (Array)
- **Value** (Number)

**< Output Ports:**

- **Index** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/kH4xLu)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayIndexBetween"*
**Docs:** [https://cables.gl/op/Ops.Array.ArrayIndexBetween](https://cables.gl/op/Ops.Array.ArrayIndexBetween)

---

### ArrayIndexMinMax
![ArrayIndexMinMax op](images/ops/Ops_Array_ArrayIndexMinMax.svg)

**Full Name:** `Ops.Array.ArrayIndexMinMax`
**Description:** Find lowest/highest numbers in an array

**> Input Ports:**

- **Array** (Array)

**< Output Ports:**

- **Max** (Number)
- **Index Max** (Number)
- **Min** (Number)
- **Index Min** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/gamucI)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayIndexMinMax"*
**Docs:** [https://cables.gl/op/Ops.Array.ArrayIndexMinMax](https://cables.gl/op/Ops.Array.ArrayIndexMinMax)

---

### ArrayIteratorArray
![ArrayIteratorArray op](images/ops/Ops_Array_ArrayIteratorArray.svg)

**Full Name:** `Ops.Array.ArrayIteratorArray`
**Description:** Iterate over an array of arrays

**> Input Ports:**

- **Exe** (Trigger)
- **Array** (Array)

**< Output Ports:**

- **Trigger** (Trigger)
- **Index** (Number)
- **Result** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/xFKQet)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayIteratorArray"*
**Docs:** [https://cables.gl/op/Ops.Array.ArrayIteratorArray](https://cables.gl/op/Ops.Array.ArrayIteratorArray)

---

### ArrayIteratorNumbers
![ArrayIteratorNumbers op](images/ops/Ops_Array_ArrayIteratorNumbers.svg)

**Full Name:** `Ops.Array.ArrayIteratorNumbers`
**Description:** Loop over every element of an array

**> Input Ports:**

- **Exe** (Trigger)
- **Array** (Array)

**< Output Ports:**

- **Trigger** (Trigger)
- **Index** (Number)
- **Value** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/Ubwk3u)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayIteratorNumbers"*
**Docs:** [https://cables.gl/op/Ops.Array.ArrayIteratorNumbers](https://cables.gl/op/Ops.Array.ArrayIteratorNumbers)

---

### ArrayIteratorObjects
![ArrayIteratorObjects op](images/ops/Ops_Array_ArrayIteratorObjects.svg)

**Full Name:** `Ops.Array.ArrayIteratorObjects`
**Description:** Iterate over an array of objects

**> Input Ports:**

- **Exe** (Trigger)
- **Array** (Array)

**< Output Ports:**

- **Trigger** (Trigger)
- **Finished** (Trigger)
- **Index** (Number)
- **Value** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/UlL2G1)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayIteratorObjects"*
**Docs:** [https://cables.gl/op/Ops.Array.ArrayIteratorObjects](https://cables.gl/op/Ops.Array.ArrayIteratorObjects)

---

### ArrayIteratorStrings
![ArrayIteratorStrings op](images/ops/Ops_Array_ArrayIteratorStrings.svg)

**Full Name:** `Ops.Array.ArrayIteratorStrings`
**Description:** Loop over every element of an array

**> Input Ports:**

- **Exe** (Trigger)
- **Array** (Array)

**< Output Ports:**

- **Trigger** (Trigger)
- **Index** (Number)
- **Value** (String)

**Example Patch:** [Open in Editor](https://cables.gl/edit/53WCcI)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayIteratorStrings"*
**Docs:** [https://cables.gl/op/Ops.Array.ArrayIteratorStrings](https://cables.gl/op/Ops.Array.ArrayIteratorStrings)

---

### ArrayIteratorTextures
![ArrayIteratorTextures op](images/ops/Ops_Array_ArrayIteratorTextures.svg)

**Full Name:** `Ops.Array.ArrayIteratorTextures`
**Description:** Iterate over an array of objects

**> Input Ports:**

- **Exe** (Trigger)
- **Array** (Array)

**< Output Ports:**

- **Trigger** (Trigger)
- **Finished** (Trigger)
- **Index** (Number)
- **Value** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/vS5fjz)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayIteratorTextures"*
**Docs:** [https://cables.gl/op/Ops.Array.ArrayIteratorTextures](https://cables.gl/op/Ops.Array.ArrayIteratorTextures)

---

### ArrayLength_v2
![ArrayLength_v2 op](images/ops/Ops_Array_ArrayLength_v2.svg)

**Full Name:** `Ops.Array.ArrayLength_v2`
**Description:** Number of items in an array

**> Input Ports:**

- **Array** (Array)

**< Output Ports:**

- **Length** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/P4qAz6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayLength_v2"*
**Docs:** [https://cables.gl/op/Ops.Array.ArrayLength_v2](https://cables.gl/op/Ops.Array.ArrayLength_v2)

---

### ArrayLogic
![ArrayLogic op](images/ops/Ops_Array_ArrayLogic.svg)

**Full Name:** `Ops.Array.ArrayLogic`
**Description:** Performs logical comparison operations on a single array of numbers

**> Input Ports:**

- **Array 0** (Array)
- **Comparison Mode Index** (Number: Integer)
- **Number For Comparison** (Number)
- **Value If True** (Number)
- **Value If False** (Number)

**< Output Ports:**

- **Array Result** (Array)
- **Array Length** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/D3DmbJ)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayLogic"*
**Docs:** [https://cables.gl/op/Ops.Array.ArrayLogic](https://cables.gl/op/Ops.Array.ArrayLogic)

---

### ArrayLogicArray
![ArrayLogicArray op](images/ops/Ops_Array_ArrayLogicArray.svg)

**Full Name:** `Ops.Array.ArrayLogicArray`
**Description:** Performs logical comparison operations on two arrays

**> Input Ports:**

- **Array 0** (Array)
- **Array 1** (Array)
- **Value If True** (Number)
- **Value If False** (Number)
- **Comparison Mode Index** (Number: Integer)

**< Output Ports:**

- **Array Result** (Array)
- **Array Length** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/T_-NmJ)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayLogicArray"*
**Docs:** [https://cables.gl/op/Ops.Array.ArrayLogicArray](https://cables.gl/op/Ops.Array.ArrayLogicArray)

---

### ArrayLogicBetween_v2
![ArrayLogicBetween_v2 op](images/ops/Ops_Array_ArrayLogicBetween_v2.svg)

**Full Name:** `Ops.Array.ArrayLogicBetween_v2`
**Description:** If value of array is between min and max then the value is 1 else 0

**> Input Ports:**

- **Array** (Array)
- **Min** (Number)
- **Max** (Number)
- **Pass Value When True** (Number: Boolean)

**< Output Ports:**

- **Result** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/jTqRet)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayLogicBetween_v2"*
**Docs:** [https://cables.gl/op/Ops.Array.ArrayLogicBetween_v2](https://cables.gl/op/Ops.Array.ArrayLogicBetween_v2)

---

### ArrayLookup
![ArrayLookup op](images/ops/Ops_Array_ArrayLookup.svg)

**Full Name:** `Ops.Array.ArrayLookup`
**Description:** Create an array that is filled with values looked up by index from another array

**> Input Ports:**

- **Indices** (Array)
- **Values** (Array)
- **Stride** (Number: Integer)

**< Output Ports:**

- **Result** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/cwJBEe)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayLookup"*
**Docs:** [https://cables.gl/op/Ops.Array.ArrayLookup](https://cables.gl/op/Ops.Array.ArrayLookup)

---

### ArrayMath
![ArrayMath op](images/ops/Ops_Array_ArrayMath.svg)

**Full Name:** `Ops.Array.ArrayMath`
**Description:** Pick from multiple mathematical modes which can all be applied to a single array

**> Input Ports:**

- **Array 0** (Array)
- **Number For Math** (Number)
- **Math Function Index** (Number: Integer)

**< Output Ports:**

- **Array Result** (Array)
- **Array Length** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/7E1hqH)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayMath"*
**Docs:** [https://cables.gl/op/Ops.Array.ArrayMath](https://cables.gl/op/Ops.Array.ArrayMath)

---

### ArrayMathArray
![ArrayMathArray op](images/ops/Ops_Array_ArrayMathArray.svg)

**Full Name:** `Ops.Array.ArrayMathArray`
**Description:** Perform a math operations on two arrays

**> Input Ports:**

- **Array 0** (Array)
- **Array 1** (Array)
- **Math Function Index** (Number: Integer)

**< Output Ports:**

- **Array Result** (Array)
- **Array Length** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/uIYNcn)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayMathArray"*
**Docs:** [https://cables.gl/op/Ops.Array.ArrayMathArray](https://cables.gl/op/Ops.Array.ArrayMathArray)

---

### ArrayMathExpression
![ArrayMathExpression op](images/ops/Ops_Array_ArrayMathExpression.svg)

**Full Name:** `Ops.Array.ArrayMathExpression`
**Description:** Calculate a user-defined mathematical expression

**> Input Ports:**

- **A** (Array)
- **B** (Array)
- **C** (Array)
- **X** (Number)
- **Y** (Number)
- **Z** (Number)
- **Expression** (String)

**< Output Ports:**

- **Result Array** (Array)
- **Array Length** (Number)
- **Expression Valid** (booleanNumber)

**Example Patch:** [Open in Editor](https://cables.gl/edit/_o2Mue)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayMathExpression"*
**Docs:** [https://cables.gl/op/Ops.Array.ArrayMathExpression](https://cables.gl/op/Ops.Array.ArrayMathExpression)

---

### ArrayMathExpressionTrigger
![ArrayMathExpressionTrigger op](images/ops/Ops_Array_ArrayMathExpressionTrigger.svg)

**Full Name:** `Ops.Array.ArrayMathExpressionTrigger`
**Description:** Calculate a user-defined mathematical expression

**> Input Ports:**

- **Update** (Trigger)
- **A** (Array)
- **B** (Array)
- **C** (Array)
- **X** (Number)
- **Y** (Number)
- **Z** (Number)
- **Expression** (String)

**< Output Ports:**

- **Next** (Trigger)
- **Result Array** (Array)
- **Array Length** (Number)
- **Expression Valid** (booleanNumber)

**Example Patch:** [Open in Editor](https://cables.gl/edit/_o2Mue)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayMathExpressionTrigger"*
**Docs:** [https://cables.gl/op/Ops.Array.ArrayMathExpressionTrigger](https://cables.gl/op/Ops.Array.ArrayMathExpressionTrigger)

---

### ArrayMax
![ArrayMax op](images/ops/Ops_Array_ArrayMax.svg)

**Full Name:** `Ops.Array.ArrayMax`
**Description:** Apply a max operation to all values in an array

**> Input Ports:**

- **Array In** (Array)
- **Value** (Number)

**< Output Ports:**

- **Array Out** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/bc0xTn)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayMax"*
**Docs:** [https://cables.gl/op/Ops.Array.ArrayMax](https://cables.gl/op/Ops.Array.ArrayMax)

---

### ArrayMerge_v3
![ArrayMerge_v3 op](images/ops/Ops_Array_ArrayMerge_v3.svg)

**Full Name:** `Ops.Array.ArrayMerge_v3`
**Description:** Merge multiple arrays - in consecutive order

**> Input Ports:**

- **Array 0** (Array)
- **Array 1** (Array)
- **Array 2** (Array)
- **Array 3** (Array)
- **Array 4** (Array)
- **Array 5** (Array)
- **Array 6** (Array)
- **Array 7** (Array)

**< Output Ports:**

- **Result** (Array)
- **Array Length** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/P7siGA)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayMerge_v3"*
**Docs:** [https://cables.gl/op/Ops.Array.ArrayMerge_v3](https://cables.gl/op/Ops.Array.ArrayMerge_v3)

---

### ArrayMergeTrigger
![ArrayMergeTrigger op](images/ops/Ops_Array_ArrayMergeTrigger.svg)

**Full Name:** `Ops.Array.ArrayMergeTrigger`
**Description:** Merge / concatenate arrays by trigger

**> Input Ports:**

- **Merge** (Trigger)
- **Array 0** (Array)
- **Array 1** (Array)
- **Array 2** (Array)
- **Array 3** (Array)
- **Array 4** (Array)
- **Array 5** (Array)
- **Array 6** (Array)
- **Array 7** (Array)
- **Array 8** (Array)
- **Array 9** (Array)
- **Array 10** (Array)
- **Array 11** (Array)

**< Output Ports:**

- **Next** (Trigger)
- **Result** (Array)
- **Array Length** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Array.ArrayMergeTrigger#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayMergeTrigger"*
**Docs:** [https://cables.gl/op/Ops.Array.ArrayMergeTrigger](https://cables.gl/op/Ops.Array.ArrayMergeTrigger)

---

### ArrayMin
![ArrayMin op](images/ops/Ops_Array_ArrayMin.svg)

**Full Name:** `Ops.Array.ArrayMin`
**Description:** Apply a min operation to all values in an array

**> Input Ports:**

- **Array In** (Array)
- **Value** (Number)

**< Output Ports:**

- **Array Out** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/bc0xTn)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayMin"*
**Docs:** [https://cables.gl/op/Ops.Array.ArrayMin](https://cables.gl/op/Ops.Array.ArrayMin)

---

### ArrayModulo
![ArrayModulo op](images/ops/Ops_Array_ArrayModulo.svg)

**Full Name:** `Ops.Array.ArrayModulo`
**Description:** Apply a modulo operation to all values in an array

**> Input Ports:**

- **Array In** (Array)
- **Value** (Number)

**< Output Ports:**

- **Array Out** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/uIYNcn)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayModulo"*
**Docs:** [https://cables.gl/op/Ops.Array.ArrayModulo](https://cables.gl/op/Ops.Array.ArrayModulo)

---

### ArrayMultiply
![ArrayMultiply op](images/ops/Ops_Array_ArrayMultiply.svg)

**Full Name:** `Ops.Array.ArrayMultiply`
**Description:** Multiply every number in an array

**> Input Ports:**

- **In** (Array)
- **Value** (Number)

**< Output Ports:**

- **Result** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/xmNqci)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayMultiply"*
**Docs:** [https://cables.gl/op/Ops.Array.ArrayMultiply](https://cables.gl/op/Ops.Array.ArrayMultiply)

---

### ArrayNumberRamp_v2
![ArrayNumberRamp_v2 op](images/ops/Ops_Array_ArrayNumberRamp_v2.svg)

**Full Name:** `Ops.Array.ArrayNumberRamp_v2`
**Description:** Create an array that contains X numbers between start and end values

**> Input Ports:**

- **Start Value** (Number)
- **End Value** (Number)
- **Entries** (Number: Integer)

**< Output Ports:**

- **Result** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/LfNG9t)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayNumberRamp_v2"*
**Docs:** [https://cables.gl/op/Ops.Array.ArrayNumberRamp_v2](https://cables.gl/op/Ops.Array.ArrayNumberRamp_v2)

---

### ArrayOfArrays
![ArrayOfArrays op](images/ops/Ops_Array_ArrayOfArrays.svg)

**Full Name:** `Ops.Array.ArrayOfArrays`
**Description:** Create an array filled with other arrays

**> Input Ports:**

- **Update** (Trigger)
- **Array 0** (Array)
- **Array 1** (Array)
- **Array 2** (Array)
- **Array 3** (Array)
- **Array 4** (Array)
- **Array 5** (Array)
- **Array 6** (Array)
- **Array 7** (Array)
- **Array 8** (Array)
- **Array 9** (Array)

**< Output Ports:**

- **Result** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/iId8ve)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayOfArrays"*
**Docs:** [https://cables.gl/op/Ops.Array.ArrayOfArrays](https://cables.gl/op/Ops.Array.ArrayOfArrays)

---

### ArrayOfObjectsFilterByKeyValue_v3
![ArrayOfObjectsFilterByKeyValue_v3 op](images/ops/Ops_Array_ArrayOfObjectsFilterByKeyValue_v3.svg)

**Full Name:** `Ops.Array.ArrayOfObjectsFilterByKeyValue_v3`
**Description:** Filter key-value pairs in objects in an array of objects

**> Input Ports:**

- **Array** (Array)
- **Filter Key** (String)
- **Filter Value** (String)
- **Invert Filter** (Number: Boolean)
- **invert result** (discard all objects that have key-value pair)

**< Output Ports:**

- **ArrayOut** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/HFRsU5)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayOfObjectsFilterByKeyValue_v3"*
**Docs:** [https://cables.gl/op/Ops.Array.ArrayOfObjectsFilterByKeyValue_v3](https://cables.gl/op/Ops.Array.ArrayOfObjectsFilterByKeyValue_v3)

---

### ArrayOfObjectsFilterKeys
![ArrayOfObjectsFilterKeys op](images/ops/Ops_Array_ArrayOfObjectsFilterKeys.svg)

**Full Name:** `Ops.Array.ArrayOfObjectsFilterKeys`
**Description:** Remove key-value pairs from objects in an array of objects

**> Input Ports:**

- **Array** (Array)
- **Keys** (String)
- **Seperator** (String)
- **Invert Filter** (Number: Boolean)

**< Output Ports:**

- **Array Out** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/HFRsU5)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayOfObjectsFilterKeys"*
**Docs:** [https://cables.gl/op/Ops.Array.ArrayOfObjectsFilterKeys](https://cables.gl/op/Ops.Array.ArrayOfObjectsFilterKeys)

---

### ArrayOfObjectsToString
![ArrayOfObjectsToString op](images/ops/Ops_Array_ArrayOfObjectsToString.svg)

**Full Name:** `Ops.Array.ArrayOfObjectsToString`
**Description:** Convert an array of objects into readable string format

**> Input Ports:**

- **Array In** (Array)

**< Output Ports:**

- **String** (String)

**Example Patch:** [Open in Editor](https://cables.gl/edit/HFRsU5)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayOfObjectsToString"*
**Docs:** [https://cables.gl/op/Ops.Array.ArrayOfObjectsToString](https://cables.gl/op/Ops.Array.ArrayOfObjectsToString)

---

### ArrayPack
![ArrayPack op](images/ops/Ops_Array_ArrayPack.svg)

**Full Name:** `Ops.Array.ArrayPack`
**Description:** Pack multiple arrays into a new array

**> Input Ports:**

- **Array 0** (Array)
- **Array 1** (Array)
- **Array 2** (Array)
- **Array 3** (Array)
- **Array 4** (Array)
- **Array 5** (Array)
- **Array 6** (Array)
- **Array 7** (Array)

**< Output Ports:**

- **Result** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/fT3AeT)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayPack"*
**Docs:** [https://cables.gl/op/Ops.Array.ArrayPack](https://cables.gl/op/Ops.Array.ArrayPack)

---

### ArrayPack2
![ArrayPack2 op](images/ops/Ops_Array_ArrayPack2.svg)

**Full Name:** `Ops.Array.ArrayPack2`
**Description:** Pack two individual arrays into a new array

**> Input Ports:**

- **Trigger In** (Trigger)
- **Array 1** (Array)
- **Array 2** (Array)

**< Output Ports:**

- **Trigger Out** (Trigger)
- **Array Out** (Array)
- **Array Length** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/WaPiSP)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayPack2"*
**Docs:** [https://cables.gl/op/Ops.Array.ArrayPack2](https://cables.gl/op/Ops.Array.ArrayPack2)

---

### ArrayPack2Simple
![ArrayPack2Simple op](images/ops/Ops_Array_ArrayPack2Simple.svg)

**Full Name:** `Ops.Array.ArrayPack2Simple`
**Description:** Pack 2 individual arrays into an array2 - without needing a trigger

**> Input Ports:**

- **Array 1** (Array)
- **Array 2** (Array)

**< Output Ports:**

- **Array Out** (Array)
- **Num Points** (Number)
- **Array Length** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/Udb6eG)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayPack2Simple"*
**Docs:** [https://cables.gl/op/Ops.Array.ArrayPack2Simple](https://cables.gl/op/Ops.Array.ArrayPack2Simple)

---

### ArrayPack3
![ArrayPack3 op](images/ops/Ops_Array_ArrayPack3.svg)

**Full Name:** `Ops.Array.ArrayPack3`
**Description:** Pack 3 individual arrays into a xyz array

**> Input Ports:**

- **Trigger In** (Trigger)
- **Array 1** (Array)
- **Array 2** (Array)
- **Array 3** (Array)

**< Output Ports:**

- **Trigger Out** (Trigger)
- **Array Out** (Array)
- **Num Points** (Number)
- **Array Length** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/As6p8i)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayPack3"*
**Docs:** [https://cables.gl/op/Ops.Array.ArrayPack3](https://cables.gl/op/Ops.Array.ArrayPack3)

---

### ArrayPack3Simple
![ArrayPack3Simple op](images/ops/Ops_Array_ArrayPack3Simple.svg)

**Full Name:** `Ops.Array.ArrayPack3Simple`
**Description:** Pack 3 individual arrays into an array3 - without needing a trigger

**> Input Ports:**

- **Array 1** (Array)
- **Array 2** (Array)
- **Array 3** (Array)

**< Output Ports:**

- **Array Out** (Array)
- **Num Points** (Number)
- **Array Length** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/Hx09v4)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayPack3Simple"*
**Docs:** [https://cables.gl/op/Ops.Array.ArrayPack3Simple](https://cables.gl/op/Ops.Array.ArrayPack3Simple)

---

### ArrayPack4
![ArrayPack4 op](images/ops/Ops_Array_ArrayPack4.svg)

**Full Name:** `Ops.Array.ArrayPack4`
**Description:** Pack 4 arrays into one array

**> Input Ports:**

- **Trigger In** (Trigger)
- **Array 1** (Array)
- **Array 2** (Array)
- **Array 3** (Array)
- **Array 4** (Array)

**< Output Ports:**

- **Trigger Out** (Trigger)
- **Array Out** (Array)
- **Array Length** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/zgbOqH)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayPack4"*
**Docs:** [https://cables.gl/op/Ops.Array.ArrayPack4](https://cables.gl/op/Ops.Array.ArrayPack4)

---

### ArrayPack4Simple
![ArrayPack4Simple op](images/ops/Ops_Array_ArrayPack4Simple.svg)

**Full Name:** `Ops.Array.ArrayPack4Simple`
**Description:** Pack 3 individual arrays into an array3 - without needing a trigger

**> Input Ports:**

- **Array 1** (Array)
- **Array 2** (Array)
- **Array 3** (Array)
- **Array 4** (Array)

**< Output Ports:**

- **Array Out** (Array)
- **Num Points** (Number)
- **Array Length** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/Hx09v4)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayPack4Simple"*
**Docs:** [https://cables.gl/op/Ops.Array.ArrayPack4Simple](https://cables.gl/op/Ops.Array.ArrayPack4Simple)

---

### ArrayPow
![ArrayPow op](images/ops/Ops_Array_ArrayPow.svg)

**Full Name:** `Ops.Array.ArrayPow`
**Description:** Values below 0 are not accepted. 1 = Array in is unaltered

**> Input Ports:**

- **Array In** (Array)
- **Pow Factor** (Number)

**< Output Ports:**

- **Array Out** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/nakc7z)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayPow"*
**Docs:** [https://cables.gl/op/Ops.Array.ArrayPow](https://cables.gl/op/Ops.Array.ArrayPow)

---

### ArrayPushString
![ArrayPushString op](images/ops/Ops_Array_ArrayPushString.svg)

**Full Name:** `Ops.Array.ArrayPushString`
**Description:** Push/Append a string to the end of an array

**> Input Ports:**

- **Array** (Array)
- **String** (String)

**< Output Ports:**

- **Result** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Array.ArrayPushString#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayPushString"*
**Docs:** [https://cables.gl/op/Ops.Array.ArrayPushString](https://cables.gl/op/Ops.Array.ArrayPushString)

---

### ArrayQuantizer
![ArrayQuantizer op](images/ops/Ops_Array_ArrayQuantizer.svg)

**Full Name:** `Ops.Array.ArrayQuantizer`
**Description:** Quantize input to nearest number in array

**> Input Ports:**

- **Value** (Number)
- **Constraints Array Input** (Array)

**< Output Ports:**

- **Quantized Value** (Number)
- **Quantization Error** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/0yr3cu)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayQuantizer"*
**Docs:** [https://cables.gl/op/Ops.Array.ArrayQuantizer](https://cables.gl/op/Ops.Array.ArrayQuantizer)

---

### ArrayRandomSelection
![ArrayRandomSelection op](images/ops/Ops_Array_ArrayRandomSelection.svg)

**Full Name:** `Ops.Array.ArrayRandomSelection`
**Description:** Extract a definable amount of values from an array

**> Input Ports:**

- **Array** (Array)
- **Elements** (Number: Integer)
- **Seed** (Number)

**< Output Ports:**

- **Result** (Array)
- **Array Length** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/ZYDYpH)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayRandomSelection"*
**Docs:** [https://cables.gl/op/Ops.Array.ArrayRandomSelection](https://cables.gl/op/Ops.Array.ArrayRandomSelection)

---

### ArrayRemoveFalsy
![ArrayRemoveFalsy op](images/ops/Ops_Array_ArrayRemoveFalsy.svg)

**Full Name:** `Ops.Array.ArrayRemoveFalsy`
**Description:** Remove falsy items from an array

**> Input Ports:**

- **Array** (Array)
- **Remove Falsy** (Number: Boolean)

**< Output Ports:**

- **Result Array** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/s6p6iO)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayRemoveFalsy"*
**Docs:** [https://cables.gl/op/Ops.Array.ArrayRemoveFalsy](https://cables.gl/op/Ops.Array.ArrayRemoveFalsy)

---

### ArrayReverse
![ArrayReverse op](images/ops/Ops_Array_ArrayReverse.svg)

**Full Name:** `Ops.Array.ArrayReverse`
**Description:** Reverse an array

**> Input Ports:**

- **Active** (Number: Boolean)

**< Output Ports:**

- **Result** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/UGUp8i)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayReverse"*
**Docs:** [https://cables.gl/op/Ops.Array.ArrayReverse](https://cables.gl/op/Ops.Array.ArrayReverse)

---

### ArrayRound
![ArrayRound op](images/ops/Ops_Array_ArrayRound.svg)

**Full Name:** `Ops.Array.ArrayRound`
**Description:** Round numbers up

**> Input Ports:**

- **In** (Array)
- **Method Index** (Number: Integer)
- **Decimal Places** (Number: Integer)

**< Output Ports:**

- **Result** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/7xdJrG)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayRound"*
**Docs:** [https://cables.gl/op/Ops.Array.ArrayRound](https://cables.gl/op/Ops.Array.ArrayRound)

---

### ArraySetNumber_v3
![ArraySetNumber_v3 op](images/ops/Ops_Array_ArraySetNumber_v3.svg)

**Full Name:** `Ops.Array.ArraySetNumber_v3`
**Description:** Set a number at index in an array

**> Input Ports:**

- **Array** (Array)
- **Index** (Number: Integer)
- **Number** (Number)

**< Output Ports:**

- **Result** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/bJrH16)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArraySetNumber_v3"*
**Docs:** [https://cables.gl/op/Ops.Array.ArraySetNumber_v3](https://cables.gl/op/Ops.Array.ArraySetNumber_v3)

---

### ArraySetString
![ArraySetString op](images/ops/Ops_Array_ArraySetString.svg)

**Full Name:** `Ops.Array.ArraySetString`
**Description:** Set a string at index in an array

**> Input Ports:**

- **Array** (Array)
- **Index** (Number: Integer)
- **Value** (String)

**< Output Ports:**

- **Result** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/b0vNrh)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArraySetString"*
**Docs:** [https://cables.gl/op/Ops.Array.ArraySetString](https://cables.gl/op/Ops.Array.ArraySetString)

---

### ArraySin
![ArraySin op](images/ops/Ops_Array_ArraySin.svg)

**Full Name:** `Ops.Array.ArraySin`
**Description:** Perform a sin or cos operation on the contents of an array

**> Input Ports:**

- **Array In** (Array)
- **Math Function Index** (Number: Integer)
- **Phase** (Number)
- **Frequency** (Number)
- **Amplitude** (Number)

**< Output Ports:**

- **Array Result** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/x1Hqrq)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArraySin"*
**Docs:** [https://cables.gl/op/Ops.Array.ArraySin](https://cables.gl/op/Ops.Array.ArraySin)

---

### ArraySmoothStep
![ArraySmoothStep op](images/ops/Ops_Array_ArraySmoothStep.svg)

**Full Name:** `Ops.Array.ArraySmoothStep`
**Description:** The fancy way of saying it is Perform Hermite interpolation between two values

**> Input Ports:**

- **Array In** (Array)
- **Min** (Number)
- **Max** (Number)

**< Output Ports:**

- **Array Out** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/Cyvm7z)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArraySmoothStep"*
**Docs:** [https://cables.gl/op/Ops.Array.ArraySmoothStep](https://cables.gl/op/Ops.Array.ArraySmoothStep)

---

### ArraySqrt
![ArraySqrt op](images/ops/Ops_Array_ArraySqrt.svg)

**Full Name:** `Ops.Array.ArraySqrt`
**Description:** Return the square root of all values in the array

**> Input Ports:**

- **In** (Array)

**< Output Ports:**

- **Result** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/g7ulSP)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArraySqrt"*
**Docs:** [https://cables.gl/op/Ops.Array.ArraySqrt](https://cables.gl/op/Ops.Array.ArraySqrt)

---

### ArraysToArrayMultiPort
![ArraysToArrayMultiPort op](images/ops/Ops_Array_ArraysToArrayMultiPort.svg)

**Full Name:** `Ops.Array.ArraysToArrayMultiPort`
**Description:** Create an array from multiple string

**> Input Ports:**

- **Arrays_0** (Array)
- **Arrays_1** (Array)
- **Add Port** (Array)

**< Output Ports:**

- **Result** (Array)
- **Num Values** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Array.ArraysToArrayMultiPort#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArraysToArrayMultiPort"*
**Docs:** [https://cables.gl/op/Ops.Array.ArraysToArrayMultiPort](https://cables.gl/op/Ops.Array.ArraysToArrayMultiPort)

---

### ArraySubtract
![ArraySubtract op](images/ops/Ops_Array_ArraySubtract.svg)

**Full Name:** `Ops.Array.ArraySubtract`
**Description:** Subtract one number from all values in an array

**> Input Ports:**

- **Array In** (Array)
- **Value** (Number)

**< Output Ports:**

- **Array Out** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/uIYNcn)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArraySubtract"*
**Docs:** [https://cables.gl/op/Ops.Array.ArraySubtract](https://cables.gl/op/Ops.Array.ArraySubtract)

---

### ArraySum
![ArraySum op](images/ops/Ops_Array_ArraySum.svg)

**Full Name:** `Ops.Array.ArraySum`
**Description:** Add one number to all values in an array

**> Input Ports:**

- **In** (Array)
- **Value** (Number)

**< Output Ports:**

- **Result** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/uIYNcn)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArraySum"*
**Docs:** [https://cables.gl/op/Ops.Array.ArraySum](https://cables.gl/op/Ops.Array.ArraySum)

---

### ArraySumPrevious
![ArraySumPrevious op](images/ops/Ops_Array_ArraySumPrevious.svg)

**Full Name:** `Ops.Array.ArraySumPrevious`
**Description:** Sum up every number in an array with the sum of the previous

**> Input Ports:**

- **Array** (Array)
- **Padding** (Number)

**< Output Ports:**

- **Result** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/udsvLu)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArraySumPrevious"*
**Docs:** [https://cables.gl/op/Ops.Array.ArraySumPrevious](https://cables.gl/op/Ops.Array.ArraySumPrevious)

---

### ArraySumUp
![ArraySumUp op](images/ops/Ops_Array_ArraySumUp.svg)

**Full Name:** `Ops.Array.ArraySumUp`
**Description:** Sum of every number in an array

**> Input Ports:**

- **Array** (Array)

**< Output Ports:**

- **Sum** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/U4M4J5)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArraySumUp"*
**Docs:** [https://cables.gl/op/Ops.Array.ArraySumUp](https://cables.gl/op/Ops.Array.ArraySumUp)

---

### ArraySwizzle
![ArraySwizzle op](images/ops/Ops_Array_ArraySwizzle.svg)

**Full Name:** `Ops.Array.ArraySwizzle`
**Description:** Manage/re-order components of an array (stride)

**> Input Ports:**

- **Array** (Array)

**< Output Ports:**

- **Result** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/MFv6cy)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArraySwizzle"*
**Docs:** [https://cables.gl/op/Ops.Array.ArraySwizzle](https://cables.gl/op/Ops.Array.ArraySwizzle)

---

### ArrayToArrays
![ArrayToArrays op](images/ops/Ops_Array_ArrayToArrays.svg)

**Full Name:** `Ops.Array.ArrayToArrays`
**Description:** Split an array up into an array of arrays

**> Input Ports:**

- **Array** (Array)
- **Stride** (Number: Integer)

**< Output Ports:**

- **Result** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/Bpx7ck)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayToArrays"*
**Docs:** [https://cables.gl/op/Ops.Array.ArrayToArrays](https://cables.gl/op/Ops.Array.ArrayToArrays)

---

### ArrayToByteBuffer
![ArrayToByteBuffer op](images/ops/Ops_Array_ArrayToByteBuffer.svg)

**Full Name:** `Ops.Array.ArrayToByteBuffer`
**Description:** Convert an array to a byte buffer (Uint8ClampedArray)

**> Input Ports:**

- **Array** (Array)

**< Output Ports:**

- **Buffer** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Array.ArrayToByteBuffer#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayToByteBuffer"*
**Docs:** [https://cables.gl/op/Ops.Array.ArrayToByteBuffer](https://cables.gl/op/Ops.Array.ArrayToByteBuffer)

---

### ArrayToString_v3
![ArrayToString_v3 op](images/ops/Ops_Array_ArrayToString_v3.svg)

**Full Name:** `Ops.Array.ArrayToString_v3`
**Description:** Join array values to a string (concat)

**> Input Ports:**

- **Array** (Array)
- **Seperator** (String)
- **New Line** (Number: Boolean)

**< Output Ports:**

- **Result** (String)

**Example Patch:** [Open in Editor](https://cables.gl/edit/U4M4J5)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayToString_v3"*
**Docs:** [https://cables.gl/op/Ops.Array.ArrayToString_v3](https://cables.gl/op/Ops.Array.ArrayToString_v3)

---

### ArrayTrigger
![ArrayTrigger op](images/ops/Ops_Array_ArrayTrigger.svg)

**Full Name:** `Ops.Array.ArrayTrigger`
**Description:** Trigger an array

**> Input Ports:**

- **Exec** (Trigger)
- **Array** (Array)

**< Output Ports:**

- **Trigger Out** (Trigger)
- **Result** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Array.ArrayTrigger#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayTrigger"*
**Docs:** [https://cables.gl/op/Ops.Array.ArrayTrigger](https://cables.gl/op/Ops.Array.ArrayTrigger)

---

### ArrayUnique
![ArrayUnique op](images/ops/Ops_Array_ArrayUnique.svg)

**Full Name:** `Ops.Array.ArrayUnique`
**Description:** Filter an array for duplicate items and returns all unique items in a new array

**> Input Ports:**

- **Array** (Array)
- **Format Index** (Number: Integer)
- **Format** (String)

**< Output Ports:**

- **ArrayOut** (Array)
- **Array Length Out** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/vIQlS-)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayUnique"*
**Docs:** [https://cables.gl/op/Ops.Array.ArrayUnique](https://cables.gl/op/Ops.Array.ArrayUnique)

---

### ArrayUniqueItemInfo
![ArrayUniqueItemInfo op](images/ops/Ops_Array_ArrayUniqueItemInfo.svg)

**Full Name:** `Ops.Array.ArrayUniqueItemInfo`
**Description:** Return information about the count of "duplicates" in an array, as an object

**> Input Ports:**

- **Array** (Array)

**< Output Ports:**

- **ObjectOut** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/72VpS-)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayUniqueItemInfo"*
**Docs:** [https://cables.gl/op/Ops.Array.ArrayUniqueItemInfo](https://cables.gl/op/Ops.Array.ArrayUniqueItemInfo)

---

### ArrayUnpack2
![ArrayUnpack2 op](images/ops/Ops_Array_ArrayUnpack2.svg)

**Full Name:** `Ops.Array.ArrayUnpack2`
**Description:** Unpack an xy array into separate arrays

**> Input Ports:**

- **Array In Xyz** (Array)

**< Output Ports:**

- **Array 1 Out** (Array)
- **Array 2 Out** (Array)
- **Array Lengths** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/N00tci)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayUnpack2"*
**Docs:** [https://cables.gl/op/Ops.Array.ArrayUnpack2](https://cables.gl/op/Ops.Array.ArrayUnpack2)

---

### ArrayUnpack3
![ArrayUnpack3 op](images/ops/Ops_Array_ArrayUnpack3.svg)

**Full Name:** `Ops.Array.ArrayUnpack3`
**Description:** Split an xyz array into 3 individual arrays

**> Input Ports:**

- **Array In Xyz** (Array)

**< Output Ports:**

- **Array 1 Out** (Array)
- **Array 2 Out** (Array)
- **Array 3 Out** (Array)
- **Array Lengths** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/lmn5Og)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayUnpack3"*
**Docs:** [https://cables.gl/op/Ops.Array.ArrayUnpack3](https://cables.gl/op/Ops.Array.ArrayUnpack3)

---

### ArrayUnpack4
![ArrayUnpack4 op](images/ops/Ops_Array_ArrayUnpack4.svg)

**Full Name:** `Ops.Array.ArrayUnpack4`
**Description:** Split an xyzw array into 4 individual arrays

**> Input Ports:**

- **Array In Xyzw** (Array)

**< Output Ports:**

- **Array 1 Out** (Array)
- **Array 2 Out** (Array)
- **Array 3 Out** (Array)
- **Array 4 Out** (Array)
- **Array Lengths** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/vl1N_M)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayUnpack4"*
**Docs:** [https://cables.gl/op/Ops.Array.ArrayUnpack4](https://cables.gl/op/Ops.Array.ArrayUnpack4)

---

### ArrayUnshiftString
![ArrayUnshiftString op](images/ops/Ops_Array_ArrayUnshiftString.svg)

**Full Name:** `Ops.Array.ArrayUnshiftString`
**Description:** Insert/add/unshift a string to the beginning of an array

**> Input Ports:**

- **Array** (Array)
- **String** (String)

**< Output Ports:**

- **Result** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/Ckkk7M)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayUnshiftString"*
**Docs:** [https://cables.gl/op/Ops.Array.ArrayUnshiftString](https://cables.gl/op/Ops.Array.ArrayUnshiftString)

---

### AverageArray
![AverageArray op](images/ops/Ops_Array_AverageArray.svg)

**Full Name:** `Ops.Array.AverageArray`
**Description:** Smooth/average values in an array

**> Input Ports:**

- **Array** (Array)
- **Iterations** (Number: Integer)
- **Mode Index** (Number: Integer)

**< Output Ports:**

- **Smoothed Array** (Array)
- **Array Length** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/t8uSdn)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "AverageArray"*
**Docs:** [https://cables.gl/op/Ops.Array.AverageArray](https://cables.gl/op/Ops.Array.AverageArray)

---

### BoolStateArray
![BoolStateArray op](images/ops/Ops_Array_BoolStateArray.svg)

**Full Name:** `Ops.Array.BoolStateArray`
**Description:** Array filled with `0`, only one can be `1`

**> Input Ports:**

- **Array Length** (Number)
- **Active Index** (Number)
- **Inactive Value** (Number)
- **Active Value** (Number)

**< Output Ports:**

- **State Array** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/9oowlJ)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "BoolStateArray"*
**Docs:** [https://cables.gl/op/Ops.Array.BoolStateArray](https://cables.gl/op/Ops.Array.BoolStateArray)

---

### CopyArray
![CopyArray op](images/ops/Ops_Array_CopyArray.svg)

**Full Name:** `Ops.Array.CopyArray`
**Description:** Copy an array with a trigger, reset to use a default array

**> Input Ports:**

- **Exec** (Trigger)
- **Array** (Array)
- **Reset** (Trigger)
- **Default** (Array)

**< Output Ports:**

- **Result** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/JqSoH-)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "CopyArray"*
**Docs:** [https://cables.gl/op/Ops.Array.CopyArray](https://cables.gl/op/Ops.Array.CopyArray)

---

### CopyArraySimple
![CopyArraySimple op](images/ops/Ops_Array_CopyArraySimple.svg)

**Full Name:** `Ops.Array.CopyArraySimple`
**Description:** Create a copy of an array

**> Input Ports:**

- *Visit [Ops.Array.CopyArraySimple documentation](https://cables.gl/op/Ops.Array.CopyArraySimple) for input port details*

**< Output Ports:**

- **Result** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Array.CopyArraySimple#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "CopyArraySimple"*
**Docs:** [https://cables.gl/op/Ops.Array.CopyArraySimple](https://cables.gl/op/Ops.Array.CopyArraySimple)

---

### CropArray
![CropArray op](images/ops/Ops_Array_CropArray.svg)

**Full Name:** `Ops.Array.CropArray`
**Description:** The array to crop

**> Input Ports:**

- **Source Array** (Array)
- **Start Index** (Number: Integer)
- **New Length** (Number: Integer)

**< Output Ports:**

- **Cropped Array** (Array)
- **Array Length** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/UuuJH-)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "CropArray"*
**Docs:** [https://cables.gl/op/Ops.Array.CropArray](https://cables.gl/op/Ops.Array.CropArray)

---

### CutArray
![CutArray op](images/ops/Ops_Array_CutArray.svg)

**Full Name:** `Ops.Array.CutArray`
**Description:** Remove elements from an array from the beginning and/or the end

**> Input Ports:**

- **Source Array** (Array)
- **Remove From Start** (Number: Integer)
- **Remove From End** (Number: Integer)

**< Output Ports:**

- **Cut Array** (Array)
- **Array Length** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/VbqZTh)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "CutArray"*
**Docs:** [https://cables.gl/op/Ops.Array.CutArray](https://cables.gl/op/Ops.Array.CutArray)

---

### EaseArray
![EaseArray op](images/ops/Ops_Array_EaseArray.svg)

**Full Name:** `Ops.Array.EaseArray`
**Description:** Apply easing curve to numbers in an array

**> Input Ports:**

- **Array** (Array)
- **Min** (Number)
- **Max** (Number)
- **Easing Index** (Number: Integer)

**< Output Ports:**

- **Result Array** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/Mbwkf6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "EaseArray"*
**Docs:** [https://cables.gl/op/Ops.Array.EaseArray](https://cables.gl/op/Ops.Array.EaseArray)

---

### EmptyArray
![EmptyArray op](images/ops/Ops_Array_EmptyArray.svg)

**Full Name:** `Ops.Array.EmptyArray`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Array.EmptyArray) for details*

**> Input Ports:**

- *Visit [Ops.Array.EmptyArray documentation](https://cables.gl/op/Ops.Array.EmptyArray) for input port details*

**< Output Ports:**

- **Result** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Array.EmptyArray#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "EmptyArray"*
**Docs:** [https://cables.gl/op/Ops.Array.EmptyArray](https://cables.gl/op/Ops.Array.EmptyArray)

---

### FillArrayRandomDuplicates_v2
![FillArrayRandomDuplicates_v2 op](images/ops/Ops_Array_FillArrayRandomDuplicates_v2.svg)

**Full Name:** `Ops.Array.FillArrayRandomDuplicates_v2`
**Description:** Fill an array with random duplicates

**> Input Ports:**

- **Array** (Array)
- **Num Elements** (Number: Integer)
- **Random Seed** (Number)

**< Output Ports:**

- **Result** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/z4S3dz)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "FillArrayRandomDuplicates_v2"*
**Docs:** [https://cables.gl/op/Ops.Array.FillArrayRandomDuplicates_v2](https://cables.gl/op/Ops.Array.FillArrayRandomDuplicates_v2)

---

### FilterArray
![FilterArray op](images/ops/Ops_Array_FilterArray.svg)

**Full Name:** `Ops.Array.FilterArray`
**Description:** Compare elements from an array and remove not matching ones

**> Input Ports:**

- **Array** (Array)
- **Stride Index** (Number: Integer)
- **the type of the array** (Array3, Array2, ...)
- **Compare Element Index** (Number: Integer)
- **which element to compare** (see stride)
- **Filter Method Index** (Number: Integer)
- **Compare To** (Number)

**< Output Ports:**

- **Result** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/Z2dVoX)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "FilterArray"*
**Docs:** [https://cables.gl/op/Ops.Array.FilterArray](https://cables.gl/op/Ops.Array.FilterArray)

---

### FilterValidArray
![FilterValidArray op](images/ops/Ops_Array_FilterValidArray.svg)

**Full Name:** `Ops.Array.FilterValidArray`
**Description:** Filter valid arrays

**> Input Ports:**

- **Array** (Array)
- **Invalid When Length Is 0** (Number: Boolean)

**< Output Ports:**

- **Last Valid Array** (Array)
- **Is Valid** (booleanNumber)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Array.FilterValidArray#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "FilterValidArray"*
**Docs:** [https://cables.gl/op/Ops.Array.FilterValidArray](https://cables.gl/op/Ops.Array.FilterValidArray)

---

### FlattenArray
![FlattenArray op](images/ops/Ops_Array_FlattenArray.svg)

**Full Name:** `Ops.Array.FlattenArray`
**Description:** Create a new array with all sub-array elements concatenated into it

**> Input Ports:**

- **Array** (Array)

**< Output Ports:**

- **Result** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/x6HFeT)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "FlattenArray"*
**Docs:** [https://cables.gl/op/Ops.Array.FlattenArray](https://cables.gl/op/Ops.Array.FlattenArray)

---

### FreezeArray
![FreezeArray op](images/ops/Ops_Array_FreezeArray.svg)

**Full Name:** `Ops.Array.FreezeArray`
**Description:** Capture the current input and copy it to the output, even after a reload

**> Input Ports:**

- **Number** (Array)
- **Button** (Trigger)

**< Output Ports:**

- **Frozen Array** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/MuPepX)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "FreezeArray"*
**Docs:** [https://cables.gl/op/Ops.Array.FreezeArray](https://cables.gl/op/Ops.Array.FreezeArray)

---

### GateArray_v2
![GateArray_v2 op](images/ops/Ops_Array_GateArray_v2.svg)

**Full Name:** `Ops.Array.GateArray_v2`
**Description:** Only allow an array through if pass through is true

**> Input Ports:**

- **Array In** (Array)
- **Pass Through** (Number: Boolean)

**< Output Ports:**

- **Array Out** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/gOaDAH)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GateArray_v2"*
**Docs:** [https://cables.gl/op/Ops.Array.GateArray_v2](https://cables.gl/op/Ops.Array.GateArray_v2)

---

### GetValuesFromArrayOfObjects
![GetValuesFromArrayOfObjects op](images/ops/Ops_Array_GetValuesFromArrayOfObjects.svg)

**Full Name:** `Ops.Array.GetValuesFromArrayOfObjects`
**Description:** Get an array of values by key of objects in an array

**> Input Ports:**

- **Array** (Array)
- **Key** (String)
- **Numbers Only** (Number: Boolean)

**< Output Ports:**

- **Result** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/KQGGeT)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GetValuesFromArrayOfObjects"*
**Docs:** [https://cables.gl/op/Ops.Array.GetValuesFromArrayOfObjects](https://cables.gl/op/Ops.Array.GetValuesFromArrayOfObjects)

---

### HSBtoRGBArray
![HSBtoRGBArray op](images/ops/Ops_Array_HSBtoRGBArray.svg)

**Full Name:** `Ops.Array.HSBtoRGBArray`
**Description:** Generate an RGBA array from up to 4 arrays (HSBA)

**> Input Ports:**

- **Trigger Input** (Trigger)
- **In Hue Array** (Array)
- **In Saturation Array** (Array)
- **In Brightness Array** (Array)
- **In Alpha Array** (Array)

**< Output Ports:**

- **Trigger Output** (Trigger)
- **Result Array** (Array)
- **Array Length** (Number)
- **RGBA Tuple Length** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/jFyRM-)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "HSBtoRGBArray"*
**Docs:** [https://cables.gl/op/Ops.Array.HSBtoRGBArray](https://cables.gl/op/Ops.Array.HSBtoRGBArray)

---

### InfoArray
![InfoArray op](images/ops/Ops_Array_InfoArray.svg)

**Full Name:** `Ops.Array.InfoArray`
**Description:** Min, Max and Average value from an array

**> Input Ports:**

- **Array** (Array)

**< Output Ports:**

- **Min** (Number)
- **Max** (Number)
- **Average** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/qySZQx)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "InfoArray"*
**Docs:** [https://cables.gl/op/Ops.Array.InfoArray](https://cables.gl/op/Ops.Array.InfoArray)

---

### InfoArray2
![InfoArray2 op](images/ops/Ops_Array_InfoArray2.svg)

**Full Name:** `Ops.Array.InfoArray2`
**Description:** Min, Max and Average values of an array2

**> Input Ports:**

- **Array** (Array)

**< Output Ports:**

- **Num Items** (Number)
- **Min X** (Number)
- **Max X** (Number)
- **Average X** (Number)
- **Min Y** (Number)
- **Max Y** (Number)
- **Average Y** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Array.InfoArray2#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "InfoArray2"*
**Docs:** [https://cables.gl/op/Ops.Array.InfoArray2](https://cables.gl/op/Ops.Array.InfoArray2)

---

### InfoArray3
![InfoArray3 op](images/ops/Ops_Array_InfoArray3.svg)

**Full Name:** `Ops.Array.InfoArray3`
**Description:** Min, Max and Average values of an array3

**> Input Ports:**

- **Array** (Array)

**< Output Ports:**

- **Num Items** (Number)
- **Min X** (Number)
- **Min Y** (Number)
- **Min Z** (Number)
- **Max X** (Number)
- **Max Y** (Number)
- **Max Z** (Number)
- **Average X** (Number)
- **Average Y** (Number)
- **Average Z** (Number)
- **Center X** (Number)
- **Center Y** (Number)
- **Center Z** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/tg7cRx)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "InfoArray3"*
**Docs:** [https://cables.gl/op/Ops.Array.InfoArray3](https://cables.gl/op/Ops.Array.InfoArray3)

---

### InterpolateArrays
![InterpolateArrays op](images/ops/Ops_Array_InterpolateArrays.svg)

**Full Name:** `Ops.Array.InterpolateArrays`
**Description:** Interpolate between two arrays (lerp) - linear interpolation

**> Input Ports:**

- **Exe** (Trigger)
- **Array 1** (Array)
- **Array 2** (Array)
- **Perc** (Number)

**< Output Ports:**

- **Next** (Trigger)
- **Result** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/qU2GB3)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "InterpolateArrays"*
**Docs:** [https://cables.gl/op/Ops.Array.InterpolateArrays](https://cables.gl/op/Ops.Array.InterpolateArrays)

---

### InterpolateArraysRange
![InterpolateArraysRange op](images/ops/Ops_Array_InterpolateArraysRange.svg)

**Full Name:** `Ops.Array.InterpolateArraysRange`
**Description:** Interpolate between two arrays, only a few numbers at the same time

**> Input Ports:**

- **Exe** (Trigger)
- **Array 1** (Array)
- **Array 2** (Array)
- **Pos** (Number)
- **Width** (Number)
- **Easing Index** (Number: Integer)
- **Reverse** (Number: Boolean)

**< Output Ports:**

- **Next** (Trigger)
- **Result** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/3GIOe6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "InterpolateArraysRange"*
**Docs:** [https://cables.gl/op/Ops.Array.InterpolateArraysRange](https://cables.gl/op/Ops.Array.InterpolateArraysRange)

---

### InterpolateNumbersArray
![InterpolateNumbersArray op](images/ops/Ops_Array_InterpolateNumbersArray.svg)

**Full Name:** `Ops.Array.InterpolateNumbersArray`
**Description:** Interpolate between all values of an array

**> Input Ports:**

- **Index Position** (Number)
- **Array** (Array)

**< Output Ports:**

- **Result** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/dbUc-L)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "InterpolateNumbersArray"*
**Docs:** [https://cables.gl/op/Ops.Array.InterpolateNumbersArray](https://cables.gl/op/Ops.Array.InterpolateNumbersArray)

---

### InterpolateNumbersArray3
![InterpolateNumbersArray3 op](images/ops/Ops_Array_InterpolateNumbersArray3.svg)

**Full Name:** `Ops.Array.InterpolateNumbersArray3`
**Description:** Get interpolated values between the indices of an array3x

**> Input Ports:**

- **Index Position** (Number)
- **Array** (Array)

**< Output Ports:**

- **X** (Number)
- **Y** (Number)
- **Z** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/Oqy2n7)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "InterpolateNumbersArray3"*
**Docs:** [https://cables.gl/op/Ops.Array.InterpolateNumbersArray3](https://cables.gl/op/Ops.Array.InterpolateNumbersArray3)

---

### LissajouseSpline
![LissajouseSpline op](images/ops/Ops_Array_LissajouseSpline.svg)

**Full Name:** `Ops.Array.LissajouseSpline`
**Description:** Generate spline using lissajous formulas

**> Input Ports:**

- **Formula Index** (Number: Integer)
- **A** (Number: Integer)
- **B** (Number: Integer)
- **C** (Number: Integer)
- **D** (Number: Integer)

**< Output Ports:**

- **Result** (Array)
- **Total Points** (Number)
- **Array Length** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/Wa8TS3)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "LissajouseSpline"*
**Docs:** [https://cables.gl/op/Ops.Array.LissajouseSpline](https://cables.gl/op/Ops.Array.LissajouseSpline)

---

### LoopArray3
![LoopArray3 op](images/ops/Ops_Array_LoopArray3.svg)

**Full Name:** `Ops.Array.LoopArray3`
**Description:** Make the 1st and last point of an array the same, good for closing splines and shapes

**> Input Ports:**

- **Array In** (Array)

**< Output Ports:**

- **Array Out** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/-x_dxN)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "LoopArray3"*
**Docs:** [https://cables.gl/op/Ops.Array.LoopArray3](https://cables.gl/op/Ops.Array.LoopArray3)

---

### MapRangeArray
![MapRangeArray op](images/ops/Ops_Array_MapRangeArray.svg)

**Full Name:** `Ops.Array.MapRangeArray`
**Description:** Map values in an array from one range into another.

**> Input Ports:**

- **Array** (Array)
- **Old Min** (Number)
- **Old Max** (Number)
- **New Min** (Number)
- **New Max** (Number)
- **Easing Index** (Number: Integer)

**< Output Ports:**

- **Result** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/ZQI6sU)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "MapRangeArray"*
**Docs:** [https://cables.gl/op/Ops.Array.MapRangeArray](https://cables.gl/op/Ops.Array.MapRangeArray)

---

### NumbersToArrayMultiPort_v2
![NumbersToArrayMultiPort_v2 op](images/ops/Ops_Array_NumbersToArrayMultiPort_v2.svg)

**Full Name:** `Ops.Array.NumbersToArrayMultiPort_v2`
**Description:** Create an array from multiple number inputs

**> Input Ports:**

- **Numbers_0** (Number)
- **Add Port** (Number)

**< Output Ports:**

- **Result** (Array)
- **Num Values** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/mCTLrh)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "NumbersToArrayMultiPort_v2"*
**Docs:** [https://cables.gl/op/Ops.Array.NumbersToArrayMultiPort_v2](https://cables.gl/op/Ops.Array.NumbersToArrayMultiPort_v2)

---

### ObjectIteratorKeys
![ObjectIteratorKeys op](images/ops/Ops_Array_ObjectIteratorKeys.svg)

**Full Name:** `Ops.Array.ObjectIteratorKeys`
**Description:** Iterate over an array of objects

**> Input Ports:**

- **Exe** (Trigger)
- **Array** (Array)

**< Output Ports:**

- **Trigger** (Trigger)
- **Finished** (Trigger)
- **Index** (Number)
- **Value** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Array.ObjectIteratorKeys#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ObjectIteratorKeys"*
**Docs:** [https://cables.gl/op/Ops.Array.ObjectIteratorKeys](https://cables.gl/op/Ops.Array.ObjectIteratorKeys)

---

### PaletteLibrary
![PaletteLibrary op](images/ops/Ops_Array_PaletteLibrary.svg)

**Full Name:** `Ops.Array.PaletteLibrary`
**Description:** Contains a collection of color palettes in groups of 5 in an array

**> Input Ports:**

- *Visit [Ops.Array.PaletteLibrary documentation](https://cables.gl/op/Ops.Array.PaletteLibrary) for input port details*

**< Output Ports:**

- **Palette Array Out** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/zpLrSP)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "PaletteLibrary"*
**Docs:** [https://cables.gl/op/Ops.Array.PaletteLibrary](https://cables.gl/op/Ops.Array.PaletteLibrary)

---

### PerlinArray
![PerlinArray op](images/ops/Ops_Array_PerlinArray.svg)

**Full Name:** `Ops.Array.PerlinArray`
**Description:** Create an array filled with Perlin noise values

**> Input Ports:**

- **Array In X** (Array)
- **Array Time** (Array)
- **Time In Y** (Number)
- **Seed 0-1** (Number)
- **Frequency** (Number)

**< Output Ports:**

- **Array Out** (Array)
- **Array Length Out** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/Vm8fhL)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "PerlinArray"*
**Docs:** [https://cables.gl/op/Ops.Array.PerlinArray](https://cables.gl/op/Ops.Array.PerlinArray)

---

### Phyllotaxis
![Phyllotaxis op](images/ops/Ops_Array_Phyllotaxis.svg)

**Full Name:** `Ops.Array.Phyllotaxis`
**Description:** Coordinate generation like arrangement of leaves in some plants

**> Input Ports:**

- **Render** (Trigger)
- **Num** (Number: Integer)
- **Scale** (Number)
- **Param** (Number)

**< Output Ports:**

- **Coordinates** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/1Pu9Tb)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Phyllotaxis"*
**Docs:** [https://cables.gl/op/Ops.Array.Phyllotaxis](https://cables.gl/op/Ops.Array.Phyllotaxis)

---

### RandomNumbersArray_v4
![RandomNumbersArray_v4 op](images/ops/Ops_Array_RandomNumbersArray_v4.svg)

**Full Name:** `Ops.Array.RandomNumbersArray_v4`
**Description:** Create a random array of 1 to 4 dimensions

**> Input Ports:**

- **Num Values** (Number: Integer)
- **Mode Index** (Number: Integer)
- **Random Seed** (Number)
- **Integer** (Number: Boolean)
- **Min A** (Number)
- **Max A** (Number)
- **Min B** (Number)
- **Max B** (Number)
- **Min C** (Number)
- **Max C** (Number)
- **Min D** (Number)
- **Max D** (Number)

**< Output Ports:**

- **Array Out** (Array)
- **Chunks Amount** (Number)
- **Array Length** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/jmm7N-)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "RandomNumbersArray_v4"*
**Docs:** [https://cables.gl/op/Ops.Array.RandomNumbersArray_v4](https://cables.gl/op/Ops.Array.RandomNumbersArray_v4)

---

### RandomWordsArray
![RandomWordsArray op](images/ops/Ops_Array_RandomWordsArray.svg)

**Full Name:** `Ops.Array.RandomWordsArray`
**Description:** Generate an array filled with random english words

**> Input Ports:**

- **Random Seed** (Number)
- **Content Index** (Number: Integer)

**< Output Ports:**

- **Words** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/VHW78i)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "RandomWordsArray"*
**Docs:** [https://cables.gl/op/Ops.Array.RandomWordsArray](https://cables.gl/op/Ops.Array.RandomWordsArray)

---

### ReduceArray3_v3
![ReduceArray3_v3 op](images/ops/Ops_Array_ReduceArray3_v3.svg)

**Full Name:** `Ops.Array.ReduceArray3_v3`
**Description:** Remove points from an array, e.g. xth points, random, duplicates

**> Input Ports:**

- **Array** (Array)
- **Remove Index** (Number: Integer)
- **Every Xth Item** (Number: Integer)
- **Threshold** (Number)
- **Seed** (Number)

**< Output Ports:**

- **Result Array** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/vgRDeT)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ReduceArray3_v3"*
**Docs:** [https://cables.gl/op/Ops.Array.ReduceArray3_v3](https://cables.gl/op/Ops.Array.ReduceArray3_v3)

---

### ReverseArray3
![ReverseArray3 op](images/ops/Ops_Array_ReverseArray3.svg)

**Full Name:** `Ops.Array.ReverseArray3`
**Description:** Reverse an array with value triplets [x, y, z, ...]

**> Input Ports:**

- **Array** (Array)
- **The Array you want to reverse** (containing triplets)

**< Output Ports:**

- **Reversed Array** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/1QJiVJ)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ReverseArray3"*
**Docs:** [https://cables.gl/op/Ops.Array.ReverseArray3](https://cables.gl/op/Ops.Array.ReverseArray3)

---

### RingBuffer
![RingBuffer op](images/ops/Ops_Array_RingBuffer.svg)

**Full Name:** `Ops.Array.RingBuffer`
**Description:** Array of fixed size, index is automatically incremented and restarts after reaching the end

**> Input Ports:**

- **Value** (Number)
- **Write** (Trigger)
- **Length** (Number: Integer)
- **Reset Index** (Trigger)

**< Output Ports:**

- **Result** (Array)
- **Index** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/NwwS97)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "RingBuffer"*
**Docs:** [https://cables.gl/op/Ops.Array.RingBuffer](https://cables.gl/op/Ops.Array.RingBuffer)

---

### RotateArray
![RotateArray op](images/ops/Ops_Array_RotateArray.svg)

**Full Name:** `Ops.Array.RotateArray`
**Description:** Shift array contents based upon rotate amount

**> Input Ports:**

- **Array In** (Array)
- **Rotate Amount** (Number: Integer)

**< Output Ports:**

- **ArrayOut** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/r7Av7z)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "RotateArray"*
**Docs:** [https://cables.gl/op/Ops.Array.RotateArray](https://cables.gl/op/Ops.Array.RotateArray)

---

### RouteArray
![RouteArray op](images/ops/Ops_Array_RouteArray.svg)

**Full Name:** `Ops.Array.RouteArray`
**Description:** Route an array to an output port

**> Input Ports:**

- **Index** (Number: Integer)
- **Array In** (Array)
- **Default Array** (Array)

**< Output Ports:**

- **Index 0 Array** (Array)
- **Index 1 Array** (Array)
- **Index 2 Array** (Array)
- **Index 3 Array** (Array)
- **Index 4 Array** (Array)
- **Index 5 Array** (Array)
- **Index 6 Array** (Array)
- **Index 7 Array** (Array)
- **Index 8 Array** (Array)
- **Index 9 Array** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/pDYxX8)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "RouteArray"*
**Docs:** [https://cables.gl/op/Ops.Array.RouteArray](https://cables.gl/op/Ops.Array.RouteArray)

---

### SetNumberArray
![SetNumberArray op](images/ops/Ops_Array_SetNumberArray.svg)

**Full Name:** `Ops.Array.SetNumberArray`
**Description:** Change the number of an array at an index

**> Input Ports:**

- **Exe** (Trigger)
- **Array** (Array)
- **Index** (Number: Integer)
- **Value** (Number)

**< Output Ports:**

- **Next** (Trigger)
- **Values** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/WRrXSn)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SetNumberArray"*
**Docs:** [https://cables.gl/op/Ops.Array.SetNumberArray](https://cables.gl/op/Ops.Array.SetNumberArray)

---

### SetNumbersArray3
![SetNumbersArray3 op](images/ops/Ops_Array_SetNumbersArray3.svg)

**Full Name:** `Ops.Array.SetNumbersArray3`
**Description:** Set three values at position index in an array

**> Input Ports:**

- **Exe** (Trigger)
- **Array** (Array)
- **Index** (Number: Integer)
- **Value 1** (Number)
- **Value 2** (Number)
- **Value 3** (Number)

**< Output Ports:**

- **Values** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/El3nlJ)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SetNumbersArray3"*
**Docs:** [https://cables.gl/op/Ops.Array.SetNumbersArray3](https://cables.gl/op/Ops.Array.SetNumbersArray3)

---

### ShuffleArray3_v3
![ShuffleArray3_v3 op](images/ops/Ops_Array_ShuffleArray3_v3.svg)

**Full Name:** `Ops.Array.ShuffleArray3_v3`
**Description:** Shuffle/Randomize the order of an array of triplets

**> Input Ports:**

- **Array3** (Array)
- **Seed** (Number)

**< Output Ports:**

- **Result** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/tbdwsh)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ShuffleArray3_v3"*
**Docs:** [https://cables.gl/op/Ops.Array.ShuffleArray3_v3](https://cables.gl/op/Ops.Array.ShuffleArray3_v3)

---

### ShuffleArray_v3
![ShuffleArray_v3 op](images/ops/Ops_Array_ShuffleArray_v3.svg)

**Full Name:** `Ops.Array.ShuffleArray_v3`
**Description:** Randomize the order of elements inside an array

**> Input Ports:**

- **Array3** (Array)
- **Seed** (Number)

**< Output Ports:**

- **Result** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/doUssh)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ShuffleArray_v3"*
**Docs:** [https://cables.gl/op/Ops.Array.ShuffleArray_v3](https://cables.gl/op/Ops.Array.ShuffleArray_v3)

---

### SimplexArray
![SimplexArray op](images/ops/Ops_Array_SimplexArray.svg)

**Full Name:** `Ops.Array.SimplexArray`
**Description:** Create an array filled with Simplex noise values (Range: -1, 1)

**> Input Ports:**

- **Array In X** (Array)
- **Array Time** (Array)
- **Time In Y** (Number)
- **Seed 0-1** (Number)
- **Frequency** (Number)

**< Output Ports:**

- **Array Out** (Array)
- **Array Length Out** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/rNAlhL)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SimplexArray"*
**Docs:** [https://cables.gl/op/Ops.Array.SimplexArray](https://cables.gl/op/Ops.Array.SimplexArray)

---

### SmoothArray
![SmoothArray op](images/ops/Ops_Array_SmoothArray.svg)

**Full Name:** `Ops.Array.SmoothArray`
**Description:** Smooth out changes in values of an array

**> Input Ports:**

- **Execute** (Trigger)
- **Array In** (Array)
- **Inc Factor** (Number)
- **Dec Factor** (Number)

**< Output Ports:**

- **Next** (Trigger)
- **Array Out** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/BgtGZK)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SmoothArray"*
**Docs:** [https://cables.gl/op/Ops.Array.SmoothArray](https://cables.gl/op/Ops.Array.SmoothArray)

---

### SortArray
![SortArray op](images/ops/Ops_Array_SortArray.svg)

**Full Name:** `Ops.Array.SortArray`
**Description:** Sort an array of numbers with one of two modes - ascending or descending

**> Input Ports:**

- **Array To Sort** (Array)

**< Output Ports:**

- **Sorted Array** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/M2f7RJ)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SortArray"*
**Docs:** [https://cables.gl/op/Ops.Array.SortArray](https://cables.gl/op/Ops.Array.SortArray)

---

### SortArray3
![SortArray3 op](images/ops/Ops_Array_SortArray3.svg)

**Full Name:** `Ops.Array.SortArray3`
**Description:** Sort an array with the lowest values of the selected component.

**> Input Ports:**

- **Array** (Array)
- **What Index** (Number: Integer)

**< Output Ports:**

- **Result** (Array)
- **The sorted array** (new array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/QS8qVJ)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SortArray3"*
**Docs:** [https://cables.gl/op/Ops.Array.SortArray3](https://cables.gl/op/Ops.Array.SortArray3)

---

### SortArrayOfOjects
![SortArrayOfOjects op](images/ops/Ops_Array_SortArrayOfOjects.svg)

**Full Name:** `Ops.Array.SortArrayOfOjects`
**Description:** Sort an array of objects by the values of a key

**> Input Ports:**

- **Array** (Array)
- **Key** (String)
- **Reverse** (Number: Boolean)

**< Output Ports:**

- **Result** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/shtaz1)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SortArrayOfOjects"*
**Docs:** [https://cables.gl/op/Ops.Array.SortArrayOfOjects](https://cables.gl/op/Ops.Array.SortArrayOfOjects)

---

### SortArrayWithIndices_v2
![SortArrayWithIndices_v2 op](images/ops/Ops_Array_SortArrayWithIndices_v2.svg)

**Full Name:** `Ops.Array.SortArrayWithIndices_v2`
**Description:** Sort an array of numbers and also get sorted indices

**> Input Ports:**

- **Array To Sort** (Array)
- **Sorting Mode Index** (Number: Integer)

**< Output Ports:**

- **Sorted Array** (Array)
- **Sorted Indices** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Array.SortArrayWithIndices_v2#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SortArrayWithIndices_v2"*
**Docs:** [https://cables.gl/op/Ops.Array.SortArrayWithIndices_v2](https://cables.gl/op/Ops.Array.SortArrayWithIndices_v2)

---

### SplineLengthArray3
![SplineLengthArray3 op](images/ops/Ops_Array_SplineLengthArray3.svg)

**Full Name:** `Ops.Array.SplineLengthArray3`
**Description:** Return a number with the total distance between the points/items in an array3

**> Input Ports:**

- **Array3x** (Array)
- **Calculate** (Trigger)

**< Output Ports:**

- **Length** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/uOzMH7)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SplineLengthArray3"*
**Docs:** [https://cables.gl/op/Ops.Array.SplineLengthArray3](https://cables.gl/op/Ops.Array.SplineLengthArray3)

---

### SplinesToLineStripArray
![SplinesToLineStripArray op](images/ops/Ops_Array_SplinesToLineStripArray.svg)

**Full Name:** `Ops.Array.SplinesToLineStripArray`
**Description:** Convert an array of splines to one "line stripped" array

**> Input Ports:**

- **Array** (Array)

**< Output Ports:**

- **Result** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/_UiSmX)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SplinesToLineStripArray"*
**Docs:** [https://cables.gl/op/Ops.Array.SplinesToLineStripArray](https://cables.gl/op/Ops.Array.SplinesToLineStripArray)

---

### StringToArray_v2
![StringToArray_v2 op](images/ops/Ops_Array_StringToArray_v2.svg)

**Full Name:** `Ops.Array.StringToArray_v2`
**Description:** Parse a string into an array (create, split string, stringToArray)

**> Input Ports:**

- **Text** (String)
- **Separator** (String)
- **Numbers** (Number: Boolean)
- **Trim** (Number: Boolean)
- **Split Lines** (Number: Boolean)

**< Output Ports:**

- **Array** (Array)
- **Parsed** (Trigger)
- **Length** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/U4M4J5)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "StringToArray_v2"*
**Docs:** [https://cables.gl/op/Ops.Array.StringToArray_v2](https://cables.gl/op/Ops.Array.StringToArray_v2)

---

### StringToCharArray
![StringToCharArray op](images/ops/Ops_Array_StringToCharArray.svg)

**Full Name:** `Ops.Array.StringToCharArray`
**Description:** Turn a string into an array of single characters or ASCII numbers

**> Input Ports:**

- **String** (String)
- **Convert To Numbers** (Number: Boolean)

**< Output Ports:**

- **Array Out** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/30a1rn)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "StringToCharArray"*
**Docs:** [https://cables.gl/op/Ops.Array.StringToCharArray](https://cables.gl/op/Ops.Array.StringToCharArray)

---

### StringToLineNumberArray
![StringToLineNumberArray op](images/ops/Ops_Array_StringToLineNumberArray.svg)

**Full Name:** `Ops.Array.StringToLineNumberArray`
**Description:** Output an array containing a line number for every character

**> Input Ports:**

- **String** (String)

**< Output Ports:**

- **Result** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Array.StringToLineNumberArray#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "StringToLineNumberArray"*
**Docs:** [https://cables.gl/op/Ops.Array.StringToLineNumberArray](https://cables.gl/op/Ops.Array.StringToLineNumberArray)

---

### SubdivideArray1
![SubdivideArray1 op](images/ops/Ops_Array_SubdivideArray1.svg)

**Full Name:** `Ops.Array.SubdivideArray1`
**Description:** For subdividing splines, smoothing lines using cubic bezier interpolation

**> Input Ports:**

- **Points** (Array)
- **Num Subdivs** (Number: Integer)
- **Smooth** (Number: Boolean)

**< Output Ports:**

- **Result** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/RJiCqH)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SubdivideArray1"*
**Docs:** [https://cables.gl/op/Ops.Array.SubdivideArray1](https://cables.gl/op/Ops.Array.SubdivideArray1)

---

### SwitchArray
![SwitchArray op](images/ops/Ops_Array_SwitchArray.svg)

**Full Name:** `Ops.Array.SwitchArray`
**Description:** Switch between multiple arrays

**> Input Ports:**

- **Index** (Number: Integer)
- **Array 0** (Array)
- **Array 1** (Array)
- **Array 2** (Array)
- **Array 3** (Array)
- **Array 4** (Array)
- **Array 5** (Array)
- **Array 6** (Array)
- **Array 7** (Array)
- **Array 8** (Array)
- **Array 9** (Array)

**< Output Ports:**

- **Result** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/4J2o8i)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SwitchArray"*
**Docs:** [https://cables.gl/op/Ops.Array.SwitchArray](https://cables.gl/op/Ops.Array.SwitchArray)

---

### SwitchArrayMultiPort_v2
![SwitchArrayMultiPort_v2 op](images/ops/Ops_Array_SwitchArrayMultiPort_v2.svg)

**Full Name:** `Ops.Array.SwitchArrayMultiPort_v2`
**Description:** Switch between multiple input arrays

**> Input Ports:**

- **Index** (Number: Integer)
- **Arrays_0** (Array)
- **Add Port** (Array)

**< Output Ports:**

- **Number** (Array)
- **Num Values** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/L7sKrh)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SwitchArrayMultiPort_v2"*
**Docs:** [https://cables.gl/op/Ops.Array.SwitchArrayMultiPort_v2](https://cables.gl/op/Ops.Array.SwitchArrayMultiPort_v2)

---

### SwitchArrayOnTrigger
![SwitchArrayOnTrigger op](images/ops/Ops_Array_SwitchArrayOnTrigger.svg)

**Full Name:** `Ops.Array.SwitchArrayOnTrigger`
**Description:** Switch between multiple arrays on trigger

**> Input Ports:**

- **Trigger 1** (Trigger)
- **Array 1** (Array)
- **Trigger 2** (Trigger)
- **Array 2** (Array)
- **Trigger 3** (Trigger)
- **Array 3** (Array)
- **Trigger 4** (Trigger)
- **Array 4** (Array)
- **Trigger 5** (Trigger)
- **Array 5** (Array)
- **Trigger 6** (Trigger)
- **Array 6** (Array)
- **Trigger 7** (Trigger)
- **Array 7** (Array)
- **Trigger 8** (Trigger)
- **Array 8** (Array)

**< Output Ports:**

- **Out Array** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Array.SwitchArrayOnTrigger#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SwitchArrayOnTrigger"*
**Docs:** [https://cables.gl/op/Ops.Array.SwitchArrayOnTrigger](https://cables.gl/op/Ops.Array.SwitchArrayOnTrigger)

---

### TextureBufferArray
![TextureBufferArray op](images/ops/Ops_Array_TextureBufferArray.svg)

**Full Name:** `Ops.Array.TextureBufferArray`
**Description:** Store various textures in an array, starts at the beginning again when end reached

**> Input Ports:**

- **Write** (Trigger)
- **Texture** (Object:Texture)
- **Num** (Number: Integer)
- **The size of the ring buffer** (how many textures it can hold)
- **Order** (Number: Boolean)
- **Clear** (Number: Boolean)

**< Output Ports:**

- **Result** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Array.TextureBufferArray#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TextureBufferArray"*
**Docs:** [https://cables.gl/op/Ops.Array.TextureBufferArray](https://cables.gl/op/Ops.Array.TextureBufferArray)

---

### WeaveArrays
![WeaveArrays op](images/ops/Ops_Array_WeaveArrays.svg)

**Full Name:** `Ops.Array.WeaveArrays`
**Description:** Weave two arrays together (combine, join, merge)

**> Input Ports:**

- **Array 1** (Array)
- **Array 2** (Array)
- **Chunk Size** (Number)

**< Output Ports:**

- **Combined Array** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/HSGq8i)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "WeaveArrays"*
**Docs:** [https://cables.gl/op/Ops.Array.WeaveArrays](https://cables.gl/op/Ops.Array.WeaveArrays)

---

