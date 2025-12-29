# Animation & Timeline in Cables.gl

## Introduction

Cables.gl provides multiple ways to create animations, from simple time-based movements to complex keyframed sequences using the timeline.

## Types of Animation

### 1. Procedural Animation
Using math and time to create continuous motion.

### 2. Keyframe Animation
Defining specific values at specific times.

### 3. Physics-Based Animation
Simulating natural motion with springs, gravity, etc.

### 4. Data-Driven Animation
Animating based on input data or user interaction.

## Procedural Animation

### The Time Op

The foundation of procedural animation:

```
Time -> Outputs current time in seconds
```

**Uses:**
- Input for trigonometric functions
- Driving continuous rotation
- Creating loops and cycles

### Basic Movement Patterns

**Linear Movement:**
```
Time -> Modulo (loop duration) -> Position
```

**Oscillation (Sine Wave):**
```
Time -> Sin -> Scale/Position
```

**Bounce:**
```
Time -> Sin -> Abs -> Position
```

**Circular Motion:**
```
Time -> Cos -> X position
Time -> Sin -> Y position
```

### Easing Functions

Transform linear time into smooth curves:

**Ease In (slow start):**
```glsl
t * t  // Quadratic
t * t * t  // Cubic
```

**Ease Out (slow end):**
```glsl
1 - (1 - t) * (1 - t)
```

**Ease In-Out (smooth both):**
```glsl
t < 0.5 ? 2 * t * t : 1 - pow(-2 * t + 2, 2) / 2
```

### The Smooth Op

Smoothly interpolate towards target values:

```
TargetValue -> Smooth -> AnimatedValue
```

**Parameter:**
- `Smoothing` - Higher = slower, smoother transitions

### Spring Animation

Create bouncy, natural motion:

```
TargetValue -> Spring -> AnimatedValue
```

**Parameters:**
- `Stiffness` - How quickly it moves
- `Damping` - How quickly it settles

## Timeline Animation

### Opening the Timeline

1. Click the timeline icon in the toolbar
2. Or press `T` to toggle timeline visibility

### Timeline Interface

```
┌─────────────────────────────────────────────────────┐
│ [Play][Pause][Stop] [Time: 00:00:00]  [BPM: 120]   │
|-─────────────────────────────────────────────────────┤
│ Property Name  │ ●────●────────●────●─────────     │
│ Property 2     │ ●─────────●──────●────────        │
│ Property 3     │ ●───────────────●──────────       │
|-─────────────────────────────────────────────────────┤
│ <- 0s        5s        10s       15s       20s ->    │
`-─────────────────────────────────────────────────────┘
```

### Adding Keyframes

1. Select the op with the property to animate
2. Move the timeline playhead to the desired time
3. Set the value
4. Click the keyframe button (or right-click the property)

### Keyframe Types

- **Linear** - Straight line between keyframes
- **Step** - Instant change at keyframe
- **Ease In** - Slow start
- **Ease Out** - Slow end
- **Ease In-Out** - Smooth start and end
- **Bezier** - Custom curve with handles

### Editing Keyframes

- **Move:** Drag keyframe left/right (time) or up/down (value)
- **Delete:** Select and press Delete
- **Copy/Paste:** Ctrl+C, Ctrl+V
- **Multi-select:** Shift+click or drag box

### Timeline Tracks

Organize animations into tracks:

- **Property tracks** - Individual values
- **Trigger tracks** - Fire events at specific times
- **Audio tracks** - Sync with music

## Non-Linear Animation Clips (New Animation System - November 2025)

The new animation system in Cables.gl introduces powerful non-linear animation capabilities through **animation clips**. Clips are reusable, addable, and mixable animation sequences that can be layered and blended to create complex motion.

### What Are Animation Clips?

Animation clips are self-contained animation sequences that can be:
- **Reusable** - Create once, apply to multiple parameters
- **Addable** - Layer multiple clips together (additive blending)
- **Mixable** - Blend between clips with different weights
- **Non-linear** - Don't require strict sequential playback

### Creating Animation Clips

#### Step 1: Enable Clip Mode

1. Add an **Anim** operator to your patch
2. Connect it to the parameter you want to animate
3. Open the Anim operator's properties
4. Enable the **Clip** option
5. Assign a **Clip Name** (e.g., "bounce", "fadeIn", "rotate360")

```
Parameter -> Anim (Clip enabled, Name: "myClip") -> Animated Value
```

#### Step 2: Define Keyframes

1. With the Anim operator selected, open the Timeline
2. Set keyframes for your animation sequence
3. Adjust easing curves and timing
4. The animation is now stored as a named clip

#### Step 3: Apply Clips to Other Parameters

Once created, clips can be applied to any other Anim operator:

1. Add another Anim operator
2. In the Timeline, right-click on a keyframe
3. Select "Apply Clip" and choose your clip name
4. The clip's animation will be applied at that keyframe

### Clip Properties and Options

#### Looping Modes

Clips support different looping behaviors:

- **None** - Play once and stop
- **Repeat** - Loop from start to end
- **Mirror** - Play forward, then backward
- **Offset** - Continue from end value

#### Interpolation Methods

- **Linear** - Straight interpolation
- **Ease In/Out** - Smooth acceleration/deceleration
- **Bezier** - Custom curve control
- **Step** - Instant value changes

### Additive Animation (Layering Clips)

Multiple clips can be **added together** to create combined effects:

```
Base Value
    |
Anim Clip 1 ("bounce") -> Add
    |
Anim Clip 2 ("rotate") -> Add
    |
Anim Clip 3 ("scale") -> Add
    |
Final Animated Value
```

**Use Cases:**
- Base idle animation + triggered bounce effect
- Procedural motion + keyframed structure
- Multiple independent motion layers

**Example: Character Animation**
```
Idle Clip (continuous breathing)
    |
Walk Clip (additive, triggered on movement)
    |
Jump Clip (additive, triggered on jump)
    |
Final Position
```

### Mixable Animation (Blending Clips)

Clips can be **mixed** with different weights to blend between animations:

```
Clip A ("walk") -> Mix (weight: 0.7)
Clip B ("run")  -> Mix (weight: 0.3)
    |
Blended Animation
```

**Blending Modes:**
- **Linear Blend** - Simple weighted average
- **Smooth Blend** - Eased transition between clips
- **Additive Blend** - Add clips together with weights

**Example: Walk-to-Run Transition**
```
Walk Clip -> Mix (weight: 1.0 - runProgress)
Run Clip  -> Mix (weight: runProgress)
    |
Smooth transition from walk to run
```

### Clip Management

#### Organizing Clips

Clips are stored within your project and can be:
- **Renamed** - Right-click clip in timeline -> Rename
- **Duplicated** - Copy clip to create variations
- **Deleted** - Remove unused clips
- **Exported/Imported** - Share clips between projects

#### Clip Library

Access all clips in your project:
1. Open Timeline
2. Click "Clips" tab
3. View all available clips
4. Drag clips onto timeline tracks

### Advanced Clip Techniques

#### Clip Offsets and Time Remapping

Apply clips at different time offsets:

```
Clip "bounce" (duration: 2s)
    |
Apply at t=0s: Full clip
Apply at t=5s: Clip starts here
Apply at t=10s: Clip with 0.5x speed (time remap)
```

#### Clip Masking

Use clips to mask or modulate other animations:

```
Base Animation -> Multiply
Clip "mask" (0 to 1) -> Multiply
    |
Masked Animation (only active where mask = 1)
```

#### Conditional Clip Playback

Control clip playback based on conditions:

```
Condition -> If
    |--> True: Play Clip A
    `--> False: Play Clip B
```

## JavaScript Custom Op Integration with Animation System

The new animation system integrates seamlessly with JavaScript custom operators, allowing programmatic control and extension of animation capabilities.

### Accessing Animation Data from Custom Ops

#### Reading Animation Values

```javascript
// Get current animation value from an Anim op
const animOp = op.patch.findOpByName("MyAnimOp");
if (animOp) {
    const currentValue = animOp.outValue.get();
    // Use the animated value
}
```

#### Monitoring Animation State

```javascript
const inTrigger = op.inTrigger("Render");
const outAnimValue = op.outNumber("Animation Value");
const outIsPlaying = op.outBool("Is Playing");

let animOp = null;

// Find the Anim op (call once on init)
op.onInit = function() {
    animOp = op.patch.findOpByName("MyAnimOp");
};

inTrigger.onTriggered = function() {
    if (animOp) {
        // Get current animated value
        outAnimValue.set(animOp.outValue.get());
        
        // Check if timeline is playing
        const timeline = op.patch.timeline;
        if (timeline) {
            outIsPlaying.set(timeline.isPlaying());
        }
    }
};
```

### Controlling Timeline from Custom Ops

#### Playback Control

```javascript
const inPlay = op.inTriggerButton("Play");
const inPause = op.inTriggerButton("Pause");
const inStop = op.inTriggerButton("Stop");
const inSeek = op.inFloat("Seek Time", 0);
const inSeekTrigger = op.inTrigger("Seek");

inPlay.onTriggered = function() {
    const timeline = op.patch.timeline;
    if (timeline) timeline.play();
};

inPause.onTriggered = function() {
    const timeline = op.patch.timeline;
    if (timeline) timeline.pause();
};

inStop.onTriggered = function() {
    const timeline = op.patch.timeline;
    if (timeline) timeline.stop();
};

inSeekTrigger.onTriggered = function() {
    const timeline = op.patch.timeline;
    if (timeline) {
        timeline.seek(inSeek.get());
    }
};
```

#### Timeline Time and Progress

```javascript
const inTrigger = op.inTrigger("Render");
const outTime = op.outNumber("Current Time");
const outProgress = op.outNumber("Progress (0-1)");
const outDuration = op.outNumber("Total Duration");

inTrigger.onTriggered = function() {
    const timeline = op.patch.timeline;
    if (timeline) {
        const currentTime = timeline.getTime();
        const duration = timeline.getDuration();
        
        outTime.set(currentTime);
        outDuration.set(duration);
        outProgress.set(duration > 0 ? currentTime / duration : 0);
    }
};
```

### Creating Animation Clips Programmatically

#### Generating Clip Data

```javascript
// Custom op that generates animation clip data
const inDuration = op.inFloat("Duration", 2.0);
const inAmplitude = op.inFloat("Amplitude", 1.0);
const inFrequency = op.inFloat("Frequency", 1.0);
const inGenerate = op.inTriggerButton("Generate Clip");
const outClipData = op.outObject("Clip Data");

inGenerate.onTriggered = function() {
    const duration = inDuration.get();
    const amplitude = inAmplitude.get();
    const freq = inFrequency.get();
    const sampleRate = 60; // samples per second
    const numSamples = Math.floor(duration * sampleRate);
    
    const keyframes = [];
    for (let i = 0; i <= numSamples; i++) {
        const t = i / numSamples;
        const time = t * duration;
        // Generate sine wave animation
        const value = Math.sin(time * freq * Math.PI * 2) * amplitude;
        keyframes.push({
            time: time,
            value: value,
            easing: "easeInOut"
        });
    }
    
    outClipData.set({
        name: "generatedSine",
        duration: duration,
        keyframes: keyframes,
        loop: "repeat"
    });
};
```

### Manipulating Animation Clips

#### Blending Multiple Clips

```javascript
// Custom op that blends multiple animation clips
const inClipA = op.inObject("Clip A Data");
const inClipB = op.inObject("Clip B Data");
const inBlendFactor = op.inFloat("Blend Factor", 0.5); // 0 = A, 1 = B
const inTime = op.inFloat("Time", 0);
const outBlendedValue = op.outNumber("Blended Value");

inTime.onChange = function() {
    const clipA = inClipA.get();
    const clipB = inClipB.get();
    const blend = inBlendFactor.get();
    const t = inTime.get();
    
    if (!clipA || !clipB) return;
    
    // Sample both clips at time t
    const valueA = sampleClip(clipA, t);
    const valueB = sampleClip(clipB, t);
    
    // Blend
    const blended = valueA * (1 - blend) + valueB * blend;
    outBlendedValue.set(blended);
};

function sampleClip(clip, time) {
    const keyframes = clip.keyframes;
    if (!keyframes || keyframes.length === 0) return 0;
    
    // Clamp time to clip duration
    time = time % clip.duration;
    
    // Find surrounding keyframes
    for (let i = 0; i < keyframes.length - 1; i++) {
        if (time >= keyframes[i].time && time <= keyframes[i + 1].time) {
            // Interpolate
            const t0 = keyframes[i].time;
            const t1 = keyframes[i + 1].time;
            const v0 = keyframes[i].value;
            const v1 = keyframes[i + 1].value;
            
            const t = (time - t0) / (t1 - t0);
            return v0 + (v1 - v0) * t;
        }
    }
    
    return keyframes[keyframes.length - 1].value;
}
```

#### Additive Clip Combination

```javascript
// Custom op that adds multiple clips together
const inClips = op.inArray("Clips Array");
const inTime = op.inFloat("Time", 0);
const outCombinedValue = op.outNumber("Combined Value");

inTime.onChange = function() {
    const clips = inClips.get();
    const t = inTime.get();
    
    if (!clips || clips.length === 0) {
        outCombinedValue.set(0);
        return;
    }
    
    let sum = 0;
    for (let i = 0; i < clips.length; i++) {
        const clip = clips[i];
        if (clip && clip.keyframes) {
            sum += sampleClip(clip, t);
        }
    }
    
    outCombinedValue.set(sum);
};
```

### Advanced: Custom Easing Functions

```javascript
// Custom op with advanced easing functions
const inValue = op.inFloat("Input (0-1)", 0);
const inEasingType = op.inSwitch("Easing", 
    ["linear", "easeInQuad", "easeOutQuad", "easeInOutQuad", 
     "easeInCubic", "easeOutCubic", "easeInOutCubic",
     "easeInElastic", "easeOutBounce"], 
    "easeInOutQuad");
const outEased = op.outNumber("Eased Value");

inValue.onChange = function() {
    const t = Math.max(0, Math.min(1, inValue.get()));
    const type = inEasingType.get();
    let eased = 0;
    
    switch(type) {
        case "linear":
            eased = t;
            break;
        case "easeInQuad":
            eased = t * t;
            break;
        case "easeOutQuad":
            eased = 1 - (1 - t) * (1 - t);
            break;
        case "easeInOutQuad":
            eased = t < 0.5 
                ? 2 * t * t 
                : 1 - Math.pow(-2 * t + 2, 2) / 2;
            break;
        case "easeInCubic":
            eased = t * t * t;
            break;
        case "easeOutCubic":
            eased = 1 - Math.pow(1 - t, 3);
            break;
        case "easeInOutCubic":
            eased = t < 0.5
                ? 4 * t * t * t
                : 1 - Math.pow(-2 * t + 2, 3) / 2;
            break;
        case "easeInElastic":
            const c4 = (2 * Math.PI) / 3;
            eased = t === 0 ? 0 : t === 1 ? 1 
                : -Math.pow(2, 10 * t - 10) * Math.sin((t * 10 - 10.75) * c4);
            break;
        case "easeOutBounce":
            const n1 = 7.5625;
            const d1 = 2.75;
            if (t < 1 / d1) {
                eased = n1 * t * t;
            } else if (t < 2 / d1) {
                eased = n1 * (t -= 1.5 / d1) * t + 0.75;
            } else if (t < 2.5 / d1) {
                eased = n1 * (t -= 2.25 / d1) * t + 0.9375;
            } else {
                eased = n1 * (t -= 2.625 / d1) * t + 0.984375;
            }
            break;
    }
    
    outEased.set(eased);
};
```

### Real-Time Animation Modification

```javascript
// Custom op that modifies animation in real-time based on input
const inBaseAnim = op.inObject("Base Animation Clip");
const inModifier = op.inFloat("Modifier", 1.0);
const inTime = op.inFloat("Time", 0);
const outModifiedValue = op.outNumber("Modified Value");

inTime.onChange = function() {
    const clip = inBaseAnim.get();
    const mod = inModifier.get();
    const t = inTime.get();
    
    if (!clip) return;
    
    // Sample base animation
    let value = sampleClip(clip, t);
    
    // Apply modifier (could be scale, offset, etc.)
    value *= mod;
    
    outModifiedValue.set(value);
};
```

### Integration Example: Physics-Driven Animation

```javascript
// Custom op that combines physics simulation with animation clips
const inAnimClip = op.inObject("Animation Clip");
const inPhysicsForce = op.inFloat("Physics Force", 0);
const inDamping = op.inFloat("Damping", 0.9);
const inTime = op.inFloat("Time", 0);
const outCombinedValue = op.outNumber("Combined Value");

let velocity = 0;
let position = 0;

inTime.onChange = function() {
    const clip = inAnimClip.get();
    const force = inPhysicsForce.get();
    const damp = inDamping.get();
    const t = inTime.get();
    
    // Get base animation value
    const animValue = clip ? sampleClip(clip, t) : 0;
    
    // Apply physics
    velocity += force;
    velocity *= damp;
    position += velocity;
    
    // Combine animation + physics
    const combined = animValue + position;
    outCombinedValue.set(combined);
};
```

### Best Practices for Animation + Custom Ops

1. **Cache Clip Sampling** - If sampling clips every frame, cache results when time hasn't changed
2. **Batch Operations** - Process multiple clips in one op rather than multiple ops
3. **Use Native Anim Op When Possible** - Only use custom ops when you need functionality beyond built-in features
4. **Optimize Keyframe Lookups** - Use binary search for large clip keyframe arrays
5. **Handle Edge Cases** - Always check for null/undefined clips and handle time out of bounds

### Example: Complete Animation Controller Op

```javascript
// Comprehensive animation controller custom op
const inPlay = op.inTriggerButton("Play");
const inPause = op.inTriggerButton("Pause");
const inStop = op.inTriggerButton("Stop");
const inSeek = op.inFloat("Seek", 0);
const inSpeed = op.inFloat("Speed", 1.0);
const inLoop = op.inBool("Loop", true);

const outTime = op.outNumber("Current Time");
const outProgress = op.outNumber("Progress");
const outIsPlaying = op.outBool("Is Playing");

let currentTime = 0;
let isPlaying = false;
let lastFrameTime = 0;

op.onInit = function() {
    lastFrameTime = op.patch.timer.getTime();
};

const inRender = op.inTrigger("Render");
inRender.onTriggered = function() {
    const now = op.patch.timer.getTime();
    const delta = now - lastFrameTime;
    lastFrameTime = now;
    
    if (isPlaying) {
        currentTime += delta * inSpeed.get();
        
        const timeline = op.patch.timeline;
        if (timeline) {
            const duration = timeline.getDuration();
            if (currentTime >= duration) {
                if (inLoop.get()) {
                    currentTime = currentTime % duration;
                } else {
                    currentTime = duration;
                    isPlaying = false;
                }
            }
            
            timeline.seek(currentTime);
        }
    }
    
    outTime.set(currentTime);
    const timeline = op.patch.timeline;
    if (timeline) {
        const duration = timeline.getDuration();
        outProgress.set(duration > 0 ? currentTime / duration : 0);
    }
    outIsPlaying.set(isPlaying);
};

inPlay.onTriggered = function() {
    isPlaying = true;
    const timeline = op.patch.timeline;
    if (timeline) timeline.play();
};

inPause.onTriggered = function() {
    isPlaying = false;
    const timeline = op.patch.timeline;
    if (timeline) timeline.pause();
};

inStop.onTriggered = function() {
    isPlaying = false;
    currentTime = 0;
    const timeline = op.patch.timeline;
    if (timeline) {
        timeline.stop();
        timeline.seek(0);
    }
};

inSeek.onChange = function() {
    currentTime = inSeek.get();
    const timeline = op.patch.timeline;
    if (timeline) timeline.seek(currentTime);
};
```

## Sequence and Timing Ops

### Sequence

Chain multiple actions in order:

```
Trigger -> Sequence
             |--> Action 1
             |--> Action 2 (after delay)
             `--> Action 3 (after delay)
```

### Delay

Pause before triggering:

```
Trigger -> Delay (seconds) -> DelayedAction
```

### Timer

Count down or up:

```
StartTrigger -> Timer -> TimeValue
```

### Interval

Trigger repeatedly:

```
Interval (every X seconds) -> RepeatedAction
```

## Animation Patterns

### Staggered Animation

Animate multiple items with offset timing:

```
ArrayIterator
    |
Index -> Delay offset
    |
AnimatedProperty
```

### Loop with Pause

```
Time -> Modulo (total duration)
     -> If < activeTime: animate
     -> Else: hold at end value
```

### Ping-Pong (Back and Forth)

```
Time -> Sin -> Map to range -> Property
```
Or with timeline: set keyframes to go forward then backward.

### One-Shot Animation

```
Trigger -> SetValue (start)
       -> Smooth -> AnimatedValue
```

## State Machines

Create complex animation logic:

### Simple States

```javascript
// In custom op
let state = "idle";

function setState(newState) {
    state = newState;
    switch(state) {
        case "idle":
            // Set idle animation params
            break;
        case "active":
            // Set active animation params
            break;
        case "exit":
            // Set exit animation params
            break;
    }
}
```

### Transition Between States

Use Smooth or Spring ops to blend between state values.

## Interactive Animation

### Mouse-Based

```
MouseX -> Map to range -> Target value -> Smooth -> Property
```

### Scroll-Based

```
ScrollPosition -> Map (0 to page height) -> (0 to 1) -> Animation progress
```

### Click-Triggered

```
MouseClick -> Toggle state -> Smooth -> Animated property
```

## Advanced Animation Systems (How to Build “Scenes”)

As patches grow, animation becomes less about a single value moving and more about **systems**:

- multiple objects animated together (“shots” / “scenes”)
- blending procedural motion with keyframed structure
- sequencing events reliably (no double-triggers, no race conditions)
- keeping things readable and maintainable

### Layering: Timeline for Structure, Procedural for Life

A reliable pattern is:

- **Timeline**: controls the big structure (when things appear, when the camera moves, when a section starts/ends)
- **Procedural**: adds micro-motion (subtle noise, breathing, idle motion, wobble)

Example idea:

```
Timeline -> Base position
Time -> Sin (small) -> Add
Result -> Transform position
```

### Shot-Based Timelines (Cinematic Organization)

Instead of one giant timeline track list, treat the timeline as a set of “shots”:

- Shot 1: intro framing
- Shot 2: reveal
- Shot 3: close-up detail
- Shot 4: outro / logo

Each shot has:

- a start time, end time
- a camera pose
- a set of object visibility/alpha states

### Animation Curves: Clamp Early, Map Late

If you see overshoot or sudden jumps, it’s usually a range mismatch.

Good practice:

- normalize to 0..1 early
- clamp to 0..1 before sensitive operations
- map to target range at the end

Conceptually:

```
t (0..1) -> Clamp -> Ease -> Map (min..max)
```

### Reusable “Rig” Pattern

For any object you animate often, create a mini rig:

- one Transform for position
- one Transform for rotation
- one Transform for scale
- optional “wobble” layer

This makes it easy to swap animation sources later without rewiring the whole patch.

### Avoiding Jitter in Interactive Animation

If input is noisy (mouse, audio, sensors):

- map input into a safe range
- apply Smooth/Spring
- optionally add dead zones

```
Input -> Map -> Clamp -> Smooth -> Property
```

### Choreographing Triggers Reliably

For sequences of actions:

- use `Sequence` for deterministic ordering
- use `Delay` for spacing
- use `Interval` for periodic triggers

The key is to avoid “implicit timing” where the order depends on frame timing.

## Advanced Recipes

### Recipe: Scroll-Driven Scene (Interactive Storytelling)

Use scroll position as a normalized progress value:

```
ScrollPosition -> Map (0..pageHeight -> 0..1) -> Clamp -> progress
progress -> Ease -> Drive camera/object parameters
```

Then you can tie multiple properties to the same progress signal for a coherent experience.

### Recipe: Beat-Synced Timeline Sections

Use BPM sync to trigger timeline jumps or section changes:

```
AudioFile -> BPMSync -> Beat trigger
Beat trigger -> Sequence -> (advance state) -> set target animation values
```

### Recipe: One-Shot “Punch” Animation (No Keyframes)

Great for UI hits, impacts, kick drums:

```
Trigger -> SetValue (1)
       -> Smooth (fast decay) -> scale/brightness
```

You can combine a fast rise + slower decay by chaining two Smooth ops with different parameters.

### Recipe: Camera Rig (Orbit + Handheld Micro Motion)

```
Time -> Sin/Cos -> Orbit position
Random (small) -> Smooth -> micro offset
Add (orbit + micro) -> Camera position
LookAt -> Camera aim
```

This produces camera movement that feels “alive” but still controlled.

## Practical Examples

### Example 1: Bouncing Ball

```
MainLoop
    |
BasicMaterial
    |
Time -> Sin -> Abs -> Y position
    |
Transform
    |
Circle
```

### Example 2: Rotating Carousel

```
MainLoop
    |
Camera
    |
ArrayIterator (items)
    |
Time + (Index * offset) -> Cos -> X position
Time + (Index * offset) -> Sin -> Z position
    |
Transform
    |
Item
```

### Example 3: Fade In Sequence

```
MainLoop
    |
BasicMaterial
    |
ArrayIterator
    |
Time - (Index * staggerDelay) -> Clamp (0, 1) -> BasicMaterial (alpha input)
    |
Shape
```

### Example 4: Timeline-Based Scene

```
Timeline
|-── 0s: Camera position keyframe
|-── 2s: Object appears (alpha 0->1)
|-── 4s: Object rotates
|-── 6s: Color change
`-── 8s: Fade out
```

### Example 5: Layered Animation Clips (Additive)

Create a character with multiple animation layers:

```
Base Position (0, 0, 0)
    |
Anim Clip "idleBreath" (vertical oscillation) -> Add
    |
Anim Clip "walkCycle" (horizontal movement, triggered) -> Add
    |
Anim Clip "jump" (vertical boost, triggered) -> Add
    |
Final Position -> Transform
```

**Setup:**
1. Create "idleBreath" clip: 2-second vertical sine wave (amplitude: 0.1)
2. Create "walkCycle" clip: 1-second horizontal movement (0 to 1, repeat)
3. Create "jump" clip: 0.5-second vertical boost (0 to 2, one-shot)
4. Connect all three Anim ops to Add ops in sequence
5. Trigger walkCycle and jump clips via user input

### Example 6: Blended Animation Clips (Mixable)

Smooth transition between walk and run:

```
Walk Clip -> Anim (weight: 1.0 - runBlend)
Run Clip  -> Anim (weight: runBlend)
    |
Mix -> Final Position
```

**Setup:**
1. Create "walk" clip: slow horizontal movement
2. Create "run" clip: fast horizontal movement
3. Use a Smooth op to blend between 0 (walk) and 1 (run)
4. Connect both clips to Mix op with blend factor

### Example 7: Reusable Clip System

Create a library of reusable animation clips:

```
Clip Library:
- "fadeIn" (alpha 0->1, 1s, easeOut)
- "fadeOut" (alpha 1->0, 1s, easeIn)
- "bounce" (scale 1->1.2->1, 0.5s, easeOut)
- "slideInLeft" (x: -100->0, 1s, easeOut)
- "rotate360" (rotation 0->360, 2s, linear)

Apply to multiple objects:
Object 1: fadeIn at t=0s, bounce at t=2s
Object 2: slideInLeft at t=1s, fadeOut at t=5s
Object 3: rotate360 at t=3s (looping)
```

### Example 8: JavaScript-Controlled Animation

Custom op that controls animation based on game state:

```
Game State -> Custom Op
    |--> State = "idle": Play "idle" clip
    |--> State = "walk": Play "walk" clip
    |--> State = "run": Play "run" clip
    `--> State = "jump": Play "jump" clip (one-shot)
    |
Selected Clip -> Anim -> Position
```

**Custom Op Code:**
```javascript
const inState = op.inString("State", "idle");
const inTime = op.inFloat("Time", 0);
const outClipName = op.outString("Clip Name");
const outValue = op.outNumber("Animation Value");

let currentClip = null;

inState.onChange = function() {
    const state = inState.get();
    switch(state) {
        case "idle":
            currentClip = "idle";
            break;
        case "walk":
            currentClip = "walk";
            break;
        case "run":
            currentClip = "run";
            break;
        case "jump":
            currentClip = "jump";
            break;
    }
    outClipName.set(currentClip);
};

inTime.onChange = function() {
    // Sample the current clip
    if (currentClip) {
        const animOp = op.patch.findOpByName("Anim_" + currentClip);
        if (animOp) {
            outValue.set(animOp.outValue.get());
        }
    }
};
```

### Example 9: Physics + Animation Clip Hybrid

Combine procedural physics with keyframed animation:

```
Anim Clip "baseMotion" (keyframed path)
    |
Add
Physics Force (gravity, wind) -> Integrate -> Add
    |
Final Position
```

**Custom Op for Physics Integration:**
```javascript
const inAnimValue = op.inFloat("Animation Value", 0);
const inPhysicsForce = op.inFloat("Physics Force", 0);
const inDamping = op.inFloat("Damping", 0.95);
const inRender = op.inTrigger("Render");
const outCombined = op.outNumber("Combined Value");

let velocity = 0;
let position = 0;

inRender.onTriggered = function() {
    const delta = op.patch.timer.getDelta();
    const anim = inAnimValue.get();
    const force = inPhysicsForce.get();
    const damp = inDamping.get();
    
    // Update physics
    velocity += force * delta;
    velocity *= damp;
    position += velocity * delta;
    
    // Combine with animation
    outCombined.set(anim + position);
};
```

### Example 10: Conditional Clip Playback

Play different clips based on conditions:

```
Condition A -> If (True: Clip A, False: Clip B)
Condition B -> If (True: Clip C, False: Clip D)
    |
Mix (blend between conditional results)
    |
Final Animation
```

## Performance Tips

1. **Limit active animations** - Don't animate everything
2. **Use requestAnimationFrame** - Built into cables.gl
3. **Cache calculations** - Don't recalculate every frame
4. **Simplify when far** - Reduce animation complexity for distant objects
5. **Use GPU** - Animate in shaders when possible

## Debugging Animation

### Slow Motion

```
Time -> Multiply (0.1) -> SlowTime
```

### Visualize Values

Add a `DrawNumber` op to see animated values in real-time.

### Pause at Problem

Use timeline pause to inspect a specific frame.

## Featured Videos

<!-- Add animation videos here -->

<!-- Example:
```vid
https://youtu.be/XXXXX
Title: Timeline Animation in Cables.gl
Author: Channel Name
Thumbnail: https://i.ytimg.com/vi/XXXXX/mqdefault.jpg
```
-->

## Exercises

### Basic Animation
1. Create a loading animation with staggered dots
2. Build an interactive hover animation
3. Design a full intro sequence with timeline
4. Create a physics-based pendulum

### Animation Clips
5. Create a reusable "bounce" clip and apply it to 5 different objects
6. Build a character animation system with 3 additive clips (idle, walk, jump)
7. Create a smooth walk-to-run transition using clip blending
8. Design a clip library with 5 common animations (fade, slide, scale, rotate, bounce)

### JavaScript Integration
9. Build a custom op that generates a sine wave animation clip programmatically
10. Create an animation controller op with play/pause/stop/seek functionality
11. Design a custom op that blends two animation clips with a configurable blend factor
12. Build a state machine op that switches between different animation clips based on input

### Advanced
13. Combine procedural animation (Time -> Sin) with a keyframed clip using additive blending
14. Create a custom easing function op and apply it to an animation clip
15. Build a system that plays different animation clips based on user interaction (mouse, keyboard, touch)
16. Design a complex scene with multiple objects, each using a combination of clips and procedural motion

---

**Previous**: [<- Audio & Sound](08-audio-sound.md) | **Next**: [Export & Deployment ->](10-export-deployment.md)


