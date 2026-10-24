# Tutorial 2 — How a Neural Network Learns From a Wrong Digit Prediction

**Project:** Aleksandria · **Issue:** [#13](https://github.com/Voryalis/aleksandria/issues/13) · **Video lead:** Mirad (`@MiradKapiz`)  
**Version:** 0.1 · 23 October 2026 · **Status:** Complete Stage 1 *draft*, awaiting scientific and content review  
**Audience:** Complete beginners · **Format:** 16:9 animated walkthrough with narration · **Target duration:** approximately 3 min 30 sec, subject to a narration trial

## Learning outcomes and connection to Tutorial 1

After this tutorial, a learner should be able to: (1) distinguish a model's **prediction** from the supplied **correct training label**, (2) explain that a **loss** measures how poorly the prediction matches that label, and (3) put the supervised training steps in order: **input → prediction → loss → backpropagation (gradients) → optimizer update → more training**. They should understand that one update does **not** guarantee the next prediction will be correct.

Use the **same handwritten digit 5** from [Tutorial 1](first-video-storyboard.md). The digit's 28 × 28 image is represented by pixel numbers, optionally normalized, while **correct label = 5** remains a separate target. Tutorial 1 explains *preparation*. This tutorial explains *learning*. Do not retell the full pixel demonstration.

## Technical and visual truth rules

- **All model predictions, scores, loss and scalar weight numbers below are invented teaching values.** They are not measurements from a trained network, a run of MNIST, or evidence that the network improved.
- A conventional ten-category digit classifier can output one score/probability per digit. For an illustrative output, assign **60% to digit 3, 30% to digit 5, and 10% in total to the other eight digits**. The predicted class is **3** because it has the largest individual probability; the true label is **5**. The bars for the eight other digits may be hidden under an `Others combined: 10%` annotation. Do not label these made-up outputs as MNIST benchmark statistics.
- With a **cross-entropy teaching example** for the correct class, `loss = −ln(P(correct digit)) = −ln(0.30) ≈ 1.20`. This is a chosen loss function and is not a universal error formula. For the spoken beginner narration, the key idea is just **larger loss means the model assigned less probability to the correct label**.
- **Backpropagation computes gradients** indicating how a small change in model parameters would affect loss. An **optimizer applies an update**. Keep these actions separate in the diagram and voiceover.
- The separate illustrative weight calculation `old weight 0.40 − (learning rate 0.10 × gradient 0.20) = new weight 0.38` is arithmetically correct, but is **not computed from the displayed hypothetical digit model**. Display it only as a small standalone example if the reviewers agree; never imply this one change produced the displayed probabilities.
- During **training**, the label is used to compute the loss. During later **inference on an unknown image**, the model predicts without being given the correct label in advance. A label might subsequently be obtained for evaluation, but it is not part of the pixel input.
- A single update might reduce the loss on the selected example, but improvement is **not guaranteed** for all inputs. Training repeats over many examples, and evaluation uses separate data.

## Scene-by-scene storyboard and narration

> **Production guidance:** Each scene shows a visible transformation or comparison. Do not just display a paragraph of the narration. Times are editorial targets to rehearse, not proven recording lengths.

### Scene 1 — Connect to the first tutorial (0:00–0:20)

**On screen:** The already prepared image of a handwritten `5` and a separate card `Correct label: 5`. Title: `How does the network learn?`. Briefly animate pixel values feeding toward a simple schematic network.

**Animation:** Bring over the same visual style and label box as Tutorial 1. Keep the `5` label outside the network input arrow.

**Narration:**
> Last time, we turned a handwritten digit into numerical input. We also attached the correct training label, five. Now let's see what can happen when a neural network makes the wrong prediction, and how training responds.

**Why this scene:** Creates continuity without repeating the earlier lesson; reminds learners that the target is separate from the input.

### Scene 2 — Show the network producing a prediction (0:20–0:46)

**On screen:** `Prepared pixels` → `Neural network` → output score bars. Highlight `3: 60%`, `5: 30%`, `Other digits together: 10%`. Caption `Invented scores for explanation only`. Underneath, reveal `Predicted digit = 3`.

**Animation:** Move one image through the network. Reveal 3 and 5 bars first, then the combined others label. Highlight `3` because it has the highest individual percentage.

**Narration:**
> The network processes those pixel values and produces scores for possible digits. Here is a made-up example: it assigns sixty percent to three, thirty percent to five, and ten percent altogether to the others. Its predicted answer is three.

**Why this scene:** Shows what a prediction actually looks like; avoids treating the output as a guaranteed fact.

### Scene 3 — Compare the prediction with the label (0:46–1:12)

**On screen:** Two side-by-side cards `Prediction: 3` and `Correct label: 5`. Reveal `They do not match`. Then a new card `LOSS = a number summarizing the error`.

**Animation:** Outline the wrong prediction, reveal the expected answer, and then place a comparison arrow leading to a `Loss` box. No weights change yet.

**Narration:**
> But the correct label for this training image is five. The prediction and the answer disagree. During supervised training, we compare the model's output with that label using a loss function. The loss turns this disagreement into a number the training procedure can use.

**Why this scene:** Keeps prediction, label and loss conceptually separate before presenting optimization.

### Scene 4 — Give the loss a concrete meaning (1:12–1:39)

**On screen:** Emphasize `Probability assigned to correct digit 5 = 0.30`. Under it show an optional smaller note: `Illustrative cross-entropy: −ln(0.30) ≈ 1.20`. Caption `Illustrative calculation, not a measured experiment`. Then reveal `Goal during training: reduce loss over examples`.

**Animation:** Highlight the correct-class bar, move attention to the loss box and show a simple gauge labelled `loss` without inventing a before-and-after measurement.

**Narration:**
> One possible loss function looks at how much probability the model gave to the correct digit. Here, five received only thirty percent. That produces a penalty. Training tries to adjust the model so its losses become smaller across useful examples, not just this picture.

**Why this scene:** Relates the abstract word *loss* to the actual sample output while keeping optional mathematics out of the main voiceover.

### Scene 5 — Backpropagation calculates gradients (1:39–2:04)

**On screen:** Network diagram with a backward-moving dotted arrow labelled `Backpropagation: calculate gradients`. Add a small caption `Gradient: how loss changes when a parameter changes`. Do **not** animate the weights as changed yet.

**Animation:** Light up the loss box first, then move a dotted arrow backward through network layers and reveal gradient symbols beside selected connections.

**Narration:**
> Next comes backpropagation. It works backward through the network to calculate gradients. These tell the training procedure how small changes to the network's adjustable parameters, such as weights, would affect the loss. Backpropagation calculates the information needed for an update.

**Why this scene:** Avoids the misconception that backpropagation itself is the weight-update step.

### Scene 6 — Optimizer updates weights (2:04–2:31)

**On screen:** A separate step labelled `Optimizer: update parameters`. Show arrows from gradients to weights. Optional inset, labelled `Separate toy weight example`, with `0.40 − 0.10 × 0.20 = 0.38`. Keep the original three probability bars *unchanged* so viewers do not infer these update numbers generated them.

**Animation:** Only after the `Optimizer` title appears, alter the thickness of one schematic connection. Put the example arithmetic into a small inset, not on the main model output.

**Narration:**
> An optimizer, for example gradient descent, uses those gradients and a chosen learning rate to update the weights. In this separate toy calculation, a weight moves from zero point four zero to zero point three eight. The exact change in a real network depends on its data and gradients.

**Why this scene:** Makes the optimizer's responsibility visible; the independent toy equation provides an honest numeric demonstration without inventing a real training run.

### Scene 7 — Repeat training, then evaluate (2:31–3:02)

**On screen:** Animated loop: `Labeled input → prediction → loss → gradients → optimizer update ↺`. Repeat the loop symbolically with multiple different digit cards. To the side show `Check performance on separate test images`. No invented accuracy percentage, no instant switch to a correct prediction.

**Animation:** Run the loop twice at readable speed, then send a distinct set of test cards to a `Evaluation` box without a back-arrow into training.

**Narration:**
> Training repeats this process across many labeled examples. Over time the model may learn useful patterns, but one update cannot guarantee a correct answer. We also check predictions on images held out from training. That helps us see whether the learned patterns work on new examples.

**Why this scene:** Makes iteration clear without the false guarantee of immediate correctness or perfect generalization.

### Scene 8 — Recap and learner check (3:02–3:32)

**On screen:** Six-step graphic, using separate boxes: `Input → Prediction → Loss → Gradients → Weight update → Repeat`. Underneath ask `Does backpropagation change the weights, or calculate gradients?`. **Pause for 3 seconds**. Reveal `It calculates gradients. The optimizer updates weights.` End card: `Next: use and test what the model learned`.

**Animation:** Highlight the stages in order. Hold on the viewer question for at least three seconds, then reveal the answer and leave the sequence visible for the closing seconds.

**Narration:**
> So the network predicts, the loss compares that prediction with the answer, backpropagation calculates gradients, and an optimizer updates parameters. Then training continues. Quick question: does backpropagation update weights, or calculate gradients? [Pause three seconds.] It calculates gradients. The optimizer applies the update.

**Why this scene:** A targeted retrieval question checks the most likely confusion and closes the full learning loop.

## Production checklist and asset requests

**Mirad (`@MiradKapiz`)**
- [x] Draft the illustrative example, time-coded scenes, exact narration, and step order.
- [ ] Rehearse narration aloud and change timings based on a real test.
- [ ] Confirm all invented values and caveats remain visible in the final animation.
- [ ] Integrate agreed visual assets, produce editable scenes in Canva and edit later in Clipchamp.
- [ ] Record actual revisions, source checks and significant AI use in the team and personal logs.

**Arseniy (`@17sen`) visual requests (draft requests, not confirmed deliveries)**
1. Reusable digit-5 input and distinct correct-label card matching Tutorial 1.
2. Editable neuron/network schematic with labelled input, hidden and output layers and arrows in both directions.
3. Ten-digit classifier results: show scores for 3 and 5 and group the other eight; conspicuous `Illustrative output` label.
4. Prediction-vs-label cards; a separate `loss` box; reverse dotted gradient arrows; optimizer update arrows.
5. Reusable six-step training loop, ending with separate unseen/test images.

**Grigory (`@loauyhf`) content review (pending)**
- [ ] Confirm terminology and causal sequence match the *approved* chapter on training, including training versus inference and the distinction between backpropagation and optimizer.
- [ ] Check whether the brief optional cross-entropy inset is suitable for the team's beginner learning objectives.

**Tamerlan (`@Tamer088`) quality review (pending)**
- [ ] Verify the 60% + 30% + 10% illustrative output, `−ln(0.30) ≈ 1.20`, and `0.40 − 0.10 × 0.20 = 0.38`.
- [ ] Confirm the invented scores and weight step are not misrepresented as results of one actual training run.
- [ ] Evaluate readability, narration pacing, accessibility and learner quiz with a real test if available.

**Issue #13 done only when:** a scientifically reviewed storyboard agrees with the checked shared Markdown, has clear visuals and narration, and is accepted for later production. **A finished video is not claimed.**

## Reference checks and disclosure

- [Keras MNIST dataset API](https://keras.io/api/datasets/mnist/): handwritten-digit image dimensions and separate digit labels.
- [TensorFlow beginner training example](https://www.tensorflow.org/tutorials/quickstart/beginner): normalization, flattened input in one model, model training and evaluation.
- [Issue #13](https://github.com/Voryalis/aleksandria/issues/13) and [Issue #4](https://github.com/Voryalis/aleksandria/issues/4): the team's scope and accepted task structure.
- **External conceptual verification still required by the content and QA leads** for exact wording about loss, backpropagation and optimizers before publishing an educational final video.

**AI assistance disclosure:** Drafting and mathematical consistency checking were assisted by ChatGPT on 23 October 2026 at the video lead's request. This document is a proposed teaching storyboard, not evidence of a completed recording, real neural-network experiment, independent human review or team approval. Mirad should check and adapt the work and record the actual use and revisions in the required individual/team logs.
