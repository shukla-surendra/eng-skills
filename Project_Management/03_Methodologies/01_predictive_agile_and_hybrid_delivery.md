# Predictive, Agile, and Hybrid Delivery — Deep Dive

`../../Communication-Mastery/02_Thinking_Frameworks/12_project_management_literacy_for_engineers.md` §4 introduced these as a summary table. This chapter goes one level deeper — the roles, events, and artifacts inside Scrum specifically (since it's the delivery framework an engineer is most likely to sit inside daily), Kanban's flow metrics, SAFe's scaling mechanics, and the Agile Manifesto's actual text, which is worth knowing verbatim because it is quoted constantly and rarely read.

## Index

1. [The Agile Manifesto, Verbatim](#1-the-agile-manifesto-verbatim)
2. [Scrum in Detail: Roles, Events, Artifacts](#2-scrum-in-detail-roles-events-artifacts)
3. [Kanban in Detail: Flow and Metrics](#3-kanban-in-detail-flow-and-metrics)
4. [Scaled Agile: SAFe and the Scaling Problem](#4-scaled-agile-safe-and-the-scaling-problem)
5. [Choosing (or Reading) a Life Cycle](#5-choosing-or-reading-a-life-cycle)
6. [Glossary — Vocabulary Used in This Chapter](#6-glossary--vocabulary-used-in-this-chapter)

---

## 1. The Agile Manifesto, Verbatim

Written in 2001 by seventeen software practitioners, and the actual source of "agile" as a term — worth quoting exactly, because paraphrases routinely drop the crucial second half of each line:

> We are uncovering better ways of developing software by doing it and helping others do it. Through this work we have come to value:
>
> **Individuals and interactions** over processes and tools
> **Working software** over comprehensive documentation
> **Customer collaboration** over contract negotiation
> **Responding to change** over following a plan
>
> That is, while there is value in the items on the right, we value the items on the left more.

The last line is the part almost universally dropped in casual usage, and it matters: the manifesto does not claim documentation, process, contracts, and plans are worthless — it states a *relative* priority. "We're agile, so we don't need documentation" is a misreading of the manifesto's own explicit disclaimer, and it's worth being able to correct precisely when it's used to justify skipping something that's actually needed (a design doc, a written SOW).

Alongside the manifesto, twelve supporting principles were published; the ones with the most direct bearing on an engineer's daily practice:

| Principle (paraphrased) | Practical implication |
|---|---|
| Deliver working software frequently, from a couple of weeks to a couple of months, with a preference for the shorter timescale | Justifies short iterations over big-bang releases |
| Working software is the primary measure of progress | A demo beats a status report as evidence of progress |
| The best architectures, requirements, and designs emerge from self-organizing teams | The rationale behind giving teams design latitude rather than fully specifying upfront |
| At regular intervals, the team reflects on how to become more effective, then tunes and adjusts | The formal justification for the retrospective (§2) |

[↑ Back to index](#index)

## 2. Scrum in Detail: Roles, Events, Artifacts

Scrum is the most widely adopted agile framework and the one most engineers will encounter by default. It defines exactly three roles, five events, and three artifacts — deliberately minimal, and worth knowing precisely because deviations from this minimal set ("we do Scrum but skip retros") are extremely common and worth being able to name as deviations, not as Scrum itself.

### Roles

| Role | Owns |
|---|---|
| **Product Owner** | The backlog — what gets built and in what order, maximizing the value of the team's output |
| **Scrum Master** | The process — removing impediments, facilitating events, shielding the team from disruption, coaching Scrum practice |
| **Developers** (the term Scrum uses for all delivery-team members, regardless of discipline) | The "how" — how the work gets done within a sprint |

### Events

| Event | Purpose | Typical cadence |
|---|---|---|
| **Sprint** | The container — a fixed-length iteration (1–4 weeks, most commonly 2) inside which all other events occur | Continuous, back-to-back |
| **Sprint Planning** | The team selects backlog items and defines a sprint goal | Start of each sprint |
| **Daily Scrum (standup)** | A short, team-only sync on progress toward the sprint goal and impediments | Daily |
| **Sprint Review** | Inspect the increment with stakeholders, adapt the backlog based on feedback | End of each sprint |
| **Sprint Retrospective** | The team inspects its own process and agrees on improvements | End of each sprint, after the review |

### Artifacts

| Artifact | Definition | Commitment attached |
|---|---|---|
| **Product Backlog** | The single, ordered list of everything known to be needed in the product | **Product Goal** — the long-term objective the backlog serves |
| **Sprint Backlog** | The subset of backlog items selected for the sprint, plus the plan for delivering them | **Sprint Goal** — the single objective the sprint exists to achieve |
| **Increment** | A concrete stepping stone toward the product goal — each increment must be usable | **Definition of Done** — the shared, explicit quality standard every increment must meet |

The three "commitments" (Product Goal, Sprint Goal, Definition of Done) are frequently the missing piece when a team says Scrum "isn't working" — a sprint with a full backlog of tickets but no stated Sprint Goal has no way to judge whether the sprint actually succeeded, only whether tickets got closed, which are not the same thing.

[↑ Back to index](#index)

## 3. Kanban in Detail: Flow and Metrics

Kanban has no fixed iterations, no prescribed roles — it optimizes continuous flow through a visualized workflow, governed by explicit **Work-in-Progress (WIP) limits**. Its core metrics are worth knowing because they answer a different question than Scrum's (which asks "did we deliver the sprint commitment") — Kanban asks "how fast and how predictably does work move through the system":

| Metric | Definition | What it tells you |
|---|---|---|
| **Lead time** | Total elapsed time from when a work item is requested to when it's delivered | The customer-facing promise — how long a request actually takes end-to-end |
| **Cycle time** | Elapsed time from when work actually *starts* on an item to when it's delivered | The team's actual processing speed, excluding queue-wait time |
| **Throughput** | Number of items completed per unit of time | How much capacity the system has |
| **WIP limit** | A hard cap on how many items may be in a given workflow stage at once | The mechanism that keeps cycle time predictable — Little's Law (below) formalizes why |
| **Cumulative Flow Diagram (CFD)** | A stacked area chart showing the count of items in each workflow stage over time | Visually reveals bottlenecks — a widening band at any stage means work is piling up there |

**Little's Law**, the mathematical backbone of Kanban: *Average Cycle Time = Average WIP / Average Throughput*. The practical consequence: the only reliable way to reduce cycle time (make things finish faster) without adding capacity is to **reduce WIP** — which is precisely why "just start a sixth thing while five are already in flight" is a process violation and not merely an eagerness to help (`../../Communication-Mastery/02_Thinking_Frameworks/12_project_management_literacy_for_engineers.md` §4 makes this point operationally; this is the formula underneath it).

[↑ Back to index](#index)

## 4. Scaled Agile: SAFe and the Scaling Problem

**SAFe (Scaled Agile Framework)** and similar scaling frameworks (LeSS, Nexus, Scrum@Scale) exist to solve a problem Scrum and Kanban don't address by themselves: coordinating *many* agile teams whose work depends on each other, inside an enterprise that still runs annual/quarterly budgeting.

| SAFe concept | Definition |
|---|---|
| **Agile Release Train (ART)** | A long-lived team of agile teams (typically 50–125 people) that plans, commits, and delivers together |
| **PI (Program Increment)** | A timebox (typically 8–12 weeks / 4–6 sprints) within which an ART delivers incremental value |
| **PI Planning** | A large, cross-team event where all teams on an ART plan the upcoming PI together, explicitly surfacing and negotiating cross-team dependencies |
| **PI Objectives** | Business-value-oriented goals each team commits to for the PI, with a confidence rating |
| **Solution Train** | A coordination layer above multiple ARTs, for very large solutions |

The reason PI Planning matters disproportionately to an engineer, already flagged in `../../Communication-Mastery/02_Thinking_Frameworks/12_project_management_literacy_for_engineers.md` §4: **it is the one event where cross-team dependencies get formally committed** — missing it, or attending without having thought through one's own team's dependencies in advance, means other teams' commitments get made *about* the engineer's work without the engineer's input.

[↑ Back to index](#index)

## 5. Choosing (or Reading) a Life Cycle

A practical decision table — useful both for actually choosing an approach and for correctly interpreting why an existing project runs the way it does:

| Factor | Favors predictive | Favors agile |
|---|---|---|
| Requirements clarity | Well understood, stable | Expected to evolve, discovered through building |
| Regulatory/contractual constraints | Fixed-price, compliance-heavy, formal sign-off required | Flexible, internally funded |
| Customer/stakeholder availability | Low — can't provide continuous feedback | High — can review and redirect frequently |
| Risk of late-stage change | Low, and expensive to accommodate anyway | High, and cheap to accommodate via short iterations |
| Team's physical/organizational structure | Distributed across many vendors, formal handoffs | Co-located or well-integrated, empowered team |

Most large enterprises land on **hybrid**: predictive at the macro/program level (fixed annual budget, phase gates, formal vendor contracts) with agile execution inside individual teams. Recognizing this hybrid shape for what it is — rather than expecting either textbook waterfall or textbook Scrum and being confused when the reality matches neither — is the single most useful piece of methodology literacy an engineer can carry into a new organization, echoing the "every org runs a dialect" point from `../../Communication-Mastery/02_Thinking_Frameworks/12_project_management_literacy_for_engineers.md` §4.

[↑ Back to index](#index)

## 6. Glossary — Vocabulary Used in This Chapter

| Term/Phrase | Meaning |
|---|---|
| Agile Manifesto | The 2001 foundational statement of values behind agile software development |
| Self-organizing (team) | A team that determines its own approach to the work, rather than being directed in detail |
| Product Owner | The Scrum role owning and prioritizing the backlog |
| Scrum Master | The Scrum role owning the process and removing impediments |
| Sprint Goal | The single objective a sprint exists to achieve |
| Definition of Done | The shared, explicit quality bar every increment must meet |
| Lead time | Total elapsed time from request to delivery |
| Cycle time | Elapsed time from work start to delivery, excluding queue wait |
| Throughput | The number of items completed per unit of time |
| Little's Law | The formula: average cycle time = average WIP / average throughput |
| Cumulative Flow Diagram | A stacked area chart visualizing workflow-stage bottlenecks over time |
| Agile Release Train (ART) | A long-lived team-of-teams in SAFe that plans and delivers together |
| Program Increment (PI) | A multi-sprint timebox within which an ART delivers value |
| PI Planning | The cross-team event where an ART plans and commits to a Program Increment together |
| Backbone | (figurative) The core structural principle underlying a system |
| Textbook (adjective) | Matching the idealized, formally-described version of something exactly |

[↑ Back to index](#index)
