# Aleksandria — Stage 1 Task List

## Status Legend

- **Planned:** Work is identified but completion has not been verified.
- **In progress:** Work has demonstrably started.
- **Blocked:** Work cannot proceed until a documented dependency is resolved.
- **In review:** Work has been submitted for review.
- **Done:** Work is complete and supported by verifiable evidence.

Do not mark a task Done solely because a file exists or contains a placeholder. Update statuses based on actual work.

## Task Register

| ID | Task | Owner | Deadline | Status | Dependencies / Acceptance criteria |
|---|---|---|---|---|---|
| PM-01 | Confirm project scope, target audience, measurable learning objectives, and chapter sequence. | Iatsenko Aleksandr (Coordinator), with Virin Grigorii (Content Lead) | Before Markdown V1.0; exact internal date pending confirmation | Planned — confirm current state | Objectives must be clear, measurable, and consistent with the five existing chapter files. |
| PM-02 | Complete `project-management/project-plan.md`. | Iatsenko Aleksandr | Internal deadline pending confirmation | Planned — confirm current state | Include scope, audience, objectives, chapter sequence, roles, deliverables, milestones, dependencies, and pending decisions. |
| PM-03 | Complete `project-management/task-list.md` and maintain task ownership and status. | Iatsenko Aleksandr | Internal deadline pending confirmation | Planned — confirm current state | Every task must have an owner, deadline or explicit pending deadline, status, and acceptance criteria. |
| PM-04 | Confirm the roster, task assignments, GitHub access, and unresolved blockers. | Iatsenko Aleksandr, Abdullayev Kamran | As soon as practicable; exact date pending | Planned — confirm current state | Record confirmed decisions and blockers; do not assume access or approval. |
| PM-05 | Hold or confirm actual team meetings and record decisions and action items. | Iatsenko Aleksandr; Abdullayev Kamran records the verified log | Weekly | Planned — record actual meetings | Use WeChat for coordination. Record actual meeting dates, participants, decisions, actions, and evidence. |
| PM-06 | Maintain `project-management/project-log.md` with verified activities and evidence. | Abdullayev Kamran (CIO) | Throughout Stage 1 | Planned — confirm current state | Log actual dates, contributors, changes, evidence links, next actions, and relevant AI assistance and verification. |
| CT-01 | Finalize measurable learning objectives and map them to the five chapter files. | Virin Grigorii | Before Markdown V1.0; exact internal date pending confirmation | Planned — confirm current state | Cover raw-data issues, data preparation, neural-network inputs and weights, error-driven learning, and data quality and representativeness. |
| CT-02 | Develop `docs/01-big-data.md`. | Virin Grigorii, coordinating substantive contributions from the team | 24 October 2026, 23:55 UTC+8 — Stage 1 milestone | Planned — confirm current state | Explain Big Data, especially volume, variety, and veracity; discuss data quality and preprocessing; include a labeled handwritten-digit example and verified citations. |
| CT-03 | Develop `docs/02-connectionist-ai.md`. | Virin Grigorii, with contributions coordinated across the team | 24 October 2026, 23:55 UTC+8 — Stage 1 milestone | Planned — confirm current state | Explain connectionism, artificial neurons, and interconnected processing units at beginner level. Include definitions, an example, and citations. |
| CT-04 | Develop `docs/03-neural-networks.md`. | Virin Grigorii, with contributions coordinated across the team | 24 October 2026, 23:55 UTC+8 — Stage 1 milestone | Planned — confirm current state | Explain inputs, weights, layers, activation functions, predictions, loss, training, and backpropagation at beginner level. |
| CT-05 | Develop `docs/04-integration.md`. | Virin Grigorii, coordinating with Abdullayev Kamran and relevant contributors | 24 October 2026, 23:55 UTC+8 — Stage 1 milestone | Planned — confirm current state | Trace the handwritten-digit example from raw data and preprocessing to model inputs, training, validation, and evaluation. |
| CT-06 | Develop `docs/05-applications.md`. | Virin Grigorii, coordinating with Koldas Tamerlan | 24 October 2026, 23:55 UTC+8 — Stage 1 milestone | Planned — confirm current state | Discuss practical applications, limitations, data bias, representativeness, privacy, and responsible use with verified citations. |
| REF-01 | Consolidate and verify research sources and in-text citations. | Virin Grigorii, coordinating with the designated reference-task owner; owner confirmation pending | Before Markdown V1.0 review | Planned — owner confirmation pending | Complete `references.md`; verify that sources support the claims and are cited in the relevant chapters. Do not treat unchecked URLs as verified citations. |
| QA-01 | Conduct independent factual and beginner-accessibility review of developed content. | Koldas Tamerlan (Quality Lead) | Before Markdown V1.0 is declared complete | Planned — confirm current state | Record specific findings, supporting evidence, required changes, and review outcomes. |
| QA-02 | Resolve review findings and record actual changes. | Relevant content owner; Koldas Tamerlan verifies corrections | Before Markdown V1.0 is declared complete | Planned — depends on QA-01 | Each finding must be addressed, explicitly left open with a reason, or tracked as a blocker. |
| VIS-01 | Prepare supporting diagrams and visual assets for the learning materials. | Balanin Arsentii (Visual Design Lead) | Internal deadline pending confirmation | Planned — confirm current state | Visuals must support the approved content, use consistent terminology, and be checked for clarity and accuracy. |
| VID-01 | Prepare video plan and scripts aligned with the learning objectives. | Kapiz Mirad (Video Lead) | Internal deadline pending confirmation | Planned — confirm current state | Scripts must align with the chapters and shared handwritten-digit example. Mini-lecture topic approval remains pending. |
| SUB-01 | Check the required submission package against instructor rules. | Iatsenko Aleksandr, coordinating with the team | Final deadline pending confirmation | Planned — deadline pending | Verify required formats, deliverables, citations, contribution evidence, and any required submission procedure before declaring readiness. |

## Team Responsibilities

| Member | Role | Primary task areas |
|---|---|---|
| Iatsenko Aleksandr | CEO / Project Coordinator | PM-01 to PM-05, SUB-01 |
| Abdullayev Kamran | CIO / Repository & Technical Workflow | PM-04, PM-06, technical workflow and repository support |
| Virin Grigorii | Content Lead | CT-01 to CT-06, coordination of REF-01 |
| Kapiz Mirad | Video Lead | VID-01 |
| Koldas Tamerlan | Quality Lead | QA-01, QA-02, quality support for CT-06 |
| Balanin Arsentii | Visual Design Lead | VIS-01 |

All team members should make identifiable, substantive contributions and be able to explain their own work. Shared contributions must be recorded accurately.

## Coordination and Review Workflow

1. Coordinate through WeChat and hold one team meeting each week.
2. Use GitHub Issues to track assigned work and blockers.
3. Make focused changes on branches where appropriate.
4. Use descriptive commit messages and open pull requests linked to the relevant issue.
5. Request review before merging into `main`.
6. Record actual activities and evidence in `project-management/project-log.md`.
7. Update each task's status only when the status is supported by actual progress.
8. Escalate unresolved dependencies or access problems to the coordinator and CIO.

## Stage 1 Acceptance Checklist

- [ ] Project scope, objectives, and chapter sequence are confirmed.
- [ ] `project-management/project-plan.md` is reviewed by the responsible owner.
- [ ] `project-management/task-list.md` has concrete tasks, owners, deadlines, statuses, and acceptance criteria.
- [ ] The five chapter files contain substantive teaching content rather than headings alone.
- [ ] The shared handwritten-digit example connects data preparation and neural-network learning.
- [ ] Learner activities include explained answers.
- [ ] In-text citations and `references.md` have been verified.
- [ ] Independent quality-review findings and their resolutions are documented.
- [ ] The project log contains actual activities, decisions, contributors, and evidence.
- [ ] Remaining blockers and pending decisions are explicitly documented.
- [ ] The final submission requirements and deadline have been confirmed.

## Pending Items

- Confirm current status of every task before changing any item to In progress, In review, or Done.
- Confirm intermediate deadlines with the team.
- Confirm the owner of the separate reference-consolidation task.
- Confirm the mini-lecture topic.
- Confirm GitHub access and assignment blockers.
- Confirm the final submission deadline and exact required package.
