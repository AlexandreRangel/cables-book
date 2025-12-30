# Ops.String

*Part of the [All Operators Reference](13-_AllOps.md)*

---

## Ops.String

### AddLineBreaks_v2
![AddLineBreaks_v2 op](images/ops/Ops_String_AddLineBreaks_v2.svg)

**Full Name:** `Ops.String.AddLineBreaks_v2`
**Description:** Insert a line break in a string of words

**> Input Ports:**
- **String** (String)
- **Max Characters Per Line** (Number: Integer)

**< Output Ports:**
- **Result** (String)

**Example Patch:** [Open in Editor](https://cables.gl/edit/4f-D16)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "AddLineBreaks_v2"*
**Docs:** [https://cables.gl/op/Ops.String.AddLineBreaks_v2](https://cables.gl/op/Ops.String.AddLineBreaks_v2)

---

### ArrayContainsString
![ArrayContainsString op](images/ops/Ops_String_ArrayContainsString.svg)

**Full Name:** `Ops.String.ArrayContainsString`
**Description:** Check if an array contains a string which can also be a number (find,search,indexOf)

**> Input Ports:**
- **Array** (Array)
- **SearchValue** (String)

**< Output Ports:**
- **Found** (booleanNumber)
- **Index** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/VuK4ve)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayContainsString"*
**Docs:** [https://cables.gl/op/Ops.String.ArrayContainsString](https://cables.gl/op/Ops.String.ArrayContainsString)

---

### ArrayOfStrings
![ArrayOfStrings op](images/ops/Ops_String_ArrayOfStrings.svg)

**Full Name:** `Ops.String.ArrayOfStrings`
**Description:** Create an array of strings and optionally attach index-number

**> Input Ports:**
- **String** (String)
- **Length** (Number: Integer)
- **Attach Number** (Number: Boolean)

**< Output Ports:**
- **Array** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/haeXx3)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayOfStrings"*
**Docs:** [https://cables.gl/op/Ops.String.ArrayOfStrings](https://cables.gl/op/Ops.String.ArrayOfStrings)

---

### CharacterRotate
![CharacterRotate op](images/ops/Ops_String_CharacterRotate.svg)

**Full Name:** `Ops.String.CharacterRotate`
**Description:** String rotate characters like a split-flap display

**> Input Ports:**
- **Update** (Trigger)
- **Reset** (Trigger)
- **Text** (String)
- **Random Seed** (Number)
- **Characters** (String)

**< Output Ports:**
- **Result** (String)

**Example Patch:** [Open in Editor](https://cables.gl/edit/-IuM8S)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "CharacterRotate"*
**Docs:** [https://cables.gl/op/Ops.String.CharacterRotate](https://cables.gl/op/Ops.String.CharacterRotate)

---

### Concat_v2
![Concat_v2 op](images/ops/Ops_String_Concat_v2.svg)

**Full Name:** `Ops.String.Concat_v2`
**Description:** Joins two strings together

**> Input Ports:**
- **String1** (String)
- **String2** (String)
- **New Line** (Number: Boolean)
- **Active** (Number: Boolean)

**< Output Ports:**
- **Result** (String)

**Example Patch:** [Open in Editor](https://cables.gl/edit/a8qVz6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Concat_v2"*
**Docs:** [https://cables.gl/op/Ops.String.Concat_v2](https://cables.gl/op/Ops.String.Concat_v2)

---

### ConcatMulti_v2
![ConcatMulti_v2 op](images/ops/Ops_String_ConcatMulti_v2.svg)

**Full Name:** `Ops.String.ConcatMulti_v2`
**Description:** Joins multiple strings together

**> Input Ports:**
- **String 0** (String)
- **String 1** (String)
- **String 2** (String)
- **String 3** (String)
- **String 4** (String)
- **String 5** (String)
- **String 6** (String)
- **String 7** (String)

**< Output Ports:**
- **Concat String** (String)

**Example Patch:** [Open in Editor](https://cables.gl/edit/DNW-QJ)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ConcatMulti_v2"*
**Docs:** [https://cables.gl/op/Ops.String.ConcatMulti_v2](https://cables.gl/op/Ops.String.ConcatMulti_v2)

---

### ConcatMultiPort_v2
![ConcatMultiPort_v2 op](images/ops/Ops_String_ConcatMultiPort_v2.svg)

**Full Name:** `Ops.String.ConcatMultiPort_v2`
**Description:** concatinate/join multiple string inputs

**> Input Ports:**
- **Strings_0** (String)
- **Add Port** (String)

**< Output Ports:**
- **String** (String)
- **Num Strings** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/PBHPrh)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ConcatMultiPort_v2"*
**Docs:** [https://cables.gl/op/Ops.String.ConcatMultiPort_v2](https://cables.gl/op/Ops.String.ConcatMultiPort_v2)

---

### CopyToClipboard
![CopyToClipboard op](images/ops/Ops_String_CopyToClipboard.svg)

**Full Name:** `Ops.String.CopyToClipboard`
**Description:** Copy string to clipboard on trigger

**> Input Ports:**
- **Copy** (Trigger)
- **String** (String)

**< Output Ports:**
- **Success** (booleanNumber)

**Example Patch:** [Open in Editor](https://cables.gl/edit/Rquam4)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "CopyToClipboard"*
**Docs:** [https://cables.gl/op/Ops.String.CopyToClipboard](https://cables.gl/op/Ops.String.CopyToClipboard)

---

### DelayStringSimple
![DelayStringSimple op](images/ops/Ops_String_DelayStringSimple.svg)

**Full Name:** `Ops.String.DelayStringSimple`
**Description:** delay the output of a string by n seconds

**> Input Ports:**
- **Value** (String)
- **Delay** (Number)

**< Output Ports:**
- **Out Value** (String)

**Example Patch:** [Open in Editor](https://cables.gl/edit/kqtJkE)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "DelayStringSimple"*
**Docs:** [https://cables.gl/op/Ops.String.DelayStringSimple](https://cables.gl/op/Ops.String.DelayStringSimple)

---

### EndsWith
![EndsWith op](images/ops/Ops_String_EndsWith.svg)

**Full Name:** `Ops.String.EndsWith`
**Description:** does a string starts with another string?

**> Input Ports:**
- **String** (String)
- **Search** (String)

**< Output Ports:**
- **Ends With** (booleanNumber)

**Example Patch:** [Open in Editor](https://cables.gl/edit/X0EBz1)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "EndsWith"*
**Docs:** [https://cables.gl/op/Ops.String.EndsWith](https://cables.gl/op/Ops.String.EndsWith)

---

### FileUrlsToArrayMultiPort_v2
![FileUrlsToArrayMultiPort_v2 op](images/ops/Ops_String_FileUrlsToArrayMultiPort_v2.svg)

**Full Name:** `Ops.String.FileUrlsToArrayMultiPort_v2`
**Description:** create an array from multiple string

**> Input Ports:**
- **Strings_0** (String)
- **Add Port** (String)

**< Output Ports:**
- **Result** (Array)
- **Num Values** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/uoPbz1)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "FileUrlsToArrayMultiPort_v2"*
**Docs:** [https://cables.gl/op/Ops.String.FileUrlsToArrayMultiPort_v2](https://cables.gl/op/Ops.String.FileUrlsToArrayMultiPort_v2)

---

### FilterValidString
![FilterValidString op](images/ops/Ops_String_FilterValidString.svg)

**Full Name:** `Ops.String.FilterValidString`
**Description:** filter valid strings (not null,undefined or empty)

**> Input Ports:**
- **String** (String)
- **Invalid If Null** (Number: Boolean)
- **Invalid If Undefined** (Number: Boolean)
- **Invalid If Empty** (Number: Boolean)
- **Invalid If 0** (Number: Boolean)

**< Output Ports:**
- **Last Valid String** (String)
- **Is Valid** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.String.FilterValidString#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "FilterValidString"*
**Docs:** [https://cables.gl/op/Ops.String.FilterValidString](https://cables.gl/op/Ops.String.FilterValidString)

---

### FreezeString
![FreezeString op](images/ops/Ops_String_FreezeString.svg)

**Full Name:** `Ops.String.FreezeString`
**Description:** capture the current input and copy it to the output, even after a reload

**> Input Ports:**
- **String** (String)
- **Button** (Trigger)

**< Output Ports:**
- **Frozen String** (String)

**Example Patch:** [Open in Editor](https://cables.gl/edit/MuPepX)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "FreezeString"*
**Docs:** [https://cables.gl/op/Ops.String.FreezeString](https://cables.gl/op/Ops.String.FreezeString)

---

### GateString
![GateString op](images/ops/Ops_String_GateString.svg)

**Full Name:** `Ops.String.GateString`
**Description:** Output string if pass through is true

**> Input Ports:**
- **String In** (String)
- **Pass Through** (Number: Boolean)
- **Custom Value** (String)

**< Output Ports:**
- **String Out** (String)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.String.GateString#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GateString"*
**Docs:** [https://cables.gl/op/Ops.String.GateString](https://cables.gl/op/Ops.String.GateString)

---

### HandleBarsHtml_v2
![HandleBarsHtml_v2 op](images/ops/Ops_String_HandleBarsHtml_v2.svg)

**Full Name:** `Ops.String.HandleBarsHtml_v2`
**Description:** string conversion using handlebars template engine

**> Input Ports:**
- **Template** (String)
- **Data** (Object)
- **Array** (Array)

**< Output Ports:**
- **Result** (String)
- **Errors** (String)

**Example Patch:** [Open in Editor](https://cables.gl/edit/TKQIs7)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "HandleBarsHtml_v2"*
**Docs:** [https://cables.gl/op/Ops.String.HandleBarsHtml_v2](https://cables.gl/op/Ops.String.HandleBarsHtml_v2)

---

### HtmlDecode
![HtmlDecode op](images/ops/Ops_String_HtmlDecode.svg)

**Full Name:** `Ops.String.HtmlDecode`
**Description:** convert a html encoded string to a normal UTF8 string

**> Input Ports:**
- **String** (String)

**< Output Ports:**
- **Result** (String)

**Example Patch:** [Open in Editor](https://cables.gl/edit/jVwciO)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "HtmlDecode"*
**Docs:** [https://cables.gl/op/Ops.String.HtmlDecode](https://cables.gl/op/Ops.String.HtmlDecode)

---

### HtmlEncode
![HtmlEncode op](images/ops/Ops_String_HtmlEncode.svg)

**Full Name:** `Ops.String.HtmlEncode`
**Description:** encode a string to html

**> Input Ports:**
- **String** (String)

**< Output Ports:**
- **Result** (String)

**Example Patch:** [Open in Editor](https://cables.gl/edit/jVwciO)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "HtmlEncode"*
**Docs:** [https://cables.gl/op/Ops.String.HtmlEncode](https://cables.gl/op/Ops.String.HtmlEncode)

---

### LeftPad_v2
![LeftPad_v2 op](images/ops/Ops_String_LeftPad_v2.svg)

**Full Name:** `Ops.String.LeftPad_v2`
**Description:** create a fixed length string from a number 1 -> 0001

**> Input Ports:**
- **Value** (String)
- **Char** (String)
- **Num** (Number: Integer)

**< Output Ports:**
- **String** (String)

**Example Patch:** [Open in Editor](https://cables.gl/edit/8LJxz7)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "LeftPad_v2"*
**Docs:** [https://cables.gl/op/Ops.String.LeftPad_v2](https://cables.gl/op/Ops.String.LeftPad_v2)

---

### LimitLineBreaks_v2
![LimitLineBreaks_v2 op](images/ops/Ops_String_LimitLineBreaks_v2.svg)

**Full Name:** `Ops.String.LimitLineBreaks_v2`
**Description:** Limit number of lines in a string

**> Input Ports:**
- **String** (String)
- **Num Lines** (Number: Integer)
- **Reverse** (Number: Boolean)
- **Force Num Lines** (Number: Boolean)

**< Output Ports:**
- **Result** (String)

**Example Patch:** [Open in Editor](https://cables.gl/edit/ZCUND-)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "LimitLineBreaks_v2"*
**Docs:** [https://cables.gl/op/Ops.String.LimitLineBreaks_v2](https://cables.gl/op/Ops.String.LimitLineBreaks_v2)

---

### LineBreak
![LineBreak op](images/ops/Ops_String_LineBreak.svg)

**Full Name:** `Ops.String.LineBreak`
**Description:** Outputs a linebreak, or adds a linebreak to a string

**> Input Ports:**
- **String** (String)

**< Output Ports:**
- **Result** (String)

**Example Patch:** [Open in Editor](https://cables.gl/edit/U7PniO)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "LineBreak"*
**Docs:** [https://cables.gl/op/Ops.String.LineBreak](https://cables.gl/op/Ops.String.LineBreak)

---

### LineBreaksHtml
![LineBreaksHtml op](images/ops/Ops_String_LineBreaksHtml.svg)

**Full Name:** `Ops.String.LineBreaksHtml`
**Description:** Convert linebreaks to html breaks

**> Input Ports:**
- **String** (String)
- **Add Num Breaks** (Number: Integer)

**< Output Ports:**
- **HTML** (String)

**Example Patch:** [Open in Editor](https://cables.gl/edit/M0BG16)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "LineBreaksHtml"*
**Docs:** [https://cables.gl/op/Ops.String.LineBreaksHtml](https://cables.gl/op/Ops.String.LineBreaksHtml)

---

### LoremIpsum
![LoremIpsum op](images/ops/Ops_String_LoremIpsum.svg)

**Full Name:** `Ops.String.LoremIpsum`
**Description:** Lorem ipsum dolor sit amet

**> Input Ports:**
- *Visit [Ops.String.LoremIpsum documentation](https://cables.gl/op/Ops.String.LoremIpsum) for input port details*

**< Output Ports:**
- **String** (String)
- **HTML String** (String)
- **Array** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/4f-D16)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "LoremIpsum"*
**Docs:** [https://cables.gl/op/Ops.String.LoremIpsum](https://cables.gl/op/Ops.String.LoremIpsum)

---

### Lowercase_v2
![Lowercase_v2 op](images/ops/Ops_String_Lowercase_v2.svg)

**Full Name:** `Ops.String.Lowercase_v2`
**Description:** convert all characters to small letters

**> Input Ports:**
- **String** (String)

**< Output Ports:**
- **Result** (String)

**Example Patch:** [Open in Editor](https://cables.gl/edit/a8qVz6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Lowercase_v2"*
**Docs:** [https://cables.gl/op/Ops.String.Lowercase_v2](https://cables.gl/op/Ops.String.Lowercase_v2)

---

### Md5
![Md5 op](images/ops/Ops_String_Md5.svg)

**Full Name:** `Ops.String.Md5`
**Description:** Create a md5 hash of a string

**> Input Ports:**
- **String** (String)

**< Output Ports:**
- **MD5 Hash** (String)

**Example Patch:** [Open in Editor](https://cables.gl/edit/IyC0O8)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Md5"*
**Docs:** [https://cables.gl/op/Ops.String.Md5](https://cables.gl/op/Ops.String.Md5)

---

### NumberFormatter
![NumberFormatter op](images/ops/Ops_String_NumberFormatter.svg)

**Full Name:** `Ops.String.NumberFormatter`
**Description:** Format a number to a string in the given locale and format

**> Input Ports:**
- **Input Number** (Number)
- **Locale String** (String)
- **Minimum Integer Digits** (Number: Integer)
- **Minimum Fraction Digits** (Number: Integer)
- **Maximum Fraction Digits** (Number: Integer)
- **Minimum Significant Digits** (Number: Integer)
- **Maximum Significant Digits** (Number: Integer)
- **Use Grouping** (Number: Boolean)
- **Currency Name** (String)

**< Output Ports:**
- **Formatted Number** (String)
- **Has Error** (booleanNumber)

**Example Patch:** [Open in Editor](https://cables.gl/edit/-h-Rx3)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "NumberFormatter"*
**Docs:** [https://cables.gl/op/Ops.String.NumberFormatter](https://cables.gl/op/Ops.String.NumberFormatter)

---

### NumberSwitchByString
![NumberSwitchByString op](images/ops/Ops_String_NumberSwitchByString.svg)

**Full Name:** `Ops.String.NumberSwitchByString`
**Description:** associate numbers by strings

**> Input Ports:**
- **String** (String)
- **String 1** (String)
- **Number 1** (Number)
- **String 2** (String)
- **Number 2** (Number)
- **String 3** (String)
- **Number 3** (Number)
- **String 4** (String)
- **Number 4** (Number)
- **String 5** (String)
- **Number 5** (Number)
- **String 6** (String)
- **Number 6** (Number)
- **String 7** (String)
- **Number 7** (Number)
- **String 8** (String)
- **Number 8** (Number)
- **String 9** (String)
- **Number 9** (Number)
- **String 10** (String)
- **Number 10** (Number)

**< Output Ports:**
- **Result** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/CWSBeE)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "NumberSwitchByString"*
**Docs:** [https://cables.gl/op/Ops.String.NumberSwitchByString](https://cables.gl/op/Ops.String.NumberSwitchByString)

---

### NumberToString_v2
![NumberToString_v2 op](images/ops/Ops_String_NumberToString_v2.svg)

**Full Name:** `Ops.String.NumberToString_v2`
**Description:** Convert a number to a string

**> Input Ports:**
- **Number** (Number)
- **Decimal Places** (Number: Integer)

**< Output Ports:**
- **Result** (String)

**Example Patch:** [Open in Editor](https://cables.gl/edit/fo6nci)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "NumberToString_v2"*
**Docs:** [https://cables.gl/op/Ops.String.NumberToString_v2](https://cables.gl/op/Ops.String.NumberToString_v2)

---

### NumTotalLineBreaks
![NumTotalLineBreaks op](images/ops/Ops_String_NumTotalLineBreaks.svg)

**Full Name:** `Ops.String.NumTotalLineBreaks`
**Description:** Count number of line breaks in a string

**> Input Ports:**
- **String** (String)

**< Output Ports:**
- **Total Lines** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/lkDCeT)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "NumTotalLineBreaks"*
**Docs:** [https://cables.gl/op/Ops.String.NumTotalLineBreaks](https://cables.gl/op/Ops.String.NumTotalLineBreaks)

---

### OrString
![OrString op](images/ops/Ops_String_OrString.svg)

**Full Name:** `Ops.String.OrString`
**Description:** outputs the first valid string

**> Input Ports:**
- **String 1** (String)
- **String 2** (String)
- **String 3** (String)
- **String 4** (String)
- **String 5** (String)
- **String 6** (String)
- **String 7** (String)
- **String 8** (String)

**< Output Ports:**
- **Result** (String)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.String.OrString#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "OrString"*
**Docs:** [https://cables.gl/op/Ops.String.OrString](https://cables.gl/op/Ops.String.OrString)

---

### ParseInt_v2
![ParseInt_v2 op](images/ops/Ops_String_ParseInt_v2.svg)

**Full Name:** `Ops.String.ParseInt_v2`
**Description:** Parse a string to a integer number / string to number

**> Input Ports:**
- **String** (String)

**< Output Ports:**
- **Number** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.String.ParseInt_v2#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ParseInt_v2"*
**Docs:** [https://cables.gl/op/Ops.String.ParseInt_v2](https://cables.gl/op/Ops.String.ParseInt_v2)

---

### RandomString_v3
![RandomString_v3 op](images/ops/Ops_String_RandomString_v3.svg)

**Full Name:** `Ops.String.RandomString_v3`
**Description:** Generate a random string of given characters

**> Input Ports:**
- **Chars** (String)
- **Length** (Number: Integer)
- **Seed** (Number)

**< Output Ports:**
- **Result** (String)

**Example Patch:** [Open in Editor](https://cables.gl/edit/HqmXN8)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "RandomString_v3"*
**Docs:** [https://cables.gl/op/Ops.String.RandomString_v3](https://cables.gl/op/Ops.String.RandomString_v3)

---

### RightPad_v2
![RightPad_v2 op](images/ops/Ops_String_RightPad_v2.svg)

**Full Name:** `Ops.String.RightPad_v2`
**Description:** create a string with a fixed length filling the space with a character

**> Input Ports:**
- **Value** (String)
- **Char** (String)
- **Num** (Number: Integer)

**< Output Ports:**
- **String** (String)

**Example Patch:** [Open in Editor](https://cables.gl/edit/8LJxz7)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "RightPad_v2"*
**Docs:** [https://cables.gl/op/Ops.String.RightPad_v2](https://cables.gl/op/Ops.String.RightPad_v2)

---

### RightPadNumber_v2
![RightPadNumber_v2 op](images/ops/Ops_String_RightPadNumber_v2.svg)

**Full Name:** `Ops.String.RightPadNumber_v2`
**Description:** Converts a number to a string with num decimal places, adds 0's

**> Input Ports:**
- **Value** (Number)
- **Num** (Number: Integer)

**< Output Ports:**
- **String** (String)

**Example Patch:** [Open in Editor](https://cables.gl/edit/ps8ZHq)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "RightPadNumber_v2"*
**Docs:** [https://cables.gl/op/Ops.String.RightPadNumber_v2](https://cables.gl/op/Ops.String.RightPadNumber_v2)

---

### RouteString
![RouteString op](images/ops/Ops_String_RouteString.svg)

**Full Name:** `Ops.String.RouteString`
**Description:** Route a string to an output port

**> Input Ports:**
- **Index** (Number: Integer)
- **String In** (String)
- **Default String** (String)
- **Set Inactive To Default** (Number: Boolean)

**< Output Ports:**
- **Index 0 String** (String)
- **Index 1 String** (String)
- **Index 2 String** (String)
- **Index 3 String** (String)
- **Index 4 String** (String)
- **Index 5 String** (String)
- **Index 6 String** (String)
- **Index 7 String** (String)
- **Index 8 String** (String)
- **Index 9 String** (String)

**Example Patch:** [Open in Editor](https://cables.gl/edit/WDoBX8)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "RouteString"*
**Docs:** [https://cables.gl/op/Ops.String.RouteString](https://cables.gl/op/Ops.String.RouteString)

---

### SaveTextFile
![SaveTextFile op](images/ops/Ops_String_SaveTextFile.svg)

**Full Name:** `Ops.String.SaveTextFile`
**Description:** download a textfile containing the input string

**> Input Ports:**
- **Download** (Trigger)
- **Filename** (String)
- **Content String** (String)

**< Output Ports:**
- *Visit [Ops.String.SaveTextFile documentation](https://cables.gl/op/Ops.String.SaveTextFile) for output port details*

**Example Patch:** [Open in Editor](https://cables.gl/edit/mxybpX)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SaveTextFile"*
**Docs:** [https://cables.gl/op/Ops.String.SaveTextFile](https://cables.gl/op/Ops.String.SaveTextFile)

---

### SequenceStrings
![SequenceStrings op](images/ops/Ops_String_SequenceStrings.svg)

**Full Name:** `Ops.String.SequenceStrings`
**Description:** control order and flow of strings

**> Input Ports:**
- **String 0** (String)
- **String 1** (String)
- **String 2** (String)
- **String 3** (String)
- **String 4** (String)
- **String 5** (String)
- **String 6** (String)
- **String 7** (String)
- **String 8** (String)
- **String 9** (String)
- **String 10** (String)
- **String 11** (String)
- **String 12** (String)
- **String 13** (String)
- **String 14** (String)
- **String 15** (String)

**< Output Ports:**
- **Output 0** (String)
- **Output 1** (String)
- **Output 2** (String)
- **Output 3** (String)
- **Output 4** (String)
- **Output 5** (String)
- **Output 6** (String)
- **Output 7** (String)
- **Output 8** (String)
- **Output 9** (String)
- **Output 10** (String)
- **Output 11** (String)
- **Output 12** (String)
- **Output 13** (String)
- **Output 14** (String)
- **Output 15** (String)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.String.SequenceStrings#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SequenceStrings"*
**Docs:** [https://cables.gl/op/Ops.String.SequenceStrings](https://cables.gl/op/Ops.String.SequenceStrings)

---

### StartsWith
![StartsWith op](images/ops/Ops_String_StartsWith.svg)

**Full Name:** `Ops.String.StartsWith`
**Description:** does a string starts with another string?

**> Input Ports:**
- **String** (String)
- **Search** (String)

**< Output Ports:**
- **Starts With** (booleanNumber)

**Example Patch:** [Open in Editor](https://cables.gl/edit/Hht1O8)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "StartsWith"*
**Docs:** [https://cables.gl/op/Ops.String.StartsWith](https://cables.gl/op/Ops.String.StartsWith)

---

### String_v3
![String_v3 op](images/ops/Ops_String_String_v3.svg)

**Full Name:** `Ops.String.String_v3`
**Description:** String input/output

**> Input Ports:**
- **Value** (String)

**< Output Ports:**
- **String** (String)

**Example Patch:** [Open in Editor](https://cables.gl/edit/FXRsii)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "String_v3"*
**Docs:** [https://cables.gl/op/Ops.String.String_v3](https://cables.gl/op/Ops.String.String_v3)

---

### StringCompose_v3
![StringCompose_v3 op](images/ops/Ops_String_StringCompose_v3.svg)

**Full Name:** `Ops.String.StringCompose_v3`
**Description:** Combine multiple Values to a new String

**> Input Ports:**
- **Format** (String)
- **String A** (String)
- **String B** (String)
- **String C** (String)
- **String D** (String)
- **String E** (String)
- **String F** (String)

**< Output Ports:**
- **Result** (String)

**Example Patch:** [Open in Editor](https://cables.gl/edit/U4M4J5)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "StringCompose_v3"*
**Docs:** [https://cables.gl/op/Ops.String.StringCompose_v3](https://cables.gl/op/Ops.String.StringCompose_v3)

---

### StringContains_v2
![StringContains_v2 op](images/ops/Ops_String_StringContains_v2.svg)

**Full Name:** `Ops.String.StringContains_v2`
**Description:** check if string contains another string (find,search,indexOf)

**> Input Ports:**
- **String** (String)
- **SearchValue** (String)

**< Output Ports:**
- **Found** (Number)
- **Index** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.String.StringContains_v2#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "StringContains_v2"*
**Docs:** [https://cables.gl/op/Ops.String.StringContains_v2](https://cables.gl/op/Ops.String.StringContains_v2)

---

### StringEditor
![StringEditor op](images/ops/Ops_String_StringEditor.svg)

**Full Name:** `Ops.String.StringEditor`
**Description:** string text editor

**> Input Ports:**
- **Value** (String)
- **Syntax Index** (Number: Integer)

**< Output Ports:**
- **Result** (String)

**Example Patch:** [Open in Editor](https://cables.gl/edit/Jhvn8i)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "StringEditor"*
**Docs:** [https://cables.gl/op/Ops.String.StringEditor](https://cables.gl/op/Ops.String.StringEditor)

---

### StringEquals_v2
![StringEquals_v2 op](images/ops/Ops_String_StringEquals_v2.svg)

**Full Name:** `Ops.String.StringEquals_v2`
**Description:** check if content of two strings is the same

**> Input Ports:**
- **String 1** (String)
- **String 2** (String)

**< Output Ports:**
- **Result** (booleanNumber)

**Example Patch:** [Open in Editor](https://cables.gl/edit/Nx2zci)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "StringEquals_v2"*
**Docs:** [https://cables.gl/op/Ops.String.StringEquals_v2](https://cables.gl/op/Ops.String.StringEquals_v2)

---

### StringGetLineNumAtIndex
![StringGetLineNumAtIndex op](images/ops/Ops_String_StringGetLineNumAtIndex.svg)

**Full Name:** `Ops.String.StringGetLineNumAtIndex`
**Description:** output the line number at the character index

**> Input Ports:**
- **String** (String)
- **Index** (Number: Integer)

**< Output Ports:**
- **Line** (Number)
- **Found** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.String.StringGetLineNumAtIndex#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "StringGetLineNumAtIndex"*
**Docs:** [https://cables.gl/op/Ops.String.StringGetLineNumAtIndex](https://cables.gl/op/Ops.String.StringGetLineNumAtIndex)

---

### StringIterator_v2
![StringIterator_v2 op](images/ops/Ops_String_StringIterator_v2.svg)

**Full Name:** `Ops.String.StringIterator_v2`
**Description:** iterate over every character of a string

**> Input Ports:**
- **Exec** (Trigger)
- **String** (String)

**< Output Ports:**
- **Next** (Trigger)
- **Character** (String)
- **Index** (Number)
- **Length** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.String.StringIterator_v2#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "StringIterator_v2"*
**Docs:** [https://cables.gl/op/Ops.String.StringIterator_v2](https://cables.gl/op/Ops.String.StringIterator_v2)

---

### StringLength_v2
![StringLength_v2 op](images/ops/Ops_String_StringLength_v2.svg)

**Full Name:** `Ops.String.StringLength_v2`
**Description:** number of characters in a string

**> Input Ports:**
- **String** (String)

**< Output Ports:**
- **Result** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/v9GLji)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "StringLength_v2"*
**Docs:** [https://cables.gl/op/Ops.String.StringLength_v2](https://cables.gl/op/Ops.String.StringLength_v2)

---

### StringRemoveCharacters
![StringRemoveCharacters op](images/ops/Ops_String_StringRemoveCharacters.svg)

**Full Name:** `Ops.String.StringRemoveCharacters`
**Description:** Remove every occurances of given characters from a string

**> Input Ports:**
- **String** (String)
- **Characters** (String)
- **Replace** (String)

**< Output Ports:**
- **Result** (String)

**Example Patch:** [Open in Editor](https://cables.gl/edit/ls8ciO)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "StringRemoveCharacters"*
**Docs:** [https://cables.gl/op/Ops.String.StringRemoveCharacters](https://cables.gl/op/Ops.String.StringRemoveCharacters)

---

### StringReplace
![StringReplace op](images/ops/Ops_String_StringReplace.svg)

**Full Name:** `Ops.String.StringReplace`
**Description:** replace occurrences of a string with another string

**> Input Ports:**
- **String** (String)
- **Search For** (String)
- **Replace** (String)
- **Replace What Index** (Number: Integer)

**< Output Ports:**
- **Result** (String)

**Example Patch:** [Open in Editor](https://cables.gl/edit/q0iLkE)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "StringReplace"*
**Docs:** [https://cables.gl/op/Ops.String.StringReplace](https://cables.gl/op/Ops.String.StringReplace)

---

### StringSortLines
![StringSortLines op](images/ops/Ops_String_StringSortLines.svg)

**Full Name:** `Ops.String.StringSortLines`
**Description:** sort each line of a string alphabetically

**> Input Ports:**
- **String** (String)
- **Reverse** (Number: Boolean)

**< Output Ports:**
- **Result** (String)

**Example Patch:** [Open in Editor](https://cables.gl/edit/MMS2O8)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "StringSortLines"*
**Docs:** [https://cables.gl/op/Ops.String.StringSortLines](https://cables.gl/op/Ops.String.StringSortLines)

---

### StringsToArrayMultiPort_v2
![StringsToArrayMultiPort_v2 op](images/ops/Ops_String_StringsToArrayMultiPort_v2.svg)

**Full Name:** `Ops.String.StringsToArrayMultiPort_v2`
**Description:** create an array from multiple string

**> Input Ports:**
- **Strings_0** (String)
- **Add Port** (String)

**< Output Ports:**
- **Result** (Array)
- **Num Values** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/oBPhsh)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "StringsToArrayMultiPort_v2"*
**Docs:** [https://cables.gl/op/Ops.String.StringsToArrayMultiPort_v2](https://cables.gl/op/Ops.String.StringsToArrayMultiPort_v2)

---

### StringSwitchByString
![StringSwitchByString op](images/ops/Ops_String_StringSwitchByString.svg)

**Full Name:** `Ops.String.StringSwitchByString`
**Description:** Switch between multiple strings by a string index

**> Input Ports:**
- **String** (String)
- **Default** (String)
- **String 1** (String)
- **Result String 1** (String)
- **String 2** (String)
- **Result String 2** (String)
- **String 3** (String)
- **Result String 3** (String)
- **String 4** (String)
- **Result String 4** (String)
- **String 5** (String)
- **Result String 5** (String)
- **String 6** (String)
- **Result String 6** (String)
- **String 7** (String)
- **Result String 7** (String)
- **String 8** (String)
- **Result String 8** (String)
- **String 9** (String)
- **Result String 9** (String)
- **String 10** (String)
- **Result String 10** (String)

**< Output Ports:**
- **Result** (String)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.String.StringSwitchByString#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "StringSwitchByString"*
**Docs:** [https://cables.gl/op/Ops.String.StringSwitchByString](https://cables.gl/op/Ops.String.StringSwitchByString)

---

### StringToNumber
![StringToNumber op](images/ops/Ops_String_StringToNumber.svg)

**Full Name:** `Ops.String.StringToNumber`
**Description:** Parses a string and returns a floating point number / string to number

**> Input Ports:**
- **String** (String)

**< Output Ports:**
- **Number** (Number)
- **Not A Number** (booleanNumber)

**Example Patch:** [Open in Editor](https://cables.gl/edit/XMEwci)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "StringToNumber"*
**Docs:** [https://cables.gl/op/Ops.String.StringToNumber](https://cables.gl/op/Ops.String.StringToNumber)

---

### StringTrim_v2
![StringTrim_v2 op](images/ops/Ops_String_StringTrim_v2.svg)

**Full Name:** `Ops.String.StringTrim_v2`
**Description:** Remove whitespace from both ends of a string

**> Input Ports:**
- **String** (String)

**< Output Ports:**
- **Result** (String)

**Example Patch:** [Open in Editor](https://cables.gl/edit/Ddmsii)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "StringTrim_v2"*
**Docs:** [https://cables.gl/op/Ops.String.StringTrim_v2](https://cables.gl/op/Ops.String.StringTrim_v2)

---

### StripHtml
![StripHtml op](images/ops/Ops_String_StripHtml.svg)

**Full Name:** `Ops.String.StripHtml`
**Description:** remove html tags from a string

**> Input Ports:**
- **String** (String)

**< Output Ports:**
- **Result** (String)

**Example Patch:** [Open in Editor](https://cables.gl/edit/5NsMve)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "StripHtml"*
**Docs:** [https://cables.gl/op/Ops.String.StripHtml](https://cables.gl/op/Ops.String.StripHtml)

---

### SubString_v2
![SubString_v2 op](images/ops/Ops_String_SubString_v2.svg)

**Full Name:** `Ops.String.SubString_v2`
**Description:** Subset of a string between one index and another

**> Input Ports:**
- **String** (String)
- **Start** (Number: Integer)
- **End** (Number: Integer)
- **End Of String** (Number: Boolean)

**< Output Ports:**
- **Result** (String)

**Example Patch:** [Open in Editor](https://cables.gl/edit/FvIvci)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SubString_v2"*
**Docs:** [https://cables.gl/op/Ops.String.SubString_v2](https://cables.gl/op/Ops.String.SubString_v2)

---

### SwitchString
![SwitchString op](images/ops/Ops_String_SwitchString.svg)

**Full Name:** `Ops.String.SwitchString`
**Description:** Switch between multiple strings with an index

**> Input Ports:**
- **Index** (Number: Integer)
- **String 0** (String)
- **String 1** (String)
- **String 2** (String)
- **String 3** (String)
- **String 4** (String)
- **String 5** (String)
- **String 6** (String)
- **String 7** (String)
- **String 8** (String)
- **String 9** (String)

**< Output Ports:**
- **Result** (String)

**Example Patch:** [Open in Editor](https://cables.gl/edit/2uRAci)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SwitchString"*
**Docs:** [https://cables.gl/op/Ops.String.SwitchString](https://cables.gl/op/Ops.String.SwitchString)

---

### SwitchStringMultiPort_v2
![SwitchStringMultiPort_v2 op](images/ops/Ops_String_SwitchStringMultiPort_v2.svg)

**Full Name:** `Ops.String.SwitchStringMultiPort_v2`
**Description:** switch between multiple string inputs

**> Input Ports:**
- **Index** (Number: Integer)
- **Strings_0** (String)
- **Add Port** (String)

**< Output Ports:**
- **String** (String)
- **Num Values** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/TwZ1sh)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SwitchStringMultiPort_v2"*
**Docs:** [https://cables.gl/op/Ops.String.SwitchStringMultiPort_v2](https://cables.gl/op/Ops.String.SwitchStringMultiPort_v2)

---

### Uppercase_v2
![Uppercase_v2 op](images/ops/Ops_String_Uppercase_v2.svg)

**Full Name:** `Ops.String.Uppercase_v2`
**Description:** Convert all characters in a string to upperase

**> Input Ports:**
- **String** (String)

**< Output Ports:**
- **Result** (String)

**Example Patch:** [Open in Editor](https://cables.gl/edit/a8qVz6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Uppercase_v2"*
**Docs:** [https://cables.gl/op/Ops.String.Uppercase_v2](https://cables.gl/op/Ops.String.Uppercase_v2)

---

### UUID
![UUID op](images/ops/Ops_String_UUID.svg)

**Full Name:** `Ops.String.UUID`
**Description:** outputs a unique identifier string

**> Input Ports:**
- **Generate** (Trigger)

**< Output Ports:**
- **Id** (String)

**Example Patch:** [Open in Editor](https://cables.gl/edit/ryYQwn)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "UUID"*
**Docs:** [https://cables.gl/op/Ops.String.UUID](https://cables.gl/op/Ops.String.UUID)

---

