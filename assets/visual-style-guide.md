# Aleksandria — Visual Style Guide (Stage 1)

**Owner:** Arseny Balanin / @17sen — Visual Design Lead  
**Status:** Draft for Content Lead and QA review  
**Related issues:** [#6](https://github.com/Voryalis/aleksandria/issues/6), [#12](https://github.com/Voryalis/aleksandria/issues/12)  
**Visual concept:** Ancient Greece × high technology — classical geometric ornament, restrained gold and parchment, and blue neural-network/circuit motifs.

## 1. Source and scope

This guide documents the colour values and fonts used in the editable **Aleksandria_Ancient_Greece_High_Tech.pptx** opening slides. The SVG diagrams below reuse its main colours and adapt the design for clear beginner-level instruction. This is a **proposed** visual system, not yet an approved team standard. The PowerPoint uses editable text, shapes, Greek-key line patterns, medallions, and network-node motifs; no external classical bust photographs are embedded in that PPTX.

## 2. Exact PowerPoint colour palette

All values below come from the RGB constants used to generate the two opening slides. RGB values are 8-bit channel values; hexadecimal notation is `#RRGGBB`.

| Token | HEX | RGB | Intended usage |
|---|---|---|---|
| `navy` | `#0C1B2B` | `rgb(12, 27, 43)` | Slide 1 background; dark diagram panels |
| `deep` | `#122A3E` | `rgb(18, 42, 62)` | Dark medallion/panel surfaces |
| `cream` | `#F4E9D0` | `rgb(244, 233, 208)` | Slide 2 background; light headings on dark |
| `paper` | `#E8D8B8` | `rgb(232, 216, 184)` | Column fluting / parchment accents |
| `gold` | `#BB8539` | `rgb(187, 133, 57)` | Greek-key borders, rules, medallion outlines |
| `blue` | `#27A9E5` | `rgb(39, 169, 229)` | Neural connections and data-flow emphasis |
| `pale_blue` | `#84DAF8` | `rgb(132, 218, 248)` | Highlighted network nodes and dark-slide accents |
| `ink` | `#163043` | `rgb(22, 48, 67)` | Text on light slides |
| `muted` | `#52646E` | `rgb(82, 100, 110)` | Secondary text on light slides |
| `white` | `#FAF7EF` | `rgb(250, 247, 239)` | Main text on dark slides; light card surfaces |

### Colour rules

- Use `navy` + `white` or `cream` for dark slides; `cream`/`white` + `ink` for light slides.
- Use `gold` for framing and decoration, **not** for small paragraphs on a pale background.
- Use `blue`/`pale_blue` to emphasize data flow and network structure; never rely on colour alone to distinguish components.
- Keep teaching diagrams simpler than the opening slides: remove decorative Greek-key motifs when they compete with arrows, labels, or examples.
- The colour names above are source code tokens, not official brand names.

## 3. Fonts and typographic hierarchy

**Fonts actually used in the two opening PPT slides:**

| Font family | Usage in PPT | Example sizes used |
|---|---|---|
| **Georgia** | Main titles, classical section headings, member names, numerals, italic subtitle | 36 pt title, 29 pt topic, 28 pt team title, 12 pt member names, 17 pt subtitle |
| **Aptos** | Supporting text, labels, roles, footer and technical annotation | 9–12 pt small labels/roles; 10 pt eyebrow/subtitle labels |

The opening deck is 16:9 widescreen (**13.333 × 7.5 in**). For **future classroom teaching slides**, proposed readability targets are: slide title 30–38 pt, main content 20–26 pt, diagram labels 16–20 pt, and footnotes at least 12–14 pt where possible. These are forward-looking recommendations, **not** sizes already used in the opening slides.

Georgia and Aptos may render differently on systems without those fonts; check font substitution on the final presentation computer. Keep the slide title in Georgia and technical labels in Aptos or a close sans-serif fallback.

## 4. Layout and decorative conventions

- **Opening slide:** dark navy field, thin gold frame, repeated geometric Greek-key borders, stylized columns, circular medallion, connected blue nodes, centered title block.
- **Team slide:** parchment/cream field, navy text, six light cards, gold outlines, dark circular number medallions, restrained blue node accents.
- **Teaching slides:** consistent title placement; left-to-right flow diagrams; one key idea per slide; sufficient negative space.
- Prefer vector shapes and SVG so text, arrows, and labels remain sharp.
- Do not use historical imagery to imply a factual connection between Ancient Greece and neural-network technology: the Greek motifs are a **visual identity**, not a scientific claim.

## 5. Educational diagram standards

1. **Flow direction:** left to right for processing; use arrowheads and numbered stages where helpful.
2. **Neural-network diagram:** explicitly label **input layer**, **hidden layer**, **output layer**; connections may carry learned weights. State that a small network is **schematic**, not an actual architecture used for the digit-recognition example.
3. **Data-to-AI diagram:** distinguish raw image/data, preparation, numerical input, model prediction, and **correct label** (ground truth). A prediction is not the label.
4. **Training versus inference:** a prediction pipeline alone does **not** show training. Training additionally compares predictions with labels, computes loss, and updates parameters repeatedly.
5. **Captions and accessibility:** provide descriptive SVG `<title>` and `<desc>` tags, readable labels, arrowheads, sufficient contrast, and text alternatives in Markdown. Avoid relying only on colour.
6. **Scientific review:** ask Content Lead @loauyhf and QA Lead @Tamer088 to review labels and claims; check reusability with Video Lead @MiradKapiz.
7. **Source control:** diagrams are original simplified teaching illustrations; no measured model outputs or dataset statistics are asserted. Cite external sources in the accompanying educational Markdown if external factual claims or imagery are added.

## 6. Diagram assets and proposed placement

| Asset | Role | Planned instructional sources |
|---|---|---|
| [`diagrams/neural-network.svg`](diagrams/neural-network.svg) | Schematic neuron layers and weighted connections | `docs/02-connectionist-ai.md`, `docs/03-neural-networks.md` |
| [`diagrams/data-to-ai-workflow.svg`](diagrams/data-to-ai-workflow.svg) | Image → preprocessing → pixel values → prediction, with separate correct label | `docs/01-big-data.md`, `docs/04-integration.md` |

**Review dependency:** On the date this guide was prepared, the checked teaching Markdown chapters were not populated on the default branch. Confirm final diagram placement and terminology after the Content Lead supplies reviewed text; do not mark diagram links in those chapters as verified yet.

## 7. Stage 1 verification checklist

- [x] Document colours and fonts from the existing two-slide PPTX.
- [x] Draft reusable, labelled SVG diagrams.
- [x] Describe diagram conventions and accessibility rules.
- [ ] Content Lead verifies technical labels and alignment with approved Markdown.
- [ ] QA Lead checks readability and scientific accuracy.
- [ ] Video Lead confirms asset suitability for storyboards.
- [ ] Add SVG links/captions to the relevant developed `docs/` pages and test links.
- [ ] Record actual reviewer feedback and revisions in GitHub issue/PR and personal log.

## 8. AI-use transparency

ChatGPT assisted with drafting this guide, extracting the colour/font values from the PowerPoint-generation script, and generating schematic SVG markup. Human verification is required before submission: open both diagrams, compare colours with the PPTX, check all labels against reviewed course content, and record corrections honestly.