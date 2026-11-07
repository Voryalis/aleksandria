# Chapter 2 — Connectionist AI

**Module:** Big Data & Connectionist AI · ALEKSANDRIA · Stage 2 source chapter

============================================================
1. INTRODUCTION TO CONNECTIONIST AI

============================================================

Computers can follow instructions written by people. A simple program might say: if a temperature is above a certain value, turn on a fan. This works well when the rules are clear and the situation is predictable. But many tasks are harder to describe with a complete list of rules. Recognising a handwritten letter, identifying an object in a photograph, or understanding spoken words involves many small variations. It would be difficult to write a separate rule for every possible example.

Connectionist AI approaches these problems differently. Instead of describing every rule directly, it uses many simple computational units connected together. Each unit performs a small calculation, and the combined network can identify patterns in data. This approach is called connectionism. The main computational models associated with it are artificial neural networks.

The idea is loosely inspired by the nervous system, where many biological neurons are connected and work together. However, artificial neural networks are mathematical models, not digital copies of the human brain.

### Definition — Connectionism
Connectionism is an approach to modelling information processing through networks of simple, interconnected computational units whose combined activity produces complex behaviour.

### Definition — Artificial neural network (ANN)
An artificial neural network is a computational model made of interconnected artificial neurons that transform numerical inputs into outputs.

### 1.1 Connectionist AI, Artificial Intelligence, and Machine Learning

Artificial Intelligence (AI) is the broad field of creating computer systems that perform tasks associated with intelligent behaviour. Machine Learning (ML) is an approach within AI in which systems use data to identify patterns and improve their performance, rather than relying only on rules written by a programmer. Artificial neural networks are one family of machine-learning models. Deep learning is a type of machine learning that uses neural networks with multiple processing layers.

These terms describe different levels of the same general field. AI is the broadest term; machine learning is one approach within AI; deep learning is one approach within machine learning.

### Definition — Artificial intelligence (AI)
Artificial intelligence is the field of developing computer systems capable of performing tasks that normally require aspects of human intelligence, such as recognition, reasoning, learning, or decision-making.

### Definition — Machine learning (ML)
Machine learning is an approach in which computer systems use data to identify patterns and make predictions or decisions without every rule being explicitly programmed.

### Definition — Deep learning
Deep learning is a type of machine learning that uses neural networks with multiple processing layers.

### 1.2 Connectionist and Symbolic Approaches

A symbolic AI system represents information through symbols, facts, and explicit rules. For example, a library catalogue could contain a rule saying that books published before a certain year belong to a particular historical category. The system follows the rule directly.

A connectionist system does not usually store its knowledge as a list of readable rules. Instead, patterns are represented through the numerical values and connections inside the network. A network that recognises handwritten digits, for example, may learn to distinguish the shapes of digits from many examples without being given a separate written rule for every possible handwriting style.

The two approaches have different strengths. Symbolic systems can be easier to inspect when rules are clear and explicit. Connectionist systems can be useful when patterns are complicated and difficult to describe manually. They are not necessarily enemies: some modern systems combine neural networks with symbolic methods.

### Definition — Symbolic AI
Symbolic AI is an approach to artificial intelligence that represents knowledge using explicit symbols, rules, facts, and logical relationships.

### Elaboration — Two ways to organise the Library

Imagine that the Library needs to sort incoming documents.

A symbolic system could use a written catalogue of rules: documents containing certain words or having certain properties are placed in a particular category. A connectionist system could instead examine many labelled examples and develop numerical patterns that help it recognise similar documents.

The first method depends on explicit rules. The second depends on patterns represented across many connected units. Both can be useful, and some systems combine them.

### 1.3 Why Neural Networks Are Useful

Many real-world inputs are complicated. An image contains thousands or millions of pixel values; speech is a changing signal over time; language depends on context and the order of words. It is often difficult to describe all relevant patterns using simple rules.

Neural networks can process numerical representations of these inputs and combine many small calculations. They are therefore used in image recognition, speech recognition, language processing, prediction, and content generation. Their results are not automatically correct: performance depends on the data, the network design, and the conditions in which the system is used.

============================================================
## 2. ARTIFICIAL NEURAL NETWORKS
============================================================

### 2.1 Biological Inspiration

The name "neural network" comes from its loose inspiration: the biological nervous system. A biological neuron is a specialised cell that receives signals from other cells, combines incoming activity, and may send a signal onwards. Neurons communicate through connections called synapses.

An artificial neuron uses a simplified version of this general idea. It receives numerical inputs, combines them mathematically, and produces an output. The output can then be passed to other artificial neurons.

The analogy is useful for understanding why networks are made of connected units, but it has clear limits. A biological neuron is a living cell with complex electrochemical behaviour. An artificial neuron is a mathematical function. It does not reproduce the full operation of a brain cell.

### Definition — Biological neuron
A biological neuron is a specialised cell in the nervous system that receives, processes, and transmits signals.

### Definition — Artificial neuron
An artificial neuron is a mathematical processing unit that combines numerical inputs and produces an output.

### Elaboration — The analogy and its limits

A biological neuron's dendrites receive signals, its cell body combines incoming activity, and its axon carries a signal onwards. In a simplified comparison, these can be associated with the inputs, calculation, and output of an artificial neuron.

The comparison should not be taken literally. Artificial neural networks borrow a general idea of interconnected processing units; they do not simulate every biological process inside the brain.

### 2.2 Inside an Artificial Neuron

An artificial neuron receives one or more numerical inputs. Each input is multiplied by a weight, and the results are added together. A bias is then added. The result passes through an activation function, which determines the neuron's output.

The basic expression is:

y = f(w1*x1 + w2*x2 + ... + wn*xn + b)

Here, x represents an input, w represents its weight, b is the bias, f is the activation function, and y is the output. The formula describes the basic operation of a common artificial neuron.

A weight controls how strongly an input affects the calculation. A positive weight supports an increase in the weighted sum; a negative weight pushes it in the opposite direction; a weight close to zero has little influence. The bias is an additional value that shifts the result before the activation function is applied.

### Definition — Input
An input is a numerical value supplied to an artificial neuron. It may represent a feature of the original data or the output of another neuron.

### Definition — Weight
A weight is a numerical parameter that controls the influence of an input connection on an artificial neuron.

### Definition — Bias
A bias is a numerical parameter added to the weighted sum of a neuron's inputs before the activation function is applied.

### Definition — Weighted sum
A weighted sum is the result of multiplying each input by its corresponding weight and adding the results together.

### Definition — Output
An output is the value produced by a neuron after its inputs have been processed. It may be passed to another neuron or contribute to the network's final result.

### 2.3 Activation Functions

After the weighted sum and bias have been calculated, the result is passed through an activation function. This function determines what value the neuron sends onwards.

Activation functions are important because they allow a network to represent non-linear relationships. Without non-linear activation functions, stacking layers of simple linear calculations would still behave like one overall linear calculation. This would limit the kinds of patterns the network could represent.

Several activation functions are used in practice. ReLU produces zero for negative inputs and returns the input itself for positive inputs. Sigmoid maps a value into a range between zero and one, which can be useful when an output represents a probability for a binary classification. Softmax converts a group of output scores into values that sum to one, often used for multi-class classification.

The main purpose here is to understand why an activation function exists. Detailed mathematical comparisons are not required unless they appear in the course materials.

### Definition — Activation function
An activation function is a mathematical function applied to a neuron's combined input to determine its output.

### Definition — Non-linearity
Non-linearity is a property of a function that means its output is not simply a linear relationship with its input. In neural networks, it allows layers to represent more complex patterns.

### Sidenote — Common activation functions
- ReLU (Rectified Linear Unit): outputs zero for negative values and the input itself for positive values.
- Sigmoid: maps an input to a value between zero and one.
- Softmax: converts a group of scores into values that sum to one.

### Elaboration — Why not use only addition and multiplication?

If a network used only linear calculations, adding more layers would not give it the ability to represent more complex non-linear relationships. Activation functions introduce non-linearity between layers. This is one of the reasons a multi-layer network can represent complicated patterns.

============================================================
##3. NEURAL NETWORK ARCHITECTURE
============================================================

This is the main technical section of the chapter. It should explain how artificial neurons are connected and how the structure of a network affects the kind of information it can process.

### 3.1 From One Neuron to a Network

A single artificial neuron performs a limited calculation. A network connects many neurons so that the output of one neuron can become the input of another. Each connection carries a numerical value and, in a standard neural network, has an associated weight.

The network's behaviour comes from the combined activity of its units and the way they are connected. A network may contain a small number of neurons or a very large number, depending on its purpose and design.

### Definition — Connection
A connection is a directed link that passes a value from one neuron or computational unit to another. In a standard neural network, the connection is associated with a weight.

### Definition — Neural network architecture
Neural network architecture is the overall design of a network, including its layers, units, connections, and the way information moves through it.

### 3.2 Input, Hidden, and Output Layers

A common neural network is organised into layers. The input layer receives the numerical representation of the data. One or more hidden layers perform intermediate calculations and transform the information. The output layer produces the network's final result.

The word "hidden" describes the position of a layer inside the network: it is between the input and output layers. It does not mean that the layer is secret or inaccessible. A network can have one hidden layer or many. Networks with multiple processing layers are commonly described as deep neural networks.

### Definition — Input layer
The input layer is the first layer of a neural network. It receives the numerical representation of the data.

### Definition — Hidden layer
A hidden layer is an intermediate layer that transforms information between the input and output layers.

### Definition — Output layer
The output layer is the final layer of a neural network. It produces the model's result.

### Definition — Deep neural network
A deep neural network is a neural network with multiple processing layers.

### Elaboration — A network as a sequence of Library workstations

Imagine that a document enters the Library and passes through several workstations. The first station receives it. The next stations examine and reorganise different aspects of the information. The final station produces a result, such as a category or a recommendation.

A neural network follows a similar broad structure. The input layer receives values, hidden layers transform them, and the output layer produces the result. The analogy describes the sequence of processing, not human-like thinking inside each layer.

### 3.3 How Information Passes Through a Network

In a feedforward neural network, information moves from the input layer towards the output layer. The output of one layer becomes the input to the next. Each layer performs its calculations and passes its results forward.

For example, an image-recognition system receives a photograph as numerical pixel values. These values enter the network. Hidden layers transform them into increasingly useful numerical representations. The output layer produces scores for possible categories, such as "cat", "dog", or "bird". The system then uses those scores to produce its prediction.

This chapter only describes the general direction of information flow. The detailed calculations involved in passing values through a network are called forward propagation and are explained in the next chapter.

### Definition — Feedforward neural network
A feedforward neural network is a network in which information moves from the input towards the output without recurrent loops.

### Definition — Representation
A representation is a numerical form of information that a model can process. For example, an image can be represented as an array of pixel values.

### Sidenote — Forward propagation
Forward propagation (also called a forward pass) is the process of calculating the values passed through a network from input to output. This matter is thoroughly explained in the next chapter.

### 3.4 Why Network Structure Matters

The arrangement of layers and connections affects what a network can represent and how it processes information. A network designed for a table of numerical measurements may be different from one designed for images or sequences.

Adding layers can allow a network to combine simple patterns into more complex representations. Increasing the number of neurons and connections can also increase the network's capacity, but it usually increases computational requirements. A larger network is not automatically better. Its structure must suit the task, the data, and the available computing resources.

### Definition — Model capacity
Model capacity is the ability of a model to represent different patterns or relationships. Greater capacity allows more complex patterns to be represented, but does not guarantee better performance.

### Elaboration — From simple patterns to complex patterns

In an image, a network may respond to simple visual features such as edges or textures. Later layers can combine these into larger patterns, such as parts of objects. The final output can use these representations to identify the image's contents.

This is a simplified way of describing what may happen inside a network. Individual neurons do not always correspond neatly to a human-readable feature or object.

### 3.5 Common Network Structures

A basic feedforward network is a useful starting point, but different tasks have different requirements. Some data has a spatial structure, such as an image. Other data has an order, such as a sentence, a recording, or a series of sensor measurements. Neural network architectures can be designed to take these properties into account.

#### Multilayer perceptron (MLP)

A multilayer perceptron is a feedforward neural network made of layers of neurons. In a common fully connected design, each neuron in one layer is connected to every neuron in the next layer. MLPs can be used for structured numerical data and are useful for understanding the basic layered network.

### Definition — Multilayer perceptron (MLP)
A multilayer perceptron is a feedforward neural network made of multiple layers, typically with dense connections between neighbouring layers.

#### Fully connected layer

In a fully connected layer, each unit receives input from every unit in the previous layer. This creates many connections and allows the layer to combine information from all the previous units.

### Definition — Fully connected layer
A fully connected layer is a neural network layer in which each unit is connected to every unit in the preceding layer.

### Sidenote
"Fully connected" and "dense" are commonly used to describe this type of layer.



====
##4.0 MODERN TECH & APPLICATIONS
===

Neural network architectures are designed to process specific types of data and solve distinct computational tasks. Understanding how modern AI systems work requires looking at both sides of the coin simultaneously: the application task (what the system needs to achieve) and the fitted solution (the neural architecture designed to handle that specific data structure).


## 4.1 Spatial Data & Image Applications (CNNs & Diffusion Models)

### The Challenge & Task

Images and spatial data contain local patterns where nearby pixels belong to the same edge, texture, or object. Standard fully connected networks require too many connections and fail to leverage this local structure. Common tasks in this domain include:

* **Image Recognition:** Identifying objects, symbols, or categories from image data.
* **Object Detection:** Identifying and locating instances of objects or events in data (e.g., marking a car with a bounding box).
* **Image Generation:** Producing new visual data samples based on learned patterns.

### The Fitted Solution

* **Convolutional Neural Networks (CNNs):** Use filters that move across an input to respond to local patterns (edges, textures), combining simpler patterns into complex ones in deeper layers.
* **Diffusion Models:** Generative models that learn to reverse a gradual noise-addition process, starting from pure noise and iteratively denoising to produce structured results like images (often powered internally by CNNs or other backbones).

### Definition — Convolutional neural network (CNN)

A convolutional neural network is a neural network architecture that uses convolutional operations to detect and combine local patterns in data, especially images.

### Definition — Convolution

Convolution is a mathematical operation in which a filter is applied across an input to detect local patterns.

### Definition — Filter (kernel)

A filter, also called a kernel, is a small set of numerical values applied across an input during a convolution.

### Definition — Generative model

A generative model is a model designed to produce new data samples based on patterns represented in data.

### Definition — Diffusion model

A diffusion model is a generative model that learns to produce data by reversing a gradual process of adding noise.

### Sidenote — Historical landmarks

* CNNs became especially influential in practical image recognition. LeCun and colleagues' 1998 work on document recognition is an important milestone.
* Denoising diffusion probabilistic models became highly influential through research published in 2020.

---

## 4.2 Sequential Data & Temporal Applications (RNNs and LSTMs)

### The Challenge & Task

Some data unfolds sequentially—such as words in a sentence, audio waveforms in speech, or time-series sensor readings—where the order and historical context matter. Core tasks include:

* **Speech Recognition:** Converting spoken audio into a sequence of linguistic units (words).
* **Time-Series Analysis:** Predicting machine states or metrics from historical sensor readings.

### The Fitted Solution

* **Recurrent Neural Networks (RNNs):** Process sequences by using recurrent connections or an internal state to carry information from one step to the next, allowing earlier parts of a sequence to influence later parts.
* **Long Short-Term Memory (LSTM):** A specialized type of RNN that uses a cell state and gates to control information flow, enabling the preservation of useful information over much longer sequences than basic RNNs.

### Definition — Recurrent neural network (RNN)

A recurrent neural network is a neural network architecture that processes sequential data using recurrent connections or an internal state that carries information across steps.

### Definition — Hidden state

A hidden state is an internal numerical representation carried from one sequence step to another in a recurrent network.

### Definition — Long short-term memory (LSTM)

An LSTM is a type of recurrent neural network that uses gates and a cell state to control information flow across a sequence.

### Sidenote — Historical landmarks

* LSTM was introduced by Sepp Hochreiter and Jürgen Schmidhuber in 1997.

---

## 4.3 Hybrid Tasks: Handwriting Recognition

### The Challenge & Task

Handwriting recognition converts handwritten marks into recognized characters, words, or structured text. It is inherently difficult because handwriting varies widely in size, shape, slant, spacing, and style.

### The Fitted Solution

Because handwriting can be processed as a spatial image, as a sequence of pen movements, or through a combination of both, modern systems match the task with hybrid architectures: CNNs extract visual patterns from image inputs, while recurrent or transformer-based models process the ordered sequence.

### Definition — Handwriting recognition

Handwriting recognition is the process of converting handwritten marks or writing into recognised characters, words, or structured information.

### Definition — Image recognition

Image recognition is the task of identifying objects, symbols, or categories from image data.

### Definition — Speech recognition

Speech recognition is the process of converting spoken audio into a sequence of linguistic units, usually words.

---

## 4.4 Overview of Core Tasks & Matching Architecture to Application

Neural networks process numerical representations of complicated data to produce outputs depending on the objective:

* **Classification:** Assigning an input to one or more predefined categories.
* **Regression:** Predicting a numerical value (e.g., expected temperature of a machine).
* **Recognition:** Identifying meaningful patterns, objects, symbols, or signals.
* **Detection:** Finding and locating objects or events.
* **Generation:** Producing new data samples (images, text, audio).

### Definition — Classification

Classification is a task in which a model assigns an input to one or more predefined categories.

### Definition — Regression

Regression is a task in which a model predicts a numerical value.

### Definition — Recognition

Recognition is the process of identifying meaningful patterns, objects, symbols, or signals in data.

### Definition — Detection

Detection is the task of identifying and usually locating instances of objects or events in data.

### Definition — Generation

Generation is the production of new data samples using patterns represented by a model.

### Matching Architectures to Tasks

The architecture should suit the type of information being processed. CNNs are often useful for spatial patterns in images. RNNs and LSTMs were designed to handle sequences and information carried across time. MLPs can be suitable for structured numerical inputs. Modern systems may combine several architectures or use alternatives such as transformers.

There is no single architecture that is best for every task. The choice depends on the input, the required output, the amount and quality of data, computational resources, and the conditions in which the system will be used.

### Elaboration — A few examples

* Image classification: photograph -> CNN or vision model -> predicted category.
* Handwriting recognition: handwritten word -> image/sequence model -> recognised text.
* Speech recognition: audio -> sequence model -> words.
* Sensor classification: temperature, pressure, and vibration readings -> MLP or another suitable model -> machine state.
* Image generation: noise -> diffusion model -> generated image.

The examples show common choices, not strict rules. Different architectures can solve the same task.

============================================================
## 5. LIMITATIONS AND CHALLENGES
============================================================

Neural networks can recognise complicated patterns, but they are not automatically accurate, fair, or reliable. Their performance depends on the data they receive, the structure of the model, the available computing resources, and the conditions in which the model is used.

### 6.1 Dependence on Data

Neural networks rely on examples that represent the task. If important cases are missing, labels are incorrect, measurements are faulty, or some groups are poorly represented, the model may produce unreliable results.

This connects directly to the previous Big Data chapter. Large datasets can provide many examples, but size alone does not guarantee quality or representativeness. Data must be suitable for the task.

### Definition — Generalisation
Generalisation is the ability of a model to perform well on new data that was not used to develop it.

### 6.2 Computational Requirements

Large neural networks may require substantial processing power, memory, electricity, and time. Specialised hardware such as GPUs and other accelerators can make these calculations faster. The cost of using a model also matters: a system that is practical in a large data centre may be too expensive or power-hungry for a small device.

Training and inference are different activities. Training develops the model's parameters using data and is covered in the next chapter. Inference is the use of an already trained model to produce an output for new input data.

### Definition — Inference
Inference is the process of using a trained model to produce an output from new input data.

### 6.3 Interpretability

A neural network may produce a useful result without giving a simple explanation that a person can verify. Many networks contain large numbers of parameters, and useful information can be distributed across many units and connections.

This can make it difficult to understand why a particular prediction was made. Some methods attempt to show which parts of an input influenced an output, but these explanations are not perfect descriptions of everything happening inside the model.

### Definition — Interpretability
Interpretability is the degree to which a person can understand how a model works or why it produced a particular result.

### 6.4 Generalisation and Changing Conditions

A model should work on new examples, not only on examples similar to those used during development. Its performance may fall when the environment changes. For example, an image-recognition system developed using clear daytime photographs may struggle with night-time images, heavy rain, unusual camera angles, or unfamiliar objects.

This is one reason why systems must be evaluated in conditions close to those in which they will actually be used. The detailed study of overfitting and underfitting belongs in the next chapter.

### Sidenote — Overfitting and underfitting
Overfitting and underfitting describe important ways a model can fail to learn patterns that generalise well. They are explained thoroughly in the next chapter on Neural Network Training.

### 6.5 Bias and Reliability

A model may produce different error rates for different groups of people or types of input. This can happen when the data does not represent all relevant cases equally, when measurements are less reliable for some groups, or when the system is used in a setting different from the one for which it was developed.

Reliability means more than achieving a high score on one test. A system should perform consistently under the conditions in which it is intended to be used. Its errors and limitations should be understood, monitored, and addressed.

### Definition — Reliability
Reliability is the ability of a system to perform consistently and appropriately under its intended conditions of use.

### Definition — Bias in an AI system
Bias in an AI system is a systematic distortion in data, design, or outputs that can lead to inaccurate or unfair results.

### Sidenote — Two meanings of bias
A bias in the artificial-neuron equation is a numerical parameter added to the weighted sum. Bias in an ethics or reliability discussion means systematic distortion or unfairness. These are different uses of the same word.

============================================================
##7. ADVANCED TECHNICAL RUBRIC — OPTIONAL READING
============================================================

This section is supplementary. It should expose interested students to the wider technical depth of Connectionist AI without making the main chapter unnecessarily complicated. Students must be able to skip it without losing information needed to understand the main guide.

For each topic, the rubric gives:
1. Technical topic.
2. Advanced explanation.
3. Connection to the main guide.
4. Further direction.

### 7.1 CNN Design: Receptive Fields, Stride, Padding, and Pooling

**Technical topic:** How convolutional networks build spatial representations.

**Advanced explanation:** A convolutional layer applies learned filters across an input. The receptive field is the region of the original input that can influence a particular unit. Stride controls how far a filter moves between positions; padding controls how the input borders are handled. Pooling or strided operations can reduce spatial dimensions. Stacking layers increases the effective receptive field and allows more complex features to be represented.

**Connection to the main guide:** Extends the explanation of CNN filters and why CNNs are useful for image data.

**Further direction:** Convolution arithmetic, receptive-field growth, pooling, dilated convolutions, residual connections, and modern vision architectures.

### 7.2 RNNs, LSTM Gates, and the Vanishing-Gradient Problem

**Technical topic:** How recurrent models retain information over time.

**Advanced explanation:** A basic RNN repeatedly updates a hidden state using the current input and previous state. During training across long sequences, gradient signals can become very small or very large, making long-range dependencies difficult to learn. LSTM introduces a cell state and gates, commonly described as input, forget, and output gates, that regulate information flow.

**Connection to the main guide:** Extends the idea of recurrent connections and the brief introduction to LSTM.

**Further direction:** Gated recurrent units (GRUs), bidirectional RNNs, sequence-to-sequence models, attention, and the transition from recurrent models to transformers.

### 7.3 Attention and Transformers

**Technical topic:** Attention-based sequence processing.

**Advanced explanation:** Attention calculates how strongly different elements in a sequence should influence one another. The transformer architecture uses attention mechanisms and feedforward blocks, allowing sequence elements to interact without relying on a recurrent hidden state passed one step at a time. This design supports parallel processing of sequence positions during many stages of computation and has become central to modern language and multimodal models.

**Connection to the main guide:** Extends the comparison between feedforward and recurrent architectures and provides context for modern speech, language, and vision systems.

**Further direction:** Self-attention, positional information, multi-head attention, encoder/decoder structures, vision transformers, and computational scaling.

### 7.4 Neural Network Hardware: GPUs, TPUs, NPUs, and Memory

**Technical topic:** Why neural networks rely on specialised computing hardware.

**Advanced explanation:** Many neural-network operations involve large numbers of matrix multiplications and other parallel numerical operations. GPUs are designed to perform many operations in parallel. TPUs are specialised accelerators designed for machine-learning workloads. NPUs and other accelerators aim to perform neural-network operations efficiently on devices such as phones and embedded systems. Performance also depends on memory bandwidth, data movement, numerical precision, and software optimisation.

**Connection to the main guide:** Extends the discussion of network size, architecture, and computational requirements.

**Further direction:** GPU architecture, tensor/matrix cores, TPU systolic arrays, quantisation, mixed-precision arithmetic, memory bottlenecks, edge AI, and energy use.

### 7.5 Neuromorphic Computing

**Technical topic:** Hardware inspired by nervous-system operation.

**Advanced explanation:** Neuromorphic systems attempt to reproduce selected features of neural computation in hardware, often using event-driven or spiking-neuron models. Rather than continuously processing every value in the same way as conventional digital accelerators, some designs process sparse events and aim for low-power operation.

**Connection to the main guide:** Extends the biological inspiration behind artificial neurons while showing that software neural networks and brain-inspired hardware are not the same thing.

**Further direction:** Spiking neural networks, event-based sensors, neuromorphic chips, and comparisons of energy use and latency.

### 7.6 Explainability and Interpretability

**Technical topic:** Understanding why a model produced an output.

**Advanced explanation:** Large neural networks can distribute useful information across many parameters, making it difficult to identify a simple human-readable rule behind a prediction. Methods such as saliency maps, feature attribution, activation visualisation, and counterfactual explanations attempt to show which input features or changes influenced an output. These methods provide evidence, not a perfect window into the model's internal reasoning.

**Connection to the main guide:** Extends the limitations section on interpretability and reliability.

**Further direction:** Feature attribution, Integrated Gradients, SHAP, Grad-CAM, mechanistic interpretability, and the limits of explanation methods.

### 7.7 Robustness, Distribution Shift, and Adversarial Examples

**Technical topic:** How models behave when real inputs differ from expected inputs.

**Advanced explanation:** A model may perform well on familiar test data but fail when the real-world input distribution changes. Small, carefully chosen perturbations can sometimes alter a model's prediction. Robustness research studies how to detect, measure, and reduce such failures.

**Connection to the main guide:** Extends generalisation, reliability, and safety.

**Further direction:** Distribution shift, out-of-distribution detection, adversarial examples, calibration, uncertainty estimation, and robust evaluation.

### 7.8 Generative Models Beyond Diffusion

**Technical topic:** Different approaches to generating new data.

**Advanced explanation:** Generative adversarial networks (GANs) use a generator and discriminator in competition. Variational autoencoders (VAEs) learn a probabilistic latent representation and use it to reconstruct or generate samples. Autoregressive models generate a sequence one element at a time. Diffusion models generate samples through iterative denoising.

**Connection to the main guide:** Extends the short introduction to diffusion models and the general concept of generation.

**Further direction:** Compare GANs, VAEs, autoregressive models, and diffusion models in terms of training stability, sample quality, speed, controllability, and applications.

### 7.9 Efficient Models: Quantisation, Pruning, and Distillation

**Technical topic:** Reducing the cost of neural-network deployment.

**Advanced explanation:** Quantisation represents weights and activations with lower numerical precision. Pruning removes selected parameters or connections. Knowledge distillation trains a smaller student model to reproduce useful behaviour of a larger teacher model. These techniques can reduce memory, computation, latency, or energy use, sometimes with a loss in accuracy.

**Connection to the main guide:** Extends the limitations section on computational requirements and the hardware discussion.

**Further direction:** Post-training quantisation, quantisation-aware training, structured pruning, distillation losses, and on-device inference.

**Selection note:** For a compact final guide, prioritise CNN design, RNN/LSTM, hardware, interpretability, and robustness. Include transformers if the course introduces current language models. Keep neuromorphic computing, other generative models, and efficiency methods as optional research directions.

============================================================
## 7. ETHICS AND RESPONSIBLE USE

============================================================

A neural network can influence real people. A system used to sort documents in a library may have limited consequences when it makes a mistake. A system used to assess job applicants, analyse medical images, or decide access to public services can affect people's opportunities and safety. Responsible use therefore requires more than checking whether a model produces accurate outputs.

### 8.1 Fairness

A model may make more mistakes for some groups than for others. This can happen when the data used to develop it does not represent all groups equally, when labels reflect past discrimination, or when the system is used in a different setting from the one in which it was evaluated.

Fairness requires checking how a system performs across relevant groups and considering whether differences in outcomes are justified. Removing an explicit sensitive attribute from the input does not automatically remove unfairness, because other information may act as a substitute.

### Definition — Fairness
Fairness in AI concerns avoiding unjustified differences in treatment, errors, or outcomes between people or groups.

### 8.2 Transparency

People should know when an AI system is being used in situations where that information matters. They should also be given an understandable account of what the system is intended to do, what its limits are, and how its output will be used.

Transparency does not always mean publishing every line of code or every model parameter. It means providing relevant information to the people affected by the system and to those responsible for checking it.

### Definition — Transparency
Transparency is the degree to which relevant people can understand that an AI system is being used, what it is intended to do, and what its limitations are.

### 8.3 Privacy

Data used to develop or operate a neural network may contain personal or sensitive information. Organisations should consider what information is necessary, how it is collected, who can access it, how long it is retained, and whether it could be exposed or misused.

Privacy is not only a technical issue. It also concerns whether the collection and use of information are appropriate and lawful.

### Definition — Privacy
Privacy concerns the appropriate collection, use, sharing, and control of information relating to individuals.

### 8.4 Harmful Applications and Human Oversight

Neural networks can be used in harmful ways, including deceptive impersonation, invasive surveillance, discriminatory profiling, or automated decisions without meaningful review. The risk depends on the model's capabilities, the context in which it is used, the scale of deployment, and the safeguards in place.

Human oversight is important in high-impact settings, but it must be meaningful. A person should have enough information, authority, and time to question or override a system when necessary. An automatic human approval step that nobody can realistically challenge is not meaningful oversight.

### Definition — Human oversight
Human oversight is meaningful human involvement in monitoring, reviewing, or intervening in the use of an AI system.

### Elaboration — The Library's responsibility

Imagine that the Library uses a system to recommend which documents a visitor should be allowed to access. Even if the system works quickly, it may still make unfair decisions, use personal information without a proper reason, or give staff no clear way to challenge a mistake.

The Library must therefore consider more than speed and accuracy. It must decide what data is appropriate, who can inspect the system's decisions, how errors can be challenged, and who is responsible when something goes wrong.

============================================================
## 9. CONCLUSION
============================================================

Connectionist AI builds complex behaviour from many simple computational units working together. Artificial neurons combine inputs using weights and biases, activation functions shape their outputs, and network architecture determines how information is represented and processed.

Different architectures suit different kinds of data. Feedforward networks provide a general starting point, CNNs are designed to process spatial patterns, and RNNs carry information across sequence steps. These and other neural-network approaches support tasks such as image, handwriting, and speech recognition, as well as prediction and generation.

Neural networks are powerful tools, but their results depend on data, design, computing resources, and responsible use. Understanding what a network is and how it is organised is the first step. The next chapter explains how a network is trained: how its performance is measured and how its parameters are adjusted using data.

============================================================
### 10. QUICK REVIEW
============================================================

### 10.1 Core Terms

Term | Short meaning

Connectionism | An approach based on many simple, interconnected computational units.
Artificial neural network | A network of artificial neurons that transforms numerical inputs into outputs.
Machine learning | An approach in which systems use data to identify patterns for predictions or decisions.
Deep learning | Machine learning using neural networks with multiple processing layers.
Symbolic AI | AI based on explicit symbols, rules, facts, and logical relationships.
Artificial neuron | A mathematical unit that combines inputs and produces an output.
Input | A numerical value supplied to a neuron.
Weight | A parameter controlling the influence of an input connection.
Bias | A parameter added to a neuron's weighted input sum.
Activation function | A function that determines a neuron's output.
Non-linearity | A property that allows a network to represent complex relationships.
Layer | A stage or group of computational units in a network.
Input layer | The layer that receives the data representation.
Hidden layer | An intermediate layer that transforms information.
Output layer | The layer that produces the network's result.
Architecture | The arrangement of a network's layers, units, and connections.
Feedforward network | A network in which information moves towards the output without recurrent loops.
MLP | A layered feedforward network, commonly with dense connections between neighbouring layers.
CNN | A network using convolutional operations to process local and spatial patterns.
Convolution | An operation that applies a filter across an input to detect local patterns.
Filter / kernel | A small set of numerical values applied across an input.
RNN | A network that carries information across sequence steps using recurrent connections or state.
Hidden state | Information carried from one sequence step to another.
LSTM | An RNN type using gates and a cell state to manage information over time.
Diffusion model | A generative model that learns to reverse a gradual noise-adding process.
Classification | Assigning an input to one or more categories.
Regression | Predicting a numerical value.
Recognition | Identifying meaningful patterns or items in data.
Detection | Identifying and usually locating objects or events.
Generation | Producing new data samples.
Generalisation | Performing well on new, previously unseen data.
Interpretability | How well a person can understand a model's behaviour or output.
Inference | Using a trained model to produce an output for new input data.
Fairness | Avoiding unjustified differences in treatment, errors, or outcomes.
Transparency | Making the system's purpose and limitations understandable to relevant people.
Privacy | Appropriate collection, use, sharing, and control of personal information.
Human oversight | Meaningful human involvement in reviewing or intervening in system use.

### 10.2 Check Your Understanding

1. What is connectionism?
2. How does connectionist AI differ from symbolic AI?
3. What is the relationship between AI, machine learning, and deep learning?
4. Why are artificial neurons only loosely inspired by biological neurons?
5. What are the roles of inputs, weights, bias, and an activation function?
6. Why are non-linear activation functions important?
7. What are the input, hidden, and output layers?
8. How does information move through a feedforward network?
9. Why does network architecture matter?
10. What is the difference between an MLP, a CNN, and an RNN?
11. Why are CNNs often useful for image recognition?
12. Why are recurrent networks useful for sequence data?
13. What does an LSTM add to a basic RNN?
14. What is the central idea behind a diffusion model?
15. What is the difference between classification and regression?
16. How can neural networks be used for handwriting or speech recognition?
17. Why does a large dataset not guarantee a reliable model?
18. What is generalisation?
19. Why can a model be difficult to interpret?
20. Name three ethical concerns related to neural-network applications.

### 10.3 Distinctions Worth Remembering

- AI vs. machine learning vs. deep learning: AI is the broad field; ML is one approach within AI; deep learning is ML based on multi-layer neural networks.
- Connectionist vs. symbolic AI: connectionist systems represent patterns through numerical activity across connected units; symbolic systems use explicit symbols and rules.
- Biological vs. artificial neuron: a biological neuron is a living cell; an artificial neuron is a simplified mathematical function.
- Weight vs. bias: a weight controls the influence of an input; a bias shifts the combined input before activation.
- Weight vs. activation function: a weight scales an input; an activation function transforms the combined input into an output.
- Linear vs. non-linear activation: non-linear activation allows networks to represent more complex relationships than linear calculations alone.
- Input vs. hidden vs. output layer: input receives data; hidden layers transform it; output produces the result.
- Architecture vs. training: architecture describes how a network is built; training adjusts its parameters using data. Training is the next chapter.
- Feedforward vs. recurrent network: feedforward information moves towards the output; recurrent networks carry information across sequence steps.
- CNN vs. RNN: CNNs are especially suited to spatial/local patterns; RNNs are designed for ordered sequences.
- RNN vs. LSTM: LSTM is a type of RNN with gates and a cell state to manage information over time.
- CNN vs. diffusion model: CNN is an architecture; diffusion is a generative modelling approach that uses a neural network to predict denoising steps.
- Classification vs. regression: classification predicts a category; regression predicts a numerical value.
- Recognition vs. generation: recognition identifies patterns in existing input; generation creates new data.
- Neuron bias vs. AI fairness bias: neuron bias is a numerical parameter; fairness bias is systematic distortion that may produce unfair outcomes.
- Generalisation vs. memorising examples: generalisation means working on new data; reproducing familiar examples alone does not demonstrate it.

============================================================
11. ITEMS TO CONFIRM DURING THE NEXT EDITING PASS
============================================================

These are editorial checks, not missing sections of the current outline.

- Confirm whether the course expects a particular mathematical treatment of the artificial-neuron equation.
- Confirm which activation functions students are expected to know by name.
- Confirm whether MLP, CNN, RNN, and LSTM are all part of the taught syllabus or whether some are intended only as context.
- Confirm whether diffusion models are explicitly required or are included as a brief modern example.
- Confirm whether transformers should be mentioned in the main body or only in optional reading.
- Add specific architectures, examples, or applications used by the lecturer.
- Check whether the course expects image recognition, handwriting recognition, and speech recognition as separate examples.
- Add course-specific diagrams or terminology where required.
- Keep all detailed training mechanics in Part 3: Neural Network Training.

============================================================
12. RESEARCH SOURCES
============================================================

The supplied outline is the primary source for the chapter's scope. The following references support the technical explanations and terminology. Course lecture materials should take priority when they become available.

FOUNDATIONS: CONNECTIONISM AND SYMBOLIC AI

1. Stanford Encyclopedia of Philosophy, "Connectionism" (2019 revision).
https://plato.stanford.edu/entries/connectionism/
Useful for: connectionism as an approach based on networks of units and weighted connections, and its relationship to symbolic theories.

2. Paul Smolensky, "Connectionism and the Foundations of AI", in The Foundations of Artificial Intelligence.
https://doi.org/10.1017/CBO9780511663116.031
Useful for: numerical activation values, weighted connections, and the distinction between connectionist and traditional symbolic approaches.

3. "Neuro-symbolic approaches in artificial intelligence", National Science Review (2022).
https://doi.org/10.1093/nsr/nwac035
Useful for: explaining how symbolic and neural methods can be combined.

ARTIFICIAL NEURONS AND NETWORK BASICS

4. University of Toronto, CSC311, "Introducing the Neuron".
https://www.teach.cs.toronto.edu/~csc311notes/neural_networks/neuron_intro.html
Useful for: the artificial-neuron equation, inputs, weights, bias, activation, and limits of the biological analogy.

5. OpenStax, Principles of Data Science, "Introduction to Neural Networks".
https://openstax.org/books/principles-data-science/pages/7-1-introduction-to-neural-networks
Useful for: accessible explanations of neural-network components and output interpretation.

6. University of Twente, Living Textbook, "Artificial neural networks".
https://ltb.itc.utwente.nl/798/concept/154744
Useful for: layers, weights, biases, activation functions, and feedforward/recurrent structures.

CNN AND HANDWRITING RECOGNITION

7. Yann LeCun, Léon Bottou, Yoshua Bengio, and Patrick Haffner, "Gradient-Based Learning Applied to Document Recognition", Proceedings of the IEEE, 1998.
https://doi.org/10.1109/5.726791
Useful for: CNNs for two-dimensional patterns and the historical use of neural networks for handwritten character/document recognition.

LSTM / RNN

8. Sepp Hochreiter and Jürgen Schmidhuber, "Long Short-Term Memory", Neural Computation, 1997.
https://doi.org/10.1162/neco.1997.9.8.1735
Useful for: the purpose of LSTM and its handling of long time intervals in recurrent processing.

DIFFUSION MODELS

9. Jonathan Ho, Ajay Jain, and Pieter Abbeel, "Denoising Diffusion Probabilistic Models", NeurIPS 2020.
https://arxiv.org/abs/2006.11239
Useful for: the denoising/generative principle and a widely influential diffusion approach.

HARDWARE

10. "A Survey on Deep Learning Hardware Accelerators for Heterogeneous HPC Platforms", ACM Computing Surveys.
https://doi.org/10.1145/3729215
Useful for: GPUs, TPUs, FPGAs, ASICs, NPUs, memory technologies, and neuromorphic accelerators. This is advanced reading, not a main-body source.

ETHICS AND RISK

11. NIST, AI Risk Management Framework FAQs.
https://www.nist.gov/itl/ai-risk-management-framework/ai-risk-management-framework-faqs
Useful for: trustworthiness themes including validity, reliability, safety, security, accountability, transparency, explainability, privacy, and fairness.

12. NIST, AI Risk Management Framework.
https://www.nist.gov/itl/ai-risk-management-framework
Useful for: organising responsible-AI discussion around risk management throughout design, development, deployment, and evaluation.

SOURCE-USE NOTES

- Prefer original research papers for historical claims about CNNs, LSTMs, and diffusion models.
- Prefer university teaching material and OpenStax for introductory explanations.
- Prefer NIST for the responsible-use framework.
- Do not present the advanced technical rubric as required course knowledge.
- Do not claim that a particular architecture is always best for a task. Architecture selection is contextual, and modern systems often combine methods.
- Transformer-based models are included as brief modern context, not as a required central topic unless the actual syllabus confirms this.
