# Tutorial 1 — From a Handwritten Digit to Training Data

**Project:** Aleksandria | **Issue:** [#4](https://github.com/Voryalis/aleksandria/issues/4)  
**Video lead:** Mirad (`@MiradKapiz`)  
**Version:** 0.3, 23 October 2026 | **Status:** Corrected local draft; **re-review and Grigory alignment pending**  
**Audience:** Absolute beginners | **Format:** 16:9, animated demonstration + narration  
**Estimated duration:** ~2 min 40 sec (rehearse; timings are editorial targets)

## Learning objective

After the tutorial, learners should be able to trace **handwritten digit image → grayscale pixel values → optional normalization/prepared model input**, and explain why the image is paired with a **separate correct digit label** for supervised learning.

## Accurate example used throughout

The target digit in this hypothetical teaching demonstration is **5**. A typical MNIST example has a **28 × 28** grayscale image and a separate digit label. Pixels in the original 8-bit images are integers from **0 (black)** to **255 (white)**. The storyboard also uses a **5 × 5 teaching illustration** to make individual cells readable. It is *not* a claim that MNIST uses 5 × 5 images or that these invented values came from MNIST. Sources: [Keras MNIST](https://keras.io/api/datasets/mnist/), [TensorFlow Datasets MNIST](https://www.tensorflow.org/datasets/catalog/mnist).

### Toy illustration (an invented 5 × 5 bitmap of the digit 5)

`#` represents a white mark (`255`); `.` represents black background (`0`). This is an original simplified teaching image, **not MNIST data**.

```text
#####
#....
####.
....#
#####
```

Corresponding **invented** original-intensity matrix:

```text
255 255 255 255 255
255   0   0   0   0
255 255 255 255   0
  0   0   0   0 255
255 255 255 255 255
```

This simplified figure has **only 0 or 255**, so for the *normalization* scene use a separate illustrative partially gray pixel with value **128**. This avoids pretending a gray cell existed in the binary toy grid.

Example conversion with `normalized value = pixel intensity / 255`:

| Example intensity | Visual meaning | After division by 255 |
| ---: | --- | ---: |
| 0 | black | 0.00 |
| 128 | approximately middle gray | 0.50 (rounded from 0.502) |
| 255 | white | 1.00 |

**Important:** Normalization is a **possible choice**, not something every model is required to do. `28 × 28 = 784` is the number of positions. Some simple neural networks flatten this grid into 784 values; not every neural network does.

## Scene-by-scene storyboard and exact narration

> **Production rule:** Animate a concrete example. Never replace these demonstrations with static slides read aloud. Scenes may change length after recording and review.

### Scene 1 — Hook: what the computer sees (0:00–0:15)

**On screen:** A large high-contrast handwritten `5`. Under it: `You see: 5`. Then reveal the question `What does a computer receive?` Highlight the image itself.

**Animation:** Fade in the digit and then the question; hold long enough to recognize the shape.

**Narration:**
> You can look at this drawing and recognize the number five. But a neural network needs a numerical representation of the image. How do we turn this picture into data?

**Why this step:** Starts with a familiar object and gives a reason to study pixels before introducing any terms.

### Scene 2 — Reveal pixel locations (0:15–0:35)

**On screen:** Show a representative `28 × 28` grayscale image/grid of a handwritten 5, with the title `MNIST-style digit image: 28 × 28 pixels`. Zoom in on a small area until square cells are clearly visible. Show `28 × 28 = 784 pixel positions`.

**Animation:** Place grid overlay first; magnify the top-left or middle patch. If using a *real MNIST* example, label it as such and cite the dataset. Otherwise keep the visible caption `Illustrative digit image, MNIST-style dimensions`.

**Narration:**
> A common handwritten-digit dataset is MNIST. Each image has twenty-eight rows and twenty-eight columns of grayscale pixels. That makes seven hundred and eighty-four pixel positions in one image.

**Why this step:** Gives spatial meaning to 28 × 28; avoids presenting 784 as an unexplained formula.

### Scene 3 — Replace a picture with numbers (0:35–1:02)

**On screen:** Cut to the explicitly captioned `Simplified 5 × 5 illustration, not an MNIST sample`. Show the miniature drawn 5, then the same five-by-five grid. Replace **matching cells** with the exact integers in the matrix above. Circle one white mark `255` and one black background cell `0`.

**Animation:** Reveal two rows at a time, with the source cell and its number highlighted simultaneously. Keep the digit silhouette faintly visible while the matrix appears.

**Narration:**
> Let's enlarge the idea using a simple five-by-five drawing, just for teaching. Each square is a pixel, with a number for its brightness. Here, black is zero and white is two hundred and fifty-five. The picture can now be described using numbers.

**Why this step:** Makes the picture-to-data conversion visible and checkable; explicitly differentiates the tiny illustration from real MNIST images.

### Scene 4 — Optional preparation by normalization (1:02–1:26)

**On screen:** A new card titled `Example preparation: normalize pixel intensity`. Show three separate grayscale swatches labeled `0`, `128`, and `255` with arrows to `0.00`, `0.50`, `1.00` respectively. Show the formula `new value = old value ÷ 255`.

**Animation:** For each swatch, reveal the original value and then its normalized value; emphasize `128 ÷ 255 ≈ 0.50`. Caption: `One possible preprocessing step`.

**Narration:**
> We can also prepare the numbers before giving them to a model. For example, dividing each pixel value by two hundred and fifty-five changes the range from zero through two hundred and fifty-five to zero through one. This is called normalization. It is one possible preprocessing step.

**Why this step:** Shows an actual numeric transformation rather than simply saying that data must be cleaned or prepared. It does not imply normalization is mandatory.

### Scene 5 — Form the model input (1:26–1:44)

**On screen:** Return to the `28 × 28` grid with an arrow to a box `Prepared numerical input`. Next reveal a narrow row labelled `784 values in one simple flattened representation`. Do not animate the **label 5** into this input box.

**Animation:** Scan row-by-row; collapse the grid into a long schematic sequence of numerical cells; leave `e.g.` next to the flattened layout.

**Narration:**
> The prepared pixel numbers can become model input. One simple neural network design arranges the twenty-eight-by-twenty-eight image into a list of seven hundred and eighty-four values. Other network designs can keep the grid shape.

**Why this step:** Connects preparation to the eventual network input while avoiding the misconception that every neural network requires flattening.

### Scene 6 — Pair input with the correct training label (1:44–2:06)

**On screen:** On the left, `Image / prepared pixel data`. On the right, a separate brightly outlined box `Correct label: 5`. An enclosing border is titled `ONE LABELED TRAINING EXAMPLE`. Add text under the label: `Provided by the dataset, not read from the pixels as metadata`.

**Animation:** First show the input alone; only then move a separate label card beside it. Show **two separate objects**, not one combined 785-number input vector.

**Narration:**
> To teach a model with labeled examples, we also provide the correct answer. For this drawing, that answer is five. The image data are the input. The label is the target answer used during supervised training. It is not another pixel.

**Why this step:** Directly addresses the issue's essential distinction among raw image, prepared input and correct label.

### Scene 7 — Recap and learner check (2:06–2:40)

**On screen:** Rebuild a simple flow diagram: `Handwritten image → pixel grid → numeric values → prepared model input`, with a separate lower card `Correct label: 5` joining to form a bracket `Labeled training example`. Then ask `Which part tells the model the correct answer?` Pause 3 seconds. Highlight the label box and reveal `The label: 5`.

**Animation:** Follow each arrow in order; keep the entire flow visible for the final five seconds.

**Narration:**
> Here's the whole process. We begin with an image, represent its pixels as numbers, and prepare those numbers for a model. For supervised training, we pair that input with the correct digit label. Quick check: which part gives the correct answer? [Pause three seconds before revealing the answer.] The label. Next, we can explore how the network learns from these examples.

**Why this step:** Consolidates the sequence, tests understanding and creates a natural connection to Tutorial 2 without trying to teach weight updates prematurely.

**Transition to Tutorial 2:** After the data is prepared and paired with the correct label, the next video explains the separate stages of [prediction, loss, gradient calculation and optimizer updates](second-video-storyboard.md). No network training is claimed in this first tutorial.

## 3. On-screen wording to use consistently

| Term | Exact proposed caption | Avoid saying |
| --- | --- | --- |
| Original grayscale image | `Digit image / original pixel values` | `The computer immediately knows this is 5` |
| Pixel intensity | `0 = black; 255 = white` | `Every image has only black and white pixels` |
| Miniature teaching grid | `Simplified 5 × 5 illustration (not MNIST)` | `This 5 × 5 image is MNIST` |
| Prepared input | `Optional normalization: value ÷ 255` | `All neural networks must normalize exactly this way` |
| Input representation | `784 values in one simple flattened representation` | `Every network always uses 784 inputs` |
| Target | `Correct training label: 5` | `The label is a pixel or an input feature` |

## 4. Making the scenes on Windows, beginner workflow

1. In **Canva**, create a 1920 × 1080 video project. Add seven scenes matching the sections above. Use free text boxes, square grids and arrows. Copy the exact matrix and captions rather than asking an image generator to invent numeric grids.
2. Animate **one change per scene**: digit reveal, grid overlay, cell-to-number reveal, normalization arrows, flattening, label card, complete pipeline. Prefer the simplest fades, pan/zoom and sequential reveals.
3. Export the scenes as MP4 clips (or one MP4 with each scene's duration). Name them `scene-01-hook.mp4` through `scene-07-recap.mp4`; names are suggested for local production and do not need to be added to GitHub for Stage 1.
4. In **Clipchamp**, start a 16:9 project and import the Canva exports. Set scene order/timing approximately to the storyboard above, then add self-recorded narration **or** Clipchamp text-to-speech. Verify that the voice pronounces `MNIST` and the numbers correctly.
5. Generate captions if available; manually correct words including `pixel`, `grayscale`, `normalization`, `784`, and `label`. Check that caption blocks do not cover the highlighted pixels.
6. Watch once as a beginner would, pausing after scene 6: can you separately point to the original image, prepared model input and correct target? If not, revise the visuals and narration.
7. For later production, export a 1080p MP4, check offline playback and save editable source files. Stage 1 Issue #4 only asks for the **reviewed plan and storyboard**, not this recording.

## 5. Handoffs and review requirements

**Arseniy (`@17sen`)**
- Deliver or advise on the digit/grid, pixel-to-values and input-versus-label graphics listed in `videos/video-plan.md`.
- Validate that the figure actually matches the numerical cells used in the matrix; do not use AI-generated arbitrary digits with inconsistent values.

**Grigory (`@loauyhf`)**
- Compare the script with approved `docs/` content and clarify terms that differ in the shared chapter.
- Verify there is no statement that a label is part of inference-time input.

**Tamerlan (`@Tamer088`)**
- Independently check `28 × 28 = 784`, pixel intensity range, normalization arithmetic, and the toy grid.
- Test the final question with someone unfamiliar with neural networks and record findings.

**Mirad (`@MiradKapiz`)**
- Read narration aloud, adjust timing, implement review changes and update version/review notes truthfully. Do not claim production/approval before it occurs.

### Review log (complete with real events)

| Date | Reviewer | Check and outcome | Revision by Mirad | Evidence link |
| --- | --- | --- | --- | --- |
| Pending | Grigory | Not yet reviewed | Pending | Pending |
| 23 Oct 2026 | Tamerlan | Requested Scene 3 value and asset-request correction; arithmetic and bitmap checked | Corrected plan (0/255 only in toy grid); awaiting re-review | [PR #16](https://github.com/Voryalis/aleksandria/pull/16) |
| Pending | Arseniy | Visual asset handoff not yet confirmed | Pending | Pending |

## 6. Completion criteria for Issue #4

- [x] Tools and feasible format proposed.
- [x] Full narration and time-coded storyboard drafted.
- [x] Raw/original image, numerical pixels, optional prepared input and separate label distinguished.
- [x] Specific diagrams and animations requested in companion plan (requests **drafted**, not yet sent).
- [ ] Content Lead review against checked Markdown completed.
- [ ] QA re-review and final signoff completed (initial changes requested on 23 Oct; corrections drafted).
- [ ] Video lead accepts final draft and GitHub PR is reviewed.

**Status:** Corrected content is ready to update the existing draft PR #16. The issue is **not yet complete**; independent confirmation and acceptance remain outstanding.

## 7. Sources and AI disclosure

- [Keras MNIST dataset documentation](https://keras.io/api/datasets/mnist/): 28 × 28 grayscale images, original intensity range 0–255, labels 0–9.
- [TensorFlow Datasets MNIST catalog](https://www.tensorflow.org/datasets/catalog/mnist): separate image and label features and dataset structure.
- [Issue #4](https://github.com/Voryalis/aleksandria/issues/4): expected outputs, review dependencies and instructional scope.
- [Issue #3](https://github.com/Voryalis/aleksandria/issues/3): shared Markdown source, subject to content team review.

**AI assistance:** Draft storyboard, narration, mathematical examples and production notes prepared with ChatGPT on 22 October 2026 following a user request to complete Issue #4. This draft must be reviewed by the responsible members, and any real prompts, edits and checks documented according to course rules. No image creation, voice recording, testing with learners, video editing or GitHub publishing has been carried out as part of this draft.

**23 October revision note:** Scene 3 uses *only* 0 and 255 because those are the only values in the invented bitmap. Scene 4 introduces 128 as a separate mid-gray sample. This implements the specific inconsistency reported in PR #16; no reviewer approval is claimed.
