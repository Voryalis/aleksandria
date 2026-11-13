# ALEKSANDRIA Stage 2 Video Tutorial Guide

**Big Data and Connectionist AI** · Video lead Mirad Kapiz

**Version 1.1** · 14 November 2026 · Visual novel revision

A library parcel marked **5** sets up both tutorials. The scanner guesses **3**, so the Future Gadget Lab traces what the model received and how a checked label can help a network learn. Watch Video 01 before Video 02. Both tutorials are intended for beginners and can be viewed offline.

## Video collection

| Video | MP4 filename | Duration | File size |
| --- | --- | ---: | ---: |
| 01 · From Digit Image to Training Data | `ALEKSANDRIA_Tutorial_1.mp4` | 5:00 | 27.90 MB (27,897,236 bytes) |
| 02 · How a Neural Network Learns | `ALEKSANDRIA_Tutorial_2.mp4` | 5:00 | 27.34 MB (27,335,184 bytes) |

**Total viewing time** · 10:00. Both files contain 1920 × 1080 H.264 video at 24 fps and stereo AAC audio at 48 kHz. Each file is below 250 MB.

### How to use the collection

Video 01 assumes no previous AI knowledge. Before Video 02, viewers should be able to distinguish the prepared pixel values from the checked label. [Chapter 2, Artificial Neural Networks](../docs/02-connectionist-ai.md#2-artificial-neural-networks) provides optional preparation on weights and layers.

Read the English dialogue as it appears in the visual novel text box. The current exports contain quiet instrumental music and sound effects. The team’s voice recordings are pending. Each quiz gives viewers five seconds to choose before the answer appears. Pause for longer if needed. Paper and a calculator are optional. The activities can be completed from the videos.

## Video 01 · From Digit Image to Training Data

*The Shelf Five Incident*

By the end, viewers should be able to read grayscale intensities, divide by 255, flatten an image in row order, and explain the role of a separate checked label.

| Time | Teaching outline |
| --- | --- |
| 00:00-00:35 | A parcel tag says **5** and the scanner displays an illustrative prediction of **3**. Kurisu opens the scan to inspect the input. |
| 00:35-01:15 | The digit appears on a **28 × 28** grid with **784** pixel positions. The display shows black as **0**, white as **255**, and mid-gray as **128**. |
| 01:15-02:10 | The Study Guide’s 2 × 2 crop has rows `[0, 255]` and `[128, 0]`. Dividing each value by 255 produces `[0, 1]` and `[0.502, 0]`, rounded to three decimals where needed. |
| 02:10-02:58 | Read each row from left to right, then move down. The crop becomes `[0, 1, 0.502, 0]`. Repeating the same ordering across the full grid gives this model a list of **784** values. |
| 02:58-03:45 | Mayuri checks the tag. The **checked label 5** stays on its own card. The pixel list goes into the model and the label supplies the target during supervised training. |
| 03:45-04:24 | Compare full and clipped scans of the same tag. The choices appear at **03:55**, the thinking pause runs **04:07-04:12**, and the explanation starts at **04:12**. |
| 04:24-05:00 | The group rescans the full digit and recaps the preparation steps. Credits begin at **04:41**, followed by the PhoneWave and Gelbana scene at **04:48**. |

### Learner check

**What changed when the scan clipped the stroke?** A. Pixel input · B. Checked label · C. Both

**Answer A.** The clipped scan changes the raw brightness at row 5, column 18 from **255** to **0**. Both scans use a 28 × 28 canvas. The original tag and checked label still say **5**.

## Video 02 · How a Neural Network Learns

*The Wrong Answer Experiment*

By the end, viewers should be able to interpret a prediction and its loss, distinguish backpropagation from the optimizer update, and explain why held-out examples matter.

| Time | Teaching outline |
| --- | --- |
| 00:00-00:28 | The lab reopens the case. The same **784** prepared pixel values feed the network. The checked **5** is available for the training comparison. |
| 00:28-01:02 | The forward pass uses the current weights to calculate outputs. In the illustrated example, digit **3** gets **60%**, digit **5** gets **30%**, and the other eight digits share **10%**. The highest individual probability gives prediction **3**. |
| 01:02-01:52 | Cross-entropy uses the probability assigned to the checked digit **5**. The example gives `−ln(0.30) ≈ 1.20`. Giving the correct digit a higher probability lowers this loss. |
| 01:52-02:38 | Backpropagation works backward through the network’s calculations to find gradients. A gradient describes how a small change in a weight would affect loss. The weights stay fixed during this calculation. |
| 02:38-03:30 | The optimizer applies the update. A standalone gradient descent example uses `0.40 − (0.10 × 0.20) = 0.38`. Its learning rate is **0.10** and its supplied gradient is **+0.20**. |
| 03:30-04:18 | The training loop repeats across labeled examples. Evaluation uses held-out images with weights fixed. Inference makes a prediction from a fresh parcel scan, which can then be checked by hand if needed. |
| 04:18-05:00 | The learner chooses what backpropagation does. The thinking pause runs **04:28-04:33** and the answer appears at **04:33**. The training loop recap leads into credits at **04:53**. |

### Learner check

**What does backpropagation do?** A. Update the weights · B. Calculate the gradients

**Answer B.** Backpropagation calculates the gradients. The optimizer uses those gradients to update the weights. The training cycle then repeats on more examples.

The probabilities and weight update are separate illustrations. The video supplies the gradient for the update.

## Learning activities and resource connections

| Video | Study Guide v1.1 | Shared Markdown | Stage 2 slide deck |
| --- | --- | --- | --- |
| 01 | Activity C, pp. 37-38, especially step 1 | [Chapter 4 §§4.2-4.3](../docs/04-case-study.md#42-meet-the-mnist-dataset) · MNIST and preparing the image | Slides 17 and 25-26 for image preparation. Slides 39-40 for the clipped parcel scan. |
| 02 | Activity C, pp. 37-38, especially steps 2-3 and the held-out question | [Chapter 3 §§3.2-3.6](../docs/03-neural-networks-learning.md#32-a-prediction-is-not-the-correct-answer) · prediction through evaluation. [Chapter 4 §§4.4-4.7](../docs/04-case-study.md#44-how-the-network-makes-a-prediction) · digit case study. | Slides 28-29 and 31-34 for prediction, loss, training, and evaluation. |

[Study Guide v1.1, Activity C](../guide/Big%20Data%20and%20Connectionist%20AI%20-%20Study%20Guide%20v1.1.pdf#page=37) · [Stage 2 slides, PDF](../slides/Aleksandria_Stage2_PPT_V1.pdf)

### Follow-up practice

1. **Prepare another pixel.** Divide **64** by **255**, then explain where that result belongs in the training example. It is approximately **0.251** and belongs in the pixel input list.
2. **Try the Study Guide update.** Activity C supplies a different gradient of **−0.30** and a learning rate of **0.10**. Starting from **0.40**, the updated weight is **0.43**. For a held-out test image, record the prediction error and keep the weight fixed.

## Sources and production acknowledgments

**Video production** · Team ALEKSANDRIA. **Video lead** · Mirad Kapiz. ChatGPT assisted with drafting dialogue, assembling the visual novel scenes, generating the explanatory animations, and editing and checking the exports.

**Instructional sources** · [Keras MNIST dataset documentation](https://keras.io/api/datasets/mnist/) · [TensorFlow Quickstart for Beginners](https://www.tensorflow.org/tutorials/quickstart/beginner) · [Google Machine Learning Crash Course, Neural Networks](https://developers.google.com/machine-learning/crash-course/neural-networks)

**Game art** · *STEINS;GATE* visual novel, Steam HD edition. MAGES. / 5pb. / Nitroplus. Character sprites, lab backgrounds, event art, and interface artwork are from [The Spriters Resource archive](https://www.spriters-resource.com/pc_computer/steinsgatesteamhdedition/).

**Music** · “Laboratory,” “Explanation,” and “Quiet Air” by Takeshi Abo, from the [*STEINS;GATE Original Soundtrack*](https://ototoy.jp/_/default/p/55330). Both videos include a source credit card.

## Verification and submission

- **Technical checks, 14 November 2026** · Both listed exports decoded from start to finish. Sampled frames confirm the cream teaching panels, English dialogue, question and answer screens, and the visible source credits.
- **Audio** · Integrated music and effects measure approximately **−31.6 LUFS** in Video 01 and **−32.0 LUFS** in Video 02. After the team records the dialogue, check the mix, pronunciation, synchronization, and file details against the voiced exports.
- **Independent review** · A teammate’s full viewing and a non-author’s attempt at the learner checks remain pending for this revision. The teaching panels are light. The shaded game backgrounds and dark dialogue box still need review against the team’s light-theme requirement.
- **Submission package** · Submit both individual MP4s with the PDF or Word guide. Update the listed file details if the recordings change the exports. Record the revision and AI assistance in the project and personal logs.

[Video 01 requirements #42](https://github.com/Voryalis/aleksandria/issues/42) · [Video 02 requirements #43](https://github.com/Voryalis/aleksandria/issues/43) · [Collection guide requirements #44](https://github.com/Voryalis/aleksandria/issues/44)
