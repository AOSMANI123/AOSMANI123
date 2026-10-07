# Layer eval checks from cheapest to most expensive

*From building the [LLM prompt eval harness](https://aosmani123.github.io/projects/briefing-evals/).*

I almost reached for an LLM judge first. Instead, the harness runs checks in order of cost:

1. **Structural (free, deterministic).** Does the output parse? Are all fields present? Are fields missing from the source marked `UNKNOWN`? A failure here is always a real failure.
2. **Containment (free, tolerant).** Normalize case, whitespace and punctuation, then check whether the expected value appears inside the actual value. This forgives the model for adding context around a correct answer.
3. **Judge (expensive).** Reserved for subjective quality like tone. Not needed for factual extraction, and it adds its own run-to-run variance.

The lesson: for extraction tasks, you can define "correct" structurally, so you don't need to pay a second model to tell you. Save the judge for questions that genuinely need judgment, and only run it on outputs that already passed the cheap layers.

Known blind spot: containment can't catch an invented detail tacked onto a correct value. That's documented rather than hidden.
