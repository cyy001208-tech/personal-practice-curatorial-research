---
name: personal-practice-curatorial-research
description: Analyzes a person's completed project archive as a curatorial case study, requires two or three competing person interpretations before selecting a thesis, and produces an evidence-bounded practice assessment plus a strictly separated framework of Big Idea, unresolved Critical Questions, audience-facing Key Messages, evidence-bearing Theme Constellations, and optional Portfolio Chapters. Use when the user wants to understand a practitioner through past work, curate a portfolio, conduct personal-practice research, synthesize resumes/interviews/project files, compare plausible professional identities, map projects as evidence, build an exhibition-like narrative, or assess professional identity without reducing it to future-oriented idea scoring.
---

# Personal Practice Curatorial Research

Treat a body of practice as a researchable exhibition, not a stack of projects. Use finished work, process material, testimony, context, reception, and absence to build a provisional account of what the practitioner repeatedly does, how their methods change, and what their work makes knowable.

## Governing position

- Work retrospectively. Reconstruct what happened before proposing what should happen next.
- Evaluate demonstrated professional practice, not intrinsic human worth or hidden personality.
- Make every substantive judgment traceable to evidence and expose competing readings.
- Treat the portfolio as one public manifestation of prior research, not as the research itself.
- Let arrangement and juxtaposition produce insight, but never use curatorial language to disguise thin evidence.
- Preserve incomplete, contradictory, failed, collaborative, and peripheral material when it changes the interpretation.
- Follow the user's language. Translate template labels when delivering.

Read [workflow-provenance.md](references/workflow-provenance.md) before describing, publishing, or extending this skill's research-method provenance. Read [archive-and-coding.md](references/archive-and-coding.md) before opening a new corpus. Read [competitive-interpretation-protocol.md](references/competitive-interpretation-protocol.md) before proposing a person/practice thesis. Read [curatorial-methods.md](references/curatorial-methods.md) before selecting a curatorial model. Read [assessment-boundaries.md](references/assessment-boundaries.md) before evaluating the person. Read [interpretive-role-contract.md](references/interpretive-role-contract.md) before building the research framework. Read [portfolio-exhibition-grammar.md](references/portfolio-exhibition-grammar.md) when translating research into a portfolio.

## Phase 0: Freeze the case-study brief

Record:

- subject and time boundary;
- authorized local roots;
- purpose: self-understanding, portfolio, hiring, client presentation, academic/practice research, or another named use;
- primary audience and what that audience must understand;
- output scope:
  - **Research only** — assessment plus research framework;
  - **Research + portfolio** — add an exhibition script;
  - **Archive diagnostic** — identify evidence and interview gaps without final interpretation.

If no directory is named, use the current workspace only. Never broaden to the home directory. Do not install, upload, move, or rewrite source files.

## Phase 1: Form the archive

Inventory metadata before reading broadly:

```bash
python3 scripts/inventory_project_archive.py <authorized-root> --format markdown
```

The script does not extract file contents. Its default output replaces authorized
root paths with logical labels such as `root-01`; only use
`--include-absolute-roots` for a private diagnostic that will not enter a public
portfolio or repository. Treat every generated inventory as backstage research
material. Use its manifest to choose the smallest relevant corpus and identify
files requiring conversion.

Create an archive ledger with stable source IDs and exact locators. Distinguish:

- `O###` — finished object or final output;
- `P###` — process artifact, draft, sketch, decision record, or rejected route;
- `T###` — first-person testimony or interview;
- `R###` — reception, result, feedback, or external response;
- `C###` — contextual source;
- `I###` — interpretation, never evidence.

Use [archive-ledger-template.csv](assets/archive-ledger-template.csv). Do not count duplicate versions as independent support.

## Phase 2: Reconstruct each project as an event

Complete one [project-dossier-template.md](assets/project-dossier-template.md) per selected project. Reconstruct:

1. situation and stakes;
2. stated and latent problem;
3. the practitioner's actual role;
4. collaborators and distributed authorship;
5. decisive choices and rejected alternatives;
6. methods, materials, and constraints;
7. outcome and reception;
8. later reflection or afterlife;
9. contradictions and missing evidence.

Separate what the archive shows from what the practitioner remembers. Treat memory as valuable testimony, not automatic fact.

If a decisive gap cannot be filled locally, write a narrow oral-history question. Prefer questions about specific decisions over invitations to produce a polished self-narrative.

## Phase 3: Code across projects

Open-code before imposing a theme. Extract recurring:

- verbs and actions;
- problem types;
- objects, media, and materials;
- decision criteria;
- constraints and negotiation patterns;
- collaborator relationships;
- outcomes and forms of value;
- unresolved tensions;
- omissions and absences.

Promote a code into a recurring theme only when it appears in at least two projects with distinct evidence. Allow a single-project theme only when it marks a documented turning point.

Build a cross-project matrix. Keep recurrence, strength of evidence, and distinctiveness separate: repetition alone does not prove importance, and rarity does not prove originality.

## Phase 4: Generate competing person interpretations

Use [competitive-interpretation-protocol.md](references/competitive-interpretation-protocol.md) and [competitive-person-interpretations-template.md](assets/competitive-person-interpretations-template.md).

Generate `PI-A`, `PI-B`, and optionally `PI-C` before writing a preferred portrait or Big Idea. Make them differ in explanatory center, not wording alone. For each interpretation:

- state the core proposition and predicted patterns;
- identify supporting projects and precise sources;
- identify counterevidence and projects it cannot explain;
- expose every unsupported inference step;
- separate individual authorship from team outcomes;
- remove its strongest anchor project and test whether it survives.

Compare evidence coverage, unexplained remainder, contradiction cost, inference burden, specificity, temporal robustness, authorship clarity, and holdout survival. Prefer the interpretation that explains consequential evidence with the fewest unsupported assumptions, not the most attractive label.

Record one of four outcomes:

- **Select** one interpretation while preserving the strongest rival;
- **Merge** only when an evidenced relationship adds explanatory power without becoming vague;
- **Coexist** when two identities operate in different contexts, media, roles, or periods;
- **Remain unresolved** when current evidence cannot discriminate, creating a `CQ-##`.

Do not delete the losing interpretations or their strongest evidence.

## Phase 5: Construct candidate curatorial constellations

Choose one or more operational models from [curatorial-methods.md](references/curatorial-methods.md):

- **Individual mythology** — trace recurring private motifs, working rituals, and self-representations alongside everyday sources.
- **Platforms** — treat archive, interview, contextual research, comparison, and final portfolio as separate knowledge-producing stages.
- **Leitmotifs** — use recurring questions during analysis rather than preset disciplines; reserve the final `Critical Questions` label for questions still unresolved.
- **Brain** — assemble a dense nucleus of decisive objects and fragments that reveals the practice before full projects unfold.
- **Dual perspective** — compare self-account with external context, collaborator evidence, or audience reading.
- **Lumbung** — map shared resources, collective authorship, reciprocity, and what the practitioner enables for others.

Select a model because it explains the evidence, not because its name sounds prestigious. Record what the model reveals and what it risks hiding.

Assign each project one or more curatorial roles. Treat the clusters as candidates until Key Messages are fixed:

- **Anchor** — strongest evidence for the central claim;
- **Bridge** — connects themes or periods;
- **Turning point** — changes method, position, or ambition;
- **Counterexample** — resists an overly neat portrait;
- **Context/archive** — explains conditions around other work;
- **Unresolved lead** — exposes a question still in formation.

## Phase 6: Write the evidence-bounded person/practice assessment

Use [person-practice-assessment-template.md](assets/person-practice-assessment-template.md). Complete it only after the competitive-interpretation decision. Assess:

- current professional/practice position;
- recurring questions and problem territory;
- demonstrated capabilities;
- characteristic working methods;
- judgment criteria and values expressed through decisions;
- collaboration and authorship pattern;
- trajectory, continuity, and turning points;
- productive tensions, limitations, and blind spots;
- what the portfolio currently overstates or hides.

For every claim, provide source IDs, counterevidence, and confidence:

- **Strong** — repeated direct evidence across independent projects or source types;
- **Supported** — direct evidence, but limited in range;
- **Tentative** — indirect, singular, retrospective, or conflicting evidence;
- **Unknown** — insufficient evidence;
- **Interpretive proposition** — a useful reading awaiting confirmation.

Do not assign a total score to the person. If comparison is requested, use the diagnostic dimensions in [assessment-boundaries.md](references/assessment-boundaries.md), never attractiveness or human value.

## Phase 7: Build the personal research framework

Use [interpretive-role-contract.md](references/interpretive-role-contract.md) and [curatorial-research-framework-template.md](assets/curatorial-research-framework-template.md). Attach the completed `PI-#` comparison and select / merge / coexist / unresolved decision as a pre-framework method record. It is a prerequisite, not a sixth interpretive layer.

Then present the five-layer hierarchy in this exact order:

1. **Big Idea（核心命题）** — the one total argument about the person's practice;
2. **Critical Questions（关键问题）** — one to three questions the research has not fully answered;
3. **Key Messages（关键信息）** — two to four specific judgments the audience should understand after reading;
4. **Theme Constellations（主题星座）** — the projects and materials that jointly support or complicate each Key Message;
5. **Portfolio Chapters（作品集章节）** — only when requested, the reading sequence derived from the established research.

Append the project map and evidence gaps as supporting research apparatus. Do not treat them or the interpretation decision as additional message layers.

Use working IDs: `BI-01`, `CQ-##`, `KM-##`, and `TC-##`. Require `BI-01 ← KM-## ← TC-## ← source IDs` traceability. Tie every `CQ-##` to a named unresolved gap rather than a Key Message.

Derive `BI-01` from the recorded `PI-#` decision. If two interpretations coexist, make the Big Idea describe their evidenced relationship or boundary instead of flattening them into one identity.

Form the Big Idea as:

> Across **[contexts/time]**, this practitioner repeatedly **[demonstrated action/method]** to address **[problem territory]**, producing **[form of value or consequence]**, while negotiating **[central tension]**.

Do not use aspirational identity language unless the archive demonstrates it.

Before proceeding, run the anti-synonym tests in [interpretive-role-contract.md](references/interpretive-role-contract.md). Keep necessary vocabulary consistent, but ensure each layer contributes a different proposition or function.

## Phase 8: Translate into Portfolio Chapters

Run this phase only when the user requests portfolio structure. Use [portfolio-exhibition-script-template.md](assets/portfolio-exhibition-script-template.md).

Create ordered `CH-##` Portfolio Chapters that translate research conclusions into a reading sequence. Map every chapter to existing `KM-##` and `TC-##` IDs; do not invent a new research claim at the chapter layer.

Design:

- a threshold that establishes the case without biography overload;
- a compact “Brain” of decisive evidence;
- thematic rooms or acts;
- project-to-project transitions;
- archive/process displays that perform an argumentative role;
- one counterexample or friction point;
- an exit that states the present position without forcing a future promise.

Create three reading depths:

1. **Glance** — title, one claim, one decisive image;
2. **Walk-through** — section argument and project role;
3. **Study** — process, evidence, credits, constraints, and reflection.

Treat visual appeal as a mediation condition, not the criterion by which the person or project is evaluated.

## Phase 9: Run the counter-curatorial audit

Before delivery, test:

- Does every major claim have precise evidence?
- Did polished final work silence process, failure, or contradiction?
- Did self-description overpower external evidence?
- Were team outcomes misattributed to the individual?
- Did chronology get rewritten to look inevitable?
- Could the same archive support a materially different portrait?
- Were two or three genuinely different `PI-#` interpretations frozen before the Big Idea?
- Was the initially attractive interpretation tested against its strongest counterexample?
- Does the selected interpretation minimize unsupported inference rather than maximize rhetorical appeal?
- Are unexplained projects still visible?
- If interpretations were merged, did the merge add explanatory power without becoming unfalsifiably broad?
- If identities coexist, are their boundary conditions explicit?
- Does every selected project perform a distinct role?
- Are absent projects being treated as evidence without justification?
- Can the intended audience understand the Big Idea without specialist language?
- Do Big Idea, Critical Questions, Key Messages, Theme Constellations, and Portfolio Chapters each perform their exclusive role?
- Are any two layers expressing the same judgment as near-synonymous sentences?

Revise until the assessment and framework survive these questions. Preserve unresolved disagreements instead of manufacturing coherence.

## Delivery contract

Deliver, as requested:

1. corpus and method note;
2. competing `PI-A` / `PI-B` / optional `PI-C` interpretations and comparison matrix;
3. select / merge / coexist / unresolved decision with inference burden;
4. evidence-bounded person/practice assessment;
5. `BI-01` Big Idea;
6. unresolved `CQ-##` Critical Questions;
7. audience-facing `KM-##` Key Messages;
8. evidence-bearing `TC-##` Theme Constellations and project map;
9. evidence gaps and interview questions;
10. optional ordered `CH-##` Portfolio Chapters and exhibition script;
11. limitations and confidence note.

Keep a future-direction appendix separate. If the user later wants to turn the
stable research framework into a complete portfolio text specification, hand it
off to the sibling `portfolio-exhibition-editor`. If the user instead wants to
evaluate prospective ideas, use a separate future-oriented workflow; do not let
future desirability rewrite the retrospective case.

## Method lineage

This workflow synthesizes exhibition-making and curatorial-research approaches associated with documenta 5, Documenta11, documenta 12, dOCUMENTA (13), documenta 14, documenta fifteen, MoMA archive practice, V&A exhibition-making, and Smithsonian interpretive planning. See [curatorial-methods.md](references/curatorial-methods.md) for source links and the operational translation used here.
