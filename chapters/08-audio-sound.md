# Audio & Sound in Cables.gl

## Introduction

Cables.gl has powerful audio capabilities, enabling you to create audio-reactive visuals, music visualizations, and interactive sound experiences.

## Audio Sources

### AudioFile

Load and play audio files:

```
AudioFile -> AudioAnalyzer -> Visual ops
```

**Supported Formats:**
- MP3
- WAV
- OGG

**Key Parameters:**
- `URL` - Path to audio file
- `Loop` - Repeat playback
- `Volume` - Playback volume
- `Playback Rate` - Speed control

### Microphone

Capture live audio input:

```
Microphone -> AudioAnalyzer -> Visual ops
```

**Note:** Requires user permission in browser.

### AudioBuffer

Load audio into memory for precise control.

### WebAudio Oscillator

Generate synthetic sounds:

```
Oscillator -> Audio output
```

**Types:**
- Sine
- Square
- Sawtooth
- Triangle

## Audio Analysis

### AudioAnalyzer

The core op for audio-reactive visuals:

```
AudioSource -> AudioAnalyzer
                   |
    Outputs: FFT, Volume, Bass, Mid, High
```

**Key Outputs:**
- `FFT Array` - Frequency spectrum data
- `Volume` - Overall loudness
- `Bass` - Low frequency level
- `Mid` - Middle frequency level
- `High` - High frequency level

### FFT (Fast Fourier Transform)

Breaks audio into frequency bands:

```
AudioAnalyzer -> FFTArray -> ArrayIterator
                              |
                        Visualize each band
```

**FFT Size Options:**
- 32, 64, 128, 256, 512, 1024, 2048, 4096
- Larger = more detail, but slower

### Smoothing

Apply smoothing to prevent jittery visuals:

```
AudioValue -> Smooth -> Visual parameter
```

## Common Audio-Reactive Patterns

### Volume-Based Scaling

```
AudioAnalyzer (volume) -> Scale input of shape
```

### Frequency Band Visualization

```
MainLoop
    |
BasicMaterial
    |
AudioAnalyzer -> FFTArray
    |
ArrayIterator
    |
Transform (X position from index)
    |
Transform (Y scale from FFT value)
    |
Rectangle
```

### Color from Audio

```
AudioAnalyzer (bass) -> Hue input of HSBtoRGB
HSBtoRGB -> BasicMaterial (color input)
```

### Beat Detection

```
AudioAnalyzer (volume) -> Threshold -> Trigger
                             |
                    (triggers on beat)
```

## Audio Effects

### Gain

Control volume:

```
AudioSource -> Gain -> Output
```

### Filter

Shape the frequency content:

```
AudioSource -> Filter -> Output
```

**Filter Types:**
- Lowpass - Removes high frequencies
- Highpass - Removes low frequencies  
- Bandpass - Keeps only middle frequencies
- Notch - Removes specific frequency

### Delay

Add echo effect:

```
AudioSource -> Delay -> Output
```

### Reverb

Add space/ambience:

```
AudioSource -> Reverb -> Output
```

### Compressor

Even out dynamics:

```
AudioSource -> Compressor -> Output
```

## Building a Visualizer

### Step 1: Set Up Audio

```
AudioFile (your music)
    |
AudioAnalyzer
```

### Step 2: Create Base Render

```
MainLoop
    |
Camera (for 3D) or BasicMaterial (for 2D)
```

### Step 3: Add Audio-Reactive Elements

**Example: Pulsing Circle**

```
MainLoop -> BasicMaterial
                |
AudioAnalyzer (volume)
    |
Smooth (for smoother animation)
    |
Math (multiply by desired scale)
    |
Circle (size input)
```

### Step 4: Add Frequency Visualization

```
AudioAnalyzer -> FFTArray
    |
ArrayIterator (iterate through frequencies)
    |
Index -> Calculate X position
    |
FFT Value -> Calculate height/color
    |
Rectangle (bar for each frequency)
```

## Synchronizing to Music

### BPM and Beat Sync

```
AudioFile
    |
BPMSync (set your song's BPM)
    |
Beat triggers for animations
```

### Timeline with Audio

1. Load audio file
2. Add to timeline
3. Use timeline markers for sync points
4. Keyframe animations to match audio

## Advanced Audio Techniques (Make It Feel “Musical”)

Audio-reactive visuals often fail in the same way: they’re *too jittery* and *too literal*. The goal is usually:

- stable motion with **musical** response (not “random noise” response)
- clear separation between **slow energy** (overall level) and **fast transients** (kicks/snare hits)
- mappings that feel good: log frequency, clamped ranges, smoothing that doesn’t lag

### Technique: Energy vs Transient (Two-Signal Approach)

Treat audio as two complementary control signals:

- **Energy**: smoothed volume/bass/mid/high (drives slow changes: camera drift, fog density, palette)
- **Transients**: thresholded + debounced triggers (drives discrete events: flashes, spawns, scene cuts)

**Typical building blocks:**

```
AudioAnalyzer (volume/bass/mid/high)
  +-> Smooth (slow) -> Energy signal
  +-> Threshold -> (optional Delay/Interval gating) -> Transient trigger
```

### Technique: Log Frequency Mapping (Better Spectra)

FFT bins are linear in frequency, but our hearing is closer to logarithmic. If your spectrum visualization looks “all action on the left”, try mapping indices in a non-linear way:

- compress the low bins less (give bass more space)
- compress high bins more (reduce over-detail)

Conceptually:

```
Index -> Normalize (0..1) -> Pow (curve) -> Sample FFT
```

### Technique: Peak Hold (Readable Visuals)

Human-friendly meters often have a “peak hold” that decays slowly. You can build this by:

- capturing the max value over a short window
- then decaying it over time

Conceptually:

```
AudioValue -> Max (with previous peak) -> Decay over time -> Peak output
```

### Technique: Band-Specific Control (Bass Drives Scale, High Drives Detail)

Instead of driving everything from overall volume:

- **bass** -> big scale/position changes
- **mid** -> color shifts or mid-size motion
- **high** -> small jitter/detail/particles

This makes visuals feel much more “mixed”.

### Technique: Audio -> Shader (The “Pro” Move)

Shading is where audio-reactive projects often become cinematic.

High-level pattern:

```
AudioAnalyzer (energy) -> Smooth -> Shader uniform (e.g., amount)
FFTArray -> (reduce / select bands) -> Shader uniform(s)
Time -> Shader uniform (time)
```

Then, in the shader, use audio as **a modulation source**, not as the final value. (Example: warp UVs slightly, not wildly.)

## Advanced Patch Recipes

### Recipe: Stable Beat Trigger (Avoid Double-Triggers)

The simplest fix for “machine-gun” beats is gating:

```
AudioAnalyzer (volume or bass)
  |
Threshold (set just above noise floor)
  |
(Gate / minimum time between triggers)
  |
Trigger (spawn / flash / step timeline)
```

### Recipe: Audio-Reactive Post-Processing

Drive a texture effect strength from music:

```
MainLoop -> Camera -> RenderToTexture -> TextureEffect -> Output
                          ^
AudioAnalyzer (volume) -> Smooth -> Map -> effect strength
```

### Recipe: Audio-Reactive 3D Equalizer (Optimized)

If you build an equalizer with many bars:

- keep geometry simple
- reduce FFT size to what you need
- avoid doing heavy work per bar per frame

Conceptually:

```
AudioAnalyzer -> FFTArray
  |
ArrayIterator (N bands)
  |
Transform (X from index, Y scale from FFT)
  |
Cube (bar)
```

### Recipe: Audio-Driven Palette

Map energy to hue/saturation to get coherent color shifts:

```
AudioAnalyzer (mid) -> Smooth -> Map -> Hue
AudioAnalyzer (bass) -> Smooth -> Map -> Saturation
HSBtoRGB -> BasicMaterial (color)
```

## Practical Examples

### Example 1: Bass-Reactive Background

```
MainLoop
    |
AudioFile -> AudioAnalyzer (bass)
    |
Smooth (0.9)
    |
Map (0-1 to desired range)
    |
HSBtoRGB (bass controls saturation) -> BasicMaterial (color input)
    |
BasicMaterial
    |
FullscreenRectangle
```

### Example 2: Circular Spectrum

```
MainLoop
    |
BasicMaterial
    |
AudioAnalyzer -> FFTArray
    |
ArrayIterator
    |
Transform (rotate based on index)
    |
Transform (translate by FFT value)
    |
Circle (small)
```

### Example 3: Waveform Display

```
MainLoop
    |
BasicMaterial
    |
AudioAnalyzer -> WaveformArray
    |
PointCloud or LineStrip
```

### Example 4: 3D Audio Visualization

```
MainLoop
    |
Camera -> OrbitControls
    |
AudioAnalyzer -> FFTArray
    |
ArrayIterator (creates ring)
    |
Transform (position in circle)
    |
Transform (scale Y by FFT)
    |
Cube
```

## Performance Considerations

1. **FFT Size** - Use smallest size that gives needed detail
2. **Smoothing** - Higher smoothing = less CPU for animations
3. **Update Rate** - Don't need 60fps for all audio analysis
4. **Visualizer Complexity** - Balance detail with performance

## Browser Audio Policies

Modern browsers require user interaction before playing audio:

1. Add a "Start" button
2. Start audio on button click
3. Or use `AudioContext.resume()` on first interaction

```javascript
// In custom op or patch
document.addEventListener('click', () => {
    if (audioContext.state === 'suspended') {
        audioContext.resume();
    }
}, { once: true });
```

## Featured Videos

<!-- Add audio videos here -->

<!-- Example:
```vid
https://youtu.be/XXXXX
Title: Audio Reactive Visuals in Cables.gl
Author: Channel Name
Thumbnail: https://i.ytimg.com/vi/XXXXX/mqdefault.jpg
```
-->

## Exercises

1. Create a simple volume meter with animated bars
2. Build a circular frequency spectrum visualizer
3. Make a 3D landscape that morphs to music
4. Create a beat-triggered strobe effect

---

