# Build the evaluator, not the generator

*From building the [coverage gap detector](https://aosmani123.github.io/projects/coverage-gap/).*

For a daily news brief, the obvious build is a tool that writes the brief. But any model can summarize ten articles, and dozens of products already do. The question nobody answered was: **did the brief cover what was actually available?**

So I built the scorer instead. It sweeps sources for a roster of names, collapses syndicated wire stories so one AP story in twelve outlets counts once, and scores any brief on what it missed.

Why this was the better bet:

- **Generation is a commodity; measurement isn't.** The gap in the market was the score, not the prose.
- **You can't improve what you can't see.** Without a coverage number, brief quality is invisible over time.
- **It works on any brief,** whether a person, an AI or both wrote it.

The catch to be honest about: the score is relative to the sources you configured. A 90 means "90% of what we could see," not "90% of everything that happened."
