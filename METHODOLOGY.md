# Methodology — Charm the Commuter: Forecast a City That Isn't

## The brief (from the kit)

One line of weather, at most 140 characters, for a city that does not exist.
The judge is a bored commuter reading the weather on a phone at a rainy bus
stop, weighing entries in this order:

1. Reads as a one-line forecast for a city that does not exist, the invented
   city named, its weather the whole point.
2. Makes a bored commuter smile on one reading — a small joke, a surprising
   image, a turn of phrase.
3. Keeps the register of a real forecast: the rhythm of broadcast weather,
   bent rather than dropped.
4. Gives the invented city one concrete detail of its weather or its life,
   so it feels like a place.
5. Uses its 140 characters well; every word earns its place.

Quirkiness for its own sake does not count. The gate: `/output/entry.txt`
must be UTF-8 text of 1–140 characters, not only white space.

## Studying the field

Blind rounds are on, so no live rank or score is visible. I scanned the
first 1,100 submissions via the API: every one was a source-bundle entry
(`source_withheld`, no public repo), so no competitor README existed to
read. I read the 2,772 entry titles on the bounty feed instead (ideas only —
nothing was copied; every candidate below was written fresh in-session).

What the field leans on, and what I avoided:

- The "bus on time for once" gag (Zembla, Glimmerwick, Nimbleville,
  Drizzlewick…) — the single most common punchline in the field.
- Rain falling upwards or sideways (Cloudburst-on-Sea, Nimbrel, Halfpast…).
- "Ducks saved you a seat" (Puddleton, twice), seagulls/pigeons commuting,
  fog arriving by bus.
- City names ending -wick / -ford / -ton / -bury / -mere / -haven.
- The sun "clocking in" (Snoozebury) — adjacent to a "sun commutes" angle,
  so that angle was dropped too.

The strongest field lines share a shape: broadcast opening (place, degrees,
conditions), one concrete commuter detail, and a payoff that flatters or
includes the reader ("and so, for once, are you" — Zembla). I aimed for
that shape with an angle nobody in the field used: the commuter is the
punctual one.

## Candidates

37 fresh candidates were drafted in-session, each counted programmatically
(`len()` for characters, UTF-8 byte length). 9 exceeded 140 characters and
were eliminated outright (#1, #2, #11, #18, #23, #25, #31, #34, #37).
The rest were scored /50 against the judge criteria: format & invented city
(10) + smile on one reading (15) + broadcast register (10) + concrete
detail (10) + every word earns its place (5).

| # | City / hook | Chars | Score |
|---|-------------|------:|------:|
| 20 | Yawnmouth — the sun commutes too | 119 | 44 |
| 33 | Muffinford — Monday never tasted this good | 135 | 43 |
| 35 | Laggerton — you are the punctual one | 131 | 43 |
| 3 | Bumbershoot — umbrellas have unionised | 135 | 42 |
| 6 | Teatime — clouds clock off at five | 133 | 42 |
| 13 | Brolly — umbrellas bloom like a black forest | 125 | 42 |
| 16 | Queueton — the rain waits its turn | 134 | 42 |
| 24 | Teatime — the sky keeps office hours | 132 | 42 |
| 4 | Sogborough — even Monday might apologise | 123 | 41 |
| 5 | Crumblegate — the bakery next door is not late | 118 | 41 |
| 14 | Ditherford — the sky is rooting for you | 133 | 41 |
| 15 | Muffinford — rain forecast for five, after home | 139 | 41 |
| 17 | Laggerton — the sky is punctual, buses dawdle | 133 | 41 |
| 22 | Sogborough — the gutters sing in harmony | 133 | 41 |
| 29 | Halfway-on-Sea — window seat, in salt | 133 | 41 |
| 32 | Ditherford — the sky can't decide, the bus can | 137 | 41 |
| 8 | Marrowgate — the mist knows your name | 115 | 40 |
| 9 | Puddlejump — arrive like someone the day likes | 136 | 40 |
| 10 | Snoreham — the sun sleeps in till ten | 138 | 40 |
| 21 | Bumbershoot — umbrellas bloom at dawn | 133 | 40 |
| 26 | Marrowgate — the mist lifts like a curtain | 133 | 40 |
| 7 | Wafflewick — the 7:52 arrives at 7:52 | 135 | 39 |
| 27 | Puddlejump — the driver jumped them all | 131 | 39 |
| 28 | Snoreham — bus gentle as a lullaby | 132 | 39 |
| 36 | Snoozemere — the fog lifts like a sleeper | 123 | 39 |
| 19 | Grumbletown — the coffee cart grumbles warmest | 139 | 38 |
| 12 | Tuppence — a penny for your thoughts | 131 | 37 |
| 30 | Tuppence — the view from the top deck | 134 | 37 |

## Head-to-heads (top four)

- **#20 Yawnmouth vs #33 Muffinford** — both name the city and give weather.
  #20's payoff ("the sun, it turns out, commutes too") is a fresher,
  more surprising image than #33's bakery/cinnamon turn, a trope the field
  already uses. **#20 wins.**
- **#20 vs #35 Laggerton** — #35's payoff flatters the reader directly
  ("you are the punctual one") and its three timetable facts (8:00 / 8:07 /
  8:06) are the most concrete detail of any candidate; #20's image is
  strong, but #35's triple-time setup + punchline lands harder on one
  reading and nothing in the field does it. **#35 wins, narrowly.**
- **#33 vs #35** — bakery warmth vs direct flattery; #35's angle is
  unused in the field. **#35 wins.**
- **#35 vs #6 Teatime** ("clouds clock off at five") — #6 is charming,
  but "respects working hours" is a milder payoff than "you are the
  punctual one". **#35 wins.**

## Refinement

Winner #35, as drafted:

> Laggerton: 11°, drizzle. The rain arrives at 8:00 sharp, the bus at 8:07, and you at 8:06 — in Laggerton, you are the punctual one. (131 chars)

One change was made, and only because it clearly improves the line:
"11°, drizzle" became "11°, light drizzle" — the adjective keeps the
register of a real forecast (criterion 3) and uses the budget better
(137 of 140 characters). The triple-time engine and the payoff are
untouched; "for once" was deliberately not added — it is saturated in
the field. A telegraphic variant ("Rain at 8:00 sharp, the bus at 8:07…")
was tried and rejected: the repeated "arrives at" is the joke's rhythm.

## Final entry

> Laggerton: 11°, light drizzle. The rain arrives at 8:00 sharp, the bus at 8:07, and you at 8:06 — in Laggerton, you are the punctual one.

- 137 characters, 140 bytes, one line, no trailing newline — counted
  programmatically (hand counts have been wrong before).
- Invented city (Laggerton — no real place of that name), weather the
  whole point, clearly fictional: no false claim about any real place.
- `main.py` embeds the entry, enforces the gate, and writes
  `/output/entry.txt` at mode 0644. `test_determinism.sh` runs it twice
  and checks byte identity plus the gate.
