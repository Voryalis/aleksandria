# Chapter 1 — Big Data: from raw data to neural-network inputs

**Audience:** First-year students new to AI. **Stage 1 status:** Developed draft; subject to team review.  
**Next:** [Chapter 2 — Artificial neurons and connected networks](02-connectionist-ai.md) · [Full content map](Chapters.md)

## What you will learn

By the end of this chapter, you should be able to:

1. Describe Big Data using the five V's and explain why more records are not automatically better.
2. Distinguish raw data, a prepared input, and a label.
3. Identify errors, duplicates, missing values, unrepresentative samples, and label mistakes.
4. Trace an invented handwritten-digit image into a vector of numerical inputs.

## 1.1 So, what is Big Data?

Think about the photographs, messages, and searches created every day, and then imagine collecting records from many people and devices. Big Data is not just a large pile of files: it refers to datasets whose **size, speed, or complexity** make them difficult to manage and analyze efficiently with conventional methods. The point is to extract useful, reliable information—not simply to collect more of it. [1]

Big Data is commonly introduced through five properties:

| Property | Beginner-friendly meaning | Possible difficulty |
| --- | --- | --- |
| **Volume** | How much data exists | Storing, searching, and processing many records |
| **Velocity** | How quickly data arrives or needs processing | Incoming records may exceed processing capacity |
| **Variety** | Different kinds and structures of data | Images, text, tables, and audio need different handling |
| **Veracity** | How trustworthy or reliable the data is | Noise, errors, ambiguous measurements, wrong labels |
| **Value** | Whether the data helps answer a useful question | Large datasets may add cost without useful insight |

*The five V's describe characteristics and challenges, not five independent tests that every dataset must pass.* [1]

For this module, **volume, variety, and veracity** matter most. They determine how we collect examples, represent them as numbers, and decide whether a neural network can learn useful patterns.

### Data can have different forms

A **structured** catalogue might store an image ID, digit label, and acquisition date in rows and columns. A **semi-structured** record might contain named fields but allow optional ones. An image file is not itself a row of ready-to-use numbers in the same sense as a spreadsheet, though software can decode it into numerical pixel values. This variety affects preparation.

**Connection to AI:** Some image-recognition systems are trained on examples. An image is input data, and the correct digit supplied during supervised learning is its **label**. The training process uses many such examples to adjust model parameters. These ideas are developed in Chapters 2 and 3. [2][4]

## 1.2 Why should we care about data quality?

A city analyzing traffic might learn more from measurements across many roads and times than from asking three people about traffic. But millions of measurements from only one road would still be a poor basis for estimating every road's conditions. **Quantity and representativeness are different.**

Likewise, a digit-recognition model trained only on neat, perfectly centered digits may struggle with messy handwriting. Adding more near-identical examples does not guarantee it will handle new styles. Poor labels can also teach a model undesirable associations. [2]

Consider the following **invented** records, for an illustrative digit-recognition dataset:

| Image ID | Supplied digit label | Issue |
| --- | --- | --- |
| A | 7 | Clear handwritten image |
| B | 1 | Image file is unreadable |
| C | 7 | Exact duplicate of A |
| D | 2 | Image visibly shows 7: potential label error |
| E | 7 | Image differs substantially from training examples |

The records show several *different* problems:

- **Missing or unreadable data:** The image cannot be decoded; investigate and recover it if possible, or exclude it with a recorded reason.
- **Duplicates:** An accidental duplicate can distort counts and, if the same underlying image appears in both training and evaluation sets, inflate apparent performance. Check how duplicates arose before deleting.
- **Incorrect labels:** A label of 2 attached to an image of 7 can mislead supervised training. Ask for verification rather than silently changing uncertain labels.
- **Coverage gaps:** One unusual writing style should not automatically be discarded; it may represent real users the model needs to serve.
- **Privacy and provenance:** Confirm that an image may be used and record where it came from; avoid collecting unnecessary personal details.

This is an example of the idea often called **garbage in, garbage out**: models cannot reliably compensate for every defect in the data they receive. Better data preparation can improve the *conditions* for learning; it cannot guarantee accuracy. [2]

### Prepare data with a clear purpose

A practical beginner workflow is:

1. **Define the task:** Here, predict which digit (0–9) a handwritten image represents.
2. **Collect and inspect examples:** Check that images open, have appropriate permissions, and cover plausible handwriting variations.
3. **Check labels:** A label must correspond to the actual image, including ambiguous cases needing human review.
4. **Choose a consistent representation:** Decide image dimensions, grayscale convention, and numerical range.
5. **Separate evaluation examples:** Keep examples for checking performance out of the model's fitting process. For a real project, prevent duplicate or closely related examples from crossing the split.
6. **Apply preprocessing consistently:** The same input representation used for training must be used when making later predictions. [2][3]

**Important:** Preparation rules must fit the task. Removing every unusual image would make the dataset look tidy but could hide precisely the handwriting variation the model should recognize.

## 1.3 Worked example — turn a handwritten image into model inputs

This section is a complete worked teaching example, not the output of a real digit-recognition model.

Imagine a tiny **5 × 5 grayscale image** intended to resemble the digit 7. Each value is an image pixel. In this toy convention, 0 means dark background, 255 means bright ink, and values between them mean intermediate brightness.

```text
255 255 255 255 255
  0   0   0 128   0
  0   0 255   0   0
  0 255   0   0   0
  0 255   0   0   0
```

**Step A — Treat the image as numerical data.** The image has 25 pixels. In a simple feed-forward model, one possible representation is a vector of 25 numbers, produced by reading the grid row by row. The first five values are `[255, 255, 255, 255, 255]`. Pixel position matters: shuffling the values would alter the image.

**Step B — Normalize to a common numeric scale.** Here, every pixel is known to be between 0 and 255. Divide each value by 255:

- `0 / 255 = 0`
- `128 / 255 ≈ 0.502`
- `255 / 255 = 1`

The first 10 elements of the normalized vector are therefore:

```text
[1, 1, 1, 1, 1,  0, 0, 0, 0.502, 0, ...]
```

There are still **25 features**: normalization changes their numeric scale, not their count. This fixed 255-based scaling is appropriate to this specified 8-bit grayscale convention. Other feature types may require other transformations. [3]

**Step C — Attach the training label.** If a human has verified that the image depicts 7, the example is:

```text
Input features: 25 normalized pixels
Target label:   7
```

The label is the known answer used during **supervised training**. It is *not* a pixel value, a learned weight, or a prediction. A model later produces its own predicted digit by processing the pixel inputs. [2][4]

**Step D — Keep the distinction clear.** This is one *toy training example*. It is not a large dataset, not a trained neural network, and not evidence that a classifier will correctly predict 7.

### Visual workflow

```text
Raw image + checked label
         |
         v
Check legibility / dimensions / correct label
         |
         v
Numerical pixel grid (5 x 5)
         |
         v
Normalize pixels (divide by 255)
         |
         v
Ordered vector of 25 features --------> neural-network input
Known digit label (7) ----------------> training target
```

This diagram can be adapted into the first video tutorial. The same prepared input will be reused when we introduce neurons in [Chapter 2](02-connectionist-ai.md).

## 1.4 Bigger datasets: what changes?

Suppose a team has two hypothetical collections. Collection A has many copies of the same neat handwriting. Collection B includes fewer examples but covers several writing styles and carefully checked labels. Without testing a particular model on unseen examples, **we cannot determine which collection will produce better predictions**. Dataset size, quality, and diversity all matter, as do the task and training method. [2]

Large collections can also increase storage and processing costs. Before adding data, ask whether it adds relevant examples, resolves a known coverage gap, or improves evaluation. The question is not merely “How many images do we have?” but “What can the model learn and how will we test it?”

## 1.5 Try it yourself

**Question 1 — Apply scaling.** A different pixel has value 64 on the same 0–255 scale. What is its normalized value, to three decimal places?

**Question 2 — Find the error.** A folder contains 300 copies of an identical image labeled 3 and only five images showing different styles of 8. Why might collecting another 300 copies of the image of 3 be unhelpful?

**Question 3 — Explain the objects.** For the worked example, identify: (a) the 25 features, (b) the target label, and (c) the thing a network must produce before we can compare it with the target.

**Question 4 — Make a choice.** A rare but legitimate handwriting style looks unlike the other images. Should it be deleted automatically as an outlier? Explain.

### Explained answers

1. `64 / 255 ≈ 0.251`. This is scaling from the specified 8-bit pixel range.
2. Exact duplicates add little new handwriting variation and can skew the dataset; collecting more varied, correctly labeled examples would address a different problem.
3. (a) The normalized pixel values in their fixed positions. (b) The digit `7`. (c) The model's predicted digit or scores from which a predicted digit is selected.
4. No. The style might occur in real use. Verify the image and label, then decide whether and how it belongs in the dataset; do not treat every unusual example as erroneous.

## Key terms

- **Raw data:** Data before the preparation required for a particular task.
- **Feature:** An input quantity supplied to the model (here, a pixel value at a specified position).
- **Label:** The known target associated with an example during supervised learning.
- **Normalization:** Transforming feature values to a chosen numerical scale.
- **Representativeness:** The extent to which examples reflect the population or situations of interest.
- **Inference:** Using a trained model to produce an output for an input.

## Sources and attribution

1. [IBM — What is Big Data?](https://www.ibm.com/think/topics/big-data) — definition, five V's, data-management challenges.
2. [Google Machine Learning Crash Course — Dataset characteristics](https://developers.google.com/machine-learning/crash-course/overfitting/data-characteristics) — amount, quality, bad values, missing data, and labels.
3. [Google Machine Learning Crash Course — Numerical-data normalization](https://developers.google.com/machine-learning/crash-course/numerical-data/normalization) — scaling and consistent preprocessing.
4. [Google Machine Learning Crash Course — Neural networks](https://developers.google.com/machine-learning/crash-course/neural-networks) — input features, network components, and learning.

The 5 × 5 image, records A–E, questions, and numbers are constructed instructional examples, not historical observations or measured model results. 
