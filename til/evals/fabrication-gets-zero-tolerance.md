# Fabrication gets zero tolerance; recall gets a margin

*From building the [LLM prompt eval harness](https://aosmani123.github.io/projects/briefing-evals/).*

LLM output changes run to run. If an eval gate fails on that natural variance, people stop trusting it and turn it off. If it's too loose, it misses real regressions.

What worked was treating failure types differently instead of picking one tolerance number:

- **Fabrication: zero tolerance.** Any increase in invented values fails the gate. A guess in an executive briefing is worse than a blank, so this check can't flex.
- **Recall: baseline minus 2 fields.** Re-running the same prompt on the same cases moves recall by about one field, so a margin of two absorbs noise without hiding a real drop.
- **New numbers not in the source: always flagged.** A number the source never contained is suspicious every time.

The lesson: a single "pass if 90% correct" threshold treats a formatting slip and a hallucination as the same miss. They aren't. Decide which failures are allowed to wobble and which are not.
