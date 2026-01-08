# Ops.Math


```{=latex}
\OpsSubsubNoSubsectionNumbering\setcounter{subsubsection}{0}
```
### Abs
![Abs op](images/ops/Ops_Math_Abs.svg)

**Full Name:** `Ops.Math.Abs`

Returns the absolute, positive value.

**`\inputsymbol`{=latex} Inputs**

- **Number** (Number)

**`\outputsymbol`{=latex} Output**

- **Result** (Number)
- **The absolute value of Number** (always positive)

**Example Patch:** [cables.gl/edit/vtPZ7i](https://cables.gl/edit/vtPZ7i)

**Doc:** [cables.gl/op/Ops.Math.Abs](https://cables.gl/op/Ops.Math.Abs)

### Accumulator
![Accumulator op](images/ops/Ops_Math_Accumulator.svg)

**Full Name:** `Ops.Math.Accumulator`

Add to and multiply a number, set to current value.

**`\inputsymbol`{=latex} Inputs**

- **Trigger In** (Trigger)
- **Add To Number** (Number)
- **Multiplier To Add Number** (Number)
- **Default Value** (Number)
- **Set Default Value** (Trigger)

**`\outputsymbol`{=latex} Output**

- **Current Value** (Number)

**Example Patch:** [cables.gl/edit/Ejzvsx](https://cables.gl/edit/Ejzvsx)

**Doc:** [cables.gl/op/Ops.Math.Accumulator](https://cables.gl/op/Ops.Math.Accumulator)

### AddUp
![AddUp op](images/ops/Ops_Math_AddUp.svg)

**Full Name:** `Ops.Math.AddUp`

*Visit [documentation](https://cables.gl/op/Ops.Math.AddUp) for details*.

**`\inputsymbol`{=latex} Inputs**

- **Number** (Number)
- **Add** (Trigger)
- **Reset** (Trigger)

**`\outputsymbol`{=latex} Output**

- **Result** (Number)

**Example Patch:** [cables.gl/edit/cWh78i](https://cables.gl/edit/cWh78i)

**Doc:** [cables.gl/op/Ops.Math.AddUp](https://cables.gl/op/Ops.Math.AddUp)

### AngleBetweenPoints
![AngleBetweenPoints op](images/ops/Ops_Math_AngleBetweenPoints.svg)

**Full Name:** `Ops.Math.AngleBetweenPoints`

outputs the angle between two points (degree).

**`\inputsymbol`{=latex} Inputs**

- **Point 1 X** (Number)
- **Point 1 Y** (Number)
- **Point 2 X** (Number)
- **Point 2 Y** (Number)

**`\outputsymbol`{=latex} Output**

- **Angle** (Number)

**Example Patch:** [cables.gl/edit/aMsTGc](https://cables.gl/edit/aMsTGc)

**Doc:** [cables.gl/op/Ops.Math.AngleBetweenPoints](https://cables.gl/op/Ops.Math.AngleBetweenPoints)

### Array3MultiplyMatrix
![Array3MultiplyMatrix op](images/ops/Ops_Math_Array3MultiplyMatrix.svg)

**Full Name:** `Ops.Math.Array3MultiplyMatrix`

multiply every XYZ coordinate with a matrix.

**`\inputsymbol`{=latex} Inputs**

- **Update** (Trigger)
- **Array** (Array)
- **Matrix** (Array)

**`\outputsymbol`{=latex} Output**

- **Result** (Array)

**Example Patch:** [cables.gl/op/Ops.Math.Array3MultiplyMatrix#example](https://cables.gl/op/Ops.Math.Array3MultiplyMatrix#example)

**Doc:** [cables.gl/op/Ops.Math.Array3MultiplyMatrix](https://cables.gl/op/Ops.Math.Array3MultiplyMatrix)

### Array3To2dProjection
![Array3To2dProjection op](images/ops/Ops_Math_Array3To2dProjection.svg)

**Full Name:** `Ops.Math.Array3To2dProjection`

calculate 2d positions of an array3x.

**`\inputsymbol`{=latex} Inputs**

- **Exec** (Trigger)
- **Array3x** (Array)
- **Fov** (Number)
- **W** (Number)
- **H** (Number)
- **Pos X** (Number)
- **Pos Y** (Number)
- **Mul** (Number)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)
- **Array2x** (Array)

**Example Patch:** [cables.gl/op/Ops.Math.Array3To2dProjection#example](https://cables.gl/op/Ops.Math.Array3To2dProjection#example)

**Doc:** [cables.gl/op/Ops.Math.Array3To2dProjection](https://cables.gl/op/Ops.Math.Array3To2dProjection)

### Atan2
![Atan2 op](images/ops/Ops_Math_Atan2.svg)

**Full Name:** `Ops.Math.Atan2`

Calculates the angle from a specified point to the coordinate origin.

**`\inputsymbol`{=latex} Inputs**

- **X** (Number)
- **Y** (Number)
- **Phase** (Number)
- **Frequency** (Number)

**`\outputsymbol`{=latex} Output**

- **Result** (Number)

**Example Patch:** [cables.gl/op/Ops.Math.Atan2#example](https://cables.gl/op/Ops.Math.Atan2#example)

**Doc:** [cables.gl/op/Ops.Math.Atan2](https://cables.gl/op/Ops.Math.Atan2)

### Average
![Average op](images/ops/Ops_Math_Average.svg)

**Full Name:** `Ops.Math.Average`

average of last two values.

**`\inputsymbol`{=latex} Inputs**

- **Number** (Number)
- **Influence** (Number)

**`\outputsymbol`{=latex} Output**

- **Result** (Number)

**Example Patch:** [cables.gl/op/Ops.Math.Average#example](https://cables.gl/op/Ops.Math.Average#example)

**Doc:** [cables.gl/op/Ops.Math.Average](https://cables.gl/op/Ops.Math.Average)

### ButterflyCurve
![ButterflyCurve op](images/ops/Ops_Math_ButterflyCurve.svg)

**Full Name:** `Ops.Math.ButterflyCurve`

generate coordinates of a butterfly curve.

**`\inputsymbol`{=latex} Inputs**

- **Value** (Number)

**`\outputsymbol`{=latex} Output**

- **X** (Number)
- **Y** (Number)

**Example Patch:** [cables.gl/op/Ops.Math.ButterflyCurve#example](https://cables.gl/op/Ops.Math.ButterflyCurve#example)

**Doc:** [cables.gl/op/Ops.Math.ButterflyCurve](https://cables.gl/op/Ops.Math.ButterflyCurve)

### Ceil
![Ceil op](images/ops/Ops_Math_Ceil.svg)

**Full Name:** `Ops.Math.Ceil`

Returns the smallest integer greater than or equal to a given number.

**`\inputsymbol`{=latex} Inputs**

- **Number** (Number)

**`\outputsymbol`{=latex} Output**

- **Result** (Number)

**Example Patch:** [cables.gl/edit/nPvVW2](https://cables.gl/edit/nPvVW2)

**Doc:** [cables.gl/op/Ops.Math.Ceil](https://cables.gl/op/Ops.Math.Ceil)

### CircleCoordinates
![CircleCoordinates op](images/ops/Ops_Math_CircleCoordinates.svg)

**Full Name:** `Ops.Math.CircleCoordinates`

x and y coordinates of a circle.

**`\inputsymbol`{=latex} Inputs**

- **Position** (Number)
- **Radius** (Number)

**`\outputsymbol`{=latex} Output**

- **X** (Number)
- **Y** (Number)

**Example Patch:** [cables.gl/edit/uAkdL5](https://cables.gl/edit/uAkdL5)

**Doc:** [cables.gl/op/Ops.Math.CircleCoordinates](https://cables.gl/op/Ops.Math.CircleCoordinates)

### Clamp
![Clamp op](images/ops/Ops_Math_Clamp.svg)

**Full Name:** `Ops.Math.Clamp`

Makes sure a value is within range cuts off the rest.

**`\inputsymbol`{=latex} Inputs**

- **Val** (Number)
- **Min** (Number)
- **Max** (Number)
- **Ignore Outside Values** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Result** (Number)

**Example Patch:** [cables.gl/op/Ops.Math.Clamp#example](https://cables.gl/op/Ops.Math.Clamp#example)

**Doc:** [cables.gl/op/Ops.Math.Clamp](https://cables.gl/op/Ops.Math.Clamp)

### Cosine
![Cosine op](images/ops/Ops_Math_Cosine.svg)

**Full Name:** `Ops.Math.Cosine`

Calculates the cosine of an angle.

**`\inputsymbol`{=latex} Inputs**

- **Value** (Number)
- **Phase** (Number)
- **Frequency** (Number)
- **Amplitude** (Number)
- **Asine** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Result** (Number)

**Example Patch:** [cables.gl/edit/RhfUW2](https://cables.gl/edit/RhfUW2)

**Doc:** [cables.gl/op/Ops.Math.Cosine](https://cables.gl/op/Ops.Math.Cosine)

### Cross
![Cross op](images/ops/Ops_Math_Cross.svg)

**Full Name:** `Ops.Math.Cross`

Computes the cross product of two vec3's.

**`\inputsymbol`{=latex} Inputs**

- **Exec** (Trigger)
- **X1** (Number)
- **Y1** (Number)
- **Z1** (Number)
- **X2** (Number)
- **Y2** (Number)
- **Z2** (Number)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)
- **X** (Number)
- **Y** (Number)
- **Z** (Number)

**Example Patch:** [cables.gl/op/Ops.Math.Cross#example](https://cables.gl/op/Ops.Math.Cross#example)

**Doc:** [cables.gl/op/Ops.Math.Cross](https://cables.gl/op/Ops.Math.Cross)

### Degrees
![Degrees op](images/ops/Ops_Math_Degrees.svg)

**Full Name:** `Ops.Math.Degrees`

Converts a radian measurement to its corresponding value in degrees.

**`\inputsymbol`{=latex} Inputs**

- **Radians** (Number)

**`\outputsymbol`{=latex} Output**

- **Result** (Number)

**Example Patch:** [cables.gl/op/Ops.Math.Degrees#example](https://cables.gl/op/Ops.Math.Degrees#example)

**Doc:** [cables.gl/op/Ops.Math.Degrees](https://cables.gl/op/Ops.Math.Degrees)

### DegreeToVector
![DegreeToVector op](images/ops/Ops_Math_DegreeToVector.svg)

**Full Name:** `Ops.Math.DegreeToVector`

Calculates a vector (x and y) based on an angle in degrees.

**`\inputsymbol`{=latex} Inputs**

- **Degree** (Number)
- **The angle you want to convert** (in degrees)

**`\outputsymbol`{=latex} Output**

- **X** (Number)
- **Y** (Number)

**Example Patch:** [cables.gl/edit/k76YnO](https://cables.gl/edit/k76YnO)

**Doc:** [cables.gl/op/Ops.Math.DegreeToVector](https://cables.gl/op/Ops.Math.DegreeToVector)

### Delta
![Delta op](images/ops/Ops_Math_Delta.svg)

**Full Name:** `Ops.Math.Delta`

difference to the last value (previous, store).

**`\inputsymbol`{=latex} Inputs**

- **Value** (Number)
- **Change Always** (Number: Boolean)
- **Reset** (Trigger)

**`\outputsymbol`{=latex} Output**

- **Delta** (Number)

**Example Patch:** [cables.gl/op/Ops.Math.Delta#example](https://cables.gl/op/Ops.Math.Delta#example)

**Doc:** [cables.gl/op/Ops.Math.Delta](https://cables.gl/op/Ops.Math.Delta)

### DeltaSum
![DeltaSum op](images/ops/Ops_Math_DeltaSum.svg)

**Full Name:** `Ops.Math.DeltaSum`

add delta values to an clamped absolute value.

**`\inputsymbol`{=latex} Inputs**

- **Delta Value** (Number)
- **Default Value** (Number)
- **Multiply** (Number)
- **Reset** (Trigger)
- **Limit** (Number: Boolean)
- **Min** (Number)
- **Max** (Number)
- **Rubberband** (Number)

**`\outputsymbol`{=latex} Output**

- **Absolute Value** (Number)

**Example Patch:** [cables.gl/edit/hH8f_6](https://cables.gl/edit/hH8f_6)

**Doc:** [cables.gl/op/Ops.Math.DeltaSum](https://cables.gl/op/Ops.Math.DeltaSum)

### Difference
![Difference op](images/ops/Ops_Math_Difference.svg)

**Full Name:** `Ops.Math.Difference`

Difference between two numbers.

**`\inputsymbol`{=latex} Inputs**

- **Number A** (Number)
- **Number B** (Number)

**`\outputsymbol`{=latex} Output**

- **Result** (Number)

**Example Patch:** [cables.gl/op/Ops.Math.Difference#example](https://cables.gl/op/Ops.Math.Difference#example)

**Doc:** [cables.gl/op/Ops.Math.Difference](https://cables.gl/op/Ops.Math.Difference)

### Distance2d
![Distance2d op](images/ops/Ops_Math_Distance2d.svg)

**Full Name:** `Ops.Math.Distance2d`

Calculates the Distance between two 2d points.

**`\inputsymbol`{=latex} Inputs**

- **X1** (Number)
- **Y1** (Number)
- **X2** (Number)
- **Y2** (Number)

**`\outputsymbol`{=latex} Output**

- **Distance** (Number)

**Example Patch:** [cables.gl/edit/7mTKgg](https://cables.gl/edit/7mTKgg)

**Doc:** [cables.gl/op/Ops.Math.Distance2d](https://cables.gl/op/Ops.Math.Distance2d)

### Distance3d_v2
![Distance3d_v2 op](images/ops/Ops_Math_Distance3d_v2.svg)

**Full Name:** `Ops.Math.Distance3d_v2`

distance between two 3d points, calculated when triggered.

**`\inputsymbol`{=latex} Inputs**

- **Calc** (Trigger)
- **X1** (Number)
- **Y1** (Number)
- **Z1** (Number)
- **X2** (Number)
- **Y2** (Number)
- **Z2** (Number)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)
- **Distance** (Number)

**Example Patch:** [cables.gl/op/Ops.Math.Distance3d_v2#example](https://cables.gl/op/Ops.Math.Distance3d_v2#example)

**Doc:** [cables.gl/op/Ops.Math.Distance3d_v2](https://cables.gl/op/Ops.Math.Distance3d_v2)

### Divide
![Divide op](images/ops/Ops_Math_Divide.svg)

**Full Name:** `Ops.Math.Divide`

Divides a number by another.

**`\inputsymbol`{=latex} Inputs**

- **Number1** (Number)
- **Number2** (Number)

**`\outputsymbol`{=latex} Output**

- **Result** (Number)

**Example Patch:** [cables.gl/op/Ops.Math.Divide#example](https://cables.gl/op/Ops.Math.Divide#example)

**Doc:** [cables.gl/op/Ops.Math.Divide](https://cables.gl/op/Ops.Math.Divide)

### Ease
![Ease op](images/ops/Ops_Math_Ease.svg)

**Full Name:** `Ops.Math.Ease`

map a value to an easing curve.

**`\inputsymbol`{=latex} Inputs**

- **Value** (Number)
- **Min** (Number)
- **Max** (Number)
- **Easing Index** (Number: Integer)

**`\outputsymbol`{=latex} Output**

- **Result** (Number)

**Example Patch:** [cables.gl/edit/rLxYY6](https://cables.gl/edit/rLxYY6)

**Doc:** [cables.gl/op/Ops.Math.Ease](https://cables.gl/op/Ops.Math.Ease)

### Exp
![Exp op](images/ops/Ops_Math_Exp.svg)

**Full Name:** `Ops.Math.Exp`

Calculates the power of Euler’s number.

**`\inputsymbol`{=latex} Inputs**

- **Number** (Number)

**`\outputsymbol`{=latex} Output**

- **Result** (Number)

**Example Patch:** [cables.gl/op/Ops.Math.Exp#example](https://cables.gl/op/Ops.Math.Exp#example)

**Doc:** [cables.gl/op/Ops.Math.Exp](https://cables.gl/op/Ops.Math.Exp)

### FlipSign
![FlipSign op](images/ops/Ops_Math_FlipSign.svg)

**Full Name:** `Ops.Math.FlipSign`

positive numbers become negative and vice versa (negate).

**`\inputsymbol`{=latex} Inputs**

- **Value** (Number)

**`\outputsymbol`{=latex} Output**

- **Result** (Number)

**Example Patch:** [cables.gl/op/Ops.Math.FlipSign#example](https://cables.gl/op/Ops.Math.FlipSign#example)

**Doc:** [cables.gl/op/Ops.Math.FlipSign](https://cables.gl/op/Ops.Math.FlipSign)

### Floor
![Floor op](images/ops/Ops_Math_Floor.svg)

**Full Name:** `Ops.Math.Floor`

returns the largest integer less than or equal to a given number.

**`\inputsymbol`{=latex} Inputs**

- **Number** (Number)

**`\outputsymbol`{=latex} Output**

- **Result** (Number)

**Example Patch:** [cables.gl/edit/nPvVW2](https://cables.gl/edit/nPvVW2)

**Doc:** [cables.gl/op/Ops.Math.Floor](https://cables.gl/op/Ops.Math.Floor)

### Fract
![Fract op](images/ops/Ops_Math_Fract.svg)

**Full Name:** `Ops.Math.Fract`

returns the fractional part of a number.

**`\inputsymbol`{=latex} Inputs**

- **Value** (Number)

**`\outputsymbol`{=latex} Output**

- **Result** (Number)

**Example Patch:** [cables.gl/edit/VWb2t7](https://cables.gl/edit/VWb2t7)

**Doc:** [cables.gl/op/Ops.Math.Fract](https://cables.gl/op/Ops.Math.Fract)

### GaussianRandomArray
![GaussianRandomArray op](images/ops/Ops_Math_GaussianRandomArray.svg)

**Full Name:** `Ops.Math.GaussianRandomArray`

random numbers fitting a Gaussian, or normal, distribution.

**`\inputsymbol`{=latex} Inputs**

- **Num** (Number: Integer)
- **Deviation** (Number)
- **Random Seed** (Number)

**`\outputsymbol`{=latex} Output**

- **Array** (Array)

**Example Patch:** [cables.gl/edit/i14QNS](https://cables.gl/edit/i14QNS)

**Doc:** [cables.gl/op/Ops.Math.GaussianRandomArray](https://cables.gl/op/Ops.Math.GaussianRandomArray)

### Incrementor
![Incrementor op](images/ops/Ops_Math_Incrementor.svg)

**Full Name:** `Ops.Math.Incrementor`

increment a number by triggering.

**`\inputsymbol`{=latex} Inputs**

- **Increment** (Trigger)
- **Decrement** (Trigger)
- **Limit** (Number: Boolean)
- **Length** (Number: Integer)
- **Default** (Number: Integer)
- **Reset** (Trigger)

**`\outputsymbol`{=latex} Output**

- **Changed** (Trigger)
- **Value** (Number)
- **Restarted** (Trigger)

**Example Patch:** [cables.gl/edit/OdcvGu](https://cables.gl/edit/OdcvGu)

**Doc:** [cables.gl/op/Ops.Math.Incrementor](https://cables.gl/op/Ops.Math.Incrementor)

### IndexFraction
![IndexFraction op](images/ops/Ops_Math_IndexFraction.svg)

**Full Name:** `Ops.Math.IndexFraction`

return fraction of value by index.

**`\inputsymbol`{=latex} Inputs**

- **Number** (Number)
- **Index** (Number: Integer)

**`\outputsymbol`{=latex} Output**

- **Result** (Number)

**Example Patch:** [cables.gl/edit/SV3NPO](https://cables.gl/edit/SV3NPO)

**Doc:** [cables.gl/op/Ops.Math.IndexFraction](https://cables.gl/op/Ops.Math.IndexFraction)

### Interpolate
![Interpolate op](images/ops/Ops_Math_Interpolate.svg)

**Full Name:** `Ops.Math.Interpolate`

Interpolate between values, lerp, linear interpolate.

**`\inputsymbol`{=latex} Inputs**

- **Value 1** (Number)
- **Value 2** (Number)
- **Percentage** (Number)

**`\outputsymbol`{=latex} Output**

- **Result** (Number)

**Example Patch:** [cables.gl/op/Ops.Math.Interpolate#example](https://cables.gl/op/Ops.Math.Interpolate#example)

**Doc:** [cables.gl/op/Ops.Math.Interpolate](https://cables.gl/op/Ops.Math.Interpolate)

### IsNumberRising
![IsNumberRising op](images/ops/Ops_Math_IsNumberRising.svg)

**Full Name:** `Ops.Math.IsNumberRising`

detect if a number rising or falling.

**`\inputsymbol`{=latex} Inputs**

- **Number** (Number)

**`\outputsymbol`{=latex} Output**

- **Rising** (Number)

**Example Patch:** [cables.gl/edit/UN11cI](https://cables.gl/edit/UN11cI)

**Doc:** [cables.gl/op/Ops.Math.IsNumberRising](https://cables.gl/op/Ops.Math.IsNumberRising)

### Log
![Log op](images/ops/Ops_Math_Log.svg)

**Full Name:** `Ops.Math.Log`

Calculates the logarithm of Number.

**`\inputsymbol`{=latex} Inputs**

- **Number** (Number)

**`\outputsymbol`{=latex} Output**

- **Result** (Number)

**Example Patch:** [cables.gl/op/Ops.Math.Log#example](https://cables.gl/op/Ops.Math.Log#example)

**Doc:** [cables.gl/op/Ops.Math.Log](https://cables.gl/op/Ops.Math.Log)

### MapGeoCoordsSpherical
![MapGeoCoordsSpherical op](images/ops/Ops_Math_MapGeoCoordsSpherical.svg)

**Full Name:** `Ops.Math.MapGeoCoordsSpherical`

map geo locations (latitude - longitude) to spherical coordinates.

**`\inputsymbol`{=latex} Inputs**

- **Coordinates** (Array)
- **Radius** (Number)

**`\outputsymbol`{=latex} Output**

- **Result** (Array)

**Example Patch:** [cables.gl/edit/BvXW5Q](https://cables.gl/edit/BvXW5Q)

**Doc:** [cables.gl/op/Ops.Math.MapGeoCoordsSpherical](https://cables.gl/op/Ops.Math.MapGeoCoordsSpherical)

### MapRange
![MapRange op](images/ops/Ops_Math_MapRange.svg)

**Full Name:** `Ops.Math.MapRange`

Maps a value from one range into another.

**`\inputsymbol`{=latex} Inputs**

- **Value** (Number)
- **Old Min** (Number)
- **Old Max** (Number)
- **New Min** (Number)
- **New Max** (Number)
- **Easing Index** (Number: Integer)
- **Clamp** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Result** (Number)

**Example Patch:** [cables.gl/edit/YFIVGc](https://cables.gl/edit/YFIVGc)

**Doc:** [cables.gl/op/Ops.Math.MapRange](https://cables.gl/op/Ops.Math.MapRange)

### Math
![Math op](images/ops/Ops_Math_Math.svg)

**Full Name:** `Ops.Math.Math`

Allows different mathematical operations to be applied to two numbers.

**`\inputsymbol`{=latex} Inputs**

- **Number 0** (Number)
- **Number 1** (Number)
- **Math Mode Index** (Number: Integer)

**`\outputsymbol`{=latex} Output**

- **Result** (Number)

**Example Patch:** [cables.gl/edit/mTqdVJ](https://cables.gl/edit/mTqdVJ)

**Doc:** [cables.gl/op/Ops.Math.Math](https://cables.gl/op/Ops.Math.Math)

### MathExpression
![MathExpression op](images/ops/Ops_Math_MathExpression.svg)

**Full Name:** `Ops.Math.MathExpression`

calculates a user defined mathematical expression.

**`\inputsymbol`{=latex} Inputs**

- **A** (Number)
- **B** (Number)
- **C** (Number)
- **D** (Number)
- **Expression** (String)

**`\outputsymbol`{=latex} Output**

- **Result** (Number)
- **Expression Valid** (booleanNumber)

**Example Patch:** [cables.gl/edit/s5-tve](https://cables.gl/edit/s5-tve)

**Doc:** [cables.gl/op/Ops.Math.MathExpression](https://cables.gl/op/Ops.Math.MathExpression)

### Max
![Max op](images/ops/Ops_Math_Max.svg)

**Full Name:** `Ops.Math.Max`

Sets the output to the input value which is higher.

**`\inputsymbol`{=latex} Inputs**

- **Value** (Number)
- **Maximum** (Number)

**`\outputsymbol`{=latex} Output**

- **Result** (Number)

**Example Patch:** [cables.gl/edit/hV3X7i](https://cables.gl/edit/hV3X7i)

**Doc:** [cables.gl/op/Ops.Math.Max](https://cables.gl/op/Ops.Math.Max)

### MaxSinceReset
![MaxSinceReset op](images/ops/Ops_Math_MaxSinceReset.svg)

**Full Name:** `Ops.Math.MaxSinceReset`

Outputs the maximum value since reset has been triggered.

**`\inputsymbol`{=latex} Inputs**

- **Value** (Number)
- **Reset** (Trigger)

**`\outputsymbol`{=latex} Output**

- **Maximum** (Number)

**Example Patch:** [cables.gl/op/Ops.Math.MaxSinceReset#example](https://cables.gl/op/Ops.Math.MaxSinceReset#example)

**Doc:** [cables.gl/op/Ops.Math.MaxSinceReset](https://cables.gl/op/Ops.Math.MaxSinceReset)

### MercatorCoord
![MercatorCoord op](images/ops/Ops_Math_MercatorCoord.svg)

**Full Name:** `Ops.Math.MercatorCoord`

project mercator coordinates.

**`\inputsymbol`{=latex} Inputs**

- **Latitude** (Number)
- **Longitude** (Number)
- **MapWidth** (Number)
- **MapHeight** (Number)

**`\outputsymbol`{=latex} Output**

- **X** (Number)
- **Y** (Number)

**Example Patch:** [cables.gl/edit/oi9AI4](https://cables.gl/edit/oi9AI4)

**Doc:** [cables.gl/op/Ops.Math.MercatorCoord](https://cables.gl/op/Ops.Math.MercatorCoord)

### MercatorCoordsArray
![MercatorCoordsArray op](images/ops/Ops_Math_MercatorCoordsArray.svg)

**Full Name:** `Ops.Math.MercatorCoordsArray`

Mercator map and center an array of latitudes and longitudes to a local coordinate system.

**`\inputsymbol`{=latex} Inputs**

- **LatLon Array** (Array)
- **MapWidth** (Number)
- **Center Lat** (Number)
- **Center Lon** (Number)

**`\outputsymbol`{=latex} Output**

- **Result** (Array)

**Example Patch:** [cables.gl/edit/vgRDeT](https://cables.gl/edit/vgRDeT)

**Doc:** [cables.gl/op/Ops.Math.MercatorCoordsArray](https://cables.gl/op/Ops.Math.MercatorCoordsArray)

### Min_v3
![Min_v3 op](images/ops/Ops_Math_Min_v3.svg)

**Full Name:** `Ops.Math.Min_v3`

Result will be the smaller number of the inputs.

**`\inputsymbol`{=latex} Inputs**

- **Value 1** (Number)
- **Value 2** (Number)

**`\outputsymbol`{=latex} Output**

- **Result** (Number)

**Example Patch:** [cables.gl/edit/rvAW7i](https://cables.gl/edit/rvAW7i)

**Doc:** [cables.gl/op/Ops.Math.Min_v3](https://cables.gl/op/Ops.Math.Min_v3)

### MinSinceReset
![MinSinceReset op](images/ops/Ops_Math_MinSinceReset.svg)

**Full Name:** `Ops.Math.MinSinceReset`

Outputs the minimum value since reset has been triggered.

**`\inputsymbol`{=latex} Inputs**

- **Value** (Number)
- **Reset** (Trigger)

**`\outputsymbol`{=latex} Output**

- **Minimum** (Number)

**Example Patch:** [cables.gl/op/Ops.Math.MinSinceReset#example](https://cables.gl/op/Ops.Math.MinSinceReset#example)

**Doc:** [cables.gl/op/Ops.Math.MinSinceReset](https://cables.gl/op/Ops.Math.MinSinceReset)

### Modulo
![Modulo op](images/ops/Ops_Math_Modulo.svg)

**Full Name:** `Ops.Math.Modulo`

outputs the remainder after division of one number by another.

**`\inputsymbol`{=latex} Inputs**

- **Number1** (Number)
- **Number2** (Number)
- **Pingpong** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Result** (Number)

**Example Patch:** [cables.gl/op/Ops.Math.Modulo#example](https://cables.gl/op/Ops.Math.Modulo#example)

**Doc:** [cables.gl/op/Ops.Math.Modulo](https://cables.gl/op/Ops.Math.Modulo)

### MulMatrixXyz
![MulMatrixXyz op](images/ops/Ops_Math_MulMatrixXyz.svg)

**Full Name:** `Ops.Math.MulMatrixXyz`

multiply XYZ values with a gl matrix vec3 x mat4.

**`\inputsymbol`{=latex} Inputs**

- **Update** (Trigger)
- **X** (Number)
- **Y** (Number)
- **Z** (Number)
- **Matrix** (Array)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)
- **Result X** (Number)
- **Result Y** (Number)
- **Result Z** (Number)

**Example Patch:** [cables.gl/edit/QlOcck](https://cables.gl/edit/QlOcck)

**Doc:** [cables.gl/op/Ops.Math.MulMatrixXyz](https://cables.gl/op/Ops.Math.MulMatrixXyz)

### Multiply
![Multiply op](images/ops/Ops_Math_Multiply.svg)

**Full Name:** `Ops.Math.Multiply`

Multiplies two numbers.

**`\inputsymbol`{=latex} Inputs**

- **Number1** (Number)
- **Number2** (Number)

**`\outputsymbol`{=latex} Output**

- **Result** (Number)

**Example Patch:** [cables.gl/edit/0010r1](https://cables.gl/edit/0010r1)

**Doc:** [cables.gl/op/Ops.Math.Multiply](https://cables.gl/op/Ops.Math.Multiply)

### Multiply3Numbers
![Multiply3Numbers op](images/ops/Ops_Math_Multiply3Numbers.svg)

**Full Name:** `Ops.Math.Multiply3Numbers`

multiply three numbers.

**`\inputsymbol`{=latex} Inputs**

- **R** (Number)
- **G** (Number)
- **B** (Number)
- **Multiply** (Number)

**`\outputsymbol`{=latex} Output**

- **ResultR** (Number)
- **ResultG** (Number)
- **ResultB** (Number)

**Example Patch:** [cables.gl/op/Ops.Math.Multiply3Numbers#example](https://cables.gl/op/Ops.Math.Multiply3Numbers#example)

**Doc:** [cables.gl/op/Ops.Math.Multiply3Numbers](https://cables.gl/op/Ops.Math.Multiply3Numbers)

### Normalize
![Normalize op](images/ops/Ops_Math_Normalize.svg)

**Full Name:** `Ops.Math.Normalize`

normalize a vector.

**`\inputsymbol`{=latex} Inputs**

- **X** (Number)
- **Y** (Number)
- **Z** (Number)

**`\outputsymbol`{=latex} Output**

- **Result X** (Number)
- **Result Y** (Number)
- **Result Z** (Number)

**Example Patch:** [cables.gl/edit/O8S5O8](https://cables.gl/edit/O8S5O8)

**Doc:** [cables.gl/op/Ops.Math.Normalize](https://cables.gl/op/Ops.Math.Normalize)

### NumberDivisible
![NumberDivisible op](images/ops/Ops_Math_NumberDivisible.svg)

**Full Name:** `Ops.Math.NumberDivisible`

is a number capable of being divided.

**`\inputsymbol`{=latex} Inputs**

- **Number** (Number)
- **Divisor** (Number)

**`\outputsymbol`{=latex} Output**

- **Result** (Number)

**Example Patch:** [cables.gl/edit/-IqoJ5](https://cables.gl/edit/-IqoJ5)

**Doc:** [cables.gl/op/Ops.Math.NumberDivisible](https://cables.gl/op/Ops.Math.NumberDivisible)

### OneMinus
![OneMinus op](images/ops/Ops_Math_OneMinus.svg)

**Full Name:** `Ops.Math.OneMinus`

subtract a number from one.

**`\inputsymbol`{=latex} Inputs**

- **Value** (Number)

**`\outputsymbol`{=latex} Output**

- **Result** (Number)

**Example Patch:** [cables.gl/edit/8-XQ5d](https://cables.gl/edit/8-XQ5d)

**Doc:** [cables.gl/op/Ops.Math.OneMinus](https://cables.gl/op/Ops.Math.OneMinus)

### PerlinNoise_v2
![PerlinNoise_v2 op](images/ops/Ops_Math_PerlinNoise_v2.svg)

**Full Name:** `Ops.Math.PerlinNoise_v2`

outputs a perlin noise value like random.

**`\inputsymbol`{=latex} Inputs**

- **X** (Number)
- **Y** (Number)
- **Z** (Number)
- **Scale** (Number)
- **Seed** (Number)

**`\outputsymbol`{=latex} Output**

- **Result** (Number)

**Example Patch:** [cables.gl/edit/gOCdhL](https://cables.gl/edit/gOCdhL)

**Doc:** [cables.gl/op/Ops.Math.PerlinNoise_v2](https://cables.gl/op/Ops.Math.PerlinNoise_v2)

### Pi
![Pi op](images/ops/Ops_Math_Pi.svg)

**Full Name:** `Ops.Math.Pi`

returns PI (3.141592653589793) * multiply amount.

**`\inputsymbol`{=latex} Inputs**

- **Multiply Amount** (Number)

**`\outputsymbol`{=latex} Output**

- **Pi** (Number)

**Example Patch:** [cables.gl/op/Ops.Math.Pi#example](https://cables.gl/op/Ops.Math.Pi#example)

**Doc:** [cables.gl/op/Ops.Math.Pi](https://cables.gl/op/Ops.Math.Pi)

### PointInRectangle2d
![PointInRectangle2d op](images/ops/Ops_Math_PointInRectangle2d.svg)

**Full Name:** `Ops.Math.PointInRectangle2d`

test if a point is in or outside of a rectangle.

**`\inputsymbol`{=latex} Inputs**

- **X** (Number)
- **Y** (Number)
- **Rect Top** (Number)
- **Rect Left** (Number)
- **Rect Right** (Number)
- **Rect Bottom** (Number)

**`\outputsymbol`{=latex} Output**

- **Result** (Number)
- **Pos X** (Number)
- **Pos Y** (Number)

**Example Patch:** [cables.gl/edit/dG4B98](https://cables.gl/edit/dG4B98)

**Doc:** [cables.gl/op/Ops.Math.PointInRectangle2d](https://cables.gl/op/Ops.Math.PointInRectangle2d)

### Pow
![Pow op](images/ops/Ops_Math_Pow.svg)

**Full Name:** `Ops.Math.Pow`

value of x to the power of y.

**`\inputsymbol`{=latex} Inputs**

- **Base** (Number)
- **Exponent** (Number)

**`\outputsymbol`{=latex} Output**

- **Result** (Number)

**Example Patch:** [cables.gl/op/Ops.Math.Pow#example](https://cables.gl/op/Ops.Math.Pow#example)

**Doc:** [cables.gl/op/Ops.Math.Pow](https://cables.gl/op/Ops.Math.Pow)

### PowerOfTwoSize
![PowerOfTwoSize op](images/ops/Ops_Math_PowerOfTwoSize.svg)

**Full Name:** `Ops.Math.PowerOfTwoSize`

Return the next values as power of two.

**`\inputsymbol`{=latex} Inputs**

- **Width** (Number: Integer)
- **Height** (Number: Integer)
- **Strategy Index** (Number: Integer)

**`\outputsymbol`{=latex} Output**

- **Width Result** (Number)
- **Height Result** (Number)

**Example Patch:** [cables.gl/op/Ops.Math.PowerOfTwoSize#example](https://cables.gl/op/Ops.Math.PowerOfTwoSize#example)

**Doc:** [cables.gl/op/Ops.Math.PowerOfTwoSize](https://cables.gl/op/Ops.Math.PowerOfTwoSize)

### Radians
![Radians op](images/ops/Ops_Math_Radians.svg)

**Full Name:** `Ops.Math.Radians`

Converts a degree measurement to its corresponding value in radians.

**`\inputsymbol`{=latex} Inputs**

- **Degrees** (Number)

**`\outputsymbol`{=latex} Output**

- **Result** (Number)

**Example Patch:** [cables.gl/op/Ops.Math.Radians#example](https://cables.gl/op/Ops.Math.Radians#example)

**Doc:** [cables.gl/op/Ops.Math.Radians](https://cables.gl/op/Ops.Math.Radians)

### RandomCounter
![RandomCounter op](images/ops/Ops_Math_RandomCounter.svg)

**Full Name:** `Ops.Math.RandomCounter`

add up random numbers by triggering.

**`\inputsymbol`{=latex} Inputs**

- **Count** (Trigger)
- **Step Min** (Number)
- **Step Max** (Number)

**`\outputsymbol`{=latex} Output**

- **Result** (Number)

**Example Patch:** [cables.gl/edit/I8AxeE](https://cables.gl/edit/I8AxeE)

**Doc:** [cables.gl/op/Ops.Math.RandomCounter](https://cables.gl/op/Ops.Math.RandomCounter)

### RandomNumbers_v3
![RandomNumbers_v3 op](images/ops/Ops_Math_RandomNumbers_v3.svg)

**Full Name:** `Ops.Math.RandomNumbers_v3`

Simple way to get random numbers without using arrays.

**`\inputsymbol`{=latex} Inputs**

- **Seed** (Number)
- **Min** (Number)
- **Max** (Number)

**`\outputsymbol`{=latex} Output**

- **X** (Number)
- **Y** (Number)
- **Z** (Number)
- **W** (Number)

**Example Patch:** [cables.gl/edit/W_z9bI](https://cables.gl/edit/W_z9bI)

**Doc:** [cables.gl/op/Ops.Math.RandomNumbers_v3](https://cables.gl/op/Ops.Math.RandomNumbers_v3)

### RandomNumbersFromString
![RandomNumbersFromString op](images/ops/Ops_Math_RandomNumbersFromString.svg)

**Full Name:** `Ops.Math.RandomNumbersFromString`

Random number generator from a string seed.

**`\inputsymbol`{=latex} Inputs**

- **Input String** (String)
- **Random Number Count** (Number: Integer)

**`\outputsymbol`{=latex} Output**

- **Random Value** (Number)
- **Random Numbers** (Array)

**Example Patch:** [cables.gl/edit/aAaJgt](https://cables.gl/edit/aAaJgt)

**Doc:** [cables.gl/op/Ops.Math.RandomNumbersFromString](https://cables.gl/op/Ops.Math.RandomNumbersFromString)

### RotationFromNormal
![RotationFromNormal op](images/ops/Ops_Math_RotationFromNormal.svg)

**Full Name:** `Ops.Math.RotationFromNormal`

Create rotation matrix from normal.

**`\inputsymbol`{=latex} Inputs**

- **Normal X** (Number)
- **Normal Y** (Number)
- **Normal Z** (Number)
- **Recalculate** (Trigger)

**`\outputsymbol`{=latex} Output**

- **RotationMatrix** (Array)

**Example Patch:** [cables.gl/op/Ops.Math.RotationFromNormal#example](https://cables.gl/op/Ops.Math.RotationFromNormal#example)

**Doc:** [cables.gl/op/Ops.Math.RotationFromNormal](https://cables.gl/op/Ops.Math.RotationFromNormal)

### Round
![Round op](images/ops/Ops_Math_Round.svg)

**Full Name:** `Ops.Math.Round`

Outputs number rounded to the nearest integer.

**`\inputsymbol`{=latex} Inputs**

- **Number** (Number)
- **Decimal Places** (Number: Integer)

**`\outputsymbol`{=latex} Output**

- **Result** (Number)

**Example Patch:** [cables.gl/edit/nPvVW2](https://cables.gl/edit/nPvVW2)

**Doc:** [cables.gl/op/Ops.Math.Round](https://cables.gl/op/Ops.Math.Round)

### RoundEven
![RoundEven op](images/ops/Ops_Math_RoundEven.svg)

**Full Name:** `Ops.Math.RoundEven`

round to the next even number.

**`\inputsymbol`{=latex} Inputs**

- **Number** (Number)
- **Mode Index** (Number: Integer)

**`\outputsymbol`{=latex} Output**

- **Result** (Number)

**Example Patch:** [cables.gl/edit/a0z7hL](https://cables.gl/edit/a0z7hL)

**Doc:** [cables.gl/op/Ops.Math.RoundEven](https://cables.gl/op/Ops.Math.RoundEven)

### SchlickBias
![SchlickBias op](images/ops/Ops_Math_SchlickBias.svg)

**Full Name:** `Ops.Math.SchlickBias`

Custom easing curve via schlick bias and gain.

**`\inputsymbol`{=latex} Inputs**

- **Value** (Number)
- **Gain** (Number)
- **Bias** (Number)

**`\outputsymbol`{=latex} Output**

- **Result** (Number)

**Example Patch:** [cables.gl/edit/FO9IG3](https://cables.gl/edit/FO9IG3)

**Doc:** [cables.gl/op/Ops.Math.SchlickBias](https://cables.gl/op/Ops.Math.SchlickBias)

### Sign
![Sign op](images/ops/Ops_Math_Sign.svg)

**Full Name:** `Ops.Math.Sign`

get sign of value.

**`\inputsymbol`{=latex} Inputs**

- **Value** (Number)
- **Remove Zero** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Result** (Number)

**Example Patch:** [cables.gl/edit/pixllg](https://cables.gl/edit/pixllg)

**Doc:** [cables.gl/op/Ops.Math.Sign](https://cables.gl/op/Ops.Math.Sign)

### SimpleMovingAverage
![SimpleMovingAverage op](images/ops/Ops_Math_SimpleMovingAverage.svg)

**Full Name:** `Ops.Math.SimpleMovingAverage`

Calculate the Average of the last X values.

**`\inputsymbol`{=latex} Inputs**

- **Value** (Number)
- **Number Of Values** (Number: Integer)

**`\outputsymbol`{=latex} Output**

- **Result** (Number)

**Example Patch:** [cables.gl/op/Ops.Math.SimpleMovingAverage#example](https://cables.gl/op/Ops.Math.SimpleMovingAverage#example)

**Doc:** [cables.gl/op/Ops.Math.SimpleMovingAverage](https://cables.gl/op/Ops.Math.SimpleMovingAverage)

### Sine
![Sine op](images/ops/Ops_Math_Sine.svg)

**Full Name:** `Ops.Math.Sine`

Calculates the sine of an angle.

**`\inputsymbol`{=latex} Inputs**

- **Value** (Number)
- **Phase** (Number)
- **Frequency** (Number)
- **Amplitude** (Number)
- **Asine** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Result** (Number)

**Example Patch:** [cables.gl/edit/RhfUW2](https://cables.gl/edit/RhfUW2)

**Doc:** [cables.gl/op/Ops.Math.Sine](https://cables.gl/op/Ops.Math.Sine)

### Speed
![Speed op](images/ops/Ops_Math_Speed.svg)

**Full Name:** `Ops.Math.Speed`

measure speed of how much a value changes.

**`\inputsymbol`{=latex} Inputs**

- **Update** (Trigger)
- **Value** (Number)

**`\outputsymbol`{=latex} Output**

- **Speed** (Number)

**Example Patch:** [cables.gl/edit/Sgmd39](https://cables.gl/edit/Sgmd39)

**Doc:** [cables.gl/op/Ops.Math.Speed](https://cables.gl/op/Ops.Math.Speed)

### Sqrt
![Sqrt op](images/ops/Ops_Math_Sqrt.svg)

**Full Name:** `Ops.Math.Sqrt`

square root of a number.

**`\inputsymbol`{=latex} Inputs**

- **Number** (Number)

**`\outputsymbol`{=latex} Output**

- **Result** (Number)

**Example Patch:** [cables.gl/op/Ops.Math.Sqrt#example](https://cables.gl/op/Ops.Math.Sqrt#example)

**Doc:** [cables.gl/op/Ops.Math.Sqrt](https://cables.gl/op/Ops.Math.Sqrt)

### Subtract
![Subtract op](images/ops/Ops_Math_Subtract.svg)

**Full Name:** `Ops.Math.Subtract`

Subtracts Number2 from Number1 (minus, -).

**`\inputsymbol`{=latex} Inputs**

- **Number1** (Number)
- **Number2** (Number)

**`\outputsymbol`{=latex} Output**

- **Result** (Number)

**Example Patch:** [cables.gl/op/Ops.Math.Subtract#example](https://cables.gl/op/Ops.Math.Subtract#example)

**Doc:** [cables.gl/op/Ops.Math.Subtract](https://cables.gl/op/Ops.Math.Subtract)

### Sum
![Sum op](images/ops/Ops_Math_Sum.svg)

**Full Name:** `Ops.Math.Sum`

Result of the addition.

**`\inputsymbol`{=latex} Inputs**

- **Number1** (Number)
- **Number2** (Number)

**`\outputsymbol`{=latex} Output**

- **Result** (Number)

**Example Patch:** [cables.gl/edit/P7d1r1](https://cables.gl/edit/P7d1r1)

**Doc:** [cables.gl/op/Ops.Math.Sum](https://cables.gl/op/Ops.Math.Sum)

### Tangent
![Tangent op](images/ops/Ops_Math_Tangent.svg)

**Full Name:** `Ops.Math.Tangent`

Calculates the ratio of the sine and cosine of an angle.

**`\inputsymbol`{=latex} Inputs**

- **Value** (Number)
- **Phase** (Number)
- **Frequency** (Number)
- **Amplitude** (Number)
- **Asine** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Result** (Number)

**Example Patch:** [cables.gl/op/Ops.Math.Tangent#example](https://cables.gl/op/Ops.Math.Tangent#example)

**Doc:** [cables.gl/op/Ops.Math.Tangent](https://cables.gl/op/Ops.Math.Tangent)

### TriggerMathExpression
![TriggerMathExpression op](images/ops/Ops_Math_TriggerMathExpression.svg)

**Full Name:** `Ops.Math.TriggerMathExpression`

calculates a user defined mathematical expression.

**`\inputsymbol`{=latex} Inputs**

- **Calculate** (Trigger)
- **Expression** (String)
- **X** (Number)
- **Y** (Number)
- **Z** (Number)
- **W** (Number)
- **A** (Number)
- **B** (Number)
- **C** (Number)
- **D** (Number)
- **I** (Number)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)
- **Result** (Number)
- **Expression Valid** (booleanNumber)

**Example Patch:** [cables.gl/edit/6K7A5f](https://cables.gl/edit/6K7A5f)

**Doc:** [cables.gl/op/Ops.Math.TriggerMathExpression](https://cables.gl/op/Ops.Math.TriggerMathExpression)

### TriggerRandomNumber_v3
![TriggerRandomNumber_v3 op](images/ops/Ops_Math_TriggerRandomNumber_v3.svg)

**Full Name:** `Ops.Math.TriggerRandomNumber_v3`

Generate random number between min and max.

**`\inputsymbol`{=latex} Inputs**

- **Generate** (Trigger)
- **Min** (Number)
- **Max** (Number)
- **Integer** (Number: Boolean)
- **No Consecutive Duplicates** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)
- **Result** (Number)

**Example Patch:** [cables.gl/edit/s3FP7f](https://cables.gl/edit/s3FP7f)

**Doc:** [cables.gl/op/Ops.Math.TriggerRandomNumber_v3](https://cables.gl/op/Ops.Math.TriggerRandomNumber_v3)

### VectorLength
![VectorLength op](images/ops/Ops_Math_VectorLength.svg)

**Full Name:** `Ops.Math.VectorLength`

length of a vector.

**`\inputsymbol`{=latex} Inputs**

- **X** (Number)
- **Y** (Number)
- **Z** (Number)

**`\outputsymbol`{=latex} Output**

- **Length** (Number)

**Example Patch:** [cables.gl/op/Ops.Math.VectorLength#example](https://cables.gl/op/Ops.Math.VectorLength#example)

**Doc:** [cables.gl/op/Ops.Math.VectorLength](https://cables.gl/op/Ops.Math.VectorLength)


