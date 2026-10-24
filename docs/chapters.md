# ALEKSANDRIA — Stage 1 Content Structure

**Audience:** Beginners with basic high-school mathematics and no previous machine-learning or programming experience.

**Driving question:** How does a neural network learn to recognize a handwritten digit from data?

**Scope decision:** We follow one example—handwritten-digit recognition—through data preparation, network prediction, training, and evaluation. The five V's introduce Big Data, with particular attention to volume, variety, and veracity. Detailed engineering of distributed databases, model architectures, and calculus derivations is outside this beginner module.

## Measurable learning objectives

After studying the complete module, learners should be able to:

1. Identify common problems in raw data and explain how preprocessing helps.
2. Trace a small example from an image to numerical model inputs and a label.
3. Compute the weighted sum of a simple artificial neuron and explain the role of bias and activation.
4. Explain how neurons arranged in layers contribute to a prediction.
5. Distinguish predictions, loss, gradients/backpropagation, and optimizer updates at a conceptual level.
6. Explain why data quantity, quality, representativeness, and learning method affect results.

## Chapter 1 — Big Data: from raw records to usable inputs

**Status:** Developed Stage 1 draft at [01-big-data.md](01-big-data.md).

- **1.1 What counts as Big Data?** Working definition; the five V's: volume, velocity, variety, veracity, value; why scale alone does not guarantee usefulness.
- **1.2 Data before learning.** Structured, semi-structured, and unstructured data; collection, storage, labels, and provenance; basic privacy considerations.
- **1.3 Preparing a dataset.** Missing values, duplicates, incorrect labels, inconsistent representations, bias, and normalization; which changes are safe, and why training and test data must be kept separate.
- **1.4 Trace one image.** An invented 2 × 2 grayscale digit fragment becomes an ordered vector of pixel values normalized to 0–1; attach a digit label.
- **1.5 Learning check.** Diagnose a defective digit dataset and compute simple scaled values.
- **Bridge to Chapter 2.** Prepared numbers are inputs; they do not determine predictions without a model.

**Media plan:** Study guide: annotated preparation example + glossary; slides: raw-image → pixel grid → vector diagram; video tutorial 1: digit image, numeric pixels, label, and data-quality check.

## Chapter 2 — Artificial neurons and connected networks

**Status:** Complete non-introductory Stage 1 instructional sample at [02-connectionist-ai.md](02-connectionist-ai.md).

- **2.1 A model that takes numbers as input.** Identify input features, weights, bias, weighted sum, and activation function.
- **2.2 Worked neuron computation.** Calculate a weighted sum and ReLU activation by hand; change one parameter and recompute.
- **2.3 Why use multiple neurons?** Input, hidden, and output layers; connections and learned numerical parameters; representational limitations of a single linear unit.
- **2.4 A digit-prediction walkthrough.** An ordered pixel vector enters a small conceptual network; output scores are interpreted as predictions, not certain facts.
- **2.5 Exercise and explained answers.** Calculation, layer labels, and misconceptions.
- **Bridge to Chapter 3.** How training changes parameters is treated separately from using a trained network.

**Media plan:** Study guide: worked numerical example + self-check; slides: labeled neuron and multilayer network; video tutorial 2: reuse the network drawing before showing training.

## Chapter 3 — How a neural network learns

**Status:** Structured for later content development; not represented as a completed chapter.

- **3.1 Supervised examples:** pixel vectors plus correct digit labels; training, validation, and test sets.
- **3.2 Prediction versus expected answer:** a hypothetical model outputs scores for digit classes; distinguish a model output from a reference label.
- **3.3 Loss:** a number measuring how a prediction differs from its target; select and explain a beginner-friendly loss example.
- **3.4 Backpropagation:** calculate gradients describing how parameters affect loss (conceptual explanation, no calculus proof).
- **3.5 Optimizer update:** use a gradient and learning rate to adjust weights; repeat over training examples.
- **3.6 Limitations:** overfitting, biased samples, bad labels, and the difference between training performance and generalization.
- **Learning check:** arrange training steps in order and correct the statement “backpropagation and updating weights are the same operation.”

**Media plan:** Study guide: cycle with explained answer; slides: predict → compare → compute gradients → update; video tutorial 2: animated prediction, error, and parameter correction.

## Chapter 4 — Case study: recognizing handwritten digits

**Status:** Structured for later content development; not represented as a completed chapter.

- **4.1 The question and input:** identify a handwritten digit image and its known label.
- **4.2 Preparation:** grayscale representation, scale, dimensions, flattening, and checking labels.
- **4.3 Prediction:** display a hypothetical output for digits 0–9; distinguish a correct example from an incorrect example.
- **4.4 Learning and evaluation:** connect error to repeated training; separate training examples from unseen evaluation examples.
- **4.5 What changes the result?** Quantity vs quality, legibility, variation in handwriting, class balance, and task-specific data.
- **4.6 Responsible use:** uncertainty, limitations, accessibility, and privacy where relevant.
- **Final activity:** annotate a complete data → model → output → error → improvement diagram.

**Media plan:** One recurring digit example appears in the study guide, slides, and two tutorials so their explanations can be checked against the same Markdown.

## Stage 1 completion and later production

- **Written instructional sample:** Chapter 2 contains a full, non-introductory passage with definitions, a diagram, arithmetic, learner activity, explained answers, and sources; Chapter 1 establishes and illustrates the preceding data concepts.
- **Remaining material:** Chapters 3 and 4 are outlined, not falsely claimed complete.
- **Review before merge:** Content Lead checks scope and consistency with the project plan; QA Lead verifies terminology, worked examples, source support, and beginner readability; CIO verifies relative links and structure.
- **Production rule:** The study guide, slides, and tutorials must be adapted from the reviewed Markdown, not independently invented.

## Main reference set

- [IBM — What is Big Data?](https://www.ibm.com/think/topics/big-data)
- [Google Machine Learning Crash Course — Datasets and their characteristics](https://developers.google.com/machine-learning/crash-course/overfitting/data-characteristics)
- [Google Machine Learning Crash Course — Numerical-data normalization](https://developers.google.com/machine-learning/crash-course/numerical-data/normalization)
- [Google Machine Learning Crash Course — Neural networks](https://developers.google.com/machine-learning/crash-course/neural-networks)
- [Michael Nielsen — Neural Networks and Deep Learning](https://neuralnetworksanddeeplearning.com/)

All toy pixel grids, arithmetic, and activities in these draft chapters are original illustrative examples, not measurements of a trained digit-recognition system.
