ALEKSANDRIA Stage 2 Video Tutorial Guide

Big Data and Connectionist AI<br/>Video Lead Mirad Kapiz<br/>Version 1.0 | 6 November 2026

This collection explains how a handwritten digit becomes numerical input and how supervised training uses a known answer to guide parameter updates. Watch Video 01 before Video 02. Both tutorials are intended for beginners and can be viewed offline.

Video collection

Video 01  From Digit Image to Training Data

Aleksandria_Video01_From_Digit_Image_to_Training_Data.mp4

Duration **6:54.87** | Size **33.37 MB** (33,368,414 bytes).

Video 02  How a Neural Network Learns

Aleksandria_Video02_How_a_Neural_Network_Learns.mp4

Duration **5:36.28** | Size **25.23 MB** (25,226,549 bytes).

Total viewing time is approximately **12 minutes 31 seconds**. Each individual file is below the teacher's 250 MB limit. Both reviewed files contain H.264 video at 960 x 544 pixels and AAC mono audio at 44.1 kHz.

How to use the collection

Watch the demonstrations in order. Pause at each question, choose an answer, and then continue to the explanation. Paper and a calculator are optional; no code, software installation or dataset download is needed. No additional supporting files are required for the activities shown.

Viewing notes

Video 01 assumes no previous AI knowledge. Before Video 02, learners should understand numerical pixel inputs and separate target labels; Chapter 2 provides optional preparation on weights and network layers. Navigation times in the following outlines are approximate visual topic locations, rather than word-for-word transcript timestamps.


---

Video 01 teaching outline

Learning goals: identify pixel values, calculate the illustrated normalization, describe ordered model inputs, and distinguish inputs from the correct training label. The video uses a digit 5; the 5 x 5 grid is a toy illustration, while the full image format has 28 x 28 positions.

00:00  From a drawing to data

The opening asks what a computer receives when it sees a digit. A handwritten 5 establishes the difference between a recognizable picture and the numerical representation needed by a model.

About 00:20  Pixel positions

The image is shown as a 28 x 28 grayscale grid, giving 784 positions. Magnified cells and a moving scan direct attention to individual pixel locations and their brightness values.

About 01:40  The picture written as numbers

A small 5 x 5 image is paired with its numerical grid. In the displayed convention, bright marks are 255 and dark background cells are 0. Matching positions are highlighted to show that each number belongs to a particular cell.

About 02:30  Normalize brightness values

The demonstration divides intensities by 255: 0 becomes 0, 128 becomes approximately 0.50, and 255 becomes 1. This changes the numerical scale, not the number of pixels or the digit label. The gray swatch is a separate grayscale illustration.

About 03:40  Arrange the prepared input

A row scan illustrates arranging 784 values in a consistent order for one simple model. Flattening rearranges the values; other architectures can keep the grid shape.

About 04:30  Keep the correct answer separate

The model input and correct label 5 appear in separate cards. The label supplies the known training target; it is not another pixel or a replacement for the image.

About 05:10  Connect the preparation steps

The complete pipeline links the handwritten image, pixel grid, numerical values and prepared input. The label remains a separate item paired with that input during supervised learning.

About 05:50 to 06:54.87  Learner question and explained answer

The learner chooses between A, 784 pixel values, and B, correct label 5, to identify the supplied correct answer. The answer screen identifies B: the pixel values describe the image, while the label supplies its checked target. The closing screen introduces the next question: how does the network learn?


---

Video 02 teaching outline

Learning goals: distinguish prediction and target, explain loss, separate backpropagation from optimizer updates, and explain repeated training and evaluation on separate data. The displayed probabilities, loss example and weight calculation are illustrative, not measured model performance.

00:00  Prepared input and separate target

The digit 5 is represented by 784 numerical pixel values. The network receives the pixel input; correct label 5 stays outside that input pathway and is available for the training comparison.

About 00:40  A prediction can be wrong

Animated probability bars show 60% for digit 3, 30% for digit 5 and 10% for the other eight classes combined. Digit 3 has the largest individual probability, so it is selected even though the checked label is 5.

About 01:10  Compare prediction and label

Prediction 3 and correct label 5 are shown side by side. Their mismatch leads to a loss box, distinguishing the model's answer, the supplied target and the numerical comparison.

About 01:40  Give loss a numerical value

The example uses cross-entropy for the correct-class probability 0.30: loss = -ln(0.30), approximately 1.20. This is a particular classification loss; it is not an accuracy percentage or a subtraction of digit class numbers.

About 02:20  Backpropagation calculates gradients

Backward-moving markers illustrate gradient calculation through the connected layers. Gradients describe how small parameter changes would locally affect loss. The visual explicitly states that weights have not changed yet and that only selected units are shown schematically.

About 03:10  The optimizer updates parameters

The separate toy update reveals 0.40 - (0.10 x 0.20) = 0.38. The learning rate controls step size. These supplied values illustrate the update rule; they were not derived from the displayed digit probabilities.

About 04:10  Repeat and evaluate

The training sequence repeats: input, prediction, loss, gradients and weight update. Separate test images move toward evaluation. One update does not guarantee a correct prediction, and performance on familiar training examples does not establish performance on new data.

About 05:00 to 05:36.28  Learner question and explained answer

The video asks whether backpropagation updates weights or calculates gradients. The answer is revealed: it calculates gradients; the optimizer updates weights. The final sequence reinforces the order of the learning steps.


---

Learning activities and resource connections

Video 01 learner check

**Question:** Which element supplies the known correct digit: A, 784 pixel values, or B, correct label 5?<br/>**Answer:** B. Pixel values are input features; the checked label is the separate target used to judge the output during supervised training.

Video 02 learner check

**Question:** Does backpropagation update weights or calculate gradients?<br/>**Answer:** It calculates gradients. The optimizer uses them to update parameters. The sequence is prediction, loss, gradient calculation, parameter update, then repetition.

Follow up practice

For numerical preparation, complete Chapter 1 Section 1.5 Questions 1 and 3: scale a value of 64 using division by 255 and identify features, target and model output. The scaled value is approximately 0.251. For a new training example, put prediction, loss, backpropagation and optimizer update in order and explain why test images must be separate from training updates.

Shared written content

Video 01 connects to Chapter 1 Section 1.3, the worked image-to-input example, and Chapter 4 Sections 4.2 and 4.3, MNIST dimensions and image preparation. Chapter 1 uses a toy digit 7; the videos and revised Chapter 4 use digit 5. These are separate teaching illustrations.

Video 02 connects to Chapter 3 Sections 3.2 through 3.6 and Chapter 4 Sections 4.4 through 4.7. The revised Stage 2 chapters explicitly include the video's digit-5 probabilities, cross-entropy calculation and separate 0.40-to-0.38 update.

<link href="https://github.com/Voryalis/aleksandria/blob/main/docs/01-big-data.md" color="#125577">Chapter 1 Big Data</link>

<link href="https://github.com/Voryalis/aleksandria/blob/main/docs/03-neural-networks-learning.md" color="#125577">Chapter 3 How a Neural Network Learns</link>

<link href="https://github.com/Voryalis/aleksandria/blob/main/docs/04-case-study.md" color="#125577">Chapter 4 Handwritten Digit Case Study</link>

Presentation connections

The repository's proposed slide outline links Video 01 to slide 5, A Digit Image Becomes Numbers. Video 02 connects to slides 8 and 9, Prediction Versus Correct Answer and How Training Changes a Network; slides 10 and 12 provide integration and review. These are proposed outline numbers, not verified pagination of the final slide deck.

<link href="https://github.com/Voryalis/aleksandria/blob/main/slides/slide-outline.md" color="#125577">Repository slide outline</link>

The precise final Study Guide page numbers and Test Bank question identifiers require the team's final versions. Until those cross-references are confirmed, the named chapter sections and practice questions above provide specific usable learning connections.


---

Sources and production acknowledgments

Video production and editing: Mirad Kapiz, Video Lead. Team identity: Aleksandria. The supplied educational graphics and animations use digit-recognition illustrations; no trained-model experiment or benchmark result is claimed.

Content references

<link href="https://github.com/Voryalis/aleksandria/blob/main/videos/first-video-storyboard.md" color="#125577">ALEKSANDRIA Tutorial 1 storyboard</link>

<link href="https://github.com/Voryalis/aleksandria/blob/main/videos/second-video-storyboard.md" color="#125577">ALEKSANDRIA Tutorial 2 storyboard</link>

<link href="https://keras.io/api/datasets/mnist/" color="#125577">Keras MNIST dataset documentation</link>

<link href="https://www.tensorflow.org/tutorials/quickstart/beginner" color="#125577">TensorFlow Quickstart for Beginners</link>

<link href="https://developers.google.com/machine-learning/crash-course/neural-networks" color="#125577">Google Machine Learning Crash Course Neural Networks</link>

<link href="https://developers.google.com/machine-learning/crash-course/overfitting" color="#125577">Google Machine Learning Crash Course Overfitting</link>

AI assistance

ChatGPT assisted with narration drafting and simplification, image editing and selected explanatory animations. In Tutorial 2, Scenes 02, 05, 06 and 07 use locally rendered diagram motion; an image-editing tool removed the production pause instruction from the quiz slide. This assistance does not constitute independent teammate review or evidence of a trained network.

The team should record the actual assistance and revision evidence in its project and personal logs. Additional borrowed media, music or synthetic narration, if used in the finished edits, require their actual source credits; none are invented in this guide.

Submission package

Submit the two individually named MP4 files and this guide. The teaching outlines above satisfy the guide's outline component. No external link replaces the required video uploads. Keep editable production files for revision; no extra learner data or software is needed for the activities shown.


---

Verification and remaining review

Review date: 6 November 2026. The checked source exports were tutorial 1.mp4 and tutorial 2.mp4 from Mirad's Videos folder. The named submission copies have identical contents; only their filenames differ.

Completed technical checks

Both complete audio and video streams decoded without errors. Video 01 is 33,368,414 bytes and Video 02 is 25,226,549 bytes, below 250 MB each. Both contain AAC audio. Measured mean levels are approximately -20.3 dBFS and -20.9 dBFS respectively, with peaks near 0 dBFS. These measurements establish audio presence and levels, not intelligibility or correct pronunciation.

Visual and content checks

Frames sampled throughout both videos show the preparation sequence in Video 01 and the prediction-loss-gradient-update sequence in Video 02. The numerical examples shown are arithmetically consistent. Both learner questions have visible explained answer screens. Video 02 includes the hypothetical-example disclosure and keeps backpropagation and optimizer updates distinct.

Outstanding items

**Theme:** Video 01 uses dark teaching backgrounds. This conflicts with the white/light-theme requirement in GitHub issue 42. Video 02 uses light backgrounds. Revise Video 01 or obtain an explicit team decision before treating the theme check as passed.

**Independent review:** A teammate must still watch each entire final compressed export and a non-author must attempt the learner questions. No completed peer review or learner-test result is claimed here.

**Audio and accessibility:** Full listening review of intelligibility, pronunciation, noise, synchronization and pacing remains necessary. No captions are visible in the sampled frames and no separate subtitle stream is listed. Add or check captions where needed for understanding and accessibility.

**Presentation:** Video 01 shows an editor watermark and a blue mark below the learner question in sampled frames. Check whether these should be removed. The exports are 960 x 544, so inspect smaller explanatory labels at normal playback size before submission.

**Credits and cross references:** Confirm any borrowed media credits, log the actual AI use, and replace provisional slide-outline mappings with final Study Guide, Test Bank and slide references when those files are available.

These review findings distinguish verified file and visual properties from required human checks. Completion of the guide does not mark pending acceptance checks as passed.

<link href="https://github.com/Voryalis/aleksandria/issues/42" color="#125577">Video 01 production requirements issue 42</link>

<link href="https://github.com/Voryalis/aleksandria/issues/43" color="#125577">Video 02 production requirements issue 43</link>

<link href="https://github.com/Voryalis/aleksandria/issues/44" color="#125577">Collection guide requirements issue 44</link>
