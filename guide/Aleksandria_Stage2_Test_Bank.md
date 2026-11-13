# Stage 2 Test Bank

**Big Data and Connectionist AI**

Team ALEKSANDRIA · Operation World Line · Version 1.2

Check how well you can follow a digit from the lab archive to a model’s decision. All values needed to answer the questions are included.

![Rintaro Okabe](../interactive-learning/python-game/web/assets/okabe.webp)

| Section | Items | Points |
|---|---:|---:|
| [Part A True or False](#part-a-true-or-false) | 20 | 20 |
| [Part B Multiple choice](#part-b-multiple-choice) | 20 | 20 |
| [Part C Open-ended questions](#part-c-open-ended-questions) | 6 | 40 |
| **Total** | **46** | **80** |

Use the [companion Study Guide](Aleksandria_Stage2_Study_Guide.md) to review topics after attempting the questions. The [explained answer key](#answer-key-true-or-false) follows Part C.

## Part A True or False

Mark each statement True or False. Each correct response earns one point.

**Q01**  A sensor stream can pose a velocity challenge even when each individual reading is small.

*Guide* · [Big Data](Aleksandria_Stage2_Study_Guide.md#big-data)

**Q02**  A collection can contain structured tables alongside unstructured audio recordings.

*Guide* · [Big Data](Aleksandria_Stage2_Study_Guide.md#big-data)

**Q03**  If a dataset is large enough, incorrect labels stop being a veracity concern.

*Guide* · [Big Data](Aleksandria_Stage2_Study_Guide.md#big-data)

**Q04**  Batch processing handles every incoming record immediately on arrival.

*Guide* · [Prepare the scan archive](Aleksandria_Stage2_Study_Guide.md#prepare-the-scan-archive)

**Q05**  A missing digit label can always be replaced with zero without changing the meaning of the record.

*Guide* · [Activity A Clean the scan archive](Aleksandria_Stage2_Study_Guide.md#activity-a-clean-the-scan-archive)

**Q06**  A record may pass a format check and still contain a plausible but incorrect value.

*Guide* · [Prepare the scan archive](Aleksandria_Stage2_Study_Guide.md#prepare-the-scan-archive)

**Q07**  A line chart can help show how a measurement changes over time.

*Guide* · [Read the evidence](Aleksandria_Stage2_Study_Guide.md#read-the-evidence)

**Q08**  Changing the bias changes a neuron's weighted sum even when its inputs and weights stay fixed.

*Guide* · [Artificial neurons](Aleksandria_Stage2_Study_Guide.md#artificial-neurons)

**Q09**  A rule-based system must train a neural network before applying a human-written rule.

*Guide* · [How layers make a prediction](Aleksandria_Stage2_Study_Guide.md#how-layers-make-a-prediction)

**Q10**  ReLU turns a negative input into its positive magnitude.

*Guide* · [Artificial neurons](Aleksandria_Stage2_Study_Guide.md#artificial-neurons)

## Part A Continued

**Q11**  An MLP can only learn from input features that are statistically independent.

*Guide* · [How layers make a prediction](Aleksandria_Stage2_Study_Guide.md#how-layers-make-a-prediction)

**Q12**  A hidden layer can pass its computed values to the next layer.

*Guide* · [How layers make a prediction](Aleksandria_Stage2_Study_Guide.md#how-layers-make-a-prediction)

**Q13**  In the guide's digit example, the target label tells the training process which digit the image represents.

*Guide* · [Training and evaluation](Aleksandria_Stage2_Study_Guide.md#training-and-evaluation)

**Q14**  A trained network can produce a prediction without updating its weights.

*Guide* · [Gradient descent](Aleksandria_Stage2_Study_Guide.md#gradient-descent)

**Q15**  The lab keeps one copy of a scan in training and a pixel-identical copy in the test set. Its performance on that test image measures how well it handles a scan it has never seen.

*Guide* · [Training and evaluation](Aleksandria_Stage2_Study_Guide.md#training-and-evaluation) · [Activity A Clean the scan archive](Aleksandria_Stage2_Study_Guide.md#activity-a-clean-the-scan-archive)

**Q16**  For the same nonzero gradient, a larger positive learning rate produces a larger update magnitude in standard gradient descent.

*Guide* · [Gradient descent](Aleksandria_Stage2_Study_Guide.md#gradient-descent)

**Q17**  Processing one mini-batch always completes an epoch.

*Guide* · [Gradient descent](Aleksandria_Stage2_Study_Guide.md#gradient-descent)

**Q18**  Zero loss on the training set guarantees zero loss on unseen handwriting.

*Guide* · [Read training and validation loss](Aleksandria_Stage2_Study_Guide.md#read-training-and-validation-loss)

**Q19**  Keeping extra personal information indefinitely follows data minimisation whenever the data is encrypted.

*Guide* · [Read the evidence](Aleksandria_Stage2_Study_Guide.md#read-the-evidence)

**Q20**  A human reviewer can be given authority to correct an uncertain automated decision.

*Guide* · [Two predictions for a checked 5](Aleksandria_Stage2_Study_Guide.md#two-predictions-for-a-checked-5)

## Part B Multiple choice

Choose one best answer per item. Each correct response earns one point.

**Q21**  The lab receives GPS updates every second from 5,000 delivery vehicles. It has enough storage, but route alerts become stale before the updates are processed. Which characteristic is most directly involved?

- **A.** Volume
- **B.** Variety
- **C.** Velocity
- **D.** Veracity

*Guide* · [Big Data](Aleksandria_Stage2_Study_Guide.md#big-data)

**Q22**  In Activity D, both runs use the same XOR points and settings. At epoch 12, A (no hidden layer) has training loss 0.523 and held-out loss 0.595. B (one layer of four tanh neurons) has training loss 0.110 and held-out loss 0.113. Which conclusion follows?

- **A.** The two configurations performed equally on held-out data.
- **B.** B had lower held-out loss on this dataset at epoch 12.
- **C.** B’s measured loss is its digit-recognition error rate.
- **D.** A’s held-out loss was lower than B’s at epoch 12.

*Guide* · [Playground offline worksheet](Aleksandria_Stage2_Study_Guide.md#playground-offline-worksheet) · [Activity D Compare two networks](Aleksandria_Stage2_Study_Guide.md#activity-d-compare-two-networks)

**Q23**  A folder contains raw video, audio, and image files. How are the media contents typically classified?

- **A.** Structured data
- **B.** Semi-structured data
- **C.** Unstructured data
- **D.** Relational tables

*Guide* · [Big Data](Aleksandria_Stage2_Study_Guide.md#big-data)

**Q24**  Why do hidden layers often use nonlinear activations?

- **A.** They keep every weight positive during training.
- **B.** They let stacked layers represent functions beyond one affine transformation.
- **C.** They set the scale for the optimizer’s updates.
- **D.** They determine how many labelled examples are in each batch.

*Guide* · [Artificial neurons](Aleksandria_Stage2_Study_Guide.md#artificial-neurons)

**Q25**  Which architecture commonly reuses small filters across a two-dimensional image to detect local features?

- **A.** A fully connected MLP
- **B.** A standard RNN
- **C.** An LSTM
- **D.** A CNN

*Guide* · [How layers make a prediction](Aleksandria_Stage2_Study_Guide.md#how-layers-make-a-prediction)

## Multiple choice Q26 to Q30

**Q26**  A learner compares three hidden-layer sizes using Playground’s displayed Test loss and picks the size with the lowest value. What would give an independent final evaluation of the chosen size?

- **A.** Use the same held-out points again after selecting the size.
- **B.** Use the selected model’s training loss.
- **C.** Evaluate the fixed model on fresh points held out from training and selection.
- **D.** Add the held-out points to training before measuring their loss.

*Guide* · [Playground offline worksheet](Aleksandria_Stage2_Study_Guide.md#playground-offline-worksheet) · [Activity D Compare two networks](Aleksandria_Stage2_Study_Guide.md#activity-d-compare-two-networks)

**Q27**  For a scalar weight w, learning rate η, and loss gradient g, which is the standard gradient descent update?

- **A.** w_new = w_old − η × g
- **B.** w_new = w_old + η × g
- **C.** w_new = g − η × w_old
- **D.** w_new = w_old − g ÷ η

*Guide* · [Gradient descent](Aleksandria_Stage2_Study_Guide.md#gradient-descent)

**Q28**  After several epochs, training loss keeps falling while validation loss rises. What is the most likely concern?

- **A.** The model is underfitting the training data.
- **B.** The two losses prove that the data splits overlap.
- **C.** The model may be overfitting the training data.
- **D.** The model is generalising better at later epochs.

*Guide* · [Read training and validation loss](Aleksandria_Stage2_Study_Guide.md#read-training-and-validation-loss)

**Q29**  Which split should be held aside until the team has finished choosing model settings?

- **A.** Training set
- **B.** Validation set
- **C.** Test set
- **D.** Most recent training batch

*Guide* · [Training and evaluation](Aleksandria_Stage2_Study_Guide.md#training-and-evaluation)

**Q30**  Daru’s program uses the explicit rule “flag a scan if its pixel count differs from 784.” Which approach does this illustrate?

- **A.** Supervised neural-network training
- **B.** Symbolic AI
- **C.** Unsupervised clustering
- **D.** Regression on labelled examples

*Guide* · [How layers make a prediction](Aleksandria_Stage2_Study_Guide.md#how-layers-make-a-prediction)

## Multiple choice Q31 to Q35

**Q31**  An analyst already knows that library visits fell last month. Which kind of analysis investigates why they fell?

- **A.** Descriptive
- **B.** Predictive
- **C.** Prescriptive
- **D.** Diagnostic

*Guide* · [Read the evidence](Aleksandria_Stage2_Study_Guide.md#read-the-evidence)

**Q32**  Two rows show the same scan ID, image, and label. How should the exact duplicate be handled before creating data splits?

- **A.** Keep one copy in each split.
- **B.** Keep both rows and use their frequency as a separate input feature.
- **C.** Keep one copy and assign it to one split.
- **D.** Give the second row a fresh ID and split the rows independently.

*Guide* · [Activity A Clean the scan archive](Aleksandria_Stage2_Study_Guide.md#activity-a-clean-the-scan-archive)

**Q33**  An 8-bit grayscale pixel is 64. Approximately what value does it have after division by 255?

- **A.** 0.064
- **B.** 0.251
- **C.** 0.500
- **D.** 0.749

*Guide* · [Handwritten-digit recognition](Aleksandria_Stage2_Study_Guide.md#handwritten-digit-recognition)

**Q34**  The checked label is 5. The classifier gives digit 3 probability 0.60, digit 5 probability 0.30, and the remaining digits 0.10 combined. Which prediction and target should the lab record?

- **A.** Prediction 5, target 3
- **B.** Prediction 5, target 5
- **C.** Prediction 3, target 3
- **D.** Prediction 3, target 5

*Guide* · [Two predictions for a checked 5](Aleksandria_Stage2_Study_Guide.md#two-predictions-for-a-checked-5) · [Activity C Trace a digit prediction](Aleksandria_Stage2_Study_Guide.md#activity-c-trace-a-digit-prediction)

**Q35**  Which order describes one supervised training step?

- **A.** Forward pass, loss calculation, gradient calculation, parameter update
- **B.** Loss calculation, gradient calculation, forward pass, parameter update
- **C.** Forward pass, parameter update, loss calculation, gradient calculation
- **D.** Gradient calculation, parameter update, forward pass, loss calculation

*Guide* · [Training and evaluation](Aleksandria_Stage2_Study_Guide.md#training-and-evaluation)

## Multiple choice Q36 to Q40

**Q36**  A weight is −0.20, its gradient is −0.40, and the learning rate is 0.10. What is its new value after one gradient descent step?

- **A.** −0.24
- **B.** −0.16
- **C.** 0.16
- **D.** 0.24

*Guide* · [Gradient descent](Aleksandria_Stage2_Study_Guide.md#gradient-descent)

**Q37**  A neuron uses inputs 1 and 2, weights 0.5 and −0.25, and bias 0.10. What is its ReLU output?

- **A.** 0
- **B.** −0.10
- **C.** 0.50
- **D.** 0.10

*Guide* · [Artificial neurons](Aleksandria_Stage2_Study_Guide.md#artificial-neurons) · [Activity B Calculate a neuron](Aleksandria_Stage2_Study_Guide.md#activity-b-calculate-a-neuron)

**Q38**  The lab wants to estimate performance on handwriting from people whose writing the model has never seen. Which split answers that question?

- **A.** Reserve all scans from selected writers for the test set.
- **B.** Randomly split every writer's scans across training and test sets.
- **C.** Keep one scan from each training writer in the test set.
- **D.** Copy hard training scans into the test set.

*Guide* · [Training and evaluation](Aleksandria_Stage2_Study_Guide.md#training-and-evaluation) · [Read the evidence](Aleksandria_Stage2_Study_Guide.md#read-the-evidence)

**Q39**  The lab’s parcel sorter predicts the last digit of a destination code with low confidence. Which action best supports meaningful human oversight?

- **A.** Route the parcel immediately based on the predicted digit.
- **B.** Give the operator only the predicted digit and require confirmation.
- **C.** Show the scan and prediction to an operator who can correct the route.
- **D.** Use the most common destination as the default in uncertain cases.

*Guide* · [Two predictions for a checked 5](Aleksandria_Stage2_Study_Guide.md#two-predictions-for-a-checked-5) · [Activity C Trace a digit prediction](Aleksandria_Stage2_Study_Guide.md#activity-c-trace-a-digit-prediction)

**Q40**  A handwriting dataset contains mainly samples from one writer. Which next step best addresses that gap?

- **A.** Make more copies of the existing writer's scans.
- **B.** Collect labelled scans from more writers and evaluate on writers held out from training.
- **C.** Remove every image the model currently misclassifies.
- **D.** Increase the learning rate without changing the data.

*Guide* · [Read the evidence](Aleksandria_Stage2_Study_Guide.md#read-the-evidence)

## Part C Open-ended questions

Show your reasoning. Use a developed explanation, calculations or a labelled diagram. You can earn partial credit.

**Q41**  Daru’s sensor pipeline accepts readings between −50 °F and 150 °F, inclusive, then converts accepted values with C = (5/9) × (F − 32). Trace 77 °F and 170 °F. Explain how validation differs from transformation, and describe how you would investigate a plausible reading from a sensor suspected of drifting. Include one example of what the lab should record about an excluded reading.

*Guide* · [Prepare the scan archive](Aleksandria_Stage2_Study_Guide.md#prepare-the-scan-archive) · 5 points

**Q42**  Kurisu tests a neuron with inputs (0.5, −0.8, 1.2), weights (0.4, 1.5, −0.5), and bias 0.20. Show the weighted products, sum and ReLU output. Find the bias that makes the sum zero and give one bias above and one below that threshold. Compute both outputs and explain the change.

*Guide* · [Artificial neurons](Aleksandria_Stage2_Study_Guide.md#artificial-neurons) · [Activity B Calculate a neuron](Aleksandria_Stage2_Study_Guide.md#activity-b-calculate-a-neuron) · 5 points

**Q43**  A weight is 0.65 and the learning rate is 0.05. Show the update for a supplied gradient of +0.30. Repeat from the same starting weight with −0.30. Explain the two directions, what a learning rate of 0.10 would do to the two step sizes, and what additional computation would tell you whether the next digit prediction is correct.

*Guide* · [Gradient descent](Aleksandria_Stage2_Study_Guide.md#gradient-descent) · [Activity C Trace a digit prediction](Aleksandria_Stage2_Study_Guide.md#activity-c-trace-a-digit-prediction) · 5 points

## Part C Continued

**Q44**  The lab has two jobs: flag a scanner fault from eight fixed numerical readings, and recognise a digit from a 28 × 28 grid. Compare a dense MLP with a CNN and recommend a starting model for each. A dense layer has 16 units connected to all 784 pixels. A convolutional layer has eight 3 × 3 filters with one input channel. Ignoring biases, calculate the weight count of each specified layer. Explain weight sharing, why the counts alone cannot establish accuracy, and how you would compare two digit classifiers on new handwriting.

*Guide* · [How layers make a prediction](Aleksandria_Stage2_Study_Guide.md#how-layers-make-a-prediction) · [Training and evaluation](Aleksandria_Stage2_Study_Guide.md#training-and-evaluation) · 10 points

**Q45**  The lab’s parcel model learns from old routing decisions. Historic records show that scans from one collection site were often mislabelled, and most training images came from another site. Explain how a clean-looking dataset can preserve those patterns. Propose one data minimisation measure, one way to disclose the system’s limits, and a review workflow for an uncertain or disputed route. State what the reviewer can inspect and change.

*Guide* · [Read the evidence](Aleksandria_Stage2_Study_Guide.md#read-the-evidence) · [Two predictions for a checked 5](Aleksandria_Stage2_Study_Guide.md#two-predictions-for-a-checked-5) · 10 points

**Q46**  A crop from a digit labelled 7 contains rows [255, 64] and [0, 128]. Flatten the crop in row order, divide by 255 and round to three decimals. The model assigns digit 1 probability 0.55 and digit 7 probability 0.45. Record the predicted digit and target. Explain what to do if the scan belongs to a held-out writer, and how to prevent duplicate scans and repeated writers from crossing splits.

*Guide* · [Handwritten-digit recognition](Aleksandria_Stage2_Study_Guide.md#handwritten-digit-recognition) · [Training and evaluation](Aleksandria_Stage2_Study_Guide.md#training-and-evaluation) · 5 points

## Answer key True or False

**Q01 · True**  Velocity concerns how quickly data arrives or needs to be processed. The size of one reading does not determine the arrival rate.

**Q02 · True**  A single project can combine records with a fixed schema and media without a tabular schema.

**Q03 · False**  Incorrect labels undermine data reliability at any scale. Collecting more records does not correct existing labels.

**Q04 · False**  Batch processing groups records for later processing. Stream processing handles incoming data as it arrives.

**Q05 · False**  Zero is a valid digit label. Treat the label as missing and verify it against the source or flag the record.

**Q06 · True**  Validation checks specified rules. A value can satisfy those rules and still disagree with the original observation.

**Q07 · True**  Connecting measurements in time order helps a reader see changes and trends.

**Q08 · True**  Bias is added to the sum of the weighted inputs.

**Q09 · False**  A symbolic system can apply an explicit rule directly to the facts it receives.

**Q10 · False**  ReLU returns zero for negative inputs and preserves positive inputs.

## True or False key continued

**Q11 · False**  An MLP can learn relationships between features. It simply lacks a built-in spatial grid structure.

**Q12 · True**  The activations from one layer can serve as the next layer's inputs.

**Q13 · True**  The label provides the expected answer for comparison with the model prediction.

**Q14 · True**  During ordinary inference, the model uses the current parameters to compute an output.

**Q15 · False**  The duplicate exposes the same image during fitting. Remove the copy or group it with the original in one split.

**Q16 · True**  The magnitude of the update is the learning rate multiplied by the magnitude of the gradient.

**Q17 · False**  An epoch is one pass over the training dataset. It generally includes several mini-batches.

**Q18 · False**  A model can fit its training data closely and still perform poorly on new writers.

**Q19 · False**  Encryption protects retained data. Minimisation concerns collecting and retaining only what serves the task.

**Q20 · True**  Meaningful oversight requires a way to inspect the case and change or escalate the outcome.

## Answer key Multiple choice

**Q21 · C**  Velocity is the bottleneck because the system cannot keep up with incoming updates. A concerns total quantity, B concerns formats and D concerns trustworthiness.

**Q22 · B**  B’s held-out loss is 0.113, below A’s 0.595. A and D disagree with the table. C confuses Playground’s loss on synthetic points with a digit classifier’s error rate.

**Q23 · C**  The media contents lack a fixed record schema. A and D describe structured records and tables. B can describe metadata or tagged documents, such as JSON logs.

**Q24 · B**  Composing affine layers still gives one affine transformation. Nonlinearity makes more flexible functions possible. It does not constrain weights to be positive (A), set the optimizer’s update scale (C), or determine batch size (D).

**Q25 · D**  A CNN shares filter weights across image locations. A dense MLP has separate weights for each connected input and unit. Standard RNNs and LSTMs (B and C) are associated with processing sequences.

**Q26 · C**  The displayed held-out points influenced model selection, so they served as validation. A reuses them, B measures fit to training and D exposes those points during fitting.

**Q27 · A**  Subtract the learning rate times the gradient. B changes the sign, C uses the gradient in place of the old weight and D divides by the rate.

**Q28 · C**  A widening training–validation gap is consistent with overfitting. A is less plausible when the model fits training data increasingly well. The curves alone do not demonstrate overlap (B). The rising validation loss contradicts D.

**Q29 · C**  Keep final test data untouched until settings are chosen. A and D are for fitting weights. B is for comparing settings or choosing when to stop.

**Q30 · B**  The decision follows an explicit rule about the pixel count. The other options require learning from examples or grouping observations by patterns.

## Multiple choice key continued

**Q31 · D**  Diagnostic analysis investigates why the change occurred. A describes the change, B forecasts outcomes and C helps choose an action.

**Q32 · C**  One exact copy preserves the example without duplicate leakage. A leaks across splits. B gives a recording artefact extra influence. D relabels the row ID while keeping identical pixels.

**Q33 · B**  64 ÷ 255 = 0.25098…, about 0.251. A divides by 1,000. C and D are closer to scaling 128 and 191, respectively.

**Q34 · D**  Digit 3 has the highest individual probability. The checked label remains 5. A swaps their roles. B uses the target as the prediction. C uses the prediction as the target.

**Q35 · A**  Compute outputs before the loss, gradients after the loss and the update after the gradients. B and D start before the forward pass. C tries to update before obtaining a gradient.

**Q36 · B**  −0.20 − (0.10 × (−0.40)) = −0.16. A applies the change in the wrong direction. C and D start from the wrong sign or lose the sign of the result.

**Q37 · D**  The products are 0.50 and −0.50. With bias 0.10, z = 0.10 and ReLU preserves it. A ignores the bias, B is negative and C omits the second product and bias.

**Q38 · A**  Whole-writer separation keeps selected writers unseen during training. B and C retain writer overlap. D repeats training examples in the test set.

**Q39 · C**  The operator needs original evidence and the authority to act. A bypasses review, B withholds the scan and D substitutes a default without examining the case.

**Q40 · B**  More writers improve coverage and a held-out writer split tests transfer. A duplicates the narrow sample, C discards useful error evidence and D changes training without improving coverage.

## Answer key Open-ended questions

Award equivalent credit for valid reasoning and alternative solutions that meet the stated criteria.

### Q41  Validate and convert readings

Validation checks the specified range. The 77 °F reading passes and becomes (5/9) × (77 − 32) = 25 °C. The 170 °F reading fails and is flagged or excluded before conversion. An in-range value can still reflect drift or wrong units. Check it against a calibrated reference or recent maintenance record. Log the raw value, unit and rejection reason with the record ID.

**Scoring** · 5 points · 1 for distinguishing the operations, 2 for tracing both readings, 1 for a credible verification step and 1 for an auditable exclusion record.

### Q42  Trace a ReLU threshold

The weighted terms are 0.20, −1.20 and −0.60. They sum to −1.60. With b = 0.20, z = −1.40 and ReLU is 0. The threshold is b = 1.60, where z and ReLU are both zero. For example, b = 1.70 gives z = 0.10 and ReLU 0.10. With b = 1.50, z = −0.10 and ReLU 0. Accept other correct values on either side.

**Scoring** · 5 points · 2 for products and starting sum, 1 for the original output, 1 for the threshold and 1 for both examples and the explanation.

### Q43  Compare gradient updates

With +0.30, subtract 0.015 to get 0.635. With −0.30, subtract −0.015 to get 0.665. At rate 0.10, each step has twice the magnitude (0.030), in the same direction as before. Run a new forward pass with the complete updated model and compare its prediction with the checked label.

**Scoring** · 5 points · 2 for the two updates, 1 for the gradient sign, 1 for both doubled step magnitudes and 1 for the next-prediction check.

## Open-ended key continued

### Q44  Choose and compare architectures

A small dense MLP is a reasonable starting point for the fixed features. A CNN can exploit spatial neighbourhoods in the image grid. The stated dense layer has 784 × 16 = 12,544 weights. The stated convolutional layer has 3 × 3 × 1 × 8 = 72 weights, reused over image locations. These are layer counts with different outputs. They establish neither a full-model size nor accuracy. Tune candidates using validation data, then compare the fixed models on a separate set of scans from unseen writers. Accept justified baselines with comparable tests.

**Scoring** · 10 points · 2 for the recommendations, 2 for both weight counts, 2 for explaining reuse, 1 for the limit of the comparison and 3 for an independent comparison design.

### Q45  Design human oversight

Removing duplicates and filling missing values cannot repair wrong historical labels or the lack of scans from an underrepresented site. Verify labels from both sites and collect needed examples. Store only necessary images, checked destinations and appropriately limited IDs. Explain the known site-specific limits and when routing is escalated. Give a reviewer the scan, model recommendation and verified destination record, plus authority to correct or escalate the case. Accept other evidence-backed workflows.

**Scoring** · 10 points · 4 for identifying both quality and coverage issues, 3 for practical minimisation and transparency, and 3 for access to evidence, authority and a concrete correction path.

### Q46  Evaluate a digit from an unseen writer

The vector is [1.000, 0.251, 0.000, 0.502]. The model predicts 1, while the checked target is 7. Record the error with the fitted parameters fixed. Remove duplicate scans before splitting and keep all scans by each writer in one split. If retaining copies is necessary, group them before assigning splits, keeping duplicate groups and writers together.

**Scoring** · 5 points · 2 for the vector, 1 for the prediction and target, 1 for fixed-weight evaluation and 1 for addressing both copy leakage and writer overlap.

## References and image credits

Questions reference exact Study Guide headings. The guide lists sources for Big Data, neural networks, model evaluation and the recorded Playground results.

- Team ALEKSANDRIA · [Stage 2 Study Guide](Aleksandria_Stage2_Study_Guide.md).
- Daniel Smilkov and Shan Carter · [TensorFlow Playground](https://playground.tensorflow.org/). Q22 reports its recorded losses.
- *Steins;Gate: Linear Bounded Phenogram* · [Rintaro Okabe sprite](https://www.spriters-resource.com/pc_computer/steinsgatelinearboundedphenogram/asset/153185/), archived by delta. Used here from the Operation World Line game. The artwork retains its original rights.
- Rob Robinette · [Nixie Tube Clock](https://commons.wikimedia.org/wiki/File:Nixie_Tube_Clock.jpg). [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Cropped and resized for the print and Word covers. The cropped photograph retains the same license.

Original teaching material · Team ALEKSANDRIA. See the [project content license](../LICENSE-CONTENT.md). Instrument Serif is licensed under the [SIL Open Font License](https://github.com/google/fonts/blob/main/ofl/instrumentserif/OFL.txt).
