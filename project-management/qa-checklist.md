# Aleksandria QA Checklist

Project: **Aleksandria — Big Data & Connectionist AI**  
Team: **Team Aleksandria**  
Audience: university students with little or no prior experience in AI.  
QA coordination owner: **@Tamer088**  
Revision date: **2026-10-21**

This checklist covers content accuracy, beginner learning, production quality, evidence, and submission requirements. It updates the earlier generic checklist using the supplied teacher materials. It is a review tool, not a record of completed checks.

## How to use this checklist

1. Select the assignment and stage being reviewed. Record the author, reviewer, version, and evidence in [qa-log.md](qa-log.md).
2. Apply the common checks and the sections relevant to that assignment. Future work is **NOT DUE**, not passed and not automatically N/A.
3. Record each applicable check as **PASS**, **ISSUE**, **BLOCKED**, or **NOT CHECKED**. Use **N/A** only with a reason permitted by the assignment. A section passes only when every applicable check passes.
4. Keep this master checklist reusable. Record results for each material separately rather than marking one shared copy as completed for the whole project.
5. A person other than the original author must perform the peer checks required below. AI assistance does not replace the required human review.
6. Record a useful confirmation when no error is found. Never invent an error, result, score, meeting, contribution, or verification step.
7. Consult [qa-requirements.md](qa-requirements.md) for source references, deadlines, exceptions, and unresolved conflicts. The provided current assignment requirements control explicit exceptions. Do not silently resolve contradictory instructions.

## A. Common learning and accuracy checks

- [ ] **A01** The material identifies its purpose, learning goals, audience, prerequisites, and version.
- [ ] **A02** The sequence introduces prerequisite ideas first, develops one main idea at a time, and connects explanation, example, application, reflection, and takeaway.
- [ ] **A03** New terminology, symbols, and formulas are explained in plain language. Examples and visuals include explanations of what to notice.
- [ ] **A04** Important definitions and claims have been checked against reliable, identifiable sources; key references lead to the original source where available.
- [ ] **A05** Sources exist and support the specific claims. Numbers, quotations, context, dates, versions, and limitations agree with the source.
- [ ] **A06** Worked examples, calculations, code, answers, and activity instructions have been independently reproduced. Inputs, units, rounding, setup, expected results, and relevant limitations are recorded.
- [ ] **A07** Learners have meaningful opportunities to predict, compare, solve, experiment, explain, or find an error, with instructions and useful feedback.
- [ ] **A08** A selected explanation or activity has been tried by someone other than its author; their confusion, observations, and resulting changes or confirmations are recorded.
- [ ] **A09** Borrowed explanations, images, diagrams, code, datasets, media, and adapted previous student work are attributed. AI-use records do not replace citations.
- [ ] **A10** Wording, definitions, examples, answers, and learner-facing references agree across Markdown, guide, test bank, slides, and videos.
- [ ] **A11** Visuals explain the content, labels are legible, meaning is not conveyed by color alone, and informative visuals have a textual explanation or alternative text.
- [ ] **A12** Layout, tone, terminology, and visual identity are consistent. Stories, humor, and decorative elements support learning without obscuring the concept.

## B. Topic checks for Big Data and Connectionist AI

These are project-specific QA checks proposed for the stated topic. Confirm the exact module scope against the course materials; they are not an invented teacher syllabus.

- [ ] **B01** The chosen Big Data characteristics are defined consistently, illustrated with concrete examples, and connected to data collection, processing, and use.
- [ ] **B02** Data, dataset, feature, label, model, and prediction are distinguished where used. The relationship between Big Data, machine learning, and connectionist AI is explained.
- [ ] **B03** Neuron diagrams match the explanation of inputs, weights, bias, activation, and outputs. Any numerical forward-pass example can be reproduced.
- [ ] **B04** Training and prediction are distinguished. Loss, parameter updates, learning rate, and epochs are introduced at an appropriate level. Backpropagation and optimization are not conflated if both are covered.
- [ ] **B05** Training, validation, and test data are distinguished where applicable. Examples are checked for data leakage and unsupported claims about generalization.
- [ ] **B06** Overfitting, underfitting, and relevant evaluation measures are explained using evidence suitable for beginners. Training performance is not presented as proof of performance on new data.
- [ ] **B07** Claims about dataset size, data quality, model performance, or human-like understanding are qualified and supported rather than stated as universal guarantees.
- [ ] **B08** Practical demonstrations specify the dataset, starting settings, learner action, observations, and expected interpretation. Variable results are described honestly, without invented experimental outcomes.
- [ ] **B09** Real-world applications explain the data, task, output, benefit, limitation, and supporting source.
- [ ] **B10** Ethical cases address relevant issues such as bias, privacy, consent, transparency, misuse, or accountability through a concrete scenario and reasoned discussion.
- [ ] **B11** Analogies to brains or human learning are identified as analogies and their limits are explained.
- [ ] **B12** Advanced material and optional extensions are clearly separated from the core beginner learning route.

## C. GitHub and Markdown

- [ ] **C01** The README identifies Team Aleksandria, the module, members and GitHub usernames, intended learners, folder structure, material locations, progress, and remaining work.
- [ ] **C02** The current plan and task list can be located. Tasks have an expected result, owner, internal deadline, status, and relevant dependencies.
- [ ] **C03** The repository contains the current Markdown, references, and required assets, using meaningful names and working relative paths.
- [ ] **C04** Commits show meaningful changes over time. Authors and contributions are identifiable; author and uploader are distinguished when necessary.
- [ ] **C05** Evidence shows actual changes and review outcomes, not only commit counts or a repository homepage screenshot.
- [ ] **C06** GitHub rendering and the exported readable copy have been checked for headings, tables, formulas, code blocks, images, links, and anchors.
- [ ] **C07** The extracted submission works outside GitHub, with required images, example files, and local references intact.
- [ ] **C08** Teacher access and supplementary links work. Large external media locations are clearly identified without replacing required submitted files.
- [ ] **C09** Personal logs, student IDs, and other private evidence are kept out of publicly accessible repository content.

## D. Stage 1 Markdown V1 and project planning

- [ ] **D01** The outline covers the whole intended module, with learning outcomes, prerequisites, topics, planned activities, and honest section statuses.
- [ ] **D02** At least one coherent topic or connected group of subtopics is fully developed, with explanations, terminology, a worked example, a useful visual where appropriate, an application task, an explained answer, and references.
- [ ] **D03** The remainder shows meaningful substantive progress; a developed sample is not used to disguise an otherwise empty outline.
- [ ] **D04** Another team member has reviewed the developed material. At least one concrete outcome records what was checked, what was found, and what was corrected or confirmed.
- [ ] **D05** The team explains how the developed content can support the guide, slides, and video. Finished versions of all three are not required at this stage.
- [ ] **D06** The project plan covers team information, strengths and learning needs, responsibilities, scope, resources, mini-lecture idea, schedule, communication, risks, and workload.
- [ ] **D07** The master task list covers the whole project, with detailed Stage 1 tasks and reasonable dependencies and internal deadlines.
- [ ] **D08** Team members have reviewed the plan and understand the core content and their responsibilities. Planning decisions and significant AI help are recorded authentically.

## E. Stage 2 Markdown V2

- [ ] **E01** Every core topic in the agreed scope contains substantive learning content. Remaining core gaps are identified and do not count as completed content.
- [ ] **E02** Every major topic has a suitable example or demonstration and an opportunity to apply the idea, with checked answers or expected outcomes.
- [ ] **E03** Every core section has been reviewed by someone other than its original author.
- [ ] **E04** A non-author has attempted selected explanations or activities as a learner; observations and resulting revisions are recorded.
- [ ] **E05** A revision summary records feedback or a problem, the change and reason, and its exact location. Rejected suggestions include reasons.
- [ ] **E06** A mapping connects Markdown sections to guide sections, test-bank questions, slide topics, and video topics. Use “not selected for video” where appropriate.
- [ ] **E07** Corrections have reached the Markdown source and every affected resource. The complete updated content, not only changed fragments, is ready to submit.

## F. Study Guide

- [ ] **F01** The guide contains identification, usable contents, learning goals, prerequisites, a learning route, core explanations, case studies, activities, exercises, explained feedback, summaries, glossary, resources, and references.
- [ ] **F02** Each major topic gives learners something meaningful to do. The guide supports independent learning rather than relying on copied slides or links.
- [ ] **F03** Each substantial activity specifies its goal, preparation, task, observation, reflection, and feedback.
- [ ] **F04** External resources identify the title/provider, purpose, relevant section or timestamps, learner task, and important limitations; the team has inspected them.
- [ ] **F05** Platform activities use tested settings and clear starting points. Account, installation, language, and network requirements are explained.
- [ ] **F06** Linked resources have been tested with another account or a suitable signed-out session, including permissions to run, copy, attempt quizzes, and view feedback.
- [ ] **F07** Online activities have usable fallbacks, such as sample outputs or screenshots with analysis questions. Essential instructions and expected outcomes remain in the submitted guide.
- [ ] **F08** Team-created programs or notebooks include actual sources, required data, and setup instructions; Colab work includes the `.ipynb` file and instructions for using a personal copy.
- [ ] **F09** The complete guide is readable, coherent, engaging, and consistent with the checked Markdown and other resources.

## G. Test Bank

- [ ] **G01** There are at least **20 True/False**, **20 Multiple Choice**, and **6 open-ended** questions: at least **46** questions in total.
- [ ] **G02** Questions cover core concepts, identify their topic or guide section, and balance understanding and application; at least one requires higher-order thinking.
- [ ] **G03** Wording is unambiguous, distractors are plausible, and each MCQ states whether one or multiple answers are required.
- [ ] **G04** Open-ended tasks invite developed reasoning, normally over 100 words or equivalent diagrams, calculations, or worked steps.
- [ ] **G05** Some questions connect to guide activities and include enough information to answer without opening an external platform.
- [ ] **G06** Questions appear before a separately labelled answer key. True/False answers explain and correct false statements; MCQs explain the choices; open-ended answers give expected key points and valid alternatives.
- [ ] **G07** Another team member has attempted and reviewed **every question**, including its answer and reasoning. Question IDs and review evidence are recorded.
- [ ] **G08** Numbering, symbols, terminology, difficulty, and coverage are consistent; unnecessary repetition is removed.
- [ ] **G09** The Test Bank is a separate editable **Word document**. PDF or online formats are supplementary.

## H. PPT Slides

- [ ] **H01** The slides tell a complete teaching story through the module's essential ideas, with an opening problem, goals, roadmap, connected examples, audience participation, conclusion, and next steps.
- [ ] **H02** Slides have one main teaching purpose each. Large text, contrast, and legible diagrams work in full-screen presentation; approximately 28–32 pt is a starting guide, not a substitute for testing readability.
- [ ] **H03** Explanations, activity instructions, timing, expected answers, transitions, misconceptions, and sources appear in presenter notes where needed.
- [ ] **H04** Audience activities allow thinking time and provide a later answer or debrief.
- [ ] **H05** Demonstrations have a prepared starting state, tested media, and an offline fallback.
- [ ] **H06** The presentation reaches meaningful content promptly, shows ideas through examples, and builds to a useful final application or insight.
- [ ] **H07** Specific guide sections, question IDs, and video references are accurate and useful.
- [ ] **H08** Another member has reviewed the slides and rehearsed a representative section using the notes.
- [ ] **H09** The actual submitted **PPTX**, notes, and supporting files have been tested. A PDF does not replace editable slides and notes.

## I. Video Tutorials

- [ ] **I01** The submitted collection has **1–8 finished MP4 videos**, each **no larger than 250 MB**. Record actual file sizes and leave an upload margin.
- [ ] **I02** The collection covers the essential ideas in a coherent order. Each video has a clear purpose, prerequisites where needed, guided explanation, demonstration, learning check, and conclusion.
- [ ] **I03** Narration explains reasoning beyond slide text. Examples, diagrams, calculations, and demonstrated results are accurate.
- [ ] **I04** Pacing allows beginners to follow. Unnecessary setup, repetition, filler, and distracting effects are removed. Five to ten minutes is a guideline, not a mandatory duration range.
- [ ] **I05** Demonstrations identify settings, starting conditions, inputs, and outputs, and explain why the result matters.
- [ ] **I06** Learning checks allow thinking time and provide an explanation or expected outcome.
- [ ] **I07** Narration and visuals are synchronized. Speech, labels, code, diagrams, and actions remain clear in the final compressed export.
- [ ] **I08** Captions are provided where needed for understanding/accessibility and checked if used. Synthetic narration is checked for pronunciation, pacing, and accuracy.
- [ ] **I09** Another team member has watched **every final compressed video in full**. A non-creator has tried a selected tutorial and its learning check.
- [ ] **I10** The tutorial guide lists titles, filenames, durations, sizes, goals, viewing order, prerequisites, chapter timestamps for longer videos, and specific links to related materials.
- [ ] **I11** The tutorial guide includes narration scripts or detailed teaching outlines matching the recordings; required activity files are supplied.
- [ ] **I12** MP4 files are uploaded individually to Lexue. A ZIP or external video link does not replace the required videos or bypass the size limit.
- [ ] **I13** Self-review uses the supplied Stage 2 Video V1 rubric: coverage 20, accuracy 20, audiovisual quality 20, engagement 15, active learning 15, coherence 10, total 100. Any conversion to course XP remains subject to teacher guidance.

## J. Optional interactive supplements and peer-review scope

The current Study Guide assignment explicitly removes last year's compulsory Lexue platform task. Meaningful activities are still required; building a separate platform is optional. The peer-review assignment still requests an Interactive Learning System, so its scope must be clarified separately.

- [ ] **J01** If a supplement is included, its learning purpose, starting instructions, learner actions, expected outcomes, and contribution to the guide are clear.
- [ ] **J02** Navigation, access, media, question scoring, attempts, hints, and feedback are tested from a learner's perspective. Screenshots alone do not prove functionality.
- [ ] **J03** Activities have appropriate variety, alignment, plausible distractors, clear wording, and explanatory feedback beyond “correct/incorrect.”
- [ ] **J04** The team records design/adaptation work and actual testing, supplies required sources/data, and provides a fallback where necessary.
- [ ] **J05** For a system assessed with the supplied interactive checklist, record its specific design and AI-assisted question-critique checks, followed by human verification and an AI-use record.
- [ ] **J06** Do not penalize the absence of an optional platform in the current Study Guide assignment. Do not decide how to score a missing peer-review system until the teacher clarifies that assignment.

## K. Project logs, personal logs, and AI evidence

- [ ] **K01** Dated project entries distinguish actual work, attempts, outcomes, learning, unresolved questions, and next steps with owners and intended dates.
- [ ] **K02** Meeting summaries record attendees, purpose, decisions, reasons where useful, and follow-up actions. Screenshots do not replace the written summary.
- [ ] **K03** Readable excerpts, results, or screenshots and captions appear beside or immediately below the relevant entry. External links are supplementary.
- [ ] **K04** Significant AI use records date/person/tool, purpose, important prompts/outputs/follow-ups, verification and decisions, and outcome/learning. Record this QA-document preparation too.
- [ ] **K05** Each member writes an authentic personal account, including course learning beyond the project module. Individual evidence supports their own role; a project-log reference alone is insufficient.
- [ ] **K06** Stage 1 logs cover the beginning through October 24. Stage 2 submissions cover **October 25–November 7 only**, with no invented later activities.
- [ ] **K07** Contribution scores are evidence-based and agreed by the team: the highest contribution is 100, equal scores are possible, and scores need not sum to 100.
- [ ] **K08** The project log is one Word/PDF document. Personal logs are collected into a separate Word/PDF document, with a contents list and a new page per member. Single documents are not zipped.
- [ ] **K09** Personal details and individual reflections are submitted through the designated private assignment channel, not published in GitHub or the public class resource space.

## L. Live Status Report and later peer review

- [ ] **L01** The status report shows actual progress, readable GitHub/Markdown evidence, a representative teaching example, a problem, and next steps.
- [ ] **L02** The whole delivered report, including any live opening/closing around a recording, lasts no more than **4 minutes**. It has been rehearsed.
- [ ] **L03** All presentation-ready files are extracted on a **USB drive** and playback, sound, and visuals are tested. Materials are submitted before the presentation begins as well as by the applicable deadline.
- [ ] **L04** Peer review covers two teams: one confirmed assigned team and one chosen team. Team Aleksandria's assignment must be confirmed because its name is absent from the supplied matching table.
- [ ] **L05** Each required peer deliverable has a numerical grade with the applicable rubric, evidence, strengths, and specific respectful improvement actions; no grades are invented before inspection.
- [ ] **L06** Both team reviews are in one Word/PDF with screenshots or precise visual references, and feedback is posted in each team's Lexue space by the team after review.

## M. Submission checks

- [ ] **M01** The deadline and rubric conflicts in the requirements register have been checked with the teacher; unresolved points remain visible.
- [ ] **M02** Required assessed content and evidence are inside the submitted files. Only explicitly permitted supplementary resources rely on links.
- [ ] **M03** Stage 1 Markdown ZIP includes the source snapshot and assets, readable content PDF, and Word/PDF report with snapshot date, commit identifier, review outcome, contributions, and readable development evidence.
- [ ] **M04** Stage 1 project plan is a Word/PDF with the actual plan and task-list snapshot, repository location, and required team information.
- [ ] **M05** Stage 2 Markdown ZIP includes the complete updated source/assets, rendered PDF, and concise report with revisions, review results, resource mapping, development evidence, and remaining gaps.
- [ ] **M06** Study Guide ZIP includes the complete Word/PDF guide, separate editable Word Test Bank, and required support files. No separate general submission report is required for this assignment.
- [ ] **M07** PPT is submitted directly when it is one PPTX; multiple required files use one organized ZIP. Videos use the individual-upload requirements in section I.
- [ ] **M08** Filenames identify Aleksandria, stage, assignment, and version. Required identity information is placed in the appropriate submission, with public/private information separated.
- [ ] **M09** ZIPs have been extracted into a different folder and the actual submitted copies opened and tested. Media, notes, assets, questions, answers, and evidence are readable and complete.
- [ ] **M10** All members have checked the team submission; the designated submission lead submits one copy and records the actual submission outcome.

## Completion boundaries

The original GitHub issue #5 can be completed when the agreed initial content has been reviewed and its real findings or confirmations are documented, according to that issue's stated completion condition. Creating this checklist completes only its checklist-creation task after the team accepts the file.

Closing issue #5 does not prove that all course assignments are ready. Submission readiness requires the relevant assignment checks, required files, access, evidence, and confirmed handling of unresolved requirements. For internal QA, significant accuracy or usability failures require correction and retesting before approval; this is a team workflow rule, not an invented teacher grading formula.
