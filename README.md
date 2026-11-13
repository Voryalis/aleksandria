# ALEKSANDRIA — Big Data & Connectionist AI

An educational project by **Team ALEKSANDRIA** for the university course *Foundations of Computer Science & AI*. We build connected, beginner-friendly teaching resources about Big Data, artificial neurons, neural networks, and learning from data.

**Project stages** · Stage 1 planning and initial content → Stage 2 learning resources → [Stage 3 live mini-lecture](#collaboration-and-stage-3).

## Learning goals

Our recurring example is **handwritten-digit recognition**: turn an image into pixel values, prepare labelled data, interpret a model prediction, understand training updates, and evaluate mistakes responsibly.

Learners should be able to:

1. Explain Big Data using the five Vs and why data quality and representativeness matter.
2. Describe how raw images become numeric inputs and labelled examples.
3. Identify inputs, weights, biases, activation functions, and network layers.
4. Explain prediction, loss, backpropagation, and optimizer updates at a beginner level.
5. Distinguish training improvement from performance on held-out data.

## Stage 2 learning resources

| Resource | Location | Contents |
| --- | --- | --- |
| Shared Markdown content V2 | [Module map](docs/chapters.md) | Introduction, four chapters, and additional learning material |
| Study Guide v1.2 | [PDF](guide/Aleksandria_Stage2_Study_Guide.pdf) · [Markdown](guide/Aleksandria_Stage2_Study_Guide.md) | Four activities with worked answers, plus a glossary |
| Test Bank v1.2 | [Markdown](guide/Aleksandria_Stage2_Test_Bank.md) | 20 true/false, 20 multiple-choice, and 6 open-ended questions with explained answers. The course ZIP includes the editable Word copy. |
| PPT Slides | [PowerPoint](slides/Aleksandria_Stage2_PPT_V1.pptx) | Light-themed Operation World Line deck with 42 slides and presenter notes |
| Video Tutorials | [Video Guide](videos/Aleksandria_Stage2_VideoGuide.md) · [Storyboards and video plan](videos/) | Two five-minute visual novel tutorials on preparing digit images and training a neural network. The course requires individual MP4 uploads to Lexue. |
| Operation World Line learning game | [Game and installation guide](interactive-learning/python-game/README.md) | Steins;Gate visual novel supplement with bundled art and a local Python launcher |
| QA and project records | [Task tracker](project-management/task-list.md) · [QA log](project-management/qa-log.md) | Course deliverables, review findings, and submission checks |
| References | [`references.md`](references.md) | Source list |

In the Study Guide, Activity C traces a handwritten-digit prediction. Activity D compares two networks in TensorFlow Playground and includes an offline worksheet with recorded results. [Activity C](guide/Aleksandria_Stage2_Study_Guide.md#activity-c-trace-a-digit-prediction) · [Activity D](guide/Aleksandria_Stage2_Study_Guide.md#activity-d-compare-two-networks) · [Offline worksheet](guide/Aleksandria_Stage2_Study_Guide.md#playground-offline-worksheet)

## Shared Markdown teaching sequence

1. [Introduction](docs/00-introduction.md)
2. [Chapter 1 — Big Data](docs/01-big-data.md): five Vs, data quality, and preprocessing.
3. [Chapter 2 — Connectionist AI](docs/02-connectionist-ai.md): neurons, weights, bias, and connected networks.
4. [Chapter 3 — Neural-network learning](docs/03-neural-networks-learning.md): prediction, error, gradients, and parameter updates.
5. [Chapter 4 — Handwritten-digit case study](docs/04-case-study.md): one example connecting data, learning, and evaluation.
6. [Module map](docs/chapters.md) and [additional learning material](docs/end-of-guide-information.md).

The Markdown content is the shared source for the Study Guide, slides, and tutorials. Corrections should be carried through to all affected resources.

## Interactive supplement — Operation World Line

[**Open the game and installation guide**](interactive-learning/python-game/).

**Operation World Line** is a Steins;Gate visual novel set in the Future Gadget Lab. Read a D-Mail on Okabe’s phone, check handwriting data with Daru, interpret predictions with Kurisu, train a sigmoid neuron at the PhoneWave workbench, and evaluate unseen handwriting with Mayuri. Seven questions and a neuron challenge provide feedback and a score out of 10.

### Download and run

Install **Python 3.9 or newer** and use a current web browser. Download and extract the [repository ZIP](https://github.com/Voryalis/aleksandria/archive/refs/heads/main.zip), or clone the repository with Git. The art, fonts, and interface are bundled. The game uses Python’s standard library and works offline after download.

From the extracted or cloned repository, open `interactive-learning/python-game/` and use the launcher for your system.

| System | Launch |
| --- | --- |
| Windows | Double-click `Start-Windows.bat`, or run `py -3 game.py` in that folder |
| macOS | Double-click `Start-Mac.command`, or run `python3 game.py` in that folder |
| Linux | Run `python3 game.py` in that folder |

For a terminal launch from the repository root on macOS or Linux, run the following commands.

```bash
cd interactive-learning/python-game
python3 game.py
```

Keep the entire `python-game/` folder together, including `web/`. Python opens a local server on `127.0.0.1` and launches the browser. Keep the terminal open during play and press Ctrl+C to stop. If the browser stays closed, copy the address printed in the terminal. See the [installation and troubleshooting guide](interactive-learning/python-game/README.md#installation) for Python setup and launcher help.

### Verification

Run the supplied Python checks from the game folder.

```bash
cd interactive-learning/python-game
python3 -m unittest -v test_game.py
```

The three Python tests passed locally. Automated Chromium playthroughs covered the prologue, phone, backlog, all four missions, scoring, reset, replay, and summary downloads at desktop and phone widths. An independent learner trial remains pending.

The neuron exercise calculates updates for one synthetic example. Evaluation on unseen data is required to measure model accuracy. The [game README](interactive-learning/python-game/README.md) documents the mathematics, artwork sources, font licenses, and AI assistance.

## Team

| Member | Responsibility | GitHub |
| --- | --- | --- |
| Aleksandr | CEO / Team coordination | [@destra825](https://github.com/destra825) |
| Kamran | CIO / Repository and technical workflow | [@Voryalis](https://github.com/Voryalis) |
| Grigory | Content lead | [@loauyhf](https://github.com/loauyhf) |
| Mirad | Video lead | [@MiradKapiz](https://github.com/MiradKapiz) |
| Tamerlan | Quality lead | [@Tamer088](https://github.com/Tamer088) |
| Arseniy | Visual design lead | [@17sen](https://github.com/17sen) |

## Repository structure

| Path | Contents |
| --- | --- |
| [`docs/`](docs/) | Shared instructional Markdown content |
| [`guide/`](guide/) | Study Guide, Test Bank, and figures |
| [`slides/`](slides/) | Module teaching slides and related files |
| [`videos/`](videos/) | Video guide, scripts/storyboards, and plans |
| [`interactive-learning/python-game/`](interactive-learning/python-game/) | Operation World Line source, launchers, tests, and bundled interface assets |
| [`assets/`](assets/) | Diagrams and visual guidance |
| [`project-management/`](project-management/) | Plans, logs, task tracking, and QA |
| [`references.md`](references.md) | Research references |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | Contribution instructions |

## Licensing

- **Original software** uses the [MIT License](LICENSE), including the game
  code, tests, launchers, and web interface code.
- **Original teaching materials** use [CC BY 4.0](LICENSE-CONTENT.md), including
  the chapters, Study Guide, Test Bank, slide content, tutorial guides, and
  original diagrams.
- **Third-party material** follows its source terms. See the
  [asset credits and license notices](LICENSE-CONTENT.md#third-party-material)
  for the Steins;Gate artwork and music, fonts, and Wikimedia Commons images.

## Collaboration and Stage 3

The team coordinates work through issues, branches, and pull requests. [GitHub Issues](https://github.com/Voryalis/aleksandria/issues) · [Team Google Drive](https://drive.google.com/drive/folders/1Itr4fr4STo3VSAMMnOjuk-1wPruCGBS3)

The professor approved **“How Does a Neural Network Learn to Recognize Voices?”** for the Stage 3 live mini-lecture. The lesson will use labelled audio examples to explain how a neural network identifies a speaker. [Stage 3 coordination](https://github.com/Voryalis/aleksandria/issues/49)
