# Chapter 3 — How a Neural Network Learns

**Version:** Stage 2 revised draft, 6 November 2026. Pending team acceptance.

**Audience:** Beginners with basic high-school mathematics and no previous machine-learning or programming experience.

**Prerequisites:** [Chapter 1 — Big Data](01-big-data.md) · [Chapter 2 — Artificial Neurons and Connected Networks](02-connectionist-ai.md)

**Guiding question:** How does a neural network use examples, measure mistakes, and adjust its parameters?

## Chapter Purpose and Learning Objectives

Chapter 1 introduced numerical image data and preprocessing. Chapter 2 explained how connected neurons use weights, biases, and activation functions to produce outputs. This chapter explains **training**: using examples and a learning algorithm to adjust a network's parameters.

We follow an illustrative image of the digit **5**, matching the target digit in Tutorials 1 and 2. The model's prediction and the supplied correct label remain separate. All numerical model outputs and parameter updates below are invented teaching examples, not experimental results.

After studying this chapter, learners should be able to:

1. Explain the roles of input features and target labels in supervised learning.
2. Distinguish training, validation, and test sets.
3. Distinguish a model prediction from a reference label.
4. Calculate a simple squared-error loss and explain its purpose.
5. Describe gradients and the role of backpropagation.
6. Explain how an optimizer uses gradients and a learning rate to update parameters.
7. Describe a repeated training cycle and recognize limitations such as overfitting and poor data quality.

## 3.1 Learning from Examples with Known Answers

In **supervised learning**, examples contain both input data and a known target. The network produces an output from the input. The training process compares this output with the target and uses that comparison to guide parameter updates.

For handwritten-digit recognition, the input is an image represented by numerical pixel values. The target is the correct digit recorded with that image. For our example, the target label is **5**.

Standard MNIST images have 28 rows and 28 columns: `28 × 28 = 784` pixel positions. A simple fully connected model can use a flattened list of 784 values. A smaller 5 × 5 diagram may illustrate the same idea with 25 values, but it is a toy illustration rather than the standard MNIST format. Other network architectures can preserve spatial dimensions. See the [TensorFlow MNIST example](https://www.tensorflow.org/tutorials/quickstart/beginner).

```text
Image of digit 5 → prepared pixel values → neural network → model output
                                                                |
                                                                v
Correct label: 5 ------------------------------------------> loss calculation
```

The target label is **not another pixel or an extra input feature**. During training, it is used to calculate loss. During ordinary inference on a new image, the correct label is not supplied to the model in advance.

### Training, Validation, and Test Sets

Separate groups of examples serve different purposes:

| Dataset split | Purpose |
|---|---|
| Training set | Calculate learning signals and update weights and biases. |
| Validation set | Compare model choices and monitor performance during development. |
| Test set | Evaluate the selected model after development decisions have been made. |

```text
Checked examples
      |
      +-- Training set ----> learn and update parameters
      |
      +-- Validation set --> compare choices during development
      |
      +-- Test set --------> final evaluation
```

There is no universal split percentage suitable for every task. The important point is to preserve the different roles. Repeatedly using test results to select settings turns the test set into part of development and weakens its value as an independent evaluation.

Duplicates, near-duplicates, or related versions of the same original image can cause **data leakage** if they cross between splits. Training and evaluation data should also reflect the situations the model is expected to handle. These principles are discussed in Google's [datasets, generalization, and overfitting module](https://developers.google.com/machine-learning/crash-course/overfitting).

## 3.2 A Prediction Is Not the Correct Answer

The network processes the input and produces output scores. For a digit classifier, each score corresponds to a candidate digit. Selecting the highest-scoring class gives a predicted digit.

The **prediction** comes from the model. The **reference label** comes from the checked dataset. They can disagree.

| Item | Illustrative value | Origin |
|---|---|---|
| Correct label | 5 | Label supplied with the training example |
| Highest-scoring output class | 3 | Hypothetical model output |
| Predicted digit | 3 | Class selected from the model's output scores |

The model has predicted **3**, while the correct label is **5**. It is wrong on this example. This single comparison does not tell us its overall accuracy across a dataset.

Raw scores are not automatically probabilities and do not necessarily add to 1. A suitable transformation, such as softmax in a multiclass classifier, can convert scores into probabilities. The distinction is demonstrated in the [TensorFlow beginner tutorial](https://www.tensorflow.org/tutorials/quickstart/beginner).

Tutorial 2 uses an explicitly invented probability example: digit 3 receives 60%, digit 5 receives 30%, and the other eight digits receive 10% combined. The predicted class is 3 because it has the largest individual probability. These are teaching values, not MNIST benchmark results.

## 3.3 Loss: Putting a Number on the Mismatch

A **loss function** is a mathematical rule for comparing a model's output with its target. Its result, the **loss**, provides a numerical training signal. Loss does not itself change parameters.

Different tasks use different loss functions. To introduce the arithmetic, consider a separate single-output example with a numerical target. Define its loss as squared error:

```text
Target value:       1.0
Model output:       0.6
Difference:         0.6 − 1.0 = −0.4
Squared-error loss: (−0.4)² = 0.16
```

If the output were 0.9 instead:

```text
Loss = (0.9 − 1.0)² = (−0.1)² = 0.01
```

For this particular rule, the second output is closer to the target and has a smaller loss. This is a scalar teaching example; it is not a calculation performed directly on digit class numbers, and it is not the universal loss for digit classification.

For multiclass classification, a common choice is **cross-entropy**. In the probability example used in Tutorial 2, the correct digit 5 receives probability 0.30. Its single-example cross-entropy is:

```text
Loss = −ln(probability assigned to the correct class)
     = −ln(0.30)
     ≈ 1.20
```

Here, `ln` means the natural logarithm. Giving more probability to the correct class lowers this loss. Implementations may accept probabilities or raw scores and handle the conversion internally; the loss must be configured to match the model output. See the [TensorFlow classification example](https://www.tensorflow.org/tutorials/quickstart/beginner).

Loss and accuracy measure different things. Accuracy records how many predicted classes are correct; a classification loss also depends on the model's output values. Two models can have the same accuracy but different losses. Lower training loss alone does not prove better performance on unseen data.

## 3.4 Gradients and Backpropagation

A network may contain many adjustable **parameters**, including weights and biases. Loss tells us how well the current output fits a target, but it does not by itself identify which parameters should change.

A **gradient** describes how loss changes with respect to model parameters. For one parameter, the derivative's sign indicates the local direction of change, and its magnitude describes local sensitivity. With many parameters, the gradient collects this information across them.

Imagine standing on a slope. The gradient points toward the steepest local increase. Taking a sufficiently small step in the opposite direction can lower your height. This is only an analogy: a network's loss depends on many parameters, rather than two geographical coordinates.

**Backpropagation** efficiently calculates loss gradients by working backward through the network's connected calculations using the chain rule. No calculus derivation is needed to distinguish its role:

```text
Forward pass:     input → network output → loss
Backward pass:    loss → gradients through the network
```

**Backpropagation calculates gradients; it does not itself apply the parameter update.** A gradient is also different from the loss value. Loss measures the current mismatch, while gradients describe local changes in that loss. Google's [neural-network module](https://developers.google.com/machine-learning/crash-course/neural-networks) introduces network computation and training.

## 3.5 The Optimizer Updates Parameters

An **optimizer** uses gradients to choose and apply parameter updates. A basic example is **gradient descent**, which moves parameters in the direction opposite to their gradients.

The **learning rate** controls the size of the step. A very small rate can make learning slow; an excessively large rate can overshoot useful values or make training unstable.

Consider a separate invented one-parameter update:

```text
Old weight:       0.50
Gradient:         +0.40
Learning rate:    0.10

New weight = old weight − (learning rate × gradient)
           = 0.50 − (0.10 × 0.40)
           = 0.46
```

The positive gradient indicates that increasing this weight would locally increase loss, so gradient descent decreases it. This calculation illustrates the update rule. The gradient is supplied for the example; it was not derived from the earlier digit probabilities or the scalar-loss example.

Tutorial 2 uses another standalone example of the same rule:

```text
0.40 − (0.10 × 0.20) = 0.38
```

Neither calculation establishes a measured improvement or produces a new set of classifier probabilities. A single update does not guarantee correct predictions or lower loss for every input. Google's [gradient-descent explanation](https://developers.google.com/machine-learning/crash-course/linear-regression/gradient-descent) develops the update rule using linear regression.

### Repeated Training

```text
1. Select labelled training examples
                  |
                  v
2. Forward pass: produce model outputs
                  |
                  v
3. Compare outputs with targets and calculate loss
                  |
                  v
4. Backpropagation: calculate gradients
                  |
                  v
5. Optimizer: update weights and biases
                  |
                  +----> repeat with more training examples
```

A **batch** is a group of examples processed together. In the standard training loop described here, an **iteration** processes a batch and applies an update. An **epoch** is one complete pass through the training set. One epoch can contain many iterations, and training can use multiple epochs.

Training changes the parameters. **Inference** uses a model to produce outputs for inputs and normally does not update those parameters.

## 3.6 Why Good Training Results Are Not Enough

The goal is to learn patterns that remain useful on new examples, not simply to achieve a small loss on familiar training data.

### Overfitting and Generalization

**Overfitting** occurs when a model fits training data too specifically, including details or noise that do not help with new data. It may perform well during training and much less well on unseen examples.

**Generalization** is the ability to produce useful outputs for new data beyond the examples used for training. During development, improving training performance alongside worsening validation performance can be a warning sign of overfitting. The test set is reserved for the selected model's final evaluation. See Google's [overfitting module](https://developers.google.com/machine-learning/crash-course/overfitting).

### Unrepresentative Data

If the training data cover only a narrow range of handwriting styles, the network may struggle with other styles. Adding more examples of the same narrow type does not necessarily fix the coverage gap. An unusual example is not automatically an incorrect example.

### Incorrect Labels and Other Quality Problems

An incorrect label supplies the wrong target. If an image of 5 is labelled 3, supervised training is asked to associate that input with the wrong class. Repeated label errors, duplicated examples, missing information, and damaged images can all reduce the usefulness of training data.

Validation and test sets help reveal problems; they do not repair poor data. More epochs, more data, or a larger network do not automatically guarantee better results.

## Chapter Summary

- Supervised learning uses input data and separate target labels.
- Model predictions may disagree with the supplied correct answers.
- A chosen loss function measures mismatch numerically.
- Backpropagation calculates gradients of loss with respect to parameters.
- An optimizer uses gradients and a learning rate to update parameters.
- Training repeats across examples; inference normally uses parameters without updating them.
- Validation supports development decisions, while test data support final evaluation.
- Data quality, representativeness, and overfitting affect performance on new examples.

## Glossary

| Term | Meaning |
|---|---|
| Supervised learning | Learning from examples containing input data and known targets. |
| Target / reference label | The supplied answer associated with an example. |
| Prediction | An output produced by the model for an input. |
| Training set | Examples used for learning and parameter updates. |
| Validation set | Separate examples used to compare choices during development. |
| Test set | Separate examples reserved for final evaluation. |
| Loss | A numerical mismatch measure calculated using a chosen loss function. |
| Squared error | The square of the difference between a numerical output and its target. |
| Cross-entropy | A classification loss that penalizes assigning low probability to the correct class. |
| Parameter | An adjustable model value, such as a weight or bias. |
| Gradient | Local rates of change of a quantity with respect to parameters. |
| Backpropagation | An algorithm for calculating loss gradients backward through a network. |
| Optimizer | An algorithm that applies parameter updates; the examples here use gradients. |
| Gradient descent | Updating parameters in the direction opposite to their gradients. |
| Learning rate | A setting controlling update step size. |
| Forward pass | Calculating the model's output from its input. |
| Batch | A group of examples processed together. |
| Iteration | One batch-processing and update step in the training loop described here. |
| Epoch | One complete pass through the training set. |
| Inference | Using a model to produce an output for an input. |
| Overfitting | Fitting training examples too specifically and generalizing poorly. |
| Generalization | Producing useful outputs for new data beyond the training examples. |

## Sources

1. [Google Machine Learning Crash Course — Neural Networks](https://developers.google.com/machine-learning/crash-course/neural-networks): network computation and training concepts.
2. [Google Machine Learning Crash Course — Datasets, Generalization, and Overfitting](https://developers.google.com/machine-learning/crash-course/overfitting): data quality, dataset splits, and generalization.
3. [Google Machine Learning Crash Course — Linear Regression: Gradient Descent](https://developers.google.com/machine-learning/crash-course/linear-regression/gradient-descent): gradients, learning rate, and parameter updates.
4. [TensorFlow — Quickstart for Beginners](https://www.tensorflow.org/tutorials/quickstart/beginner): MNIST preprocessing, flattened inputs, probabilities, classification loss, training, and evaluation.

**Example disclosure:** The digit predictions, probabilities, scalar outputs, and weight updates in this chapter are hypothetical teaching examples. No model experiment or accuracy result is claimed.
