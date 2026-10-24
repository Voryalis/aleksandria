# ALEKSANDRIA — Stage 1 Project Log

**Module:** Big Data and Connectionist AI  
**Reporting period:** 21–24 October 2026  
**Prepared from:** `ALEKSANDRIA_Stage1_ProjectLog.docx` (team-supplied Word document, version 1.0, dated 24 October 2026)  
**Repository:** https://github.com/Voryalis/aleksandria  
**Working language:** English  
**Project communication:** WeChat; GitHub for shared source and issue/PR tracking  
**Stage 1 deadline:** 24 October 2026, 23:59 Beijing time (UTC+08:00)

> **Evidence and privacy note:** This is a public-repository working record derived from the team's Word log. It distinguishes statements recorded in that document from items independently checked in GitHub. The original Word log remains the source for embedded screenshots and the private submission's student IDs and proposed contribution scores; those personal assessment details are not reproduced in this public repository. GitHub links support the evidence but do **not** replace readable evidence embedded in the submitted Word/PDF document.

## A. Chronological project log

### 21 October 2026 — First team meeting and initial coordination

**When and where:** 16:30–20:00 (UTC+08:00), Wencui I503.  
**Note-taker:** Kamran Abdullayev (Mark).  
**Participants:** Aleksandr, Kamran (Mark), Grigory, Mirad, Tamerlan, Arseniy (as recorded in Meeting M-01).

**What was done:** The team discussed a collaboration workflow involving GitHub and a shared Google Drive, made minor changes to `README.md`, and considered whether the broad module name was sufficiently focused for a beginner teaching project.

**Result:** The team had not yet recorded consensus on a narrower teaching focus in the first-meeting record. Initial task ownership was documented, but the full details of every proposed workflow convention were not recorded.

**Learning / difficulty:** A broad course module is not yet a sufficiently specific teaching sequence. The team identified the need for a focused guiding question, clear beginner-level outcomes, scope boundaries, and traceable shared revisions.

**Unresolved:** Narrower topic/focus was recorded as **TBD at that meeting**. This is the *21 October decision record*, not proof the topic remained undecided later.

**Next:** Agree and record the final focus, compare it with official module requirements, and assign the decision owner/deadline. The first meeting record did not supply those details.

**Evidence E1:** The repository [README](../README.md) states the module, learning goals, project structure, and team workflow. See also [Meeting M-01](#meeting-m-01--first-team-meeting).

### 23 October 2026 — Project plan drafting and task breakdown

**Who:** Aleksandr Iatsenko, coordinator.  
**What was done:** The supplied project log states that Aleksandr used ChatGPT to help organize a Stage 1 project plan and master task list from the team draft and assignment instructions. The plan documents roles, target learners, learning objectives, a proposed scope, resource deliverables, milestones, risks, and dependencies.

**Result:** The proposed teaching path connects Big Data and data quality with preprocessing/numerical representation, artificial neurons, neural-network layers, training, and a handwritten-digit recognition case study. The same checked Markdown content is intended to support the study guide, slides, and video tutorials.

**Learning / difficulty:** Planning became more actionable when general goals were expressed as tasks with owners, deadlines, completion criteria, and dependencies. Different teaching formats should retain the same verified scientific meaning.

**Unresolved / next:** Reconcile the proposed outline with the first meeting's unresolved focus, confirm compliance with the official topic requirements, and review all AI-assisted text and proposed task statuses before formal submission.

**Evidence E2:** The [repository project plan](project-plan.md) and [task list](task-list.md) show the chapter mapping, owners, schedule, and expected deliverables. The complete team-supplied Word plan contains the fuller planning snapshot. **Evidence E3:** The Word log embeds a screenshot of the ChatGPT planning exchange; the AI-use record below describes the purpose and limits of that evidence.

### 24 October 2026 — Planning checkpoint recorded in the Word log

**Who:** Aleksandr (coordination), Kamran (repository/workflow), Grigory (content), Mirad (video), Tamerlan (quality), Arseniy (visual design). These are team leads, not exclusive authors.

**Work recorded in the plan:** The 24 October Word plan marks preparatory tasks as done, including reviewing assignment rules, confirming roles and repository access, planning learner outcomes and chapter structure, allocating tasks, proposing a review workflow, recording scheduling risks, and preparing the planning snapshot. These are **statuses reported by the plan**, not independent proof that every teaching-content or review requirement was completed.

**Results / expected shared source:** The planned chapter sequence follows data quality and numerical inputs through artificial neurons, neural-network learning, and handwritten-digit recognition. The plan assigns each lead a resource area while expecting all members to contribute meaningful work.

**Learning / difficulty:** A planned or checked-off task needs corresponding artifacts and review evidence. The team identified risks involving excessive scope, unequal workload, unsupported scientific claims, inconsistent versions across media, delays in video work, and missing contribution/AI-use evidence.

**Unresolved / next:** Confirm the narrower scope decision, complete the required Stage 1 instructional content, document independent review outcomes, and reconcile the Word plan's later Markdown-drafting dates with the 24 October Stage 1 Markdown deadline. Plans for 25 October–7 November are future milestones, **not** completed work on 24 October.

**Evidence E2:** The Word plan and the repository's [project plan](project-plan.md) and [task list](task-list.md). **Evidence E4:** The Word log embeds a screenshot of an AI-generated repository setup proposal; it demonstrates suggested steps, not necessarily their implementation.

### 24 October 2026 — Repository verification and outstanding Stage 1 content gap

**Source of this check:** Direct inspection of the GitHub `main` tree and linked assignment issues when converting the supplied Word log into Markdown. The inspected tree was at commit [`b3434145f21f`](https://github.com/Voryalis/aleksandria/commit/b3434145f21fbfad0b7f3f5e25f3bdae17422d44).

**Confirmed repository outcomes:**

- The repository contains a README, contribution instructions, a project plan/task list, the [chapter outline](../docs/chapters.md), references, video storyboards, a slide outline, a visual style guide, two SVG diagrams, and QA templates/records.
- The five intended main teaching files — [01-big-data](../docs/01-big-data.md), [02-connectionist-ai](../docs/02-connectionist-ai.md), [03-neural-networks](../docs/03-neural-networks.md), [04-integration](../docs/04-integration.md), and [05-applications](../docs/05-applications.md) — were **empty on `main` at inspection**. The outline, storyboard, diagrams, and administrative documents are not equivalent to completed teaching chapters.
- The [QA log](qa-log.md) explicitly described itself as a review template without completed independent learning-material reviews at the inspected version.
- Video scripts and diagrams existed as working resources, but an approved and reviewed teaching chapter was not confirmed.

**Issue ownership:** [Issue #3](https://github.com/Voryalis/aleksandria/issues/3) assigns coordination of substantive content in all five `docs/` files to **Grigory (@loauyhf)**, with the first chapter explicitly his writing task. [Issue #1](https://github.com/Voryalis/aleksandria/issues/1) assigns **Aleksandr (@destra825)** coordination of task division among team members. [Issue #5](https://github.com/Voryalis/aleksandria/issues/5) assigns **Tamerlan (@Tamer088)** independent content/source review.

**Next actions, by the Stage 1 deadline:** Grigory and assigned authors should populate the main Markdown with the whole module outline and at least one fully developed non-introductory teaching section (definitions, worked example, visual, learner activity, explained answer, references); Tamerlan should record an actual independent review; Aleksandr should reconcile schedule and task ownership; Kamran should capture the resulting content/PR evidence for the self-contained submission package. These are **outstanding actions**, not claims of completion.

**Evidence E5:** The actual GitHub tree/contents, [issue #3](https://github.com/Voryalis/aleksandria/issues/3), [issue #5](https://github.com/Voryalis/aleksandria/issues/5), and the cited snapshot commit.

## B. Meeting summaries

### Meeting M-01 — First team meeting

| Field | Recorded details |
| --- | --- |
| Date / time | Wednesday, 21 October 2026, 16:30–20:00 (UTC+08:00) |
| Location | Wencui I503 |
| Note-taker | Kamran Abdullayev |
| Attendees | Aleksandr, Kamran (Mark), Grigory, Mirad, Tamerlan, Arseniy |
| Purpose | Discuss GitHub/shared Drive workflow, correct minor README issues, assess focus |
| Key discussion | Concern that the assigned module was too broad for one coherent teaching focus; collaboration workflow and minor README corrections were discussed |
| Decision | No final narrower focus recorded at this meeting; more detailed conventions were not all written down |
| Follow-up | Compare narrower options and record an agreed focus; owner and date not supplied in this meeting record |

#### Task snapshot cited in the Word meeting summary

The statuses below reproduce **what the meeting summary reported** and should not be read as proof that every listed deliverable met its final completion criteria.

| Task | Lead / GitHub | Target | Status recorded in the source |
| --- | --- | --- | --- |
| Project plan and coordination | Aleksandr / @destra825 | 24 Oct | Issue marked closed/done |
| README, CONTRIBUTING, PR workflow | Kamran / @Voryalis | 24 Oct | Minor corrections reported; commit verification required |
| Chapter outline and first teaching Markdown | Grigory / @loauyhf | 24 Oct | Meeting summary marks task done; **current five chapter files were empty at repository inspection** |
| Video plan and first storyboard | Mirad / @MiradKapiz | 24 Oct | Meeting summary marks task done; scripts in repository |
| QA checklist and source/content review | Tamerlan / @Tamer088 | 24 Oct | Meeting summary marks task done; **QA templates do not establish independent chapter review** |
| Visual style and two diagrams | Arseniy / @17sen | 24 Oct | Meeting summary marks task done; visual files present |
| Narrow teaching focus | Whole team | Not recorded | Open at first meeting |

No additional substantive meeting summaries were supplied with the Word document; no other meeting is asserted here.

## C. Evidence register and readable examples

The Word source includes embedded screenshots for E1–E4. This public Markdown contains descriptions and short readable evidence excerpts; the **formal Stage 1 Word/PDF submission must retain the actual readable screenshots immediately beside the relevant activity**.

| Label | Existing source or evidence | What it supports | Verification limits |
| --- | --- | --- | --- |
| E1 | [Repository and README](https://github.com/Voryalis/aleksandria) | Shared repository and navigation structure | Does not alone establish authorship or quality of content |
| E2 | Supplied Word project plan; [repository plan](project-plan.md) and [task list](task-list.md) | Proposed learner objectives, modules, roles, dates, and task status | Reported statuses require supporting work artifacts |
| E3 | ChatGPT planning screenshot embedded in supplied Word log | AI assistance with organizing the plan | Screenshot is a selected interaction; independent team validation is not established |
| E4 | ChatGPT repository-setup screenshot embedded in supplied Word log | Suggested README, content, assets, and project-management structure | A proposed tree does not prove all files were written |
| E5 | GitHub [snapshot commit](https://github.com/Voryalis/aleksandria/commit/b3434145f21fbfad0b7f3f5e25f3bdae17422d44) and [content issue #3](https://github.com/Voryalis/aleksandria/issues/3) | Verifiable file presence and outstanding empty-chapter gap | State applies to the inspected snapshot, not future commits |
| E6 | [Video 1 storyboard](../videos/first-video-storyboard.md), [video 2 storyboard](../videos/second-video-storyboard.md), [slide outline](../slides/slide-outline.md), [visual guide](../assets/visual-style-guide.md), [QA log](qa-log.md) | Substantive planning/drafting artifacts for resource leads | Existence alone does not establish formal approval |

**Readable excerpt — planned learning sequence (E2).** Big Data/data quality → preparation and numerical representation → artificial neuron and neural-network layers → prediction and training → handwritten-digit recognition. This is a *planned teaching structure*, not proof that all instruction was written.

**Readable excerpt — repository setup guidance (E4).** The screenshot proposes creating a `README.md`, topic-oriented `docs/` files, `assets/diagrams/`, and `project-management/` files. The current repository contains these folders, but individual files must be checked for actual content.

**Readable excerpt — concrete content gap (E5).** On inspected `main`, each of the five expected `docs/01-...05-....md` blobs had size **0 bytes**. This is why the Stage 1 teaching-content requirement remained outstanding despite the chapter-outline and planning files.

## D. Significant AI-use records

### D1 — AI-assisted Stage 1 planning (recorded in supplied Word log)

- **Date, person, tool:** 23 October 2026; Aleksandr Iatsenko; ChatGPT (as recorded in the project plan).
- **Purpose:** Structure the team draft and assignment instructions into a Stage 1 plan and master task list.
- **Important interaction:** The Word plan identifies a request to complete the draft according to the team project-plan/task-list requirements and identify missing information. The Word project log includes a screenshot excerpt (E3).
- **Output retained:** Draft structure/wording, proposed schedule, owners, resource mapping, risks, and task breakdown.
- **Verification and judgment:** The supplied log says these items **should** be checked against actual roles, dates, teacher requirements, and recorded decisions. This does *not* assert that all those checks were performed. In particular, the first meeting's unresolved focus and the Stage 1 Markdown deadline require reconciliation.
- **Outcome / learning recorded:** The plan gives a usable coordination structure, while AI-produced proposals still require independent human agreement and factual review.

### D2 — CIO's repository setup assistance (recorded in supplied Word log)

- **Person / tool:** Kamran Abdullayev; ChatGPT. The exact date of this specific exchange was not established in the Word log.
- **Purpose:** Obtain guidance on GitHub organization, initial README, Markdown topic files, diagrams, and project-management files.
- **Important interaction:** E4 shows suggested steps and a proposed folder tree that separates teaching files, assets, task records, and references.
- **Verification and judgment:** The screenshot demonstrates **advice**, not implementation. The live repository confirms the folder structure exists, but several intended chapter files are empty.
- **Outcome / learning:** A consistent repository layout makes project contributions easier to locate; recommendations and checklists require actual artifact checks before being marked done.

### D3 — AI-assisted conversion of the Word project log into this Markdown working record

- **Date / tool:** 24 October 2026; ChatGPT.
- **Requester:** Kamran's project conversation; this request was to create and commit `project-management/project-log.md` using the supplied Word log.
- **Prompt excerpt:** “write the project log md file based on the doc i sent to you and commit it on git”.
- **AI output:** This Markdown transcription/reorganization with headings, chronology, meeting summary, readable evidence descriptions, and explicit separation between recorded claims and independently observed repository status.
- **Checks performed in this assistance:** Compared the supplied Word log's headings/tables with the converted content; checked current GitHub `main`, file presence, and issues #1/#3/#5. **Team review and sign-off are not claimed.**
- **Next verification:** Kamran and the team should confirm the wording, decisions, attribution, AI-use evidence, and official self-contained Word submission.

## E. Stage 1 member contributions — working summary

This summarizes Stage 1 roles and evidence in the Word log. **The relative contribution scores and student IDs in the supplied Word document are omitted from this public GitHub copy** and must be reviewed and retained in the private formal submission. These are responsibilities and documented artifacts, not a final teacher assessment.

| Member | Role and recorded work | Evidence and outstanding checks |
| --- | --- | --- |
| Iatsenko Aleksandr | CEO; planning, role allocation, AI-assisted Word plan and task list | 23–24 Oct; E2–E3; confirm actual team decisions and schedule |
| Abdullayev Kamran | CIO; GitHub workflow, repository organization, first-meeting notes, project-log coordination | 21–24 Oct; E1, E4–E5; confirm changes and meeting details |
| Virin Grigorii | Content Lead; outline and coordination of teaching chapters | E2 and [issue #3](https://github.com/Voryalis/aleksandria/issues/3); **substantive `docs/` content still needed** |
| Kapiz Mirad | Video Lead; video plan and storyboards | E6 and [issue #4](https://github.com/Voryalis/aleksandria/issues/4); technical review/alignment pending |
| Koldas Tamerlan | Quality Lead; QA templates, requirements and checklist | E6 and [issue #5](https://github.com/Voryalis/aleksandria/issues/5); actual independent chapter review outstanding |
| Balanin Arsentii | Visual Design Lead; visual style guidance, two diagrams, slide outline | E6, visual files and [issue #6](https://github.com/Voryalis/aleksandria/issues/6); content-linked scientific review pending |

## F. Outstanding Stage 1 checks

- [ ] Write and review at least one fully developed **non-introductory** Markdown section with a worked example, visual, exercise, explained answer, and citations; retain full module hierarchy.
- [ ] Document a specific independent content/source review with author, reviewer, findings, correction or confirmation, and evidence.
- [ ] Resolve or clearly mark the difference between the Word plan's future writing dates and the actual 24 October Stage 1 Markdown checkpoint.
- [ ] Confirm the narrower focus decision after Meeting M-01, including decision date and agreement.
- [ ] Assemble the **self-contained** Word/PDF project-log submission with original screenshots, detailed AI prompts/outputs and verification, team-reviewed contribution table, student IDs, and scores.
- [ ] Prepare the separate GitHub/Markdown Stage 1 snapshot ZIP with a submission report, Markdown sources/assets, readable instructional-content PDF, and repository-history evidence.
- [ ] Check that every member's personal learning/work log is included in the *separate* private submission and that personal logs are not published here.

**Maintenance rule:** Append dated, real events with their authors, concrete outputs, evidence, review decisions, and follow-up owners. Do not retrospectively mark future work complete without verifiable support.
