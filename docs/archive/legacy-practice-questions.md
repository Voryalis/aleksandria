# Legacy practice questions

This historical practice set contains 15 questions. Some original explanations use outdated wording about MLP features and LSTM gradients. The [current Stage 2 Test Bank](../../guide/Aleksandria_Stage2_Test_Bank.md) contains the revised assessment.

## 5. Master Test Bank

### Section 1: Multiple Choice Questions (Select the single best answer)

#### Q1. A municipal transit authority ingests real-time GPS locations every second from 5,000 active buses while simultaneously updating route delay metrics for passengers. Which V of Big Data is primarily responsible for the system's core technical challenge?
- A) Volume
- B) Variety
- C) Velocity
- D) Veracity

#### Q2. What is the fundamental operational difference between a Solid-State Drive (SSD) and a Hard Disk Drive (HDD)?
- A) HDDs offer higher endurance than SSDs due to moving mechanical platters.
- B) SSDs use solid-state flash memory without moving mechanical parts, resulting in higher read/write speeds.
- C) SSDs store data using optical technology, while HDDs store data magnetically.
- D) HDDs connect via Local Area Networks, whereas SSDs require Network Attached Storage.

#### Q3. Which data format classification best fits an unorganized repository containing `.mp4` video recordings, `.wav` audio calls, and raw `.jpeg` images?
- A) Structured data
- B) Semi-structured data
- C) Unstructured data
- D) Relational database schema

#### Q4. Why are non-linear activation functions essential components within deep neural networks?
- A) They prevent parameter weights from taking negative values.
- B) Without non-linearity, stacking multiple hidden layers collapses mathematically into a single linear transformation.
- C) They guarantee that the network's training loss reaches absolute zero during optimization.
- D) They convert raw continuous numerical features into discrete text strings.

#### Q5. A neural network architecture designed with filters that slide across two-dimensional spatial representations to extract local features is known as a:
- A) Recurrent Neural Network (RNN)
- B) Multilayer Perceptron (MLP)
- C) Convolutional Neural Network (CNN)
- D) Long Short-Term Memory (LSTM) network

#### Q6. What is the main functional role of gating mechanisms (input, forget, output gates) inside an LSTM cell?
- A) To convert classification outputs directly into scalar loss values.
- B) To regulate information flow and preserve gradient stability across long sequences.
- C) To split raw text datasets into balanced training, validation, and test splits.
- D) To execute backward passes without needing partial derivatives.

#### Q7. Which parameter update formula represents standard Gradient Descent for a scalar weight $w$, given learning rate $\eta$ and loss function $L$?
- A) $w_{new} = w_{old} + \eta \cdot \frac{\partial L}{\partial w}$
- B) $w_{new} = w_{old} - \eta \cdot \frac{\partial L}{\partial w}$
- C) $w_{new} = \frac{\partial L}{\partial w} - (\eta \cdot w_{old})$
- D) $w_{new} = w_{old} \cdot \left(1 - \frac{\partial L}{\partial w}\right)$

#### Q8. If a model exhibits a training loss near zero but a very high validation loss during development, the model is experiencing:
- A) Underfitting
- B) Data leakage
- C) Overfitting
- D) Optimal generalisation

#### Q9. Which dataset split must remain strictly isolated during hyperparameter selection and development decisions to ensure an unbiased evaluation of the final model?
- A) Training set
- B) Validation set
- C) Test set
- D) Batch set

#### Q10. A system that explicitly processes knowledge using human-written rules, structured facts, and formal logic is best categorized as:
- A) Symbolic AI
- B) Deep Learning
- C) Connectionist AI
- D) Generative Diffusion AI

---

### Section 2: Short Answer & Mathematical Calculation Problems

#### Question 11: Data Transformation & Validation
A continuous sensor records temperature values in degrees Fahrenheit ($^\circ\text{F}$). Before sending data to a deep learning pipeline, engineers apply a validation rule enforcing a reasonable operating range between $-50^\circ\text{F}$ and $150^\circ\text{F}$, followed by a linear transformation mapping the valid range to Celsius ($^\circ\text{C}$).

*Formula:*
$$C = \frac{5}{9}(F - 32)$$

1. Distinguish between the **validation** phase and the **transformation** phase in this pipeline.
2. If an ingested reading is $77^\circ\text{F}$, calculate its transformed output in $^\circ\text{C}$.

#### Question 12: Artificial Neuron Calculation
Consider a single artificial neuron with three input values:
$$x_1 = 0.5, \quad x_2 = -0.8, \quad x_3 = 1.2$$
The neuron has corresponding weights:
$$w_1 = 0.4, \quad w_2 = 1.5, \quad w_3 = -0.5$$
and a bias term $b = 0.20$.

1. Compute the exact **weighted sum** ($z = \mathbf{w}^T\mathbf{x} + b$).
2. Pass the computed weighted sum $z$ through a **ReLU activation function** defined as:
   $$f(z) = \max(0, z)$$
   Determine the final output $y$.

#### Question 13: Single-Parameter Gradient Descent Update
A single weight within a neural network currently holds the numerical value $w_{old} = 0.65$. During a backward pass, the backpropagation algorithm evaluates the partial derivative of the loss function with respect to this weight as:
$$\frac{\partial L}{\partial w} = +0.30$$
Assuming an optimization learning rate of $\eta = 0.05$:

1. Calculate the updated weight value $w_{new}$ using the gradient descent update rule.
2. Explain why the weight's magnitude increased or decreased based on the sign of the calculated gradient.

---

### Section 3: Comprehensive Essay Questions

#### Question 14: Architectural Trade-Offs (CNNs vs. LSTMs vs. MLPs)
Analyze how structural properties of data dictate appropriate neural network selection. Contrast **Multilayer Perceptrons (MLPs)**, **Convolutional Neural Networks (CNNs)**, and **Long Short-Term Memory (LSTM)** networks across the following criteria:
* Spatial vs. sequential temporal structural assumptions.
* Parameter complexity and scalability when processing high-resolution raw images.
* Operational mechanisms used to handle long-range dependencies across context streams.

#### Question 15: Ethical AI, Bias, and Governance
Discuss the interplay between **Data Quality (Veracity)** and **Algorithmic Bias** in high-stakes automated decision systems (e.g., job hiring applications or credit scoring). In your answer:
1. Explain how technical validation and deduplication fail to eliminate algorithmic bias if historical training labels retain societal bias.
2. Define the principles of **Data Minimisation**, **Transparency**, and **Human Oversight**.
3. Detail how meaningful human oversight differs from automated rubber-stamping in governance workflows.

---

## 6. Complete Answer Key & Evaluation Rubrics

### Answer Key: Section 1 (Multiple Choice)

1. **C) Velocity** — High-frequency incoming sensor streams transmitted every second demand rapid real-time stream ingestion and processing.
2. **B) SSDs use solid-state flash memory without moving mechanical parts...** — SSD flash media delivers superior read/write speeds compared to mechanical spinning platters in HDDs.
3. **C) Unstructured data** — Raw video, audio, and image files lack fixed predefined tabular schemas.
4. **B) Without non-linearity, stacking multiple hidden layers collapses mathematically into a single linear transformation.** — Linear transformations stacked upon linear transformations remain strictly linear ($W_2(W_1X) = W_{net}X$).
5. **C) Convolutional Neural Network (CNN)** — CNNs apply spatial sliding kernels to detect local patterns across grid inputs.
6. **B) To regulate information flow and preserve gradient stability across long sequences.** — LSTM gates prevent vanishing/exploding gradients in long sequences.
7. **B) $w_{new} = w_{old} - \eta \cdot \frac{\partial L}{\partial w}$** — Gradient descent moves in the opposite direction of the gradient to minimize loss.
8. **C) Overfitting** — High training accuracy paired with poor validation accuracy signals memorization of training noise.
9. **C) Test set** — The test set must remain completely unseen during development decision-making to evaluate true generalisation.
10. **A) Symbolic AI** — Symbolic paradigms utilize explicit rules, facts, and logic rather than learned numerical parameter vectors.

---

### Solutions: Section 2 (Short Answer & Calculations)

#### Solution 11: Data Transformation & Validation
1. **Distinction:**
   * **Validation** checks incoming raw values against boundary rules (verifying $-50^\circ\text{F} \le F \le 150^\circ\text{F}$). If valid, data proceeds; if invalid, it is flagged/filtered.
   * **Transformation** actively changes the valid value's numerical unit or structure without discarding it ($^\circ\text{F} \to ^\circ\text{C}$).
2. **Calculation:**
   $$C = \frac{5}{9}(77 - 32) = \frac{5}{9}(45) = 5 \times 5 = 25^\circ\text{C}$$

#### Solution 12: Artificial Neuron Calculation
1. **Weighted Sum Calculation:**
   $$z = (w_1 \cdot x_1) + (w_2 \cdot x_2) + (w_3 \cdot x_3) + b$$
   $$z = (0.4 \cdot 0.5) + (1.5 \cdot -0.8) + (-0.5 \cdot 1.2) + 0.20$$
   $$z = 0.20 - 1.20 - 0.60 + 0.20 = -1.40$$
2. **ReLU Activation:**
   $$f(z) = \max(0, -1.40) = 0$$
   **Final Output ($y$):** $0.0$

#### Solution 13: Single-Parameter Gradient Descent Update
1. **Update Calculation:**
   $$w_{new} = w_{old} - \left(\eta \cdot \frac{\partial L}{\partial w}\right)$$
   $$w_{new} = 0.65 - (0.05 \cdot 0.30) = 0.65 - 0.015 = 0.635$$
2. **Explanation:**
   Because the gradient is positive ($+0.30$), increasing the weight locally increases loss. Gradient descent subtracts the scaled gradient term, decreasing the weight to $0.635$ to lower the loss.

---

### Evaluation Rubrics: Section 3 (Essays)

#### Question 14 Rubric (Architectural Trade-Offs — 10 Points Total)
* **Structural Assumptions (3 Points):**
  * *MLP:* Assumes flat, independent input feature vectors; ignores spatial or sequence ordering.
  * *CNN:* Assumes two-dimensional spatial grid locality (nearby pixels form edges/textures).
  * *LSTM:* Assumes sequential temporal dependencies where past inputs contextualize future tokens.
* **Parameter Complexity & Scalability on Images (3 Points):**
  * Identifies that fully connected MLPs on high-resolution images require millions of weight parameters ($784 \to \text{hidden}$ vs. $1024 \times 1024 \times 3$), leading to memory bottlenecks and severe overfitting.
  * Explains how CNNs use **weight sharing** (reusing small $3 \times 3$ or $5 \times 5$ filters across the entire spatial grid), drastically reducing parameter counts.
* **Handling Long-Range Sequence Context (4 Points):**
  * Explains how standard RNNs suffer from vanishing/exploding gradients across long timesteps.
  * Explains how LSTMs solve this using internal cell states and forget/input/output gates to control information retention over extended sequences.

#### Question 15 Rubric (Ethical AI, Bias, and Governance — 10 Points Total)
* **Veracity vs. Algorithmic Bias (4 Points):**
  * Demonstrates that technical cleaning (removing corrupt records or null entries) cannot fix systemic historical bias encoded in ground-truth target labels.
  * Notes that removing protected attributes (e.g., race, gender) fails to eliminate bias due to proxy features (e.g., postal code, historical employment gaps).
* **Governance Definitions (3 Points):**
  * *Data Minimisation:* Collecting and retaining only strict, necessary data relevant to specified system tasks.
  * *Transparency:* Clearly informing stakeholders when AI is used, how outputs are produced, and what system limitations exist.
  * *Human Oversight:* Maintaining meaningful human control over AI decisions.
* **Meaningful Oversight vs. Rubber-Stamping (3 Points):**
  * Explains that meaningful oversight requires human reviewers to have adequate time, operational authority, domain expertise, and clear explanations to override automated outputs.
  * Defines "rubber-stamping" as passive automated approvals without critical evaluation or context.
