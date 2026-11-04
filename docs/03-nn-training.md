# Chapter 3 — How a neural network learns

**Status:** Stage 1 content skeleton for future development. This is a structured production draft, not a completed instructional chapter.  
**Audience:** Beginners with basic high-school mathematics and no previous machine-learning or programming experience.  
**Prerequisites:** [Chapter 1 — Big Data: from raw data to neural-network inputs](01-big-data.md) · [Chapter 2 — Artificial neurons and connected networks](02-connectionist-ai.md)

**Guiding question:** How does a neural network use examples, measure its mistakes, and adjust its parameters so that its predictions improve?

## Chapter purpose and scope

Chapter 1 showed how a handwritten image can become an ordered vector of numerical pixel features with a separate target label. Chapter 2 showed how artificial neurons use weights, bias, and activation functions to produce outputs.

This chapter explains **training**: the process of using labelled examples to adjust a network's parameters. It follows one digit-recognition example from a known answer to a prediction, a measure of error, and a parameter update.

The chapter explains gradients and backpropagation conceptually. It uses small invented numbers to illustrate the sequence, but does not derive gradients with calculus or explain the engineering of large-scale training systems.

## Learning objectives

After studying this chapter, learners should be able to:

1. Explain why supervised learning examples contain both input features and target labels.
2. Distinguish training, validation, and test sets and describe their different purposes.
3. Explain the difference between a model prediction and the reference label.
4. Describe loss as a numerical measure of how poorly a model's output matches its target.
5. Explain what a gradient tells us and how backpropagation calculates gradients through a network.
6. Distinguish calculating gradients from using an optimizer to update parameters.
7. Describe one training cycle and explain why repeated updates do not guarantee good performance on new data.
8. Identify overfitting, unrepresentative samples, and incorrect labels as limitations of learning from data.

## 3.1 Learn from examples with known answers

### Core idea

A network cannot learn which patterns are useful merely by receiving a collection of pixel values. In **supervised learning**, each training example includes input data and a known target answer. The network makes a prediction from the input; the training process compares that prediction with the target and uses the difference to guide learning.

Continue with the Chapter 1 example: a prepared 5 × 5 image becomes 25 ordered, normalized pixel features. If the image has been checked and is known to show the digit 7, its target label is 7.

```text
Training example
  Input features:  25 ordered pixel values
  Target label:    7

                 |
                 v
          Neural network
                 |
                 v
          Model prediction
```

### Terms and definitions

**Supervised learning**  
Explanation: In some learning tasks, examples come with answers that have already been supplied or checked. The model can compare its own output with those answers while learning. This is useful when we have examples for which the correct result is known, such as handwritten images labelled with their digits.

Definition: **Supervised learning** is a machine-learning approach in which a model learns from examples that contain input data and a known target.

**Training example**  
Explanation: A training example is one item the model uses while learning. For digit recognition, it contains an image represented as numerical features and the digit label associated with that image.

Definition: A **training example** is one labelled input record used to adjust a model during training.

**Target / target label**  
Explanation: The target is the answer the model is being asked to produce. For the example image of a 7, the target label is 7. It is supplied with the data; it is not produced by the network.

Definition: A **target label** is the known correct class or answer associated with an example.

### Training, validation, and test sets

Explanation: We need separate groups of examples because a model should not be judged only on the same examples it used to learn. One group is used to adjust the model. Another helps the team make development decisions. A final group is kept aside for an evaluation after those decisions. Keeping these roles separate gives a more useful picture of how the model may perform on new images.

Definitions:

- **Training set:** The group of examples used to calculate learning signals and update the model's parameters.
- **Validation set:** A separate group used during development to compare model versions or choices, without using it as the training data for parameter updates.
- **Test set:** A separate group kept aside for the final evaluation of the selected model.

Suggested visual:

```text
All checked examples
        |
        +---- Training set ----> learn / update parameters
        |
        +---- Validation set --> compare choices during development
        |
        +---- Test set --------> final evaluation
```

Production notes:
- State that exact split proportions depend on the task and dataset; do not prescribe a universal percentage.
- Explain that examples from the same original image or near-duplicates should not be allowed to leak across sets.
- Keep the Chapter 1 warning: the data must be representative of the handwriting the system is expected to handle.
- Do not imply that the validation set is used in exactly the same way as the training set.

## 3.2 A prediction is not the expected answer

### Core idea

The network processes the pixel features and produces output scores. Those scores are the model's result, not the answer supplied by the dataset. The target label is the reference answer. Training needs both: the prediction tells us what the model currently outputs, while the target tells us what it should have output for that example.

Use the Chapter 2 distinction:
- **Prediction:** the output produced by the model for the supplied image.
- **Reference label:** the known label attached to that image in the dataset.

Illustrative example:

| Item | Value | Where it comes from |
| --- | ---: | --- |
| Reference label | 7 | Checked training example |
| Highest-scoring output class | 3 | Hypothetical model output |
| Predicted digit | 3 | Class selected from the model's outputs |

The model has predicted 3, while the reference label is 7. The prediction is incorrect for this example. This comparison does not, by itself, tell us how well the model performs across a dataset.

### Terms and definitions

**Prediction**  
Explanation: A model must produce an output before we can compare it with a known answer. For a digit classifier, the output layer provides scores for candidate digits, and a rule such as selecting the largest score can produce a predicted digit.

Definition: A **prediction** is the output a model produces for a given input.

**Reference label**  
Explanation: The reference label is the answer recorded with the example and used as the comparison point. It is separate from the model's prediction, even when both happen to be the same.

Definition: A **reference label** is the checked target value associated with an example and used to judge its prediction.

Production notes:
- Reuse Chapter 2's warning: arbitrary output scores are not automatically probabilities and do not need to add to 1.
- Do not describe a prediction as certain or guaranteed.
- Keep the example hypothetical; do not present it as a measured result from a trained system.

## 3.3 Loss: put a number on the mismatch

### Core idea

A model's prediction can be close to the target or far from it. To guide training, we need a numerical way to describe how poorly the model's output matches the target. This number is called **loss**. A loss value gives the training process a measurable signal: the optimizer will later use information about how loss changes when parameters change.

For a beginner-friendly arithmetic illustration, use a single-output neuron with a target value. This is a simplified example for understanding the idea of loss; it is not the full loss calculation for a ten-class digit classifier.

Illustrative scalar example:

```text
Target value:       1.0
Model output:       0.6
Difference:         0.6 - 1.0 = -0.4
Squared difference: (-0.4) × (-0.4) = 0.16
```

For this teaching example, define the loss as the squared difference between the model output and the target:

```text
loss = (model output - target)²
loss = (0.6 - 1.0)²
loss = 0.16
```

If the output were 0.9 instead, the loss would be 0.01. In this example, the second output is closer to the target and has a smaller loss.

### Terms and definitions

**Loss**  
Explanation: Loss turns a mismatch between a model's output and its target into a number. It gives the learning process a way to compare how well different parameter settings fit the examples. A smaller loss means a smaller mismatch according to the chosen loss rule; it does not automatically mean the model is useful in every real situation.

Definition: **Loss** is a numerical measure of the mismatch between a model's output and its target, calculated using a chosen loss function.

**Loss function**  
Explanation: Different tasks need different ways to measure a mismatch. The rule used to calculate the loss must fit the task and the model's output. The squared-difference rule above is easy to calculate by hand, so it is useful for introducing the idea before studying a full classification loss.

Definition: A **loss function** is a mathematical rule that calculates a loss value from a model's output and its target.

**Squared error**  
Explanation: Squaring a difference makes the result non-negative and gives larger differences a stronger effect than smaller ones. In the simple example, a difference of −0.4 becomes a squared error of 0.16.

Definition: **Squared error** is the square of the difference between a predicted numerical value and its target value.

Production notes:
- Label the arithmetic as a one-output teaching example, not the actual loss used by every digit classifier.
- A later, optional extension may introduce cross-entropy for classification, after explaining why classification needs a suitable loss function.
- Do not say that loss is always the same as classification error or percentage accuracy.
- Do not claim that a lower training loss alone proves better performance on unseen data.

## 3.4 Gradients and backpropagation: find how parameters affect loss

### Core idea

A loss value tells us how poorly the model performed on an example, but it does not yet tell us which parameter to change or in which direction. A network may contain many weights and biases. We need information about how a small change to each parameter would affect the loss.

A **gradient** provides this information. Backpropagation is the method commonly used in neural networks to calculate these gradients efficiently, working backward from the loss through the network's calculations. The result helps the optimizer decide how to adjust the parameters.

Use a simple landscape analogy only as a supporting explanation: imagine standing on a slope and wanting to move downhill. The gradient describes the local direction of steepest increase; moving in the opposite direction can reduce the value. Make clear that a neural network has many parameters, so its loss landscape is not a simple two-dimensional hill.

### Terms and definitions

**Parameter**  
Explanation: A network's weights and biases are numbers that affect its outputs. Training changes these values so that the network can improve its results on the examples.

Definition: A **parameter** is a numerical value inside a model, such as a weight or bias, that can be adjusted during training.

**Gradient**  
Explanation: A parameter can be increased or decreased, and either change may affect the loss. The gradient describes how the loss changes with respect to a parameter. Its sign indicates the local direction of change, while its size indicates how sensitive the loss is to that parameter near the current value.

Definition: A **gradient** is the rate and direction of change of a quantity, such as loss, with respect to one or more model parameters.

**Backpropagation**  
Explanation: A network is made of connected calculations. Backpropagation starts with the loss and works backward through those calculations to determine how each parameter contributed to the loss. It makes gradient calculation practical for networks with many connected neurons. The method uses the chain rule from calculus, but this chapter does not derive that rule.

Definition: **Backpropagation** is an algorithm that calculates gradients of a network's loss with respect to its parameters by working backward through the network.

Production notes:
- Use a forward arrow for input → output → loss and a backward arrow for loss → gradient calculations.
- Explain that backpropagation calculates gradients; it does not itself change the weights.
- Avoid suggesting that the gradient is the error value or the loss value.
- No calculus proof is required. A small visual or parameter-change comparison is sufficient.

## 3.5 Optimizer update: use gradients to adjust parameters

### Core idea

After gradients have been calculated, the model still has its old parameter values. A separate step uses the gradients to change those values. An **optimizer** carries out this update. One common beginner example is gradient descent: it adjusts a parameter in the direction that is expected to reduce loss.

The **learning rate** controls the size of an update. If it is too small, learning may be slow. If it is too large, updates may overshoot or make training unstable. The learning rate is a setting chosen for training; it is not the same thing as a gradient.

Illustrative one-parameter update:

```text
Old weight:       0.50
Gradient:         +0.40
Learning rate:    0.10

New weight = old weight - (learning rate × gradient)
New weight = 0.50 - (0.10 × 0.40)
New weight = 0.46
```

This invented calculation shows an update in the direction opposite to a positive gradient. It is not a trained model result.

### Terms and definitions

**Optimizer**  
Explanation: Gradients describe how loss changes when parameters change. The optimizer uses that information to choose and apply parameter updates. It is therefore a different part of training from backpropagation.

Definition: An **optimizer** is an algorithm that uses gradients to update a model's parameters during training.

**Gradient descent**  
Explanation: One basic update method is to move each parameter a small step in the direction opposite to its gradient. This is intended to reduce the loss locally. Repeating the process can improve the model, although it does not guarantee a good final result.

Definition: **Gradient descent** is an optimization method that updates parameters in the direction opposite to their gradients.

**Learning rate**  
Explanation: The gradient gives a direction and rate of change, but the training process also needs to choose how large a step to take. The learning rate sets the step size used by the optimizer. A poor choice can make training very slow or unstable.

Definition: The **learning rate** is a setting that controls the size of parameter updates made by an optimizer.

### Repeat the process

Explanation: A single update is rarely enough. Training repeats the sequence across many examples so that the parameters can respond to patterns in the training data rather than one isolated image.

Suggested sequence:

```text
1. Give the network a training example
                 |
                 v
2. Forward pass: calculate a prediction
                 |
                 v
3. Compare prediction with target
                 |
                 v
4. Calculate loss
                 |
                 v
5. Backpropagation: calculate gradients
                 |
                 v
6. Optimizer: update weights and biases
                 |
                 +------> repeat with more examples
```

Additional terms for the production glossary:

**Forward pass**  
Explanation: The input moves through the network from the input layer toward the output layer. Each layer performs its calculations and passes values onward.

Definition: A **forward pass** is the calculation that carries input data through a network to produce its output.

**Iteration**  
Explanation: Training is carried out in repeated steps. An iteration refers to one such step of processing the selected training data and applying an update.

Definition: An **iteration** is one training step in which the model processes a batch of training examples and the optimizer applies an update.

**Batch**  
Explanation: Instead of updating the model after every single example, training can process a small group of examples together. This group is called a batch.

Definition: A **batch** is a group of training examples processed together in one training iteration.

**Epoch**  
Explanation: A training set may contain many examples. One pass through the entire training set is called an epoch. Training often uses multiple epochs so the model can make repeated updates while seeing the training examples again.

Definition: An **epoch** is one complete pass through the training set.

Production notes:
- If the chapter uses “batch” and “epoch,” explain them before using them in diagrams or exercises.
- Do not imply that every training system updates after exactly one example.
- Keep the order precise: prediction → loss → gradients → optimizer update.
- State explicitly: backpropagation calculates gradients; the optimizer uses them to update parameters.

## 3.6 Limits of learning: good training results are not enough

### Core idea

A network can become very good at the examples it has seen without becoming equally good at new examples. The goal is not simply to reduce loss on the training set. The goal is to learn patterns that remain useful for examples the model has not used for parameter updates.

Chapter 1 introduced data quality, coverage gaps, duplicates, and incorrect labels. Those issues continue to matter during training. A network cannot be expected to learn reliable patterns from examples that are misleading or do not represent the intended use.

### Terms and definitions

**Overfitting**  
Explanation: A model may fit the training examples so closely that it also learns details that do not help with new examples. It can then perform well on training data but poorly on data it has not seen. The validation set helps identify this problem during development; the test set is used for the final evaluation.

Definition: **Overfitting** occurs when a model fits its training data too closely and performs less well on new, unseen data.

**Generalization**  
Explanation: A useful model should do more than reproduce answers for examples it has already seen. It should also make useful predictions for new examples from the situations it is intended to handle.

Definition: **Generalization** is a model's ability to produce useful outputs for new data beyond the examples used for training.

**Biased sample**  
Explanation: If the training examples overrepresent some handwriting styles and leave out others, the model may learn patterns that work mainly for the overrepresented group. More examples do not solve this problem if they repeat the same narrow coverage.

Definition: A **biased sample** is a set of examples that does not fairly represent the population or situations the model is intended to handle.

**Incorrect label**  
Explanation: A wrong label tells the model that an image belongs to the wrong class. During supervised training, this can push learning in an unhelpful direction. Labels should be checked, and uncertain examples should be reviewed rather than silently changed.

Definition: An **incorrect label** is a target value that does not match the actual example.

### Limitations to connect

- **Overfitting:** strong performance on training examples but weaker performance on new examples.
- **Biased or unrepresentative samples:** missing handwriting styles can lead to poor results for those styles.
- **Bad labels:** incorrect target answers can mislead the learning process.
- **Training performance versus generalization:** training results alone do not establish how the model will perform in real use.
- **Data quantity versus data quality:** adding many repeated or poor examples may not improve learning.

Production notes:
- Reuse the Chapter 1 examples of duplicates, a possible wrong label, and unusual handwriting.
- Explain that an unusual example is not automatically an incorrect example.
- Do not claim that a validation set or a test set fixes poor data; they help reveal problems.
- Do not promise that more epochs, more data, or a more complex network will always improve results.

## 3.7 Learning check — trace and distinguish the training steps

### Activity A: put the steps in order

Arrange these actions into the correct training sequence:

- Optimizer updates the parameters.
- The model produces a prediction.
- Backpropagation calculates gradients.
- The prediction is compared with the target and a loss is calculated.
- A labelled training example is supplied to the network.

### Activity B: distinguish the terms

For each statement, identify the correct term or explain why the statement is incorrect.

1. “The number that measures the mismatch between output and target is the gradient.”
2. “The process that calculates how parameters affect loss is the optimizer.”
3. “The method that works backward through the network to calculate gradients is backpropagation.”
4. “The setting that controls the size of an optimizer's step is the learning rate.”
5. “The known digit attached to an image is the model's prediction.”

### Activity C: calculate a simple update

A parameter has a current value of 0.80. Its gradient is +0.20, and the learning rate is 0.10.

1. Calculate the size of the update.
2. Calculate the new parameter value using gradient descent.
3. Explain why calculating the gradient and updating the parameter are two different operations.

### Activity D: recognize overfitting

A model performs very well on its training examples but makes many mistakes on the test examples. Give one possible explanation and identify which data split should be used during development to compare model choices.

### Answer guidance for later development

**A.** The expected order is: supply a labelled training example → produce a prediction → compare it with the target and calculate loss → calculate gradients using backpropagation → update parameters using the optimizer.

**B.**
1. Incorrect: loss measures the mismatch; a gradient describes how loss changes with respect to parameters.
2. Incorrect: backpropagation calculates gradients; the optimizer uses them to update parameters.
3. Correct.
4. Correct.
5. Incorrect: the known digit is the target or reference label; the prediction is produced by the model.

**C.** Update size = 0.10 × 0.20 = 0.02. New parameter = 0.80 − 0.02 = 0.78. The gradient supplies information about how loss changes; the optimizer applies a chosen update using that information.

**D.** One possible explanation is overfitting: the model has fitted the training examples too closely and does not generalize well. The validation set is used during development to compare choices. The test set is kept aside for final evaluation.

## Glossary — working list

| Term | Working definition |
| --- | --- |
| Supervised learning | A machine-learning approach in which a model learns from examples that contain input data and a known target. |
| Training example | One labelled input record used to adjust a model during training. |
| Target label | The known correct class or answer associated with an example. |
| Training set | Examples used to calculate learning signals and update model parameters. |
| Validation set | Separate examples used to compare model choices during development. |
| Test set | Separate examples kept aside for final evaluation. |
| Prediction | The output a model produces for a given input. |
| Reference label | The checked target value associated with an example and used to judge its prediction. |
| Loss | A numerical measure of mismatch between a model's output and its target. |
| Loss function | A mathematical rule that calculates loss from a model's output and its target. |
| Squared error | The square of the difference between a predicted numerical value and its target value. |
| Parameter | A numerical value inside a model, such as a weight or bias, that can be adjusted during training. |
| Gradient | The rate and direction of change of a quantity with respect to one or more parameters. |
| Backpropagation | An algorithm that calculates gradients of a network's loss with respect to its parameters by working backward through the network. |
| Optimizer | An algorithm that uses gradients to update model parameters during training. |
| Gradient descent | An optimization method that updates parameters in the direction opposite to their gradients. |
| Learning rate | A setting that controls the size of parameter updates made by an optimizer. |
| Forward pass | The calculation that carries input data through a network to produce its output. |
| Iteration | One training step in which a batch is processed and the optimizer applies an update. |
| Batch | A group of training examples processed together in one training iteration. |
| Epoch | One complete pass through the training set. |
| Overfitting | Fitting training data too closely and performing less well on new, unseen data. |
| Generalization | The ability to produce useful outputs for new data beyond the training examples. |
| Biased sample | A set of examples that does not fairly represent the intended population or situations. |
| Incorrect label | A target value that does not match the actual example. |

## Teaching-media production notes

**Study guide**
- Expand each section into connected prose while retaining the digit-recognition example.
- Include the scalar squared-error example and the one-parameter gradient-descent update.
- Add a labelled training/validation/test split diagram.
- Include the learning check and explained answers.

**PPT slides**
- Show the labelled example: 25 pixel features + target label 7.
- Show prediction and reference label as separate items.
- Animate the sequence: prediction → loss → gradients → parameter update.
- Use separate visual treatments for backpropagation (gradient calculation) and optimizer update (parameter change).
- Finish with training performance versus performance on unseen examples.

**Video tutorial 2 — continuation**
- Reuse the network drawing and prepared digit vector from Chapter 2.
- Animate one example moving forward to produce a prediction.
- Reveal the target label, calculate a simple loss, then show gradients moving backward.
- Show the optimizer applying a separate parameter update.
- End by explaining why the process repeats and why training success must be checked on separate data.

**Consistency requirements**
- Use the same terms across the study guide, slides, and video.
- Keep all numerical values explicitly hypothetical.
- Do not call arbitrary Chapter 2 output scores probabilities.
- Do not say that backpropagation and the optimizer are the same operation.
- Do not claim that reducing training loss guarantees good performance on unseen examples.

## Sources for later verification

The following sources are consistent with the source base already used in Chapter 2 and are starting points for the content review. The team should open and verify the relevant sections before treating them as final references.

1. [Google Machine Learning Crash Course — Neural networks](https://developers.google.com/machine-learning/crash-course/neural-networks) — network computation and training overview.
2. [Michael A. Nielsen — Neural Networks and Deep Learning](https://neuralnetworksanddeeplearning.com/) — introductory explanation of network learning and backpropagation.
3. [Google Machine Learning Crash Course — Overfitting](https://developers.google.com/machine-learning/crash-course/overfitting) — generalization and overfitting.
4. [Google Machine Learning Crash Course — Gradient descent](https://developers.google.com/machine-learning/crash-course/gradient-descent) — gradients, learning rate, and parameter updates.

**Review status:** Check the loss example, terminology, arithmetic, source support, and consistency with Chapters 1 and 2 before expanding this skeleton into the final instructional chapter.
