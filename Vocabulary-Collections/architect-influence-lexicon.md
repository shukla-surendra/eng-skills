# Architect & Influence Lexicon — Deep Reservoir

> Deep-lexicon reservoir, not a drill list — see `surface-vs-deep-lexicon.md` for the
> distinction and `architect-influence-active-rotation.md` for the small, gap-sourced
> subset actually meant for weekly Active Rotation. This file exists to be read, searched,
> and pulled from — not memorized wholesale. Entries are real terms-of-art from software
> architecture, systems thinking, and engineering leadership, not invented filler.

## Index

1. [Framing & Positioning](#1-framing--positioning)
2. [Trade-offs & Cost-Benefit Reasoning](#2-trade-offs--cost-benefit-reasoning)
3. [Confidence & Calibration](#3-confidence--calibration)
4. [Systems & Structural Vocabulary](#4-systems--structural-vocabulary)
5. [Scope & Boundaries](#5-scope--boundaries)
6. [Risk & Failure Framing](#6-risk--failure-framing)
7. [Disagreement & Pushback](#7-disagreement--pushback)
8. [Alignment & Consensus-Building](#8-alignment--consensus-building)
9. [Escalation & Urgency](#9-escalation--urgency)
10. [Ownership & Accountability](#10-ownership--accountability)
11. [Delegation & Team Structure](#11-delegation--team-structure)
12. [Prioritization](#12-prioritization)
13. [Decision-Closing](#13-decision-closing)
14. [Postmortem & Retrospective Language](#14-postmortem--retrospective-language)
15. [Growth, Scale & Momentum](#15-growth-scale--momentum)
16. [Anti-Patterns & Failure Modes (named)](#16-anti-patterns--failure-modes-named)
17. [Process & Delivery Vocabulary](#17-process--delivery-vocabulary)
18. [Precision Qualifiers](#18-precision-qualifiers)

---

## 1. Framing & Positioning

| Term / Phrase | Type | Meaning | Example |
|---|---|---|---|
| North star | Phrase | The single guiding objective everything else is checked against | "Reducing time-to-first-byte is the north star for this quarter." |
| Guardrails | Word | Constraints that keep a team moving fast without needing case-by-case approval | "We don't need sign-off on every migration — the guardrails are the SLA and the rollback plan." |
| First principles | Phrase | Reasoning from fundamental truths rather than analogy or precedent | "Let's go back to first principles instead of copying what the last team did." |
| Ground truth | Phrase | The actual, verified state of reality, as opposed to what's assumed or reported | "The dashboard says green, but let's check ground truth in the logs before we close this." |
| Table stakes | Phrase | The baseline requirement to even be considered, not a differentiator | "Sub-second latency is table stakes here, not something we get credit for." |
| The crux of this is… | Phrase | Names the one issue the rest of the discussion actually hinges on | "The crux of this is whether we trust the upstream data, not the model architecture." |
| Zoom out | Phrasal verb | Step back to the broader context before diving into detail | "Let's zoom out — this isn't really a caching problem, it's a data-freshness problem." |
| Zoom in on | Phrasal verb | Narrow focus onto one specific part of a larger picture | "Zoom in on the write path — that's where the contention actually is." |
| Boil down to | Phrasal verb | Reduce a complex situation to its essential point | "It boils down to whether we can tolerate eventual consistency here." |
| Cut to the chase | Idiom | Skip preamble and get to the essential point | "Let's cut to the chase — can this handle Black Friday traffic or not." |
| The throughline is… | Phrase | The single connecting thread across several separate points | "The throughline across all three incidents is untested failover." |
| Working backward | Phrase | Starting from the desired outcome and reasoning toward the steps needed | "We're working backward from the SLA, not forward from the current architecture." |
| Anchor (a discussion) | Word | Fix a conversation to a stated reference point so it doesn't drift | "Let's anchor this to the cost target before we discuss implementation." |
| Reframe | Word | Present the same situation through a different, more useful lens | "Let me reframe this — it's not a staffing problem, it's a sequencing problem." |
| Level-set | Word | Bring everyone in a discussion to the same shared understanding before proceeding | "Quick level-set: this service has no on-call rotation today, which changes the risk calculus." |
| The lens I'd use is… | Phrase | Names the specific angle or framework being applied to evaluate something | "The lens I'd use here is blast radius, not raw complexity." |

[↑ Back to index](#index)

## 2. Trade-offs & Cost-Benefit Reasoning

| Term / Phrase | Type | Meaning | Example |
|---|---|---|---|
| Opportunity cost | Phrase | What's given up by choosing one option over the next-best alternative | "The opportunity cost of building this in-house is the quarter we don't spend on the core product." |
| Sunk cost | Phrase | Money or effort already spent that shouldn't factor into a forward-looking decision | "I know we've invested six months, but that's sunk cost — the question is what's best going forward." |
| Diminishing returns | Phrase | The point where additional effort produces proportionally less benefit | "We're past diminishing returns on manual tuning — time to automate." |
| Marginal cost | Phrase | The additional cost of one more unit, distinct from the average or fixed cost | "The marginal cost of one more tenant is nearly zero once the platform's built." |
| Zero-sum | Word | A situation where one party's gain is exactly another's loss | "This isn't zero-sum — faster builds help both teams, not just ours." |
| Pareto-optimal | Phrase | A state where no one can be made better off without making someone else worse off | "That's Pareto-optimal for now — any further gain here comes at someone else's expense." |
| Low-hanging fruit | Idiom | The easiest, most accessible wins available | "Let's clear the low-hanging fruit first — the index we're missing — before the harder rewrite." |
| Path of least resistance | Idiom | The easiest available option, not necessarily the best one | "Shipping it as a cron job is the path of least resistance, but it's not the right long-term shape." |
| Asymmetric bet | Phrase | A decision where the potential upside far outweighs the limited downside, or vice versa | "This is an asymmetric bet — worst case we lose a sprint, best case we cut latency in half." |
| Optionality | Word | The value of keeping future choices open rather than committing early | "Feature-flagging this preserves optionality if the rollout goes badly." |
| Hedge | Word (verb) | Take an action that reduces exposure to a specific risk | "We hedged against the vendor's rate limits by building a fallback path." |
| One-way door | Phrase | A decision that's hard or costly to reverse | "Deleting the old schema is a one-way door — let's be sure before we do it." |
| Two-way door | Phrase | A decision that's cheap and easy to reverse if it turns out wrong | "This is a two-way door — let's just try it and roll back if it's wrong." |
| The juice isn't worth the squeeze | Idiom | The effort required exceeds the value gained | "Rewriting this in Rust for a 5% gain — the juice isn't worth the squeeze right now." |
| Cost of delay | Phrase | The lost value that accumulates the longer a decision or delivery is postponed | "The cost of delay here is real — every week we wait, the manual process burns an engineer-day." |
| Break-even point | Phrase | The point at which cumulative benefit equals cumulative cost | "The break-even point on this migration is about four months of reduced on-call load." |

[↑ Back to index](#index)

## 3. Confidence & Calibration

| Term / Phrase | Type | Meaning | Example |
|---|---|---|---|
| Gut check | Phrase | A quick, informal test of whether something feels right, ahead of formal analysis | "Before we model this properly — gut check, does 200ms sound plausible to you?" |
| Sanity check | Phrase | A quick verification that a result isn't obviously wrong | "Let's sanity-check that number against last month's traffic before we present it." |
| Back-of-envelope | Phrase | A rough, quick estimate done without rigorous data | "Back-of-envelope, this saves us about $40k a year — I'd want a real number before committing." |
| Order of magnitude | Phrase | Correct to roughly a factor of ten, not exact | "We're off by an order of magnitude here — this can't be 10ms, it's closer to 100." |
| Ballpark | Word | An approximate figure, close enough for early discussion | "Ballpark, I'd say six weeks — I'll have a real estimate after the spike." |
| Working hypothesis | Phrase | A provisional explanation, held loosely and open to revision | "Our working hypothesis is that it's a GC pause, not a network issue." |
| Best guess | Phrase | An honest estimate made with incomplete information, flagged as such | "That's my best guess, not a confirmed number — I haven't run the actual test." |
| Confidence interval | Phrase | A range within which the true value is expected to fall, with a stated likelihood | "I'd put this at a wide confidence interval — anywhere from two to six weeks." |
| Wide error bars | Phrase | High uncertainty around an estimate | "Put wide error bars on that number — we're extrapolating from three data points." |
| Provisional | Word | Tentative, subject to change as more information arrives | "Call this a provisional plan — it'll shift once we see the load test results." |
| Directional accuracy | Phrase | Correct in trend or sign, even if the exact magnitude is uncertain | "I'm confident in directional accuracy here — costs are going up, even if I can't say by how much yet." |
| Signal vs. noise | Phrase | Distinguishing a meaningful pattern from random variation | "One bad week could be noise — let's see if it's signal before we react." |
| Overfit (to a claim) | Word | Drawing too strong a conclusion from too little data | "I'd be careful not to overfit to one incident — let's see if the pattern repeats." |
| Steady-state assumption | Phrase | An estimate that assumes current, stable conditions will continue | "That number holds under a steady-state assumption — it breaks the moment traffic spikes." |
| Confidence, stated as a percentage | Phrase | Explicitly quantifying certainty rather than using vague qualifiers | "I'd put this at 80% confidence — enough to act on, not enough to bet the roadmap." |

[↑ Back to index](#index)

## 4. Systems & Structural Vocabulary

| Term / Phrase | Type | Meaning | Example |
|---|---|---|---|
| Single point of failure | Phrase | One component whose failure takes down the whole system | "That message queue is a single point of failure — nothing else has a fallback." |
| Blast radius | Phrase | The scope of impact if something fails | "Deploying to one region first keeps the blast radius small if this goes wrong." |
| Failure domain | Phrase | A boundary within which a failure is contained and doesn't spread | "Each tenant is its own failure domain — one tenant's bad query can't starve another's." |
| Bottleneck | Word | The single constraining point that limits overall throughput | "The database connection pool is the bottleneck, not the application code." |
| Critical path | Phrase | The sequence of dependent steps that determines the minimum total time | "Provisioning the cluster is on the critical path — everything else can happen in parallel." |
| Idempotent | Word | An operation that produces the same result no matter how many times it's applied | "Retries are safe here because the handler is idempotent." |
| Eventual consistency | Phrase | A guarantee that all replicas converge to the same state, just not immediately | "We accepted eventual consistency here in exchange for lower write latency." |
| Backpressure | Word | A mechanism that slows upstream producers when a downstream consumer can't keep up | "Without backpressure, a slow consumer just gets flooded until it falls over." |
| Graceful degradation | Phrase | A system that loses functionality progressively under stress rather than failing outright | "Under load, search falls back to cached results — that's graceful degradation, not a crash." |
| Circuit breaker | Phrase | A pattern that stops calling a failing dependency to prevent cascading failure | "The circuit breaker trips after five failures, so we stop hammering a dependency that's already down." |
| Brittle | Word | Prone to breaking under small changes or unexpected conditions | "That integration is brittle — one schema change upstream and it silently fails." |
| Resilient | Word | Able to absorb failure and continue operating | "The system's resilient to a single node loss; it's not resilient to a full-AZ outage yet." |
| Source of truth | Phrase | The one authoritative place a given piece of data is considered correct | "The billing service is the source of truth for account status — nothing else should own that field." |
| Steady state | Phrase | The normal, stable operating condition of a system | "In steady state this runs at 30% CPU; it's the spikes that concern me." |
| Fan-out | Phrase | One request or event triggering many downstream calls | "The fan-out on that event is the problem — one message triggers eleven service calls." |
| Convergence | Word | Multiple components or states settling toward a single, consistent outcome | "Given enough time, all replicas converge — the question is how long that window is." |
| Chesterton's fence | Phrase | The principle of understanding why something exists before removing it | "Before we delete that check, let's apply Chesterton's fence — someone added it for a reason." |
| Conway's law | Phrase | The observation that a system's architecture mirrors the communication structure of the organization that built it | "This API is a mess because it's Conway's law — three teams, three inconsistent conventions." |
| Leaky abstraction | Phrase | An abstraction that fails to fully hide the complexity underneath it | "The ORM is a leaky abstraction here — we still have to think about the underlying query plan." |
| God object | Phrase | A single component that knows or does far too much, becoming a dependency magnet | "This class has become a god object — half the codebase touches it directly." |

[↑ Back to index](#index)

## 5. Scope & Boundaries

| Term / Phrase | Type | Meaning | Example |
|---|---|---|---|
| In scope / out of scope | Phrase | Explicitly what a piece of work does and does not cover | "Retry logic is in scope; multi-region failover is explicitly out of scope for this phase." |
| Carve-out | Word | An explicit exception made to an otherwise general rule or scope | "We made a carve-out for the legacy tenant — everyone else follows the new schema." |
| Edge case | Phrase | An input or condition at the extreme boundary of what's expected | "Empty payloads are the edge case that's actually breaking this in production." |
| Corner case | Phrase | A rare situation arising from the interaction of multiple boundary conditions at once | "It's a corner case — only happens when a retry and a timeout land in the same second." |
| Happy path | Phrase | The default, expected flow through a system when nothing goes wrong | "The happy path works fine; it's every failure branch that's untested." |
| Attack surface | Phrase | The total set of points where an unauthorized actor could try to interact with a system | "Every public endpoint we add increases the attack surface." |
| Threat model | Phrase | A structured understanding of who might attack a system and how | "Our threat model doesn't currently account for a compromised internal service." |
| Hard constraint | Phrase | A requirement that cannot be relaxed under any circumstance | "Sub-100ms p99 is a hard constraint here, not an aspiration." |
| Soft constraint | Phrase | A preference that can be traded off if circumstances require it | "Team size is a soft constraint — we'd rather not grow it, but we would if the deadline demanded it." |
| Non-negotiable | Phrase | A requirement not open to compromise | "Data residency in-region is non-negotiable for this customer." |
| Footprint | Word | The total resource or system surface something occupies | "We need to shrink this service's footprint before it can run on the edge." |
| Well-defined boundary | Phrase | A clear, explicit line of ownership or responsibility between components | "These two services don't have a well-defined boundary — that's why changes in one keep breaking the other." |
| Bleed (across a boundary) | Word | Responsibility or logic improperly crossing from one component into another | "Business logic has bled into the presentation layer here." |
| Contract (between services) | Word | The agreed interface and guarantees two components rely on | "As long as we honor the contract, the consumer doesn't care how we implement it." |
| Backward compatible | Phrase | A change that doesn't break existing consumers of an interface | "This has to stay backward compatible — we can't assume every client has upgraded." |

[↑ Back to index](#index)

## 6. Risk & Failure Framing

| Term / Phrase | Type | Meaning | Example |
|---|---|---|---|
| Worst-case scenario | Phrase | The most severe plausible outcome, used to bound planning | "Worst-case scenario, we lose an hour of writes — that's what the backup interval buys us." |
| Failure mode | Phrase | A specific way a system can fail | "We've tested the network-partition failure mode but not the slow-disk one." |
| Mitigate | Word | Reduce the severity or likelihood of a risk, without necessarily eliminating it | "We can't eliminate the risk, but we can mitigate it with a shorter timeout." |
| Contain (a risk) | Word | Limit a risk's spread or impact rather than remove it entirely | "The goal isn't to prevent every bad deploy — it's to contain the blast radius when one happens." |
| Exposure | Word | The degree to which something is vulnerable to a given risk | "Our exposure here is really just the one unpatched dependency." |
| Tail risk | Phrase | A low-probability but potentially severe risk, at the extreme end of a distribution | "This is a tail risk — unlikely, but if it hits, it's a full outage." |
| Known unknown | Phrase | Something we're aware we don't know | "Latency under 10x load is a known unknown — we haven't tested it." |
| Unknown unknown | Phrase | A risk we aren't even aware exists yet | "The real danger in migrations is usually the unknown unknowns, not the risks on the list." |
| Residual risk | Phrase | The risk that remains after mitigations have been applied | "Even with retries and circuit breakers, there's residual risk from a full regional outage." |
| Risk appetite | Phrase | How much risk an organization or team is willing to accept for a given return | "Our risk appetite for this launch is low — it's customer-facing and irreversible." |
| Blast door | Phrase | A deliberate mechanism that stops a failure from propagating further | "Feature flags act as a blast door — we can cut off the bad code path without a redeploy." |
| Canary (release) | Word | Releasing a change to a small subset first, to detect problems before full rollout | "We'll canary this to 1% of traffic before rolling it out fully." |
| Rollback plan | Phrase | A pre-defined way to revert a change if it causes problems | "No deploy goes out without a tested rollback plan." |
| Chaos engineering | Phrase | Deliberately injecting failure into a system to test its resilience under controlled conditions | "We found this weakness through chaos engineering, not through a postmortem." |
| Single-threaded owner | Phrase | One person unambiguously accountable for a given outcome or system | "This incident needs a single-threaded owner, not a committee." |

[↑ Back to index](#index)

## 7. Disagreement & Pushback

| Term / Phrase | Type | Meaning | Example |
|---|---|---|---|
| I'd challenge the premise | Phrase | Disagrees with the underlying assumption, not just the conclusion | "I'd challenge the premise that we need real-time here at all." |
| Devil's advocate | Idiom | Deliberately arguing an unpopular position to stress-test the prevailing one | "Let me play devil's advocate for a second — what if the vendor just isn't reliable enough?" |
| I don't think that follows | Phrase | Rejects a stated conclusion as not logically supported by its reasoning | "I don't think that follows — lower latency doesn't necessarily mean higher conversion." |
| That's a false choice | Phrase | Rejects a proposed either/or framing as artificially limited | "That's a false choice — we can ship the MVP and start the rewrite in parallel." |
| Counterpoint | Word | A point that opposes or complicates a previous argument | "Counterpoint: that approach works today, but it doesn't scale past our next order of magnitude." |
| I'd flag a risk here | Phrase | Raises a specific concern without necessarily blocking the decision | "I'd flag a risk here — we're coupling two teams' release schedules." |
| Respectfully, I disagree | Phrase | States clear disagreement while explicitly preserving goodwill | "Respectfully, I disagree — I think this adds complexity we don't need yet." |
| Devil's in the details | Idiom | The overall plan seems fine, but the specifics could still cause real problems | "The plan looks good at a high level — the devil's in the details of the migration order." |
| That doesn't hold up under… | Phrase | States precisely the condition under which a claim stops being true | "That doesn't hold up under concurrent writes." |
| I want to stress-test this | Phrase | Signals intent to probe an idea rigorously, not merely to object | "Before we commit, I want to stress-test this against our worst month of traffic." |
| Playing devil's advocate aside… | Phrase | Transitions from an exploratory objection back to a genuine position | "Playing devil's advocate aside, I do actually think this is the right call." |
| I'm not fully bought in | Phrase | Signals partial, honest reservation without outright blocking | "I'm not fully bought in yet — I'd like to see the numbers from the pilot first." |
| Let's pressure-test that | Phrase | Proposes actively probing an idea for weaknesses before relying on it | "Let's pressure-test that assumption before it goes into the roadmap." |
| I'd rather we not conflate X and Y | Phrase | Objects to two distinct issues being treated as one | "I'd rather we not conflate the outage with the underlying architecture decision — they're separate conversations." |
| Fair, but… | Phrase | Concedes a point while still holding a distinct position | "Fair, but that only addresses the read path, not the write path." |

[↑ Back to index](#index)

## 8. Alignment & Consensus-Building

| Term / Phrase | Type | Meaning | Example |
|---|---|---|---|
| Get buy-in | Phrase | Secure genuine agreement and support, not just formal sign-off | "We need buy-in from the security team before this goes further, not just a checkbox." |
| Socialize (an idea) | Word | Informally share a proposal with stakeholders before a formal decision, to surface objections early | "Let's socialize this with the platform team before we bring it to the review." |
| Common ground | Phrase | Points of agreement that can be built on despite other disagreements | "We don't agree on the timeline, but there's common ground on the approach." |
| Meet in the middle | Idiom | Reach a compromise between two differing positions | "Let's meet in the middle — phased rollout instead of either big-bang or indefinite delay." |
| Rally behind | Phrasal verb | Unite in support of a shared decision or direction | "Once the decision's made, I need the team to rally behind it, even the folks who disagreed." |
| Disagree and commit | Phrase | Voice disagreement openly, then fully support the decision once it's made | "I'll disagree and commit here — I still think X was better, but I'm behind Y now." |
| Broad consensus | Phrase | Agreement across most, though not necessarily all, stakeholders | "We have broad consensus on the approach, even if a couple of details are still contested." |
| Read the room | Idiom | Accurately gauge the mood or receptiveness of a group before speaking or acting | "I read the room and decided this wasn't the meeting to push the migration timeline." |
| Bring people along | Phrase | Ensure stakeholders understand and support a decision, not just receive it after the fact | "We moved fast but didn't bring people along — that's why there's pushback now." |
| Pre-wire | Word | Have private conversations before a group meeting to avoid surprises and build support | "I pre-wired this with the two skeptics before the design review." |
| Common understanding | Phrase | A shared, verified interpretation of a situation across a group | "Let's make sure we have a common understanding of 'done' before we start." |
| Alignment check | Phrase | A deliberate pause to confirm everyone still agrees before proceeding | "Quick alignment check before we go further — are we still optimizing for latency over cost?" |
| Win-win | Idiom | An outcome that genuinely benefits multiple parties, not a forced compromise | "Caching at the edge is a win-win — faster for users, cheaper for us." |
| Build coalition | Phrase | Deliberately gather support from multiple stakeholders ahead of a decision | "This needs a coalition across three teams before it can move, not just our approval." |
| Table the discussion | Idiom | Formally postpone a topic rather than resolve it now | "Let's table this until we have the cost data — no point deciding blind." |

[↑ Back to index](#index)

## 9. Escalation & Urgency

| Term / Phrase | Type | Meaning | Example |
|---|---|---|---|
| Time-sensitive | Word | Requiring action within a limited window, or losing value | "This is time-sensitive — the vendor's pricing changes at the end of the month." |
| Blocking issue | Phrase | A problem that prevents further progress until resolved | "This is a blocking issue for the release, not a nice-to-have fix." |
| Raise the alarm | Idiom | Formally flag a serious concern to get attention and action | "I'd rather raise the alarm now than explain in a postmortem why I didn't." |
| Escalate | Word | Formally bring an issue to a higher level of authority for resolution | "I'm escalating this — we've been blocked for two days with no response." |
| Sound the alarm early | Phrase | Deliberately raise a concern well before it becomes critical | "Better to sound the alarm early on the capacity issue than scramble in week eleven." |
| Not a drill | Idiom | Emphasizes that a situation is genuinely serious, not hypothetical | "This is not a drill — we're actively losing data right now." |
| All hands on deck | Idiom | A situation serious enough to require everyone's immediate attention | "This is an all-hands-on-deck situation until the outage is resolved." |
| Time bomb | Idiom | A latent problem that will eventually cause serious harm if left unaddressed | "That unbounded queue is a time bomb — it's fine until it isn't." |
| Ticking clock | Idiom | Emphasizes a deadline or worsening condition that limits available time | "There's a ticking clock here — the certificate expires in nine days." |
| Priority zero | Phrase | The highest possible priority, above all other current work | "This is priority zero — everything else waits." |
| Stop the bleeding | Idiom | Take immediate action to prevent a bad situation from getting worse, before fixing it properly | "First, stop the bleeding with a rate limit; the real fix comes after." |
| Fire drill | Idiom | An urgent, disruptive scramble, often avoidable with better preparation | "This became a fire drill because nobody tested the runbook beforehand." |
| Buy time | Idiom | Take an action that delays a problem to allow more time for a proper solution | "The workaround buys us time until the real fix ships next sprint." |
| Runway (remaining) | Word | The amount of time or resource available before a constraint is hit | "We have about two weeks of runway before the disk fills up." |
| Red flag | Idiom | An early warning sign of a serious underlying problem | "The retry count doubling week over week is a red flag." |

[↑ Back to index](#index)

## 10. Ownership & Accountability

| Term / Phrase | Type | Meaning | Example |
|---|---|---|---|
| Own (a problem/system) | Word | Hold clear, accountable responsibility for something, not just involvement | "I own this decision — if it's wrong, that's on me, not the team." |
| Accountable vs. responsible | Phrase | The distinction between who answers for an outcome and who does the work | "I'm accountable for the launch; the on-call engineer is responsible for the pager." |
| Single-threaded owner | Phrase | (see §6) One unambiguous owner for a decision or system | "Every incident needs a single-threaded owner from minute one." |
| DRI (directly responsible individual) | Phrase | The one person explicitly accountable for a task or decision | "Who's the DRI on this migration? It shouldn't be ambiguous." |
| Skin in the game | Idiom | Having a genuine personal stake in the outcome of a decision | "I want the person proposing this to have skin in the game — own the on-call for it too." |
| Take the hit | Idiom | Willingly accept blame or consequence for an outcome | "I'll take the hit for this — I approved the change." |
| Fall on my sword | Idiom | Voluntarily accept full blame, often to protect others or move a situation forward | "I'll fall on my sword for the estimate being wrong — the team executed exactly as planned." |
| Buck stops here | Idiom | Ultimate accountability rests with the speaker, with no further deflection | "The buck stops here — I signed off on the deploy." |
| Hold the line | Idiom | Maintain a firm position or standard despite pressure to relax it | "We need to hold the line on code review standards, even under deadline pressure." |
| Answer for (a decision) | Phrase | Be prepared to justify a decision to others afterward | "I'm comfortable answering for this decision to the VP if it comes up." |
| Ownership boundary | Phrase | The explicit line marking what one team or person is and isn't accountable for | "The ownership boundary here is unclear — that's the actual root cause." |
| Bus factor | Phrase | The number of people who could leave before a project is seriously endangered | "The bus factor on this service is one — that's the real risk, not the code quality." |

[↑ Back to index](#index)

## 11. Delegation & Team Structure

| Term / Phrase | Type | Meaning | Example |
|---|---|---|---|
| Delegate (a decision) | Word | Formally hand off authority over a decision to someone else | "I'm delegating the vendor choice to the team — I trust the evaluation." |
| Empower | Word | Give someone the authority and confidence to act without needing approval each time | "Empower the on-call engineer to roll back without waiting for a sign-off." |
| Two-pizza team | Idiom | A team small enough to be fed by two pizzas — a heuristic for keeping teams small and autonomous | "Keep this a two-pizza team; past that, coordination cost outweighs the extra hands." |
| Autonomy vs. alignment | Phrase | The tension between letting teams decide independently and keeping the organization coordinated | "This is an autonomy-vs-alignment tradeoff — full autonomy here means inconsistent APIs elsewhere." |
| Decision rights | Phrase | Explicit clarity over who has the authority to make a given decision | "The decision rights here were never clear — that's why three teams built the same thing." |
| Span of control | Phrase | How many people or systems one person can effectively be accountable for | "That's too wide a span of control for one lead — split it." |
| RACI | Word | A framework naming who's Responsible, Accountable, Consulted, and Informed for a task | "Let's write a quick RACI before this project starts, not after the confusion begins." |
| Hands-off | Word | A management style that avoids direct intervention once direction is set | "I'll be hands-off on implementation — just keep me posted on blockers." |
| Trust but verify | Idiom | Extend autonomy while still confirming outcomes, rather than either micromanaging or ignoring | "Trust but verify — you don't need my sign-off, but show me the results after." |
| Servant leadership | Phrase | A leadership style focused on removing obstacles for the team rather than directing it | "My job here is servant leadership — clear the blockers, not dictate the solution." |

[↑ Back to index](#index)

## 12. Prioritization

| Term / Phrase | Type | Meaning | Example |
|---|---|---|---|
| Sequencing | Word | The deliberate order in which work is done, distinct from its overall scope | "This is a sequencing problem, not a scope problem — we just need to do the migration first." |
| P0 / P1 / P2 | Phrase | A tiered priority scale, P0 being the most urgent | "This is a P1 — important, but it can wait for the P0 to close first." |
| Deprioritize | Word | Deliberately lower something's priority, without necessarily abandoning it | "We're deprioritizing the redesign to focus on the reliability work this quarter." |
| Not now, not never | Phrase | Explicitly distinguishes a deferred idea from a rejected one | "This is a not-now-not-never — good idea, wrong quarter." |
| Highest-leverage | Phrase | Producing the largest effect relative to the effort required | "Fixing the flaky test suite is the highest-leverage thing we can do this sprint." |
| Impact vs. effort | Phrase | A framework for prioritizing by weighing expected benefit against required work | "On an impact-vs-effort basis, this is a clear yes — small change, large payoff." |
| MoSCoW (must/should/could/won't) | Phrase | A prioritization framework categorizing requirements by necessity | "Under MoSCoW, offline support is a 'could,' not a 'must,' for this release." |
| Ruthless prioritization | Phrase | Aggressively cutting lower-value work to focus resources on what matters most | "This quarter needs ruthless prioritization — we can't half-fund five things." |
| Sequencing risk | Phrase | The risk introduced specifically by the order tasks are done in, not their content | "There's sequencing risk here — if we migrate before the read path's ready, we lose data." |
| Trade off scope for time | Phrase | Deliberately reduce what's delivered in order to meet a fixed deadline | "We're trading off scope for time — the deadline's fixed, so the feature list has to shrink." |

[↑ Back to index](#index)

## 13. Decision-Closing

| Term / Phrase | Type | Meaning | Example |
|---|---|---|---|
| Landing the decision | Phrase | Bringing a discussion to a definitive, actionable conclusion | "Let's land the decision today — we can't keep this open another week." |
| Bias for action | Idiom | A preference for making a reasonable decision quickly over analyzing indefinitely | "I'd rather have a bias for action here — we can course-correct later." |
| Default to yes / default to no | Phrase | A stated starting stance a decision must actively argue away from | "I default to no on new dependencies unless there's a clear reason." |
| Commit and iterate | Phrase | Make a decision now with the explicit intent to revise it as more is learned | "Let's commit and iterate rather than wait for a perfect plan." |
| Close the loop | Idiom | Explicitly confirm a decision or action has been completed and communicated | "Can you close the loop with the customer once the fix ships?" |
| Path forward | Phrase | The specific, agreed next steps following a decision | "Here's the path forward: canary this week, full rollout next." |
| Make the call | Idiom | Take responsibility for deciding, especially under uncertainty | "Someone has to make the call — I'll make it." |
| Final say | Phrase | The authority whose decision is binding once made | "You have final say on the schema — I'll defer to that." |
| No more litigating this | Idiom | Signals a decision is closed and shouldn't be reopened without new information | "Unless something material changes, I'd like to stop litigating this decision." |
| Lock it in | Idiom | Formally finalize a decision so it can be acted on | "Let's lock this in before the planning meeting — no more changes after today." |

[↑ Back to index](#index)

## 14. Postmortem & Retrospective Language

| Term / Phrase | Type | Meaning | Example |
|---|---|---|---|
| Blameless postmortem | Phrase | A retrospective focused on systemic causes, not individual fault | "This is a blameless postmortem — we're here to fix the process, not assign blame." |
| Five whys | Phrase | A technique of repeatedly asking "why" to trace a problem to its root cause | "Running the five whys here, the real root cause is a missing alert, not the bad deploy." |
| Root cause | Phrase | The fundamental underlying reason for a problem, distinct from its symptoms | "The timeout was the symptom; the root cause was an unbounded retry loop." |
| Contributing factor | Phrase | A condition that made a failure worse or more likely, without being the sole cause | "Lack of monitoring was a contributing factor, even though it didn't cause the outage directly." |
| Action item | Phrase | A specific, owned, trackable follow-up task from a review | "Every postmortem needs concrete action items, not just a narrative." |
| Corrective action | Phrase | A specific change made to prevent a problem from recurring | "The corrective action here is adding a circuit breaker, not just documenting the risk." |
| Lessons learned | Phrase | The generalizable insight extracted from a specific incident | "The lessons learned apply beyond this one service — we should audit for the same pattern elsewhere." |
| Systemic issue | Phrase | A problem rooted in process or structure, not one person's mistake | "This wasn't an individual error — it's a systemic issue with how we handle config changes." |
| Near miss | Phrase | An incident that almost happened but was caught in time | "This was a near miss — worth a light postmortem even without customer impact." |
| Timeline of events | Phrase | A precise, chronological account of what happened during an incident | "Let's reconstruct the timeline of events before we speculate about cause." |

[↑ Back to index](#index)

## 15. Growth, Scale & Momentum

| Term / Phrase | Type | Meaning | Example |
|---|---|---|---|
| Inflection point | Phrase | A moment where the trend of a system or metric changes direction or rate | "We hit an inflection point around 10k users — the old architecture stopped holding." |
| Hockey-stick growth | Idiom | A pattern of slow growth followed by a sudden, sharp increase | "If adoption follows hockey-stick growth, this needs to scale by Q3, not next year." |
| Flywheel | Word | A self-reinforcing cycle where each part of a system makes the next part easier | "Better data improves the model, which improves the product, which brings more data — that's the flywheel." |
| Network effect | Phrase | A system that becomes more valuable as more people or nodes use it | "This has real network effects — more integrations make every existing one more valuable." |
| Economies of scale | Phrase | Per-unit cost decreasing as overall volume increases | "At this volume we finally get economies of scale on the infrastructure cost." |
| Critical mass | Phrase | The minimum size or adoption needed for something to become self-sustaining | "We need critical mass on the platform side before third parties will build on it." |
| Compounding | Word | An effect that builds on itself over time, producing accelerating returns | "Tech debt paydown compounds — every sprint we delay it, the next one costs more." |
| Momentum | Word | The accumulated force behind an initiative that makes continuing easier than stopping | "We have real momentum on this migration — I don't want to lose it by pausing now." |
| Plateau | Word | A period where growth or improvement levels off after a period of increase | "Performance gains have plateaued — we've hit the limits of this approach." |
| S-curve | Phrase | A growth pattern that starts slow, accelerates, then levels off | "Adoption is following the usual S-curve — we're still in the acceleration phase." |

[↑ Back to index](#index)

## 16. Anti-Patterns & Failure Modes (named)

| Term / Phrase | Type | Meaning | Example |
|---|---|---|---|
| Bikeshedding | Word | Spending disproportionate time debating a trivial issue while ignoring the important one | "We spent forty minutes bikeshedding the naming convention and five on the actual architecture." |
| Yak-shaving | Idiom | Getting pulled into an unrelated chain of tasks to accomplish an original, simple goal | "This turned into yak-shaving — fixing a typo led to upgrading three dependencies." |
| Analysis paralysis | Idiom | Being unable to decide due to excessive deliberation or data-gathering | "We're in analysis paralysis — we have enough data to decide, we just need to decide." |
| Scope creep | Phrase | The gradual, unplanned expansion of a project's requirements | "This is textbook scope creep — we added four 'small' things and the deadline's the same." |
| Gold-plating | Word | Adding unnecessary features or polish beyond what was actually required | "That's gold-plating — the requirement was correctness, not a configurable retry strategy." |
| Not-invented-here syndrome | Phrase | A bias against adopting external solutions in favor of building everything internally | "Rejecting the existing library for this is not-invented-here syndrome, not a technical argument." |
| Death by a thousand cuts | Idiom | Gradual, cumulative harm from many small issues rather than one large one | "No single decision caused this — it's death by a thousand small compromises." |
| Whack-a-mole | Idiom | Repeatedly fixing symptoms as they appear without addressing the underlying cause | "We're playing whack-a-mole with these alerts — the root cause is still there." |
| Boiling the ocean | Idiom | Attempting a task so broad in scope that it becomes practically unachievable | "Let's not boil the ocean — scope this to one service first." |
| House of cards | Idiom | A structure that appears stable but collapses entirely if one part fails | "This integration is a house of cards — one API change upstream and everything breaks." |
| Premature optimization | Phrase | Optimizing a part of a system before confirming it's actually a bottleneck | "This is premature optimization — we haven't even profiled it yet." |
| Technical bankruptcy | Phrase | A state where accumulated technical debt makes further development prohibitively costly | "We're close to technical bankruptcy on this module — every change now takes three times as long." |
| Cargo culting | Idiom | Copying the surface form of a practice without understanding why it works | "Adding that config without understanding it is cargo culting, not engineering." |
| Big ball of mud | Idiom | A system with no discernible architecture, grown haphazardly over time | "This module's become a big ball of mud — nobody can say what owns what anymore." |
| Strangler fig pattern | Phrase | Gradually replacing a legacy system by routing traffic to a new one piece by piece | "We're using the strangler fig pattern — new traffic goes to the rewrite, old traffic stays until it's fully replaced." |

[↑ Back to index](#index)

## 17. Process & Delivery Vocabulary

| Term / Phrase | Type | Meaning | Example |
|---|---|---|---|
| MVP (minimum viable product) | Phrase | The smallest version of something that still delivers real, testable value | "This is an MVP — it doesn't need every edge case handled to prove the concept." |
| Walking skeleton | Idiom | A minimal end-to-end implementation that proves the architecture works, before adding features | "Let's build a walking skeleton first — thin, but touching every layer of the system." |
| Spike (a technical spike) | Word | A short, time-boxed investigation to answer a specific technical question | "Let's do a two-day spike before committing to this approach." |
| Vertical slice | Phrase | A thin implementation cutting through every layer of a system, rather than building one layer fully first | "Ship a vertical slice first — one feature, end to end, not the whole data layer up front." |
| Feature flag | Phrase | A toggle that controls whether a piece of functionality is active, independent of deployment | "Ship it behind a feature flag so we can turn it off without a redeploy." |
| Dark launch | Phrase | Deploying a feature to production without exposing it to users, to test real-world behavior | "We dark-launched this for a week to check performance before anyone could see it." |
| Blue-green deployment | Phrase | Running two identical environments and switching traffic between them for zero-downtime releases | "Blue-green deployment means the rollback is just flipping traffic back, not a redeploy." |
| Kill switch | Phrase | A mechanism to immediately disable a feature or system in an emergency | "Every new integration needs a kill switch before it touches production traffic." |
| Runbook | Word | A documented, step-by-step procedure for handling a specific operational situation | "If this isn't in the runbook, whoever's on call at 3am won't know what to do." |
| Definition of done | Phrase | The explicit, agreed criteria that must be met before work is considered complete | "Tests passing isn't the definition of done here — it also needs a runbook entry." |
| Shift left | Phrase | Moving a concern (testing, security, review) earlier in the development process | "We're shifting security review left — into design, not after implementation." |
| Fail fast | Idiom | Designing a system or process to surface errors immediately rather than letting them propagate | "Fail fast here — better a loud error at startup than a silent bad state in production." |
| Dogfooding | Word | Using your own product internally before or alongside external release | "We're dogfooding this internally for two weeks before it goes to customers." |
| Technical debt | Phrase | The implied future cost of choosing an expedient solution now over a better one | "This isn't free — it's technical debt we're consciously taking on to hit the date." |
| Paved road | Phrase | A well-supported, recommended default path that's easier to follow than to deviate from | "We want this to be the paved road — the default choice, not just an option buried in docs." |

[↑ Back to index](#index)

## 18. Precision Qualifiers

| Term / Phrase | Type | Meaning | Example |
|---|---|---|---|
| Strictly speaking | Phrase | Introduces a technically precise clarification, often narrower than common usage | "Strictly speaking, this isn't a cache miss — it's a cold start." |
| In practice | Phrase | Distinguishes how something actually behaves from how it's theoretically expected to | "In theory this scales linearly; in practice, contention kicks in well before that." |
| All else being equal | Phrase | Isolates one variable's effect by assuming everything else stays constant | "All else being equal, the smaller payload wins — but network conditions vary." |
| On balance | Phrase | Weighing multiple factors together to reach an overall judgment | "On balance, I think the managed service is still the right call, even with the cost." |
| Narrowly | Word | Applies to a specific case only, not to be generalized | "That's true narrowly, for this one dataset — I wouldn't generalize it yet." |
| To a first approximation | Phrase | An intentionally simplified statement, accurate enough for the current purpose | "To a first approximation, cost scales with request volume — the details matter less at this stage." |
| Modulo (some factor) | Word | Setting aside a specific factor for the purpose of the current statement | "Modulo the auth changes, this is basically the same design as before." |
| With the caveat that… | Phrase | States a claim while explicitly flagging its limitation | "This works, with the caveat that it hasn't been tested past 10k concurrent users." |
| Insofar as | Phrase | Limits a claim to the specific extent it's actually true | "It's correct insofar as the input is well-formed — malformed input isn't handled yet." |
| More precisely | Phrase | Introduces a sharper, less ambiguous restatement of a prior claim | "It's not down — more precisely, it's returning stale data." |

[↑ Back to index](#index)
