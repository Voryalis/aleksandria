# Chapter 2 — Artificial neurons and connected networks

**Status:** Fully developed Stage 1 *non-introductory* teaching sample; pending Content Lead and QA review.  
**Prerequisite:** [Chapter 1 — From raw data to model inputs](01-big-data.md) · [Module structure](Chapters.md)

## Learning objectives

After this chapter, you should be able to:

1. Identify a neuron's inputs, weights, bias, weighted sum, and activation.
2. Compute the output of a two-input ReLU neuron from supplied numbers.
3. Explain what input, hidden, and output layers do.
4. Trace a prepared digit image through a conceptual network without confusing a label with a prediction.
5. Explain what training will eventually change and distinguish inference from training.

**Guiding question:** How can simple mathematical operations, repeated across connected artificial neurons, produce a prediction about an image?

## 2.1 From data to an artificial neuron

In Chapter 1 we represented a toy 5 × 5 handwritten-digit image as **25 ordered numerical pixel features** and a separate **target label**. Now we need a model that can use those numbers.

**Connectionist AI** describes approaches based on interconnected processing units whose collective activity performs a task. Artificial neural networks are a central example. They are simplified computational models; artificial neurons are *not* literal biological nerve cells. [1][2]

A single **artificial neuron** combines input values mathematically. In a common form, it takes a weighted sum, adds a bias, then applies an activation function.

```text
Input x1 ----(weight w1)----\
                              > [ add weighted inputs + bias ] -> z -> [activation] -> output a
Input x2 ----(weight w2)----/
                                       bias b
```

With two input features, the calculation is:

```text
z = (w1 × x1) + (w2 × x2) + b
a = f(z)
```

Here:

| Symbol | Meaning | Why it matters |
| --- | --- | --- |
| `x1, x2` | Input features (numbers from prepared data) | They contain the information being processed |
| `w1, w2` | Weights (numerical model parameters) | They control how much each input contributes |
| `b` | Bias (another model parameter) | It shifts the weighted sum independently of the inputs |
| `z` | Weighted sum plus bias | The value before activation |
| `f` | Activation function | It transforms the weighted sum |
| `a` | Neuron output | This can become input to another neuron |

**Do not confuse these:** A training **label** is a known target answer attached to an example. A neuron's **weight** is an adjustable model parameter. A neuron's **output** is a calculated number; by itself it need not be a digit class or probability.

## 2.2 Worked example — one neuron, step by step

We will calculate a completely invented two-input neuron by hand. These values are *not* taken from a trained digit-recognition system. They are small so the mathematics can be checked.

**Given values**

| Quantity | Value |
| --- | ---: |
| Input `x1` | 0.8 |
| Input `x2` | 0.2 |
| Weight `w1` | 0.5 |
| Weight `w2` | −0.25 |
| Bias `b` | 0.1 |

**Step 1 — Multiply each input by its weight.**

```text
w1 × x1 = 0.5 × 0.8   =  0.40
w2 × x2 = -0.25 × 0.2 = -0.05
```

**Step 2 — Add those contributions and the bias.**

```text
z = 0.40 + (-0.05) + 0.10
z = 0.45
```

**Step 3 — Apply an activation.** We choose **ReLU** (rectified linear unit):

```text
ReLU(z) = max(0, z)
ReLU(0.45) = 0.45
```

The final neuron output is **0.45**. A ReLU outputs 0 for a negative weighted sum and leaves a positive weighted sum unchanged. A different activation function would give a different output. [1]

### What if one parameter changes?

Keep both inputs and weights the same, but change the bias from **0.1** to **−0.5**.

```text
new z = 0.40 - 0.05 - 0.50 = -0.15
new a = ReLU(-0.15) = 0
```

The neuron now outputs **0**, even though the inputs have not changed. The example shows why parameter values matter. In training, parameter adjustments are driven by an optimization process rather than chosen arbitrarily. Chapter 3 will explain that distinction.

### Why an activation function?

Without nonlinear activations, stacking layers that each compute only weighted sums and biases still results in an overall linear or affine transformation. Nonlinear activations allow a multilayer network to represent more complex relationships between inputs and outputs. [1][2]

This does **not** mean more layers guarantee a good model. The architecture, data, training procedure, and evaluation all matter.

## 2.3 Connect neurons into layers

A **neural network** connects multiple neurons so that the output of one layer can become the input to the next. The simplest teaching picture has three types of layer:

- **Input layer:** Supplies features, such as the ordered pixel values from Chapter 1. The inputs are data, not predictions.
- **Hidden layer:** Performs intermediate calculations. A network can have one or more hidden layers.
- **Output layer:** Produces final model outputs, such as scores used to select a predicted digit.

For our 5 × 5 toy image, consider a **hypothetical architecture** with 25 inputs, four hidden neurons, and ten outputs:

```text
Prepared 5 × 5 image
        |
        v
25 numeric pixel inputs
        |
        v
4 hidden neurons
(each combines inputs and applies an activation)
        |
        v
10 output scores: one per candidate digit 0...9
        |
        v
Select the digit with the largest score
```

**Figure 2.1.** A *conceptual* fully connected feed-forward digit classifier. The number of hidden units is chosen for illustration; no model has been trained or tested here.

Every connection into a neuron has a weight, and neurons commonly include bias parameters. During **inference**, the trained weights remain fixed while data flows forward through the network to obtain outputs. During **training**, an optimization process changes parameters based on training examples and loss. [1][2]

For images, different architectures may be more appropriate, including designs that preserve neighborhood structure. We use a small feed-forward diagram only to teach the basic concepts.

### What exactly is an output score?

Suppose an *invented* network returns these values for three candidate digits:

| Candidate digit | Illustrative score |
| --- | ---: |
| 1 | 0.2 |
| 3 | 0.7 |
| 7 | 1.4 |

If these were the highest scores and the system used the largest-score rule, it would predict **7**. These are **arbitrary example scores**, not measured results. They are **not probabilities** and do not need to add to 1. A real ten-class output would also contain scores for digits 0, 2, 4, 5, 6, 8, and 9.

The correct label attached to the example during supervised learning could be 7—or it could be something else. The **predicted label** comes from model output; the **reference label** comes from verified example data. Comparing them is part of evaluation or training, not proof that the network was correct.

## 2.4 The full path: from handwritten data to prediction

Review the progression across Chapters 1 and 2:

```text
Image of digit 7 (invented)
        |
        v
5 × 5 pixel grid -- normalize / 255 --> 25 ordered numeric inputs
                                            |
                                            v
                                weights, biases, activations
                                            |
                                            v
                                     output scores
                                            |
                                            v
                                   predicted digit
                                            |
                        compare only when a known label is available
                                            |
                                            v
                                   reference label = 7
```

The same prepared representation must be used when the model receives a new image. In **supervised training**, the label is used to assess how the model's output compares with the target. In **inference**, a new image may arrive with no label known yet; the system still makes a prediction. [1][3]

### What the picture does and does not establish

It **does** illustrate the roles of data, parameters, computation, output, and label. It **does not** establish that the hypothetical network recognizes handwriting accurately, has been trained on real digits, or produces calibrated probabilities.

**Bridge to Chapter 3:** If a model predicts the wrong digit, we need a numerical measure of error (a **loss**), a method to compute how changing parameters affects that loss (**gradients**, typically found using **backpropagation**), and an **optimizer** that uses those gradients to update parameters. Calculating gradients and updating weights are two distinct operations. [1][2]

## 2.5 Activities — show your reasoning

### Activity A: compute a neuron

Use the original two-input worked example, but replace weight `w1 = 0.5` with `w1 = 0.25`. Keep `x1 = 0.8`, `x2 = 0.2`, `w2 = −0.25`, and `b = 0.1`. Compute the new weighted sum `z` and ReLU output `a`. Show each multiplication.

### Activity B: label the parts

In the 25 → 4 → 10 network, identify which values come from prepared image data, which layer performs intermediate calculations, and which values are final scores. Explain whether the training target `7` is one of the 25 pixel inputs.

### Activity C: check the concepts

Decide whether each statement is true or false and explain why.

1. If we double the number of images, the network must become more accurate.
2. A weight and a label mean the same thing.
3. The predicted class may disagree with the example's true label.
4. A ReLU output is always strictly greater than zero.
5. During inference, a trained network uses its parameters to calculate outputs.

### Explained answers

**A.** The new first contribution is `0.25 × 0.8 = 0.20`; the second remains `−0.25 × 0.2 = −0.05`. Thus `z = 0.20 − 0.05 + 0.10 = 0.25` and `ReLU(0.25) = 0.25`.

**B.** The 25 input numbers come from image pixels after preparation. Four hidden neurons perform intermediate calculations. Ten output scores represent candidate digits. The label `7` is the separate correct answer used during supervised training or evaluation, not an input pixel.

**C.** (1) False: relevance, quality, variety, and the training method matter. (2) False: a weight is a model parameter; a label is a supplied target. (3) True: models can make incorrect predictions. (4) False: ReLU outputs zero for `z ≤ 0`. (5) True: fixed trained parameters are used in a forward pass.

## Glossary

| Term | Concise definition |
| --- | --- |
| Artificial neuron | A computational unit that combines inputs with weights and bias and applies an activation |
| Weight | Adjustable numerical parameter multiplying an input |
| Bias | Adjustable parameter added to a neuron's weighted sum |
| Activation function | Rule that transforms the pre-activation value |
| ReLU | Activation defined by `max(0, z)` |
| Hidden layer | Layer whose calculations are between input and output |
| Prediction | Output produced by a model for given data |
| Supervised label | Known target attached to a training or evaluation example |
| Inference | Applying a trained model to an input without updating its parameters |

## Teaching-media design notes

- **Study guide:** Present the complete worked neuron table, Activity A, and explained answers.
- **PPT:** Use the labeled neuron in §2.1 and the 25 → 4 → 10 progression in §2.3; keep narration separate from slide text.
- **Video tutorial 2:** Begin with the prepared digit vector, animate the weighted-sum calculation, then show example output scores. Chapter 3 will supply the separate training/error/update sequence.
- **Consistency check:** Do not relabel the toy scores as probabilities or claim the arbitrary outputs came from a trained model.

## Sources and attribution

1. [Google Machine Learning Crash Course — Neural networks](https://developers.google.com/machine-learning/crash-course/neural-networks) — neurons, activation, layered networks, and training overview.
2. [Michael A. Nielsen — Neural Networks and Deep Learning](https://neuralnetworksanddeeplearning.com/) — introductory neural networks, forward computation, and learning.
3. [Google Machine Learning Crash Course — Numerical-data normalization](https://developers.google.com/machine-learning/crash-course/numerical-data/normalization) — consistent feature scaling.

The architecture, numerical parameters, scores, arithmetic exercises, and 5 × 5 digit illustration are **constructed examples for teaching**, not actual model measurements.
