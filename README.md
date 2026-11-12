# ALEKSANDRIA — Big Data & Connectionist AI

An educational project by **Team ALEKSANDRIA** for the university course *Foundations of Computer Science & AI*. We build connected, beginner-friendly teaching resources about Big Data, artificial neurons, neural networks, and learning from data.

**Project timeline:** Stage 1 planning and first content (24 October 2026) → Stage 2 learning-resource development (7 November 2026) → Stage 3 revision and mini-lecture (planned for November 2026).

## Learning goals

Our recurring example is **handwritten-digit recognition**: turn an image into pixel values, prepare labelled data, interpret a model prediction, understand training updates, and evaluate mistakes responsibly.

Learners should be able to:

1. Explain Big Data using the five Vs and why data quality and representativeness matter.
2. Describe how raw images become numeric inputs and labelled examples.
3. Identify inputs, weights, biases, activation functions, and network layers.
4. Explain prediction, loss, backpropagation, and optimizer updates at a beginner level.
5. Distinguish training improvement from performance on held-out data.

## Stage 2 learning resources

Stage 2 expands the initial Markdown foundation into a connected set of teaching materials.

| Resource | Location | Stage 2 status / access |
| --- | --- | --- |
| Shared Markdown content V2 | [`docs/`](docs/) | Intro, four topic chapters, learning map, and end-of-guide information available in the repository |
| Study Guide | [`guide/Big Data and Connectionist AI - Study Guide v1.1.pdf`](guide/Big%20Data%20and%20Connectionist%20AI%20-%20Study%20Guide%20v1.1.pdf) | PDF available in the repository |
| Test Bank | See the team's [shared Google Drive](https://drive.google.com/drive/folders/1Itr4fr4STo3VSAMMnOjuk-1wPruCGBS3) | Separate final Test Bank file not verified in the repository snapshot |
| PPT Slides | [`slides/Aleksandria_Stage2_PPT_V1.pptx`](slides/Aleksandria_Stage2_PPT_V1.pptx) | Editable PPT and [PDF](slides/Aleksandria_Stage2_PPT_V1.pdf) available in the repository |
| Video Tutorials | [Video Guide](videos/Aleksandria_Stage2_VideoGuide.md) · [Storyboards and video plan](videos/) | Video files are stored in shared Google Drive and have been submitted, as confirmed by the team; this repository contains their documentation rather than the MP4 files |
| Supplementary Python learning game | [`interactive-learning/python-game/`](interactive-learning/python-game/) | Source, tests, launch scripts, and independent instructions available; automated tests passed locally |
| QA and project records | [`project-management/`](project-management/) | Project log, QA checklist/log, tasks, and review files available |
| References | [`references.md`](references.md) | Source list |

**Note:** Presence of a resource in GitHub is not, by itself, confirmation that every assignment package, link, answer key, peer review, or submission was independently verified. Use the submission records and QA logs for those checks.

## Shared Markdown teaching sequence

1. [Introduction](docs/00-introduction.md)
2. [Chapter 1 — Big Data](docs/01-big-data.md): five Vs, data quality, and preprocessing.
3. [Chapter 2 — Connectionist AI](docs/02-connectionist-ai.md): neurons, weights, bias, and connected networks.
4. [Chapter 3 — Neural-network learning](docs/03-neural-networks-learning.md): prediction, error, gradients, and parameter updates.
5. [Chapter 4 — Handwritten-digit case study](docs/04-case-study.md): one example connecting data, learning, and evaluation.
6. [Module map](docs/chapters.md) and [additional learning material](docs/end-of-guide-information.md).

The Markdown content is the shared source for the Study Guide, slides, and tutorials. Corrections should be carried through to all affected resources.

## Interactive supplement — From Data to Learning

[**Open the Python learning game folder**](interactive-learning/python-game/).

This optional local browser game lets learners work through **four missions**: prepare data, interpret predictions, update a sigmoid neuron's parameters, and assess generalization and responsible AI. Seven questions and a neuron challenge provide feedback and a score out of 10.

**Requirements:** Python 3.9+; no third-party packages or internet connection.

```bash
cd interactive-learning/python-game
python3 game.py
```

On Windows use `py game.py`, or run `Start-Windows.bat`. On macOS use `Start-Mac.command` or the terminal command above. The Python process starts a server on `127.0.0.1` and opens the game in your web browser; keep it running during play.

**Automated tests:**

```bash
cd interactive-learning/python-game
python3 -m unittest -v test_game.py
```

The three supplied automated tests passed in a local Python run on 7 November 2026. A complete independent learner/browser trial is not established by these tests.

This simulation updates **one synthetic sigmoid neuron**, not an MNIST handwriting classifier; its game score is not a model-accuracy measure. See the [game's own README](interactive-learning/python-game/README.md) for detailed instructions, technical limitations, verification notes, and AI-use acknowledgement.

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
| [`guide/`](guide/) | Study Guide |
| [`slides/`](slides/) | Module teaching slides and related files |
| [`videos/`](videos/) | Video guide, scripts/storyboards, and plans |
| [`interactive-learning/python-game/`](interactive-learning/python-game/) | Optional interactive Python game |
| [`assets/`](assets/) | Diagrams and visual guidance |
| [`project-management/`](project-management/) | Plans, logs, task tracking, and QA |
| [`references.md`](references.md) | Research references |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | Contribution instructions |

## Licensing

This repository uses separate licenses for software and educational content:

- **Software — [MIT License](LICENSE):** Original source code, tests, and launch
  scripts in `interactive-learning/python-game/`, plus any other original code
  specifically identified as MIT-licensed. Commercial use, modification, and
  redistribution are permitted under the MIT terms.
- **Educational content — [CC BY 4.0](LICENSE-CONTENT.md):** Original teaching
  materials in `docs/`, `guide/`, `slides/`, `videos/`, original visuals in
  `assets/`, and original explanatory text in this README. Reuse and adaptation,
  including commercially, require appropriate attribution and indication of changes.

**Third-party content is not relicensed.** External sources, datasets, images,
and other third-party materials remain under their own terms. The CC BY 4.0
notice also excludes internal `project-management/` records. See the two
license files for scope and attribution instructions.

## Collaboration and Stage 3

Work is coordinated through [GitHub Issues](https://github.com/Voryalis/aleksandria/issues), branches, pull requests, and recorded review. The [shared Google Drive](https://drive.google.com/drive/folders/1Itr4fr4STo3VSAMMnOjuk-1wPruCGBS3) holds team submission files and videos.

The planned Stage 3 mini-lecture focuses on **“How Does a Neural Network Learn to Recognize a Handwritten Digit?”** The teaching aim is to follow a single labelled image through numeric representation, prediction, error measurement, and a learning update. Stage 3 deliverables and final review remain separate from Stage 2.

**Stage 2 milestone:** 7 November 2026, 23:59 Beijing time. **Stage 3 planned checkpoint:** 28 November 2026.
