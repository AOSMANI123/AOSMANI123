# "Human in the loop" can quietly become rubber-stamping

*From building the [seven-agent system](https://aosmani123.github.io/projects/agent-system/).*

Every agent in the system stages its work for a person: intake proposes fields, triage proposes a priority, scheduling proposes slots, the drafter proposes a briefing. Nothing is sent or booked automatically.

The risk I didn't expect: once the system can produce faster than people can review, reviewers start approving without reading. A review step that nobody reads is worse than no review step, because everyone believes the safety check happened.

What helped:

- **Make outputs scannable.** Surface the key fields and highlight what changed, so careful review is also fast review.
- **Rank the queue.** Triage scores point reviewers at the highest-stakes items first.
- **Add an independent check.** The coverage evaluator flags what a briefing missed, so quality doesn't rest on manual review alone.

I also rejected "auto-send for low-risk items." The definition of low-risk drifts, and one auto-sent decline to the wrong person costs more than minutes of review.
