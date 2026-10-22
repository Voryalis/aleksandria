# Aleksandria — Video Tutorial Plan

**Tracking:** [GitHub Issue #4](https://github.com/Voryalis/aleksandria/issues/4) (Tutorial 1); [Issue #13](https://github.com/Voryalis/aleksandria/issues/13) (Tutorial 2)  
**Video lead:** Mirad Kapiz (`@MiradKapiz`)  
**Audience:** First-year university students with no programming or machine-learning background  
**Stage:** Stage 1 planning draft, prepared 22 October 2026  
**Review status:** Draft for technical and pedagogical review; **not yet approved, recorded, or rendered**  
**Source of truth:** Team's checked educational Markdown in `docs/` (alignment pending until chapter content is reviewed)

## 1. Purpose and learning outcomes

The series uses **one recurring handwritten-digit recognition example** so the learner can connect data preparation to neural-network learning without having to learn programming first.

**Tutorial 1: From a Handwritten Digit to Training Data**
- Target length: approximately **2 min 30 sec**, 16:9 landscape.
- At the end, a beginner can (1) identify a digit image, (2) explain that a grayscale image is a grid of numerical pixel intensities, (3) distinguish raw pixel data from prepared model input, and (4) identify the correct digit label as the supervised-learning target.
- Main example: a clearly labelled **illustrative handwritten digit 5**. Use the real MNIST 28 × 28 format to explain dimensions, but never present a made-up miniature pixel grid as an actual MNIST sample.
- Output for Stage 1: reviewed `videos/first-video-storyboard.md` (not a rendered tutorial).

**Tutorial 2: Predictions, Error and Weight Updates**
- Tracked **separately** in Issue #13, not completed by Issue #4.
- Planned sequence: prepared numerical input → model prediction → compare with label → calculate a loss → adjust weights during training → retry; details require separate script and content review.
- Reuse the same digit-recognition teaching example and visual design when possible.

## 2. Production approach and tool choices

| Task | Planned tool | Reason for choosing it | Free-plan fallback |
| --- | --- | --- | --- |
| Draw and animate digit, grids, values, arrows, title cards | **Canva** | Accessible drag-and-drop animation for a beginner; can reuse team diagrams | Use basic free shapes, labels and animations; avoid premium assets |
| Arrange clips, control timing, add captions, narration and export | **Microsoft Clipchamp** on Windows | Simple timeline, voice/audio tracks and 1080p export options | Record your own voice if text-to-speech is unavailable or limited |
| Record optional on-screen demonstrations | **OBS Studio** | Free recording, especially useful for a real dataset demonstration | Skip entirely for Tutorial 1; animations are enough |
| Draft/critique script and caption text | **ChatGPT** (optional AI assistance) | Helps adapt concepts to plain speech and identify likely beginner confusion | Human review of every technical statement and prompt record required |

**AI use policy:** AI narration, subtitles, script suggestions or graphical ideas may speed up production, but they do **not** establish scientific correctness. The video lead checks them against reviewed Markdown and sources. Keep meaningful prompts, output excerpts, chosen edits and verification evidence in the actual project/personal logs. Do not claim work was filmed or tested before it was.

## 3. Style and accessibility

- **Canvas:** 1920 × 1080 (16:9), with a consistent high-contrast background and large labels. Suggested export: MP4, 1080p, ~30 fps.
- **Pacing:** one idea per scene; prefer slow highlights and stepwise reveals to flashy transitions.
- **Text:** short captions, not full paragraphs; narration should explain what visually changes.
- **Language:** introduce terms when first used: *pixel*, *intensity*, *normalization*, *training label*.
- **Color:** distinguish image/pixels, prepared input and label by position and text as well as color. Avoid relying on red/green alone.
- **Audio:** clear, moderate-paced voice; music optional and quiet or omitted; proofread manually corrected captions.
- **Truthfulness:** clearly mark the five-by-five pixel values as a *simplified teaching illustration*. No model training or numerical performance is claimed in Tutorial 1.
- **Offline use:** download and play the exported MP4 locally before final delivery; keep Canva/Clipchamp project files separately.

## 4. Tutorial 1 outline and key decisions

| Order | Demonstration | Concept taught | Why it appears here |
| --- | --- | --- | --- |
| 1 | Show a handwritten 5 and the question “What does a computer receive?” | Familiar problem and learning goal | Establishes curiosity without terminology |
| 2 | Put a visible grid over the digit | A digital grayscale image consists of pixels | Links the picture to discrete locations |
| 3 | Zoom into a simplified 5 × 5 example, then replace select cells with `0`, `128`, `255` | Pixel intensity is numerical, not a magical symbol | Makes the abstraction observable; miniature values are illustrative |
| 4 | Show `0 → 0.00`, `128 → 0.50`, `255 → 1.00` after dividing by 255 | Example of preparing or normalizing model input | Separates original data from a chosen transformation |
| 5 | Return to a **28 × 28** MNIST-style grayscale digit and show `28 × 28 = 784` | Image dimensions and possible flattened input representation | Connects toy illustration to the real example without implying every model uses flattening |
| 6 | Pair the image/input with **Label = 5** in a separate target box | A label is the correct answer supplied for supervised training | Prevents the common mistake that the label is a pixel or an input value |
| 7 | Present full pipeline and one viewer question | Image → pixel data → prepared input + label | Reinforces the learning outcomes and closes with retrieval practice |

## 5. Assets and handoffs

**Requests for Arseniy (`@17sen`, Visual Design):**
1. `assets/diagrams/digit5-grid-28x28.svg` — digit with visible 28 × 28 pixel grid; legend for dark/light intensity. If based on MNIST, record the specific sample and attribution/licence.
2. `assets/diagrams/digit5-to-values.svg` — **explicitly illustrative** 5 × 5 binary/greyscale teaching grid and legible numerical values.
3. `assets/diagrams/digit-training-example.svg` — image/pixel input and a distinct `Correct label: 5` box; editable objects suitable for animation.
4. Optional consistent background/title template for both tutorials; SVG/PNG exports with readable text at 1080p.

**From Grigory (`@loauyhf`, Content Lead):**
- Verify terminology and consistent example in `docs/` (especially data-preparation and neural-network sections).
- Confirm that the planned 28 × 28, normalization and label descriptions agree with the approved chapter, and suggest corrections where needed.

**From Tamerlan (`@Tamer088`, Quality Lead):**
- Fact-check the script and mathematical examples against cited sources.
- Test whether a beginner can distinguish (a) pixels, (b) normalized values, and (c) the label.
- Review readability, pace, accessibility and visual truthfulness, recording specific results.

**From Kamran (`@Voryalis`, CIO):**
- Coordinate branch/PR/review convention, placement in `videos/`, evidence links and Stage 1 submission snapshot.

**Video lead (Mirad):**
- Own scene pacing, narration, editing decisions, scene asset integration, review replies and eventual production.
- Independently understand and be able to explain the numerical conversion and its limits.

## 6. Technical reference and consistency checkpoints

- Standard MNIST image data are 28 × 28 grayscale pixels with integer intensities **0–255**, with a digit label in **0–9**. See Keras [MNIST API](https://keras.io/api/datasets/mnist/) and TensorFlow Datasets [MNIST catalog](https://www.tensorflow.org/datasets/catalog/mnist).
- `28 × 28 = 784` is the number of pixel positions; a **simple example model may flatten** them into 784 input features, but other architectures retain spatial structure.
- Normalization `p / 255` is **one possible preprocessing step**, not an inherent property of every dataset or neural network.
- The training **label** is the expected answer associated with an image in supervised learning, not a component of the input image. The narration does not say a new unknown image arrives with its correct label already known.
- Grayscale here uses 0 for black and 255 for white; check that animations and captions use this convention consistently.

## 7. Review and acceptance checklist (not completed yet)

- [ ] Mirad confirms chosen apps, scene timing and narration in a trial read.
- [ ] Grigory checks the planned scientific explanation against current `docs/` content and sources.
- [ ] Tamerlan independently checks facts, 5 × 5 illustration, equation, label separation and beginner comprehension.
- [ ] Arseniy confirms any requested visual assets can be supplied or an equivalent editable design can be made in Canva.
- [ ] Mirad records review findings and the actual changes (or a justified no-change result) in the PR.
- [ ] GitHub PR links **Closes #4** only after review and acceptance; do not declare the issue complete just because a draft exists.

## 8. Sources and attribution

1. [Keras, MNIST digits classification dataset](https://keras.io/api/datasets/mnist/). Describes the 28 × 28 grayscale images, 0–255 pixel values, digit labels and dataset splits.
2. [TensorFlow Datasets, MNIST](https://www.tensorflow.org/datasets/catalog/mnist). Describes `image` and `label` features and the 60,000 training / 10,000 testing split.
3. Internal team scope: `README.md`, [Issue #4](https://github.com/Voryalis/aleksandria/issues/4), [Issue #3](https://github.com/Voryalis/aleksandria/issues/3), and the shared Stage 1 planning material. Educational Markdown alignment is pending.

**Draft/AI-use disclosure:** This initial writing and storyboard organization was generated with ChatGPT at the video lead's request on 22 October 2026. It has **not** yet received teammates' reviews, been independently accepted by Mirad, or been used to produce an actual video. Record the actual interaction and any subsequent checks/edits in the relevant course logs.
