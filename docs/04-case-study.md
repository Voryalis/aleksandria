# Chapter 4 — Case Study: Teaching a Neural Network to Recognize Handwritten Digits

## 4.1 From individual ideas to one complete system

In the previous chapters, we built the pieces needed to understand a neural network:

- Chapter 1 showed that data must be collected, checked, and prepared before it can be useful.
- Chapter 2 introduced artificial neurons, weights, bias, activation functions, and layers. These are the parts a network uses to turn numerical inputs into an output.
- Chapter 3 explained how a network learns: it makes a prediction, compares that prediction with the correct answer, measures the error, and adjusts its parameters.

Now we can put those ideas together in one practical case study.

Our task is simple to describe: **given an image of a handwritten digit, predict which digit it shows.** The possible answers are the ten digits from 0 to 9.

A person can usually recognize a familiar handwritten digit almost instantly. A computer, however, does not begin by seeing a “seven” or a “three”. It receives data. In this example, the data is a grid of pixel values. The neural network must learn which patterns of values tend to belong to each digit.

We will use the MNIST dataset, a widely used collection of handwritten-digit images. The purpose of this chapter is not to claim that we have trained a particular model or achieved a particular score. Instead, we will follow the full process and use clearly marked illustrative examples to understand what happens at each stage.

## 4.2 Meet the MNIST dataset

**MNIST** is a dataset of handwritten digits used to study and test image-recognition methods. It contains 70,000 labelled images:

- 60,000 images are provided as the standard training set.
- 10,000 images are provided as the standard test set.
- Each image is a grayscale image measuring 28 pixels wide and 28 pixels high.
- Each image represents one digit, from 0 to 9, and has a label identifying that digit.

A **label** is the correct answer attached to an example. If an image shows a handwritten 6, its label is `6`. The image provides the input; the label tells us what the model is supposed to learn to predict.

Why use MNIST? It gives us a manageable task with a clear answer. The images are small, the possible classes are easy to understand, and the labels make supervised learning possible. It is also useful for comparing methods because many learners and researchers have used the same dataset.

MNIST is not a perfect representation of every kind of handwriting. Its images have a particular size, style, and format. A system trained on MNIST should not automatically be expected to work equally well on photographs of notebook pages, writing from every country, or digits written with unusual pens and layouts. We will return to this limitation later.

### What does one image contain?

A grayscale image stores a brightness value for each pixel. In the standard MNIST representation, a pixel value ranges from 0 to 255:

- `0` represents black.
- `255` represents white.
- Values between them represent shades of grey.

For example, a dark stroke in a handwritten digit may have low pixel values, while the light background may have values close to 255. The exact pattern depends on the handwriting.

The network does not receive the image as a human-readable drawing. It receives the numerical values that describe the image. This connects directly to Chapter 1: an image may look like a picture to us, but for a learning system it is data in a particular representation.

## 4.3 Preparing an image for the network

Before an image can be used as input, it must have a consistent format. **Preprocessing** means changing or checking raw data so that it is suitable for a particular task. We met this idea in Chapter 1 when we discussed missing values, inconsistent formats, incorrect labels, and normalization.

For MNIST, the preparation steps are relatively straightforward.

### Step 1: Check the image dimensions

Every standard MNIST image is 28 × 28 pixels. That means it has:

\[
28 \times 28 = 784
\]

individual pixel values.

A consistent image size matters because the network expects inputs with a fixed number of values. If one image contained 784 values and another contained 900, a network designed for 784 input features could not accept both in the same way without an additional resizing or formatting step.

### Step 2: Use the pixel values

Each of the 784 pixels has a brightness value from 0 to 255. The values describe the image, but their original scale is not always the most convenient scale for training.

### Step 3: Normalize the values

**Normalization** is a preprocessing method that changes numerical values to a more suitable scale while preserving the information needed for the task. Here, we divide every pixel value by 255.

\[
\text{normalized pixel} = \frac{\text{original pixel}}{255}
\]

The result is a value between 0 and 1. A black pixel remains 0, a white pixel becomes 1, and a grey pixel becomes a value between them.

For example:

| Original pixel value | Calculation | Normalized value |
|---:|---:|---:|
| 0 | 0 ÷ 255 | 0 |
| 64 | 64 ÷ 255 | approximately 0.25 |
| 128 | 128 ÷ 255 | approximately 0.50 |
| 192 | 192 ÷ 255 | approximately 0.75 |
| 255 | 255 ÷ 255 | 1 |

This is the same basic idea introduced in Chapter 1. We are not changing a digit from one class into another; we are expressing its pixel brightness on a consistent scale. A smaller, consistent numerical range can make the values easier for a neural network to work with during training.

### Step 4: Flatten the image into a vector

A neural network made from ordinary fully connected layers needs an ordered list of input numbers. We therefore turn the 28 × 28 grid into a single list containing 784 values. This operation is called **flattening**.

Flattening does not mean removing pixels or changing their brightness. It means arranging the existing values in a fixed order: for example, reading the first row from left to right, then the second row, and continuing until all rows have been read.

The result is a **vector**: an ordered list of numbers. In this case, the vector has 784 entries.

The original image has a two-dimensional arrangement, but the flattened vector is one-dimensional. The order must remain consistent for every image. If the first pixel represents the top-left corner in one example, it must represent the same position in every other example.

The network can now receive the image as 784 numerical input features. A **feature** is an individual piece of information used by a model to make a prediction. Here, each pixel value is one feature.

### Step 5: Keep the label separate

The image vector is the input. Its digit label is the target answer used during supervised training. We must not mix the label into the input vector: otherwise, the model could be given the answer it is meant to predict.

For example, an image of a handwritten 4 is represented by 784 pixel values, while the label `4` is stored separately. During training, the network receives the pixel values and its prediction is compared with the label.

<figure>
<pre>
Handwritten image
      |
      v
28 × 28 grayscale pixels
      |
      v
784 pixel values (0–255)
      |
      v
Normalize: divide each value by 255
      |
      v
784 values between 0 and 1
      |
      v
Flatten into an ordered input vector

Correct digit label -----------------> kept separately
</pre>
</figure>

This process brings together several ideas from Chapter 1: consistent representation, preprocessing, numerical data, normalization, and the separation of input data from its label.

## 4.4 How the network makes a prediction

The prepared vector is ready to enter the neural network. To make the example concrete, imagine a simple fully connected network with:

- 784 input units, one for each pixel value;
- one hidden layer containing 128 neurons;
- 10 output units, one for each possible digit.

We will call this an **illustrative architecture**. It is a teaching example, not a claim that this exact architecture was trained for this chapter or that it achieves a particular level of accuracy. Other network designs are possible.

### The input layer

The input layer receives the 784 normalized pixel values. It does not need to decide what the digit is. Its role is to pass the numerical information into the network.

This connects to Chapter 2: the input features are the numbers that the network will process. The pixels are not yet meaningful labels such as “top curve” or “vertical line”; they are simply numerical inputs.

### The hidden layer

The 128 neurons in the hidden layer receive values from the preceding layer. Each neuron calculates a weighted sum, adds a bias, and applies an activation function.

Recall the terms from Chapter 2:

- A **weight** is a numerical parameter that controls how strongly one input contributes to a neuron's calculation.
- A **bias** is a numerical parameter added to the weighted sum, allowing the neuron to shift the point at which it activates.
- An **activation function** is a rule applied to a neuron's calculation to produce its output. It helps the network represent more complex relationships than a stack of purely linear calculations could represent.

For example, a neuron may respond strongly to a particular combination of dark and light pixels. Another may respond to a different combination. During training, the network adjusts its weights and biases so that useful patterns can contribute to better digit predictions.

We should be careful with the word “recognize”. A hidden neuron does not necessarily correspond to a neat human concept such as “the top of a 7”. The network learns numerical patterns that help it solve the task. We can sometimes inspect what a neuron responds to, but we should not assume that every neuron has one simple, human-readable meaning.

### The output layer

The output layer contains 10 units, corresponding to the ten possible digits:

`0, 1, 2, 3, 4, 5, 6, 7, 8, 9`

Each output unit produces a **score** for its digit class. A score is a numerical value used to compare how strongly the model supports one possible answer relative to the others.

For an illustrative image, the output might look like this:

| Digit | Illustrative score |
|---:|---:|
| 0 | 0.02 |
| 1 | 0.01 |
| 2 | 0.03 |
| 3 | 0.04 |
| 4 | 0.05 |
| 5 | 0.08 |
| 6 | 0.03 |
| 7 | 0.69 |
| 8 | 0.02 |
| 9 | 0.03 |

In this example, the largest score belongs to digit 7, so the model's predicted class is 7.

The numbers in this table are invented solely to demonstrate the decision. They are not measured MNIST results. Also, raw output scores are not automatically probabilities. A model may use a separate output transformation to turn scores into probabilities. The important point here is that the largest score can be selected as the predicted class.

The operation of choosing the class with the largest score is often called **argmax**. In simple terms, it means “find the position of the largest value”. If the highest score is in the output position for digit 7, the prediction is 7.

### A complete forward pass

A **forward pass** is the process of sending input data through a network, layer by layer, to produce an output. It is called “forward” because information moves from the input layer towards the output layer.

For our digit example:

1. The network receives 784 normalized pixel values.
2. The input values are passed to the hidden layer.
3. Each hidden neuron calculates its weighted sum, adds its bias, and applies its activation function.
4. The hidden-layer outputs are passed to the output layer.
5. The 10 output units produce scores.
6. The model selects the digit with the highest score as its prediction.

This is the prediction process described in Chapter 2, now applied to a real dataset format.

## 4.5 How the network learns from MNIST

Making a prediction is not the same as learning. A network can produce an answer even when its weights and biases are not yet useful. Learning happens when training examples are used to improve those parameters.

MNIST provides images and their correct labels, so it supports **supervised learning**. Supervised learning is a method in which a model learns from examples that include both input data and the correct target answer. The model makes a prediction, compares it with the target, and uses the difference to guide improvement.

### Prediction and target

Imagine that the network receives an image whose correct label is 7.

- The input is the image represented by 784 pixel values.
- The target is the label 7.
- The prediction is the class selected by the network.

If the network predicts 7, its predicted class matches the target. If it predicts 1, the prediction is incorrect. During training, the model needs a numerical way to measure how well its output matches the target.

### Loss: measuring how wrong a prediction is

A **loss function** is a mathematical rule that calculates a number representing how poorly a model's prediction matches the correct target. The number is used during training to guide the model towards better predictions.

A smaller loss generally indicates a better match under the chosen loss function. A larger loss indicates a worse match. Loss is useful because “that answer looks wrong” is not precise enough for a learning algorithm: the training process needs a numerical signal.

For classification tasks such as digit recognition, one commonly used choice is **cross-entropy loss**. It evaluates the model's output in relation to the correct class. In a typical classification setup, it uses predicted class probabilities, or raw scores supplied to a compatible loss calculation that handles the required conversion internally.

The main idea is more important than the formula at this stage: the loss function gives the network a measurable training signal. It does not itself change the weights. It tells us how well the current model is doing on the example or batch being considered.

### Backpropagation: finding how parameters affect the loss

The next question is: how can the network know which weights and biases should change?

**Backpropagation** is the method used to calculate how changes in a network's parameters affect the loss. It works backwards from the output towards earlier layers, calculating information that can be used to adjust the parameters.

Chapter 3 introduced this idea through gradients. A **gradient** describes how a quantity changes when one or more parameters change. In neural-network training, gradients indicate how the loss would change if particular weights or biases changed slightly.

An intuitive way to think about it is to imagine adjusting the controls on a machine. If the result is not right, we want to know which controls have the greatest effect on the error and in which direction they should move. Backpropagation calculates this guidance for the network's parameters.

Backpropagation calculates gradients; it does not, by itself, perform the parameter update. These are connected but different operations.

### The optimizer: updating the parameters

An **optimizer** is the method or algorithm that uses gradients to update a model's parameters during training. It takes the information calculated during backpropagation and changes weights and biases in an attempt to reduce the loss.

One important setting is the **learning rate**. The learning rate controls the size of the parameter updates.

- If the learning rate is too large, updates may overshoot useful values and training can become unstable.
- If it is too small, learning may be very slow.
- A suitable learning rate helps the model make useful progress.

This links directly to Chapter 3: backpropagation calculates gradients, while the optimizer uses them to update the parameters. The network then makes another prediction with its updated parameters.

### Repeating the process: batches and epochs

Training does not usually stop after one image. The network needs to process many labelled examples so that its parameters can improve across a range of handwriting styles.

A **batch** is a group of training examples processed together before a parameter update. Instead of updating the network after every single image, a training procedure may calculate loss and gradients using a batch of images, then update the parameters.

An **epoch** is one complete pass through the training dataset. If the training set contains 60,000 images, one epoch means that the training procedure has processed all 60,000 training examples once. The examples may be divided into many batches.

A simplified training cycle looks like this:

<pre>
Training images + labels
          |
          v
      Select a batch
          |
          v
   Forward pass: predict
          |
          v
 Compare prediction with label
          |
          v
       Calculate loss
          |
          v
 Backpropagation: calculate gradients
          |
          v
 Optimizer: update weights and biases
          |
          v
     Process next batch
          |
          v
 Repeat until an epoch is complete
          |
          v
 Repeat for further epochs as needed
</pre>

The network is not storing a list of handwritten examples and looking up the answer each time. Training changes numerical parameters so that the model can apply what it has learned to images it has not seen before.

## 4.6 How do we know whether the model works?

A model can perform well on the examples it has already used for learning and still make mistakes on new examples. We therefore need a careful evaluation process.

Chapter 3 introduced three useful dataset splits:

- The **training set** is used to adjust the model's parameters.
- The **validation set** is used during development to compare choices and monitor performance. It is commonly created by setting aside part of the available training data.
- The **test set** is held back until final evaluation. It provides an estimate of how well the model performs on data that was not used to train or tune it.

For the standard MNIST dataset, the supplied split contains 60,000 training images and 10,000 test images. If we need a validation set, we can reserve part of the 60,000 training images for that purpose. The test set should remain separate from decisions made during training and model selection.

This separation matters. If we repeatedly use the test set to choose settings, it gradually becomes part of the development process. The final test result may then give an overly optimistic picture of performance on genuinely unseen data.

### Accuracy

**Accuracy** is the proportion of predictions that are correct out of all predictions made.

\[
\text{Accuracy} =
\frac{\text{number of correct predictions}}
{\text{total number of predictions}}
\]

For example, suppose a model correctly classifies 90 out of 100 images in a small illustrative evaluation. Its accuracy is:

\[
\frac{90}{100} = 0.90 = 90\%
\]

This is a made-up example to explain the calculation, not a reported MNIST model result.

Accuracy is easy to understand, but it does not tell us everything. It tells us how many predictions were correct overall, not which digits were confused with which other digits.

### Confusion matrix

A **confusion matrix** is a table that compares the true classes with the classes predicted by a model. It helps us see which kinds of mistakes the model makes.

For digit recognition, a confusion matrix has ten true-digit categories and ten predicted-digit categories. A correct prediction appears where the true digit and predicted digit match. An incorrect prediction appears in a different column from the true digit's row.

For example, a model might sometimes confuse handwritten 4s with 9s, or 3s with 5s. These are illustrative possibilities, not claims about a measured MNIST model. Looking at the confusion matrix helps us ask more useful questions than “What was the accuracy?” We can ask which digits are difficult and whether certain handwriting styles cause repeated errors.

### Loss and accuracy are not the same

Loss and accuracy both help us evaluate a model, but they describe different things.

- **Loss** measures the quality of predictions according to a chosen mathematical loss function. It can reflect how strongly the model supports the correct answer.
- **Accuracy** counts how many predicted classes are correct.

A model can predict the correct class but still have a relatively high loss if its output does not match the target as strongly as desired. Conversely, two models can have the same accuracy but different loss values.

That is why training often monitors loss as well as accuracy. They provide different information about model behaviour.

## 4.7 What can change the result?

A neural network's performance depends on more than the choice of algorithm. The data, its preparation, and the training process all matter. This connects the three earlier chapters: data quality from Chapter 1, network structure from Chapter 2, and the learning process from Chapter 3.

### The amount of data

More training examples can expose a model to more variations in handwriting. For example, the digit 2 can be written with a rounded top, a straight diagonal, or a long base. Seeing many examples may help the network learn that these different shapes can still represent the same digit.

However, more data does not automatically guarantee better results. If many examples are incorrectly labelled, duplicated, or unlike the examples the system will later encounter, simply increasing the dataset size may not solve the problem.

### The quality of data

Incorrect labels teach the wrong relationship. If an image of a 5 is labelled as 3, the network is asked to associate that image with the wrong answer. Repeated label errors can make learning more difficult.

Poor image quality can also matter. A digit may be faint, partly missing, blurred, or cropped. A preprocessing step that accidentally removes part of a digit can damage useful information.

This is why Chapter 1 treated data checking as an essential step rather than an optional cleanup task.

### Variation in handwriting

People write digits differently. Some write an open-top 4; others close it. Some write 1 with a small base or a top stroke. A useful dataset should include enough variation to help the model handle the kinds of handwriting it is expected to encounter.

A model trained on one narrow style may struggle when the writing style changes. This is an example of why the data used for training should be representative of the intended task.

### Class balance

A **class** is one of the categories a classification model is asked to choose from. In MNIST, the ten classes are the digits 0 through 9.

A dataset is **class-balanced** when its categories have similar numbers of examples. If one digit appears much more often than the others, a model may receive more training exposure to that digit. It is therefore useful to inspect how examples are distributed across classes rather than assume that a dataset is perfectly balanced.

The presence of all ten digits is necessary, but it does not by itself prove that the number of examples in each class is equal.

### Image preparation

The network expects inputs in a consistent format. If training images are normalized one way but later images are prepared differently, the model may receive values unlike those it learned from.

For example, suppose training images use pixel values between 0 and 1, but new images are supplied with values between 0 and 255. The numerical scale is now different. The system may behave poorly because its inputs no longer follow the same preparation process.

The same issue can arise if images have different dimensions, are cropped inconsistently, or are flattened in a different order.

### Network and training choices

The number of layers, number of neurons, activation functions, optimizer, learning rate, and number of epochs can all influence training. These are design and training choices, not magic settings that guarantee success.

A larger network is not automatically better. It may require more computation and can learn patterns that do not generalize well. A smaller network may be faster but may not capture enough useful patterns for a difficult task.

The right choices depend on the task, the data, and how the model will be evaluated.

### Overfitting

**Overfitting** happens when a model learns the training examples too specifically and performs less well on new examples. It may learn details or noise that happen to appear in the training data rather than patterns that generalize.

Imagine a learner who memorizes the answers to a practice sheet but cannot solve a slightly different question. The learner has remembered the examples without learning the broader idea. Overfitting is similar: the model performs well on familiar training data but struggles with unseen data.

The training, validation, and test split helps us notice this problem. If training performance keeps improving while validation performance stops improving or becomes worse, that can be a warning sign.

## 4.8 From a classroom example to real use

Handwritten-digit recognition is a useful demonstration because the input and expected output are easy to understand. Similar ideas can be used in systems that read numbers from forms, process postal codes, or recognize characters in scanned documents.

However, success on MNIST does not prove that a system is ready for every real-world use. Real documents may contain coloured backgrounds, lines, shadows, unusual fonts, low-resolution images, or several digits close together. A system designed for isolated 28 × 28 images may need substantial changes before it can process a full page.

A model should also be used with an understanding of its limitations. If a prediction is uncertain or incorrect, there should be a suitable way to detect or handle that situation. In applications where an error could affect a person, automated predictions may need human review.

This chapter introduces these points only briefly. The next chapter is reserved for a fuller discussion of ethics, responsible use, resources, and the glossary.

## 4.9 The complete process

We can now connect the main ideas from all four chapters in one sequence:

<pre>
DATA
MNIST images and their digit labels
        |
        v
PREPARATION
Check dimensions, use pixel values,
normalize, flatten, keep labels separate
        |
        v
MODEL
Input layer → hidden layer → output layer
Weights, biases, and activation functions
        |
        v
PREDICTION
Scores for digits 0–9
Choose the class with the highest score
        |
        v
COMPARISON
Compare prediction with the correct label
        |
        v
LOSS
Calculate how well the prediction matches
the target under the chosen loss function
        |
        v
IMPROVEMENT
Backpropagation calculates gradients
Optimizer updates weights and biases
        |
        v
EVALUATION
Use separate data to check performance
Accuracy, loss, and confusion matrix
</pre>

The process has two related modes:

- **Inference** is using a trained model to make a prediction for an input. For example, we provide an image of a handwritten digit and the model returns its predicted class.
- **Training** is the process of using labelled examples, loss, gradients, and optimizer updates to improve the model's parameters.

During inference, the model normally does not update its weights. During training, it repeatedly uses examples and feedback to adjust them.

The central lesson is that a neural network does not learn from an image simply because the image is shown to it. The image must be represented as data; the network must process that data; and training must provide a way to compare predictions with correct answers and improve the model.



## 4.11 Chapter summary

In this case study, we followed a handwritten digit from an image to a neural-network prediction.

- MNIST contains 70,000 labelled grayscale images of handwritten digits, with a standard split of 60,000 training images and 10,000 test images.
- Each image is 28 × 28 pixels, giving 784 pixel values.
- Normalization changes pixel values from the 0–255 range to the 0–1 range by dividing by 255.
- Flattening arranges the 784 values into one ordered input vector.
- The label is kept separate and provides the target during supervised training.
- A neural network processes the input through layers and produces scores for the ten digit classes.
- The predicted class can be selected by choosing the largest output score.
- During training, loss measures the mismatch with the target, backpropagation calculates gradients, and an optimizer updates the parameters.
- Separate training, validation, and test data help us train and evaluate the model responsibly.
- Accuracy, loss, and a confusion matrix provide different views of model performance.
- Data quality, handwriting variation, class balance, preprocessing, and training choices can all affect results.
- Overfitting occurs when a model fits training examples too specifically and performs less well on new data.

The journey from image to prediction brings together the foundations from the previous chapters: data must be prepared, a model must process it, and a learning method must improve it.

## Notes on examples and results

The dataset facts in this chapter describe the standard MNIST dataset. The 784–128–10 network is an illustrative architecture. The output scores, accuracy calculation, possible digit confusions, and activity scenarios are invented teaching examples. No trained-model accuracy or experimental result is claimed here.

## Sources

- [MNIST database of handwritten digits — Yann LeCun, Corinna Cortes, and Christopher J. C. Burges](http://yann.lecun.com/exdb/mnist/)
- [Google Machine Learning Crash Course — Datasets and their characteristics](https://developers.google.com/machine-learning/crash-course/overfitting/data-characteristics)
- [Google Machine Learning Crash Course — Numerical-data normalization](https://developers.google.com/machine-learning/crash-course/numerical-data/normalization)
- [Google Machine Learning Crash Course — Neural networks](https://developers.google.com/machine-learning/crash-course/neural-networks)
- [Michael Nielsen — Neural Networks and Deep Learning](https://neuralnetworksanddeeplearning.com/)
