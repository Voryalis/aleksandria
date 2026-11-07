# Chapter 4 — Case Study: Teaching a Neural Network to Recognize Handwritten Digits

**Version:** Stage 2 revised draft, 6 November 2026. Pending team acceptance.

**Audience:** University beginners with no previous machine-learning experience.

**Prerequisites:** [Chapter 1 — Big Data](01-big-data.md) · [Chapter 2 — Artificial Neurons](02-connectionist-ai.md) · [Chapter 3 — How a Neural Network Learns](03-neural-networks-learning.md)

## 4.1 From Individual Ideas to a Complete System

The previous chapters introduced the parts of a learning system:

- Chapter 1 explained data quality and preparation.
- Chapter 2 introduced inputs, weights, biases, activation functions, and layers.
- Chapter 3 explained predictions, loss, gradients, and parameter updates.

Now we connect these ideas through one task: **given an image of a handwritten digit, predict which digit it shows**. The possible classes are the digits 0 through 9.

We use the format of the MNIST dataset and a recurring illustrative digit **5**, matching Tutorials 1 and 2. Dataset facts are distinguished from invented examples. No trained-model accuracy or experimental result is claimed.

After reading this chapter, learners should be able to trace image preparation, explain a prediction, describe the training cycle, and interpret basic evaluation methods.

## 4.2 Meet the MNIST Dataset

MNIST contains **70,000 labelled grayscale images**:

- 60,000 images in the standard training set;
- 10,000 images in the standard test set;
- 28 × 28 pixels per image;
- one digit label, from 0 to 9, associated with each image.

These dataset properties are documented in the [Keras MNIST API](https://keras.io/api/datasets/mnist/).

A **label** is the target answer associated with an example. If a checked image shows a 5, its label is 5. The image supplies the input; the label supplies the target used during supervised training.

MNIST is useful because the task and image format are manageable. However, its isolated digit images are not representative of every handwriting style or every kind of real document.

### Pixel Values and the White-Background Display

Original 8-bit MNIST pixel values range from 0 to 255. The background is near 0, while digit strokes have higher values. Under a standard grayscale display, 0 appears black and 255 appears white.

**Our educational visuals use dark digits on a white background.** They can display the same information using an inverted grayscale palette. This is a presentation choice; it does not require changing the values used for training.

If values are explicitly inverted instead of changing only the display palette, the transformation is `inverted pixel = 255 − original pixel`. Such preprocessing must be documented and applied consistently to training and later inputs.

The image is a numerical grid, not a digit label already understood by the network. The network must learn relationships between the input patterns and the target classes.

## 4.3 Preparing the Image

### Step 1: Check Dimensions

Every standard MNIST image has 28 rows and 28 columns:

```text
28 × 28 = 784 pixel values
```

A model designed to receive 784 input values expects a consistent input format. A different image size would require an appropriate preparation step or a different model design.

### Step 2: Check the Data

Check that images are readable, labels correspond to the intended digits, and preprocessing does not accidentally remove useful strokes. A blurry or ambiguous image should be reviewed rather than silently assigned a different label.

### Step 3: Normalize Pixel Values

One common preparation step is scaling the original 0–255 values into the 0–1 range:

```text
normalized pixel = original pixel ÷ 255
```

| Original value | Calculation | Normalized value |
|---:|---|---:|
| 0 | 0 ÷ 255 | 0.00 |
| 64 | 64 ÷ 255 | approximately 0.25 |
| 128 | 128 ÷ 255 | approximately 0.50 |
| 192 | 192 ÷ 255 | approximately 0.75 |
| 255 | 255 ÷ 255 | 1.00 |

These are numerical intensity conversions. Their on-screen colours depend on the chosen display palette. Dividing by 255 does not change a digit's class.

This is one preprocessing choice, not a requirement that every model must use this exact method. The [TensorFlow beginner example](https://www.tensorflow.org/tutorials/quickstart/beginner) applies this scaling to MNIST.

### Step 4: Flatten for This Model

For the simple fully connected model considered here, arrange the image into an ordered list of 784 values. This is **flattening**.

For example, read the first row left to right, then the second row, and continue through all 28 rows. The same ordering must be used for every image.

Flattening rearranges the values; it does not remove pixels. Other architectures, such as convolutional networks, can retain spatial dimensions rather than use this initial flattened representation.

### Step 5: Keep the Label Separate

```text
Image of 5
    |
    v
28 × 28 grayscale grid
    |
    v
Normalize the 784 pixel values
    |
    v
Flatten into an ordered vector → network input

Correct label: 5 → separate target for the training loss
```

The label is not appended as an extra pixel or a 785th input value. Doing so would give the model the answer it is supposed to predict.

## 4.4 How the Network Makes a Prediction

Consider an **illustrative architecture**:

- 784 input values;
- one hidden layer with 128 neurons and a nonlinear activation such as ReLU;
- 10 output scores, one for each digit class.

The input passes numerical information into the network. Each hidden neuron combines its inputs using weights, adds a bias, and applies an activation function. The output layer calculates class scores.

```text
784 pixel values → 128 hidden neurons → 10 class scores
```

Weights control contributions between connected units. Biases shift a neuron's calculation. Nonlinear activation functions allow the network to represent relationships that a stack of purely linear transformations cannot express. See Google's [neural-network introduction](https://developers.google.com/machine-learning/crash-course/neural-networks).

A hidden neuron does not necessarily correspond to a clear human concept such as “the top of a 5”. It responds to learned numerical combinations, which may be difficult to interpret.

### Scores, Probabilities, and the Predicted Class

Raw output scores are not automatically probabilities. A suitable transformation, such as softmax, can produce class probabilities. A training loss may instead accept raw scores and perform the required conversion internally.

For an image whose correct label is 5, imagine the following **invented probabilities**:

| Digit | Illustrative probability |
|---:|---:|
| 0 | 1% |
| 1 | 1% |
| 2 | 1% |
| 3 | 60% |
| 4 | 1% |
| 5 | 30% |
| 6 | 1% |
| 7 | 2% |
| 8 | 1% |
| 9 | 2% |

The probabilities sum to 100%. Digit 3 has the highest individual probability, so the predicted digit is **3**. The correct label remains **5**: the prediction is wrong for this example.

Tutorial 2 groups the eight remaining digits as “Others combined: 10%”. Their individual allocation here is also invented. Neither version reports a trained model's output.

Choosing the class with the largest score or probability is called **argmax**. It selects the position of the maximum value; it does not establish that the answer is correct or certain.

The complete calculation from input through the layers to output is a **forward pass**.

## 4.5 How the Network Learns

Producing a prediction is different from learning. Learning requires a procedure that uses examples to adjust the model's parameters.

### Calculate Loss

During supervised training, a loss function compares model outputs with the target. For the invented probability of 0.30 assigned to the correct digit 5, single-example cross-entropy is:

```text
loss = −ln(probability assigned to the correct class)
     = −ln(0.30)
     ≈ 1.20
```

This is one chosen classification loss. It is not the universal definition of error for every model or task. The [TensorFlow example](https://www.tensorflow.org/tutorials/quickstart/beginner) explains classification scores, probabilities, and cross-entropy.

### Calculate Gradients

**Backpropagation** works backward through the network's calculations to determine loss gradients with respect to parameters. Gradients describe how small parameter changes would locally affect loss.

Backpropagation supplies information for an update; it does not itself apply the update.

### Update Parameters

An **optimizer** uses gradients to update weights and biases. In a basic gradient-descent example, the learning rate controls the size of the step in the direction opposite to the gradient.

As a separate toy calculation:

```text
old weight = 0.40
learning rate = 0.10
gradient = 0.20

new weight = 0.40 − (0.10 × 0.20) = 0.38
```

This gradient is supplied for illustration. It was not calculated from the displayed digit model, and the update does not establish new classifier probabilities or a measured improvement.

### Repeat Across Examples

```text
Select a batch of training images and labels
                    |
                    v
Forward pass → loss → backpropagation → optimizer update
                    |
                    +----> repeat with further batches
```

A **batch** is a group of training examples processed together. An **epoch** is one full pass through the training set. If 60,000 images are used for parameter updates, an epoch processes those 60,000 examples once. If some are reserved for validation, the actual training set is smaller.

A learning rate that is too large can make training unstable; one that is too small can slow progress. One update does not guarantee a correct next prediction or better performance for every input.

## 4.6 Evaluating the Model

The standard MNIST split supplies 60,000 training images and 10,000 test images. A validation set can be reserved from the training portion.

| Split | Role |
|---|---|
| Training | Adjust parameters. |
| Validation | Monitor development and compare model choices. |
| Test | Evaluate the selected model after development decisions. |

Do not repeatedly tune settings against the test set. Otherwise, it becomes part of model selection and provides a less independent evaluation. Google's [overfitting module](https://developers.google.com/machine-learning/crash-course/overfitting) discusses data splitting and generalization.

### Accuracy

```text
accuracy = correct predictions ÷ total predictions
```

If a hypothetical model correctly classifies 90 of 100 images:

```text
90 ÷ 100 = 0.90 = 90%
```

This demonstrates arithmetic; it is not a measured MNIST result.

### Confusion Matrix

A **confusion matrix** compares true classes with predicted classes. With rows representing true digits and columns representing predicted digits, correct predictions fall on the diagonal and mistakes fall elsewhere.

For a ten-class digit task, the full matrix has ten rows and ten columns. It can reveal which digits the model confuses, rather than showing only the overall proportion correct. No particular confusion pattern is claimed without measured results.

### Loss and Accuracy Are Different

Accuracy records how often the selected class is correct. Loss evaluates outputs using the chosen mathematical rule and can reflect how much probability is assigned to the correct class.

Two models can have identical accuracy and different loss values. Lower training loss does not, by itself, establish better performance on new data.

## 4.7 What Can Change the Result?

- **Data quantity:** More relevant examples can expose the model to additional handwriting variations, but more data do not guarantee improvement.
- **Data quality:** Incorrect labels, damaged images, or preprocessing that removes strokes can make training less useful.
- **Representativeness:** A narrow range of handwriting styles may not prepare the model for its intended users.
- **Class balance:** All ten classes being present does not mean they have equal numbers of examples. Inspect their distribution.
- **Consistent preparation:** Image dimensions, normalization, inversion choices, and flattening order must match the model's expected format.
- **Architecture and training choices:** Layers, activation functions, optimizer, learning rate, and training duration all matter. A larger model is not automatically better.

**Overfitting** occurs when the model fits training data too specifically and performs less well on new examples. Improving training results alongside worsening validation performance can indicate this problem.

## 4.8 From Classroom Illustration to Real Use

Digit recognition connects to reading numbers from forms, postal codes, and scanned documents. However, a classifier for isolated MNIST images is not a complete document-reading system.

Real documents may contain shadows, coloured backgrounds, several digits together, unusual pens, or unfamiliar handwriting. Additional preparation, segmentation, testing, and error handling may be necessary.

Images can also contain personal information. Collect only appropriate data, respect access and consent requirements, and avoid exposing sensitive documents in examples. Where errors could affect people, provide suitable human review rather than treating a model prediction as an unquestionable fact.

## 4.9 The Complete Process

```text
DATA          Labelled images
                    |
PREPARATION   Check format and quality; normalize if appropriate
                    |
MODEL INPUT   Numerical pixel values; label kept separate
                    |
PREDICTION    Network outputs → selected digit class
                    |
TRAINING      Compare outputs with label → loss
                    |
              Backpropagation → gradients
                    |
              Optimizer → parameter update → repeat

EVALUATION    Check the selected model on separate data
```

**Inference** uses the model to predict from an input, normally without updating parameters or receiving the correct answer in advance. **Training** uses examples and targets to guide parameter updates.

## 4.10 Chapter Summary

An image becomes numerical input through a consistent preparation process. A network processes those values and produces class scores. The model's prediction can disagree with the correct label.

During supervised training, loss measures mismatch, backpropagation calculates gradients, and an optimizer updates parameters. Training repeats over examples. Separate evaluation is needed to assess whether the learned patterns work on new inputs.

The central lesson is that useful results depend on the data, representation, network, learning procedure, and evaluation together.

## Sources and Example Disclosure

1. [Keras — MNIST Digits Classification Dataset](https://keras.io/api/datasets/mnist/): dataset size, dimensions, pixel range, and labels.
2. [TensorFlow — MNIST Dataset Catalog](https://www.tensorflow.org/datasets/catalog/mnist): dataset structure and example images.
3. [TensorFlow — Quickstart for Beginners](https://www.tensorflow.org/tutorials/quickstart/beginner): normalization, flattened model inputs, scores, probabilities, cross-entropy, training, and evaluation.
4. [Google Machine Learning Crash Course — Neural Networks](https://developers.google.com/machine-learning/crash-course/neural-networks): network components and computation.
5. [Google Machine Learning Crash Course — Datasets, Generalization, and Overfitting](https://developers.google.com/machine-learning/crash-course/overfitting): data quality, splitting, and generalization.

**Disclosure:** The architecture, digit predictions, probability table, weight update, and accuracy example are illustrative. They are not results of a model trained for this chapter. Display colours are chosen for the educational presentation and must not be confused with the original dataset encoding.
