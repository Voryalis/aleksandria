# Aleksandria QA Log

Project: **Aleksandria — Big Data & Connectionist AI**  
Audience: university beginners with little or no AI experience.  
QA coordination owner: **@Tamer088**  
Checklist: [qa-checklist.md](qa-checklist.md)  
Requirements and open questions: [qa-requirements.md](qa-requirements.md)

## Current status

This is an updated review-log template. The teacher's supplied requirements were examined to prepare the QA documents. No actual team learning materials, GitHub repository contents, experiments, or other teams' work have been reviewed in this log.

Empty registers mean **no review results recorded**, not “no errors found.” Keep any existing genuine records when adopting this template. Do not replace completed team work with empty tables.

## 1. Material register

Add one row per material/version. Use actual names and locations. A reviewer's identity must be recorded; required peer reviews cannot be performed solely by the original author.

| ID | Stage / assignment | Material and version | Author | Reviewer | Review status | Review record |
|---|---|---|---|---|---|---|

Review status: **NOT STARTED**, **IN REVIEW**, **BLOCKED**, **REVIEWED**, or **NOT DUE**.

REVIEWED means every applicable check was performed and results were documented. It does not mean that all findings are corrected or the material is approved. NOT DUE is reserved for later-stage checks outside the current review scope.

## 2. Material review template

Copy this template beneath a heading with the real material ID. The placeholders below are instructions, not completed evidence.

- **Material ID:** `<MAT-001>`
- **Assignment and stage:** `<assignment>`
- **Title and location:** `<path / permanent link>`
- **Version and snapshot date:** `<commit SHA / file version; date>`
- **Author:** `<name or GitHub username>`
- **Reviewer:** `<name or GitHub username; different person where required>`
- **Review date:** `<YYYY-MM-DD>`
- **Applicable source/rubric:** `<source title, version, relevant section>`
- **AI usage:** `<used / not used / unknown; affected portions>`
- **Review scope:** `<specific sections, slides, question IDs, or video filenames>`

| Check IDs | Result | What was inspected or tested | Evidence / finding IDs |
|---|---|---|---|

Results: **PASS**, **ISSUE**, **BLOCKED**, **NOT CHECKED**, **N/A**, **NOT DUE**. Explain N/A, NOT DUE, and BLOCKED. Record all applicable checklist IDs; do not infer a whole section passed from one sample.

### Concrete review outcome

- **What was checked:** `<exact definition, example, answer, activity, or requirement>`
- **Method and independent source:** `<source section, calculation, steps, setup, or learner test>`
- **Observed result:** `<what actually happened or was confirmed>`
- **Correction or confirmation:** `<change made, or why the original was confirmed correct>`
- **Evidence:** `<readable excerpt, result, screenshot, or captured comparison with caption>`
- **Unresolved matters:** `<list or none>`

At least one concrete outcome is required for the Stage 1 developed material. It may be a valid confirmation with no error. Do not manufacture a defect.

### Beginner usability check

- **Participant and relationship to author:** `<who attempted it; confirm they did not write it>`
- **Task and starting information:** `<what they were given>`
- **What they understood and completed:** `<actual observation>`
- **Where they became confused:** `<actual observation or none observed>`
- **What they could explain afterward:** `<actual response or summary>`
- **Change, confirmation, and retest:** `<result>`

### Review decision

- **Review status:** `<status>`
- **Approval status:** `<NOT ASSESSED / CHANGES REQUIRED / APPROVED>`
- **Open findings and blockers:** `<IDs>`
- **Approver, date, and approved version:** `<complete only after actual approval>`
- **Project/personal log evidence location:** `<entry ID and page/section; include evidence in submitted logs>`

## 3. Question and video coverage

Use these registers to demonstrate complete coverage where the assignment requires it. A sample is not a substitute for checking every test-bank question or watching every final video.

| Question ID | Type / guide section | Author | Independent reviewer | Answer and reasoning checked | Evidence / finding | Version / date |
|---|---|---|---|---|---|---|

Test Bank totals: True/False `<actual count>` of at least 20; MCQ `<actual count>` of at least 20; open-ended `<actual count>` of at least 6. Do not enter the minimum as the actual count without counting the submitted questions.

| Final MP4 filename / version | Duration | Actual file size | Independent reviewer | Full viewing date | Learner-check result / evidence | Findings |
|---|---|---|---|---|---|---|

Record 1–8 actual videos, each at most 250 MB. Use the final compressed file, not the editing preview. Record any learner test of a selected tutorial separately from full-video viewing.

## 4. Findings register

Use sequential IDs: QA-001, QA-002, and so on. Record problems in learning materials here; teacher-instruction conflicts belong in the separate requirements register.

| ID | Material / version / location | Problem | Severity | Owner | Target date | Status | Correction / retest evidence |
|---|---|---|---|---|---|---|---|

Internal severity definitions:

- **Critical:** a fundamental error or unusable resource invalidates an essential learning result or prevents use/submission.
- **Major:** an important inaccurate explanation, failed example, misleading answer, missing required component, or unclear essential step.
- **Minor:** a localized wording or presentation problem that does not change the central result.

These are team triage labels, not teacher score deductions.

Statuses: **OPEN**, **IN PROGRESS**, **READY FOR RETEST**, **CLOSED**, **DEFERRED**, **NOT AN ISSUE**. Deferral requires a reason, decision-maker, and revisit date/condition. CLOSED requires a successful retest. “Merged” alone is not proof of correctness.

### Finding template

- **ID and title:** `<QA-001 — concise description>`
- **Material, version, exact location:** `<file/section, slide, question ID, or timestamp>`
- **Checklist ID and requirement source:** `<ID and source>`
- **Actual versus expected result:** `<specific comparison>`
- **Reproduction / supporting source:** `<steps, settings, or source location>`
- **Evidence:** `<excerpt/screenshot/result and caption>`
- **Effect on learning or submission:** `<why it matters>`
- **Severity, owner, target date, status:** `<values>`
- **Required correction and closure criterion:** `<action and observable result>`
- **Affected resources:** `<Markdown, guide, questions, slides, videos, supplements>`
- **Correction:** `<PR/commit/new version and change summary>`
- **Retest:** `<reviewer, date, version, actual result, evidence>`
- **Deferral or rejection rationale:** `<if applicable>`

## 5. Content consistency and revision tracking

Use actual filenames, section titles, slide numbers, question IDs, and video timestamps. A topic need not appear in every medium.

| Markdown topic / version | Learning goal | Guide section | Test Bank IDs | PPT slides | Video / timestamp or not selected | Consistency check / reviewer |
|---|---|---|---|---|---|---|

| Feedback / finding | Change and reason | Exact changed location | Related resources updated | Retest evidence | Remaining action |
|---|---|---|---|---|---|

This revision table supports the Stage 2 report, but the report must contain its required summary directly. A GitHub link does not replace it.

## 6. Assignment readiness

| Assignment / snapshot | Required checks and files | Open blockers / requirement questions | Package-open test | Decision / reviewer / date | Submission receipt |
|---|---|---|---|---|---|

Record **NOT READY**, **READY FOR TEAM REVIEW**, or **APPROVED FOR SUBMISSION** only on the basis of actual evidence. Record **SUBMITTED** only after the real submission, with its receipt or other confirmation in the private evidence record.

For score-based self-review, identify the exact rubric and record criterion, maximum points, proposed points, observed evidence, and improvement action. Do not convert the generic rubric's descriptive levels into an invented official numeric scale. Do not treat a 100-point video rubric as a confirmed XP conversion.

## 7. Evidence and AI-use records

Keep a concise QA summary in GitHub. Include the necessary readable evidence beside or below the relevant entries in the submitted project and personal logs. Do not publish personal logs, student IDs, private reflections, or private screenshots in a public repository.

Each significant AI-use record must show:

1. Actual date, person, and tool.
2. Purpose and relevant task.
3. Important prompts, outputs, and follow-up exchanges.
4. Actual human verification, accepted/revised/rejected content, and reasons.
5. Actual outcome, contribution, and learning.

AI-assisted drafting of these QA documents is significant use. The supplied private template can help record it, but unperformed human checks and learning reflections must remain unfilled. Each involved student writes their own account and includes evidence of their own role.

## 8. Original issue #5 completion record

- **Agreed initial materials:** `<list>`
- **Review records and versions:** `<IDs>`
- **Concrete review outcomes:** `<locations>`
- **Documented findings and confirmations:** `<IDs / locations>`
- **Unperformed applicable checks:** `<list or none>`
- **Decision on issue completion:** `<not assessed / remains open / completion condition met>`
- **Decision-maker and date:** `<fill after actual review>`

The checklist-creation task can be completed after the updated checklist is accepted. The other tasks require genuine content checks and evidence. Stage 2 and Stage 3 work is tracked separately; completing this issue is not approval of the full course project.

## Reference review — PR #14 — 2026-10-22

- **Project:** Aleksandria — Big Data & Connectionist AI.
- **Stage:** Stage 1.
- **Material:** `references.md`.
- **Version reviewed:** PR #14, commit `6197140`.
- **Author:** @loauyhf.
- **Reviewer:** @Tamer088.
- **Related issues:** #5 and #11.
- **Review status:** IN REVIEW.
- **Approval status:** CHANGES REQUIRED.
- **Scope:** Reference-list completeness and selected bibliographic metadata.
- **Method:** Read the proposed reference list and compare the IBM, Picton, and Mining of Massive Datasets entries with the source pages listed below.
- **AI assistance:** ChatGPT/Codex helped identify candidate findings, locate source pages, and draft the review. Human verification for this entry is limited to the comparisons described here.

### Evidence

- [PR #14](https://github.com/Voryalis/aleksandria/pull/14)
- [IBM article](https://www.ibm.com/think/topics/big-data)
- [Picton publisher record](https://link.springer.com/book/10.1007/978-1-349-13530-1)
- [Mining of Massive Datasets publisher record](https://www.cambridge.org/core/books/mining-of-massive-datasets/9CFE54DDEC0DA5F9558597816E5848C3)

### Findings

The identifiers below are specific to this review.

| ID | Location | Observation | Required action | Owner | Status |
|---|---|---|---|---|---|
| REF14-01 | Lines 4–11 | General notes such as “MIT open courses”, “YouTube”, and “etc” do not identify specific resources. | Replace them with traceable references or retain unselected ideas in `sorz.md`. | @loauyhf | OPEN |
| REF14-02 | Line 12 | The IBM entry lacks a direct article URL. The linked IBM page identifies Annie Badman and Matthew Kosinski as authors. | Add the direct URL and use the agreed citation format. | @loauyhf | OPEN |
| REF14-03 | Line 20 | The entry says “Springer”; the publisher record lists “Red Globe Press London” and notes an earlier Palgrave imprint. | Reconcile the publisher information with the edition actually consulted. | @loauyhf | OPEN |
| REF14-04 | Line 38 | The edition and publication year are not identified. The linked publisher page describes the third edition from 2020. | Identify the edition actually used and complete its publication details. | @loauyhf | OPEN |

### Checks not completed in this review

- Full bibliographic verification of the remaining references.
- Verification that cited passages support specific teaching claims.
- Review of developed `docs/` explanations and learning objectives.
- Reproduction of examples, calculations, or model outputs.
- Testing of instructional Markdown navigation and diagrams.
- Verification of significant AI-derived teaching claims.

These checks remain NOT CHECKED. No instructional chapter is approved by this entry.

### Follow-up and closure

- The content owner should address the findings before the Stage 1 source-list review is completed.
- @Tamer088 should inspect the revised version and record the actual retest result.
- Findings remain OPEN until the required corrections are verified.
- Claim-to-source checks should begin as soon as the relevant teaching sections are available.
- Issue #5 remains open: this reference-list review does not complete the independent review of the Stage 1 teaching material.
