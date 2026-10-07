# Read the failures before you trust the score

*From the first real-model run of my [LLM prompt eval harness](https://aosmani123.github.io/projects/briefing-evals/).*

The numbers looked dramatic. With a naive prompt, the model "fabricated" 10 of 12 missing fields. With a prompt that spelled out the rules, it fabricated 1. Easy headline: rules cut hallucination from 83% to 8%.

Then I read the ten failures one by one.

- **Seven weren't fabrications at all.** The model wrote `Not specified` or `TBD` instead of the exact word `UNKNOWN` that my scorer looks for. It was being honest; my scorer was being literal.
- **Three were real.** It carried last year's audience size (40,000) into this year's briefing. It put a team name in a person's name field. And it labeled the emcee who introduces a keynote as the moderator.

What I took from it:

1. **A metric can be mechanically correct and still measure the wrong thing.** My mock tests proved the scorer counted correctly. They couldn't tell me it was counting formatting as dishonesty.
2. **My safety check had a blind spot.** I flagged numbers that don't appear in the source. But 40,000 *was* in the source, describing a different event. A copied number can still be the wrong number.
3. **A failure that survives every prompt is a schema problem.** The emcee-as-moderator mistake showed up under both prompts. There's no "introducer" field, so the model reaches for the closest one.
4. **Fixes have costs.** The stricter prompt also blanked out 4 fields the source did state. Worth it for an executive briefing, but it's a trade-off to measure.

The real headline: about 3 of 12 under the naive prompt, 1 of 12 with rules, and a scorer that needed fixing more than the prompt did.
