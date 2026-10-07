# Ship deterministic rules before adding an LLM

*From building the [executive writing critic](https://aosmani123.github.io/projects/writing-critic/).*

An LLM could judge tone and argument quality. But the most common problems in executive writing (hedge words, passive voice, buried ledes, low data density) are detectable with plain pattern matching.

Rules first meant the tool is:

- **Fast** (milliseconds, no network call)
- **Free** to run, with no API key
- **Reproducible** (same input, same flags)
- **Auditable** (every flag traces to a rule you can read)

The LLM layer isn't ruled out. It has a trigger: add it only if user testing shows the rules miss more than 15% of real issues. Setting that bar in advance keeps "let's add AI" from being the default answer.
