# Aleksandria — Beginner PPT Slide Outline (Stage 1)

**Owner:** Arseny Balanin / @17sen — Visual Design Lead  
**Issue:** [#12 — Plan Beginner PPT Slide Sequence](https://github.com/Voryalis/aleksandria/issues/12)  
**Status:** **Provisional** — source chapters and scientific claims require Content Lead and QA review.  
**Target audience:** University beginners with high-school mathematics; no assumed prior AI knowledge.  
**Style:** See [`../assets/visual-style-guide.md`](../assets/visual-style-guide.md).

## Source alignment

The repository project plan maps teaching content to `docs/01-big-data.md`, `02-connectionist-ai.md`, `03-neural-networks.md`, `04-integration.md`, and `05-applications.md`. This outline uses those intended section **topics**, not quotations or approved passages. At preparation time the checked Markdown chapters were empty on `main`; update precise heading/anchor references after the Content Lead publishes content.

## Proposed slide-by-slide sequence

| # | Proposed title | Learning objective / single core point | Planned `docs/` source | Diagram / visual | Notes, example or prompt |
|---|---|---|---|---|---|
| 1 | Aleksandria — Big Data & Connectionist AI | Introduce the learning topic | `README.md` and project plan | Ancient Greece × high-tech cover | Opening; no technical claims |
| 2 | Meet the Team | Identify six team roles | `README.md`, project plan | Team member cards | Check names and student IDs before final export |
| 3 | What Is Big Data? | Introduce volume, velocity, variety, veracity and value | `docs/01-big-data.md` (planned) | Five simple V icons | Explain why quality matters as well as quantity |
| 4 | Why Raw Data Needs Preparation | Identify missing, noisy or inconsistent inputs and labels | `docs/01-big-data.md` (planned) | Before/after data example | Ask: What could go wrong if a digit is labelled incorrectly? |
| 5 | A Digit Image Becomes Numbers | Trace an image to prepared pixel values and a correct label | `docs/01-big-data.md`, `docs/04-integration.md` (planned) | `../assets/diagrams/data-to-ai-workflow.svg` | Distinguish input, preprocessing and ground-truth label |
| 6 | The Artificial Neuron | Identify inputs, weights, bias, activation and output | `docs/02-connectionist-ai.md`, `docs/03-neural-networks.md` (planned) | New labelled single-neuron schematic **needed** | Short speaker notes should define each term; avoid unexplained formulas |
| 7 | Layers Form a Neural Network | Distinguish input, hidden and output layers | `docs/03-neural-networks.md` (planned) | `../assets/diagrams/neural-network.svg` | Clarify diagram is simplified, not a trained digit-recognition architecture |
| 8 | Prediction Versus Correct Answer | Explain that a model output may differ from the label | `docs/03-neural-networks.md`, `docs/04-integration.md` (planned) | Prediction / correct-label comparison **needed** | Worked example must be explicitly hypothetical unless tested |
| 9 | How Training Changes a Network | Describe repeated prediction → loss → backpropagation → optimizer update | `docs/03-neural-networks.md` (planned) | Training-cycle diagram **needed** | No claim that a single update guarantees a correct answer |
| 10 | Digit Recognition: Full Journey | Connect raw data, prepared input, prediction and evaluation | `docs/04-integration.md` (planned) | Reuse data-to-AI workflow plus separate training cycle | Ask learners to put the stages in order |
| 11 | Data Quality, Bias and Limitations | Explain why more data alone does not guarantee better results | `docs/05-applications.md` (planned) | Balanced comparison of representative vs biased examples **needed** | Mention privacy and reliability as limitations, subject to source review |
| 12 | Recap and Learner Check | Revisit major concepts in one concrete task | All reviewed `docs/` chapters | Simplified flow with missing labels | Ask: label input, preprocessing, network, prediction and correct label; provide answer in notes |

## Speaker-note and diagram plan

- **Slides 3–4:** brief definitions and one concrete data-quality example.
- **Slides 5–7:** explanatory speaker notes, with a diagram walk-through and explicit simplified-model caveat.
- **Slides 8–10:** worked digit-recognition example; keep predicted values hypothetical unless a model is actually run and results verified.
- **Slide 12:** learner prompt and explained answer in notes.
- **Reusable existing SVGs:** `assets/diagrams/data-to-ai-workflow.svg` (slides 5 and 10); `assets/diagrams/neural-network.svg` (slide 7).
- **Further visuals needed in Stage 2:** labelled artificial neuron, training/loss/update loop, and optional correct-versus-incorrect prediction graphic.

## Visual design direction

- Title/team slides: Ancient Greece × high-tech theme, gold Greek-key borders, classical Georgia headings, blue network motifs.
- Teaching slides: simplify decorative framing; use legible Aptos labels and clearly directed arrows.
- Colours and exact PPTX typography: documented in the visual style guide.
- Maintain consistency with the two opening slides but prioritize clarity and accessibility over ornamentation.

## Review and completion checklist

- [x] Draft a coherent slide sequence and learning purpose for each slide.
- [x] Map slides to the five planned Markdown chapters.
- [x] Identify existing diagram reuse and remaining visual requirements.
- [x] Mark speaker notes, examples and learner prompts.
- [ ] Replace topic-level `docs/` references with actual section headings after Markdown is populated.
- [ ] Ask Content Lead @loauyhf to check technical language and source alignment.
- [ ] Ask QA Lead @Tamer088 to review clarity, accuracy and accessibility.
- [ ] Coordinate reusable visuals with Video Lead @MiradKapiz.
- [ ] Record review feedback and actual revisions before treating issue #12 as done.

## AI assistance

ChatGPT helped draft the provisional sequence, table and review checklist using the repository plan and GitHub issue requirements. The content is a planning proposal and must be verified against the team's reviewed Markdown; no fabricated model results or completed peer reviews are claimed.