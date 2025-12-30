# Ops.Json

*Part of the [All Operators Reference](13-_AllOps.md)*

---

## Ops.Json

### ArrayOfObjectsMultiPort_v2
![ArrayOfObjectsMultiPort_v2 op](images/ops/Ops_Json_ArrayOfObjectsMultiPort_v2.svg)

**Full Name:** `Ops.Json.ArrayOfObjectsMultiPort_v2`
**Description:** create an array with multiple objects

**> Input Ports:**
- **Objects_0** (Object)
- **Add Port** (Object)

**< Output Ports:**
- **Array** (Array)
- **Num Values** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Json.ArrayOfObjectsMultiPort_v2#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayOfObjectsMultiPort_v2"*
**Docs:** [https://cables.gl/op/Ops.Json.ArrayOfObjectsMultiPort_v2](https://cables.gl/op/Ops.Json.ArrayOfObjectsMultiPort_v2)

---

### CopyObject
![CopyObject op](images/ops/Ops_Json_CopyObject.svg)

**Full Name:** `Ops.Json.CopyObject`
**Description:** Creates a copy of a JSON object

**> Input Ports:**
- *Visit [Ops.Json.CopyObject documentation](https://cables.gl/op/Ops.Json.CopyObject) for input port details*

**< Output Ports:**
- **Valid** (booleanNumber)

**Example Patch:** [Open in Editor](https://cables.gl/edit/xJCXJK)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "CopyObject"*
**Docs:** [https://cables.gl/op/Ops.Json.CopyObject](https://cables.gl/op/Ops.Json.CopyObject)

---

### CsvArray
![CsvArray op](images/ops/Ops_Json_CsvArray.svg)

**Full Name:** `Ops.Json.CsvArray`
**Description:** parse CSV files as array

**> Input Ports:**
- **File** (String)

**< Output Ports:**
- **Result** (Array)
- **Num Items** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/UlL2G1)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "CsvArray"*
**Docs:** [https://cables.gl/op/Ops.Json.CsvArray](https://cables.gl/op/Ops.Json.CsvArray)

---

### CsvColumnArray_v2
![CsvColumnArray_v2 op](images/ops/Ops_Json_CsvColumnArray_v2.svg)

**Full Name:** `Ops.Json.CsvColumnArray_v2`
**Description:** get all values of a CSV column as array of strings

**> Input Ports:**
- **Column Name** (String)
- **CSV Array** (Array)
- **Numbers** (Number: Boolean)

**< Output Ports:**
- **Result** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Json.CsvColumnArray_v2#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "CsvColumnArray_v2"*
**Docs:** [https://cables.gl/op/Ops.Json.CsvColumnArray_v2](https://cables.gl/op/Ops.Json.CsvColumnArray_v2)

---

### EmptyObject
![EmptyObject op](images/ops/Ops_Json_EmptyObject.svg)

**Full Name:** `Ops.Json.EmptyObject`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Json.EmptyObject) for details*

**> Input Ports:**
- *Visit [Ops.Json.EmptyObject documentation](https://cables.gl/op/Ops.Json.EmptyObject) for input port details*

**< Output Ports:**
- **Result** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/piMxeG)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "EmptyObject"*
**Docs:** [https://cables.gl/op/Ops.Json.EmptyObject](https://cables.gl/op/Ops.Json.EmptyObject)

---

### FilterValidObject
![FilterValidObject op](images/ops/Ops_Json_FilterValidObject.svg)

**Full Name:** `Ops.Json.FilterValidObject`
**Description:** Filter valid objects

**> Input Ports:**
- **Object** (Object)

**< Output Ports:**
- **Last Valid Object** (Object)
- **Is Valid** (booleanNumber)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Json.FilterValidObject#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "FilterValidObject"*
**Docs:** [https://cables.gl/op/Ops.Json.FilterValidObject](https://cables.gl/op/Ops.Json.FilterValidObject)

---

### GateObject
![GateObject op](images/ops/Ops_Json_GateObject.svg)

**Full Name:** `Ops.Json.GateObject`
**Description:** Will only allow an Object to to be output if the the pass through parameter evaluates to true

**> Input Ports:**
- **Object In** (Object)
- **Pass Through** (Number: Boolean)
- **Only Valid Objects** (Number: Boolean)

**< Output Ports:**
- **Object Out** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Json.GateObject#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GateObject"*
**Docs:** [https://cables.gl/op/Ops.Json.GateObject](https://cables.gl/op/Ops.Json.GateObject)

---

### HttpFetchStream
![HttpFetchStream op](images/ops/Ops_Json_HttpFetchStream.svg)

**Full Name:** `Ops.Json.HttpFetchStream`
**Description:** HttpRequest/Fetch Streaming

**> Input Ports:**
- **Fetch Response** (Object)

**< Output Ports:**
- **Result** (Object)
- **Received Result** (Trigger)
- **Started** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Json.HttpFetchStream#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "HttpFetchStream"*
**Docs:** [https://cables.gl/op/Ops.Json.HttpFetchStream](https://cables.gl/op/Ops.Json.HttpFetchStream)

---

### HttpRequest_v4
![HttpRequest_v4 op](images/ops/Ops_Json_HttpRequest_v4.svg)

**Full Name:** `Ops.Json.HttpRequest_v4`
**Description:** Request a json file and output an object (ajax, url, json,fetch)

**> Input Ports:**
- **URL** (String)
- **HTTP Method Index** (Number: Integer)
- **Request Body** (String)
- **Content-Type** (String)
- **the content type of the body sent** (if any)
- **Send Credentials** (Number: Boolean)
- **Headers** (Object)
- **Auto Request** (Number: Boolean)
- **trigger the request on any value change** (or on pagereload)
- **Empty Output On Change** (Number: Boolean)
- **Retry On Error** (Number: Boolean)
- **Reload** (Trigger)

**< Output Ports:**
- **Response Json Object** (Object)
- **Response String** (String)
- **Response Data Url** (String)
- **Status Code** (Number)
- **Is Loading** (booleanNumber)
- **Has Error** (booleanNumber)
- **Error** (String)
- **Duration MS** (Number)
- **Fetch Response** (Object)
- **Loaded** (Trigger)

**Example Patch:** [Open in Editor](https://dev.cables.gl/edit/gSRYVQ)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "HttpRequest_v4"*
**Docs:** [https://cables.gl/op/Ops.Json.HttpRequest_v4](https://cables.gl/op/Ops.Json.HttpRequest_v4)

---

### Object
![Object op](images/ops/Ops_Json_Object.svg)

**Full Name:** `Ops.Json.Object`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Json.Object) for details*

**> Input Ports:**
- **Object** (Object)

**< Output Ports:**
- **Result** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Json.Object#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Object"*
**Docs:** [https://cables.gl/op/Ops.Json.Object](https://cables.gl/op/Ops.Json.Object)

---

### ObjectDeleteKey
![ObjectDeleteKey op](images/ops/Ops_Json_ObjectDeleteKey.svg)

**Full Name:** `Ops.Json.ObjectDeleteKey`
**Description:** Remove a Property from an Object by Key

**> Input Ports:**
- **Object** (Object)
- **Key** (String)

**< Output Ports:**
- **Object Result** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/piMxeG)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ObjectDeleteKey"*
**Docs:** [https://cables.gl/op/Ops.Json.ObjectDeleteKey](https://cables.gl/op/Ops.Json.ObjectDeleteKey)

---

### ObjectFilterContentByKey
![ObjectFilterContentByKey op](images/ops/Ops_Json_ObjectFilterContentByKey.svg)

**Full Name:** `Ops.Json.ObjectFilterContentByKey`
**Description:** filter values from an object if key starts with input string

**> Input Ports:**
- **Object** (Object)
- **Name** (String)
- **Remove Null** (Number: Boolean)

**< Output Ports:**
- **Result** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/KEDALu)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ObjectFilterContentByKey"*
**Docs:** [https://cables.gl/op/Ops.Json.ObjectFilterContentByKey](https://cables.gl/op/Ops.Json.ObjectFilterContentByKey)

---

### ObjectFunnel
![ObjectFunnel op](images/ops/Ops_Json_ObjectFunnel.svg)

**Full Name:** `Ops.Json.ObjectFunnel`
**Description:** outputs the last changed object

**> Input Ports:**
- **Object1** (Object)
- **Object2** (Object)
- **Object3** (Object)
- **Object4** (Object)
- **Object5** (Object)

**< Output Ports:**
- **Out Object** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Json.ObjectFunnel#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ObjectFunnel"*
**Docs:** [https://cables.gl/op/Ops.Json.ObjectFunnel](https://cables.gl/op/Ops.Json.ObjectFunnel)

---

### ObjectGetArray_v2
![ObjectGetArray_v2 op](images/ops/Ops_Json_ObjectGetArray_v2.svg)

**Full Name:** `Ops.Json.ObjectGetArray_v2`
**Description:** Returns an array from a JSON-object

**> Input Ports:**
- **Data** (Object)
- **Key** (String)

**< Output Ports:**
- **Result** (Array)
- **Length** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/yU2Pet)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ObjectGetArray_v2"*
**Docs:** [https://cables.gl/op/Ops.Json.ObjectGetArray_v2](https://cables.gl/op/Ops.Json.ObjectGetArray_v2)

---

### ObjectGetNumber_v2
![ObjectGetNumber_v2 op](images/ops/Ops_Json_ObjectGetNumber_v2.svg)

**Full Name:** `Ops.Json.ObjectGetNumber_v2`
**Description:** Get a number from an object

**> Input Ports:**
- **Data** (Object)
- **Key** (String)

**< Output Ports:**
- **Result** (Number)
- **Found** (booleanNumber)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Json.ObjectGetNumber_v2#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ObjectGetNumber_v2"*
**Docs:** [https://cables.gl/op/Ops.Json.ObjectGetNumber_v2](https://cables.gl/op/Ops.Json.ObjectGetNumber_v2)

---

### ObjectGetObject_v2
![ObjectGetObject_v2 op](images/ops/Ops_Json_ObjectGetObject_v2.svg)

**Full Name:** `Ops.Json.ObjectGetObject_v2`
**Description:** Get an object from an object

**> Input Ports:**
- **Object** (Object)
- **Key** (String)

**< Output Ports:**
- **Result** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Json.ObjectGetObject_v2#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ObjectGetObject_v2"*
**Docs:** [https://cables.gl/op/Ops.Json.ObjectGetObject_v2](https://cables.gl/op/Ops.Json.ObjectGetObject_v2)

---

### ObjectGetString_v2
![ObjectGetString_v2 op](images/ops/Ops_Json_ObjectGetString_v2.svg)

**Full Name:** `Ops.Json.ObjectGetString_v2`
**Description:** Get string from object by key

**> Input Ports:**
- **Data** (Object)
- **Key** (String)

**< Output Ports:**
- **Result** (String)
- **Found** (booleanNumber)

**Example Patch:** [Open in Editor](https://cables.gl/edit/Sn0k9Q)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ObjectGetString_v2"*
**Docs:** [https://cables.gl/op/Ops.Json.ObjectGetString_v2](https://cables.gl/op/Ops.Json.ObjectGetString_v2)

---

### ObjectIsNull
![ObjectIsNull op](images/ops/Ops_Json_ObjectIsNull.svg)

**Full Name:** `Ops.Json.ObjectIsNull`
**Description:** check if object is null or a valid object

**> Input Ports:**
- **Object** (Object)

**< Output Ports:**
- **Result** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Json.ObjectIsNull#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ObjectIsNull"*
**Docs:** [https://cables.gl/op/Ops.Json.ObjectIsNull](https://cables.gl/op/Ops.Json.ObjectIsNull)

---

### ObjectKeys
![ObjectKeys op](images/ops/Ops_Json_ObjectKeys.svg)

**Full Name:** `Ops.Json.ObjectKeys`
**Description:** returns an array of strings, which contain the keys of the object

**> Input Ports:**
- **Object** (Object)

**< Output Ports:**
- **Keys** (Array)
- **Num Keys** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/3pkLji)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ObjectKeys"*
**Docs:** [https://cables.gl/op/Ops.Json.ObjectKeys](https://cables.gl/op/Ops.Json.ObjectKeys)

---

### ObjectMerge
![ObjectMerge op](images/ops/Ops_Json_ObjectMerge.svg)

**Full Name:** `Ops.Json.ObjectMerge`
**Description:** merge key+values of two objects

**> Input Ports:**
- **Object 1** (Object)
- **Object 2** (Object)

**< Output Ports:**
- **Object Result** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/LNJHeG)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ObjectMerge"*
**Docs:** [https://cables.gl/op/Ops.Json.ObjectMerge](https://cables.gl/op/Ops.Json.ObjectMerge)

---

### ObjectOr
![ObjectOr op](images/ops/Ops_Json_ObjectOr.svg)

**Full Name:** `Ops.Json.ObjectOr`
**Description:** result is first connected valid object

**> Input Ports:**
- **Object 1** (Object)
- **Object 2** (Object)
- **Object 3** (Object)
- **Object 4** (Object)
- **Object 5** (Object)
- **Object 6** (Object)
- **Object 7** (Object)
- **Object 8** (Object)

**< Output Ports:**
- **Result** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Json.ObjectOr#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ObjectOr"*
**Docs:** [https://cables.gl/op/Ops.Json.ObjectOr](https://cables.gl/op/Ops.Json.ObjectOr)

---

### ObjectRecorder
![ObjectRecorder op](images/ops/Ops_Json_ObjectRecorder.svg)

**Full Name:** `Ops.Json.ObjectRecorder`
**Description:** record objects and download as json file

**> Input Ports:**
- **Exec** (Trigger)
- **Reset** (Trigger)
- **Download** (Trigger)
- **Object** (Object)

**< Output Ports:**
- **Result** (Array)
- **Num Objects** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Json.ObjectRecorder#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ObjectRecorder"*
**Docs:** [https://cables.gl/op/Ops.Json.ObjectRecorder](https://cables.gl/op/Ops.Json.ObjectRecorder)

---

### ObjectSetArray_v2
![ObjectSetArray_v2 op](images/ops/Ops_Json_ObjectSetArray_v2.svg)

**Full Name:** `Ops.Json.ObjectSetArray_v2`
**Description:** Set array by key in an object

**> Input Ports:**
- **Object** (Object)
- **Key** (String)
- **Value** (Array)

**< Output Ports:**
- **Result Object** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Json.ObjectSetArray_v2#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ObjectSetArray_v2"*
**Docs:** [https://cables.gl/op/Ops.Json.ObjectSetArray_v2](https://cables.gl/op/Ops.Json.ObjectSetArray_v2)

---

### ObjectSetBool
![ObjectSetBool op](images/ops/Ops_Json_ObjectSetBool.svg)

**Full Name:** `Ops.Json.ObjectSetBool`
**Description:** set number at key in an object

**> Input Ports:**
- **Object** (Object)
- **Key** (String)
- **Boolean** (Number: Boolean)

**< Output Ports:**
- **Result Object** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/w63Au1)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ObjectSetBool"*
**Docs:** [https://cables.gl/op/Ops.Json.ObjectSetBool](https://cables.gl/op/Ops.Json.ObjectSetBool)

---

### ObjectSetColorArray
![ObjectSetColorArray op](images/ops/Ops_Json_ObjectSetColorArray.svg)

**Full Name:** `Ops.Json.ObjectSetColorArray`
**Description:** Set rgba array by key in an object

**> Input Ports:**
- **Object** (Object)
- **Key** (String)
- **R** (Number)
- **G** (Number)
- **B** (Number)
- **A** (Number)

**< Output Ports:**
- **Result Object** (Object)
- **Out R** (Number)
- **Out G** (Number)
- **Out B** (Number)
- **Out A** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/joA-JK)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ObjectSetColorArray"*
**Docs:** [https://cables.gl/op/Ops.Json.ObjectSetColorArray](https://cables.gl/op/Ops.Json.ObjectSetColorArray)

---

### ObjectSetNumber_v2
![ObjectSetNumber_v2 op](images/ops/Ops_Json_ObjectSetNumber_v2.svg)

**Full Name:** `Ops.Json.ObjectSetNumber_v2`
**Description:** set number at key in an object

**> Input Ports:**
- **Object** (Object)
- **Key** (String)
- **Number** (Number)

**< Output Ports:**
- **Result Object** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Json.ObjectSetNumber_v2#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ObjectSetNumber_v2"*
**Docs:** [https://cables.gl/op/Ops.Json.ObjectSetNumber_v2](https://cables.gl/op/Ops.Json.ObjectSetNumber_v2)

---

### ObjectSetObject_v2
![ObjectSetObject_v2 op](images/ops/Ops_Json_ObjectSetObject_v2.svg)

**Full Name:** `Ops.Json.ObjectSetObject_v2`
**Description:** set object as value in an object

**> Input Ports:**
- **Object** (Object)
- **Key** (String)
- **Object Value** (Object)

**< Output Ports:**
- **Result Object** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/7X58nR)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ObjectSetObject_v2"*
**Docs:** [https://cables.gl/op/Ops.Json.ObjectSetObject_v2](https://cables.gl/op/Ops.Json.ObjectSetObject_v2)

---

### ObjectSetString_v2
![ObjectSetString_v2 op](images/ops/Ops_Json_ObjectSetString_v2.svg)

**Full Name:** `Ops.Json.ObjectSetString_v2`
**Description:** set a string value by key in an object

**> Input Ports:**
- **Object** (Object)
- **Key** (String)
- **Value** (String)

**< Output Ports:**
- **Result Object** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Json.ObjectSetString_v2#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ObjectSetString_v2"*
**Docs:** [https://cables.gl/op/Ops.Json.ObjectSetString_v2](https://cables.gl/op/Ops.Json.ObjectSetString_v2)

---

### ObjectStringify_v2
![ObjectStringify_v2 op](images/ops/Ops_Json_ObjectStringify_v2.svg)

**Full Name:** `Ops.Json.ObjectStringify_v2`
**Description:** Convert object to string

**> Input Ports:**
- **Object** (Object)
- **Beautify** (Number: Boolean)

**< Output Ports:**
- **Result** (String)
- **Error** (booleanNumber)

**Example Patch:** [Open in Editor](https://cables.gl/edit/7X58nR)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ObjectStringify_v2"*
**Docs:** [https://cables.gl/op/Ops.Json.ObjectStringify_v2](https://cables.gl/op/Ops.Json.ObjectStringify_v2)

---

### ObjectToArray
![ObjectToArray op](images/ops/Ops_Json_ObjectToArray.svg)

**Full Name:** `Ops.Json.ObjectToArray`
**Description:** cast an object port to an array port

**> Input Ports:**
- **Object** (Object)

**< Output Ports:**
- **Array** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Json.ObjectToArray#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ObjectToArray"*
**Docs:** [https://cables.gl/op/Ops.Json.ObjectToArray](https://cables.gl/op/Ops.Json.ObjectToArray)

---

### ObjectValuesAsArray
![ObjectValuesAsArray op](images/ops/Ops_Json_ObjectValuesAsArray.svg)

**Full Name:** `Ops.Json.ObjectValuesAsArray`
**Description:** extract all object values as an array

**> Input Ports:**
- **Object** (Object)

**< Output Ports:**
- **Values** (Array)
- **Num Values** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/bIQ8cI)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ObjectValuesAsArray"*
**Docs:** [https://cables.gl/op/Ops.Json.ObjectValuesAsArray](https://cables.gl/op/Ops.Json.ObjectValuesAsArray)

---

### ParseObject_v2
![ParseObject_v2 op](images/ops/Ops_Json_ParseObject_v2.svg)

**Full Name:** `Ops.Json.ParseObject_v2`
**Description:** Parses a string to a JSON object

**> Input Ports:**
- **JSON String** (String)

**< Output Ports:**
- **Result** (Object)
- **Valid** (booleanNumber)

**Example Patch:** [Open in Editor](https://cables.gl/edit/Z17vG8)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ParseObject_v2"*
**Docs:** [https://cables.gl/op/Ops.Json.ParseObject_v2](https://cables.gl/op/Ops.Json.ParseObject_v2)

---

### RemoveDataUrlPrefix
![RemoveDataUrlPrefix op](images/ops/Ops_Json_RemoveDataUrlPrefix.svg)

**Full Name:** `Ops.Json.RemoveDataUrlPrefix`
**Description:** Removes data URL prefix from a string

**> Input Ports:**
- **String Input** (String)

**< Output Ports:**
- **String Output** (String)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Json.RemoveDataUrlPrefix#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "RemoveDataUrlPrefix"*
**Docs:** [https://cables.gl/op/Ops.Json.RemoveDataUrlPrefix](https://cables.gl/op/Ops.Json.RemoveDataUrlPrefix)

---

### RouteObject
![RouteObject op](images/ops/Ops_Json_RouteObject.svg)

**Full Name:** `Ops.Json.RouteObject`
**Description:** Route an object to an output port

**> Input Ports:**
- **Index** (Number: Integer)
- **Object In** (Object)
- **Default Object** (Object)

**< Output Ports:**
- **Index 0 Object** (Object)
- **Index 1 Object** (Object)
- **Index 2 Object** (Object)
- **Index 3 Object** (Object)
- **Index 4 Object** (Object)
- **Index 5 Object** (Object)
- **Index 6 Object** (Object)
- **Index 7 Object** (Object)
- **Index 8 Object** (Object)
- **Index 9 Object** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/-xrxX8)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "RouteObject"*
**Docs:** [https://cables.gl/op/Ops.Json.RouteObject](https://cables.gl/op/Ops.Json.RouteObject)

---

### SaveJsonFile
![SaveJsonFile op](images/ops/Ops_Json_SaveJsonFile.svg)

**Full Name:** `Ops.Json.SaveJsonFile`
**Description:** save/download an object as json file

**> Input Ports:**
- **Download** (Trigger)
- **Filename** (String)
- **Object** (Object)

**< Output Ports:**
- *Visit [Ops.Json.SaveJsonFile documentation](https://cables.gl/op/Ops.Json.SaveJsonFile) for output port details*

**Example Patch:** [Open in Editor](https://cables.gl/edit/J0c008)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SaveJsonFile"*
**Docs:** [https://cables.gl/op/Ops.Json.SaveJsonFile](https://cables.gl/op/Ops.Json.SaveJsonFile)

---

### SequenceObjects_v2
![SequenceObjects_v2 op](images/ops/Ops_Json_SequenceObjects_v2.svg)

**Full Name:** `Ops.Json.SequenceObjects_v2`
**Description:** control order and flow of objects

**> Input Ports:**
- **Number 0** (Object)
- **Number 1** (Object)
- **Number 2** (Object)
- **Number 3** (Object)
- **Number 4** (Object)
- **Number 5** (Object)
- **Number 6** (Object)
- **Number 7** (Object)
- **Number 8** (Object)
- **Number 9** (Object)
- **Number 10** (Object)
- **Number 11** (Object)
- **Number 12** (Object)
- **Number 13** (Object)
- **Number 14** (Object)
- **Number 15** (Object)

**< Output Ports:**
- **Output 0** (Object)
- **Output 1** (Object)
- **Output 2** (Object)
- **Output 3** (Object)
- **Output 4** (Object)
- **Output 5** (Object)
- **Output 6** (Object)
- **Output 7** (Object)
- **Output 8** (Object)
- **Output 9** (Object)
- **Output 10** (Object)
- **Output 11** (Object)
- **Output 12** (Object)
- **Output 13** (Object)
- **Output 14** (Object)
- **Output 15** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Json.SequenceObjects_v2#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SequenceObjects_v2"*
**Docs:** [https://cables.gl/op/Ops.Json.SequenceObjects_v2](https://cables.gl/op/Ops.Json.SequenceObjects_v2)

---

### SwitchObject
![SwitchObject op](images/ops/Ops_Json_SwitchObject.svg)

**Full Name:** `Ops.Json.SwitchObject`
**Description:** Allows switching between objects

**> Input Ports:**
- **Object Index** (Number: Integer)
- **Object Port 0** (Object)
- **Object Port 1** (Object)
- **Object Port 2** (Object)
- **Object Port 3** (Object)
- **Object Port 4** (Object)
- **Object Port 5** (Object)
- **Object Port 6** (Object)
- **Object Port 7** (Object)

**< Output Ports:**
- **Object Out** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/X55cRo)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SwitchObject"*
**Docs:** [https://cables.gl/op/Ops.Json.SwitchObject](https://cables.gl/op/Ops.Json.SwitchObject)

---

### SwitchObjectMultiPort_v2
![SwitchObjectMultiPort_v2 op](images/ops/Ops_Json_SwitchObjectMultiPort_v2.svg)

**Full Name:** `Ops.Json.SwitchObjectMultiPort_v2`
**Description:** Switch between multiple object inputs

**> Input Ports:**
- **Index** (Number: Integer)
- **Objects_0** (Object)
- **Add Port** (Object)

**< Output Ports:**
- **Object** (Object)
- **Num Values** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/PI2xsh)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SwitchObjectMultiPort_v2"*
**Docs:** [https://cables.gl/op/Ops.Json.SwitchObjectMultiPort_v2](https://cables.gl/op/Ops.Json.SwitchObjectMultiPort_v2)

---

### TriggerObject
![TriggerObject op](images/ops/Ops_Json_TriggerObject.svg)

**Full Name:** `Ops.Json.TriggerObject`
**Description:** set output object when triggered

**> Input Ports:**
- **Trigger** (Trigger)
- **Object** (Object)

**< Output Ports:**
- **Next** (Trigger)
- **Result** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Json.TriggerObject#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TriggerObject"*
**Docs:** [https://cables.gl/op/Ops.Json.TriggerObject](https://cables.gl/op/Ops.Json.TriggerObject)

---

### TriggerObjectSetNumber
![TriggerObjectSetNumber op](images/ops/Ops_Json_TriggerObjectSetNumber.svg)

**Full Name:** `Ops.Json.TriggerObjectSetNumber`
**Description:** set a number value of an object using trigger

**> Input Ports:**
- **Trigger** (Trigger)
- **Object** (Object)
- **Key** (String)
- **Number** (Number)

**< Output Ports:**
- **Next** (Trigger)
- **Result** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Json.TriggerObjectSetNumber#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TriggerObjectSetNumber"*
**Docs:** [https://cables.gl/op/Ops.Json.TriggerObjectSetNumber](https://cables.gl/op/Ops.Json.TriggerObjectSetNumber)

---

### TriggerObjectSetString
![TriggerObjectSetString op](images/ops/Ops_Json_TriggerObjectSetString.svg)

**Full Name:** `Ops.Json.TriggerObjectSetString`
**Description:** set a string value of an object using trigger

**> Input Ports:**
- **Trigger** (Trigger)
- **Object** (Object)
- **Key** (String)
- **String** (String)

**< Output Ports:**
- **Next** (Trigger)
- **Result** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Json.TriggerObjectSetString#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TriggerObjectSetString"*
**Docs:** [https://cables.gl/op/Ops.Json.TriggerObjectSetString](https://cables.gl/op/Ops.Json.TriggerObjectSetString)

---

