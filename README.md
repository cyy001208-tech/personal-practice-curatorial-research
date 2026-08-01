# Personal Practice Curatorial Research

> Research the practice before designing the portfolio.

`personal-practice-curatorial-research` is a Codex skill for studying a
person's completed project archive as a curatorial case. It uses finished work,
process material, firsthand testimony, context, reception, and absence to
produce an evidence-bounded assessment of how the person practices.

The skill does not begin by selecting the most attractive projects. It begins
by asking what kinds of professional judgment, methods, tensions, and working
relationships recur across the archive.

## Why Competing Interpretations Come First

The first plausible description of a practitioner is often elegant, memorable,
and incomplete. To reduce confirmation bias, this skill generates two or three
competing interpretations before choosing a thesis.

For example:

- a practitioner who translates complex content;
- a designer who coordinates complex projects;
- a spatial designer guided by visual narrative.

Each interpretation is tested against the archive:

- What evidence supports it?
- Which projects can it not explain?
- How much inference does it require?
- Can two interpretations be merged?
- Should two identities remain in productive tension?

The result may be a selected interpretation, a merged account, coexisting
identities, or an explicitly unresolved comparison.

## Research Outputs

The skill keeps five roles separate:

| Output | Function |
|---|---|
| **Big Idea** | The overall argument about the person's practice. |
| **Critical Questions** | Important questions the research has not fully answered. |
| **Key Messages** | Specific judgments a reader should understand. |
| **Theme Constellations** | Projects and materials that jointly support each message. |
| **Portfolio Chapters** | An optional reading order derived from the research. |

This separation prevents the final framework from becoming a set of
near-synonymous slogans.

## Workflow

```text
Authorized project archive
        ↓
Archive ledger and project dossiers
        ↓
Two or three competing person interpretations
        ↓
Evidence and inference comparison
        ↓
Evidence-bounded practice assessment
        ↓
Big Idea, Critical Questions, Key Messages,
Theme Constellations, and optional Portfolio Chapters
```

## Inputs

The skill can work with:

- completed projects and final outputs;
- drafts, sketches, decision records, and rejected routes;
- interviews, oral testimony, and later reflection;
- client or collaborator records;
- project context and external reception;
- documented gaps, contradictions, and missing evidence.

Source files remain in place. The bundled inventory script reads metadata only
and uses logical root labels by default so that a backstage manifest does not
publish the host machine's absolute paths.

## Boundaries

This skill evaluates demonstrated professional practice. It does not:

- assess intrinsic human worth or hidden personality;
- convert memory into verified fact;
- treat collaborative output as sole authorship;
- let a future-oriented desirability score rewrite the retrospective case;
- turn every repeated motif into a permanent personal essence;
- design the finished portfolio.

## Methodological Foundations

The method adapts operations from curatorial research rather than imitating an
institutional writing style:

- [documenta 5](https://documenta.de/en/retrospective/documenta-5):
  modular personal worlds built from heterogeneous evidence;
- [Documenta11](https://documenta.de/en/retrospective/documenta11):
  research platforms kept distinct from final exhibition;
- [documenta 12](https://documenta.de/en/retrospective/documenta-12):
  recurring questions that connect heterogeneous projects;
- [dOCUMENTA (13)](https://documenta.de/en/retrospective/documenta-13):
  concentrated artifacts and provisional research notes;
- [documenta fifteen](https://documenta.de/en/retrospective/documenta-fifteen):
  relational authorship and shared infrastructure;
- [Smithsonian exhibition development guidance](https://exhibits.si.edu/wp-content/uploads/2018/04/Guide-to-Exhibit-Development.pdf):
  audience, hierarchy, Big Idea, messages, and questions;
- [MoMA Oral History](https://www.moma.org/research/archives/oral-history):
  situated testimony and archival accountability.

See
[`references/curatorial-methods.md`](./personal-practice-curatorial-research/references/curatorial-methods.md)
for the full operational translation and its blind spots.

## Handoff

This repository answers:

> What kind of practitioner is this person, and why is that reading credible?

When the research framework is stable, hand it to
[`portfolio-exhibition-editor`](https://github.com/cyy001208-tech/portfolio-exhibition-editor).
That downstream skill answers a different question:

> How should this research be selected, written, and sequenced so another
> person can understand the practice accurately?

For source-heavy literature and argument reconstruction, see
[`research-space-article-ingest`](https://github.com/cyy001208-tech/CYY).

## Repository Layout

```text
README.md
personal-practice-curatorial-research/
├── SKILL.md
├── agents/
├── assets/
├── references/
├── scripts/
└── tests/
```

## Validation

The published version passes:

- Codex skill structure validation;
- Python syntax validation;
- three privacy-focused inventory tests;
- metadata-only smoke tests for Markdown, JSON, and CSV output.

## License Status

No open-source license has been granted yet. Public visibility does not by
itself grant permission to copy, modify, or redistribute this work.
