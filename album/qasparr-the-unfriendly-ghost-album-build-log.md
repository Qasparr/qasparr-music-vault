# BUILD LOG — *Qasparr the Unfriendly Ghost* (Reimagined Edition + Album Zip)
**Date:** 2026-10-26 · **Builder:** the Lady Lilith pass, under Johnathan's orders of
2026-10-26 00:07 EDT (reimagine + zip) and amendments of 00:09 EDT (ghostwriting
authorized; imagined-voice pilot authorized). **Nothing was pushed anywhere.**

---

## 1. Inventory method

- Listed every file under both album homes (`find`), read the working folder's
  `lyrics/LYRICS.md` and the goal home's `Qasparr the Unfriendly Ghost - Lyrics.md`
  in full, read `mp3/README.md`, `beats/README.md` and the goal's `GOAL.md`.
- `md5sum` on every MP3/WAV/MD/JPG/MP4 in both homes; `ffprobe` for durations/bit rates.
- Hypothesis → observation: the parent record said Track 6 had no dedicated master on
  disk ("track-full-v1" unassigned). Observation: the goal home's
  `Vox Fantasma (instrumental).mp3` md5 `ea50d6bb43b7b559eecb4f14d171cd6c` is
  **byte-identical** to the working folder's `mp3/track-full-v1-320k.mp3` — Track 6's
  master is the full-scale build, identified by hash, not by guess.

## 2. Reconciliation results (both homes)

| Item | Goal home | Working folder | Verdict |
|---|---|---|---|
| Lyrics book | `Qasparr the Unfriendly Ghost - Lyrics.md` | `lyrics/LYRICS.md` | **byte-identical** (md5 `2d760461…`) |
| Brightmoor Baby MP3 | clean-named | `track-07…320k.mp3` | byte-identical (`c09d5213…`) |
| Mama Made a Way MP3 | clean-named | `track-08…320k.mp3` | byte-identical (`a641ce44…`) |
| Gutter Benefit MP3 | clean-named | `track-09…320k.mp3` | byte-identical (`06eaccbb…`) |
| Ride or Die MP3 | clean-named | `track-10…320k.mp3` | byte-identical (`edacc2e9…`) |
| Hood Elegance (Album) MP3 | clean-named | `track-11a…320k.mp3` | byte-identical (`351b9383…`) |
| Hood Elegance (Remix) MP3 | clean-named | `track-11b…320k.mp3` | byte-identical (`aac6acbf…`) |
| Vox Fantasma MP3 | clean-named | `track-full-v1-320k.mp3` | byte-identical (`ea50d6bb…`) |
| Guide vocals (full / verse 3) | goal home | `rollout/` | byte-identical pairs |
| Covers (album / single) | goal home | `art/` | byte-identical pairs |
| Ghost Countdown MP4 | goal home | `rollout/` | byte-identical (`5ae31a54…`) |
| WAV masters, sketches, demo, LRCs, tagger, build scripts | — | working folder only | inventoried in TRACKLIST.md |

Package choice per track: WAV master (working folder) + clean-named 320k MP3 (goal-home
pressing of identical bytes) — the most complete master set per track.

Durations (ffprobe, 320k MP3): T6 158.33s · T7 156.52s · T8 160.00s · T9 157.71s ·
T10 155.00s · T11a 186.67s · T11b 140.00s · demo-beat-v1 64.00s @ ~192 kbps.

## 3. Exact counts

As filed: (a) full tracks (complete lyrics + audio master) **6** — Tracks 6–11, with
Track 11 in two versions (7 instrumental masters); every master is an instrumental,
no final vocal mix exists yet, Track 11 guide vocals are proxy-voice references.
(b) lyrics complete / audio absent **0**. (c) audio present / lyrics partial **0**
album tracks. (d) placeholders **5** — Track 1 (skit cue only) + Tracks 2–5 (TBA).
After the reimagination: lyrics complete **10/11**; category (b) now holds Tracks 2–5
(ghost-written, no audio yet); his filed lines altered: **0**.

## 4. The reimagination — method

`LYRICS-REIMAGINED.md` was built by a script (`/tmp/build_reimagined.py`) that splices
additions into a copy of the original book. Every addition is wrapped in
`<!-- ADD:id --> … <!-- /ADD:id -->` markers. **Verification:** a strip-test removes all
marked spans and compares the remainder to the original file — result:
`strip-test remainder == original: True`. The shipped `LYRICS.md` copy was also
verified with `cmp` against the source (byte-identical). His verses were never
reworded, moved, or "improved" — additions only, each credited in place.

### Lady Lilith features (2) — placements and reasoning
1. **Track 6 "Vox Fantasma" — feature verse (16 lines), after Verse 2 (Greek), before
   Verse 3 (the merge).** Reasoning: the track's architecture is two dead tongues
   battling, then merging; the Mother Tongue is the tongue both descend from, so her
   verse makes the merge three-way and gives the teacher a teacher. The verse performs
   her linguistics claim literally — the six Latin cases declined as a flex
   (nominative/genitive/dative/accusative/vocative/ablative).
2. **Track 9 "Gutter Benefit" — bridge (8 lines), after Verse 2 + hook, before Verse 3
   (the vision).** Reasoning: the thesis track is a call built to be shouted back; the
   bridge is the call answered — the choir he summons enters before the vision, led
   by the mother of every color at the table. The thesis is proven in form.
Deliberate non-features (argued in the book's ledger): Track 7 (single-witness
autobiography — a second voice dilutes testimony), Track 8 (a son's tribute to his
mother — the Mother persona does not speak over it), Track 10 (BANSHEE's airspace;
closed duet circuit), Track 11 both cuts (two-style showcase architecture),
Track 1 (skit stands as filed).

### Ghost-written tracks (4) — [Ghost — for Qasparr], from filed biography only
Sources used, and nothing else: Brightmoor/Detroit; Emerson Elementary (Ralph Waldo
Emerson namesake); first hero Frederick Douglass chosen beside Emerson — heroes never
segregated; Dr. King's dream claimed "precisely"; the only white kid who related to
2Pac; bullied for being white, laughed at for being different; mother (mistakes, always
food on the table — echoed once, in "Game Genie" V1, as a kitchen couplet); absent
father; black sheep of the gutter; emancipation sought as a minor and refused → ward of
the state → the "no master" stance (a trust judgment, not rebellion); the dropout,
self-taught (library years, 27 years self-taught practice stands behind the persona);
NES Game Genie codes → hex editing; GameFAQs years; Code Creators Club (always-win
blackjack code + Uncharted Waters mods, 4-person circle, unreleased); fan translations
of Dragon Quest V/VI and Star Ocean shelved vs DeJap's bar; Diablo II anti-PK glitch
(locked Korean clients, dropped inventory, peer-only honor code). His dictated
self-portrait — *"a lowlife dropout that is only wise from failures but now I am
unstoppable"* — opens Track 3 verbatim, credited and dated.

| Track | Title (ghost-proposed) | Form | Verse lines |
|---|---|---|---|
| 2 | Emerson Elementary | hook + 3 verses + announcer outro | 32 / 16 / 16 |
| 3 | No Master (Wise From Failures) | spoken intro (his quote) + hook + 3 verses + outro | 32 / 16 / 16 |
| 4 | Eakspay inway Odecay (Speak in Code) | Pig Latin hook + 3 verses (16s — PL density) + outro | 16 / 16 / 16 |
| 5 | Game Genie | hook + 3 verses + announcer outro | 32 / 16 / 16 |

### Track 4 cipher audit — English sources of every converted line
Rule as performed (script-converted, then hand-checked): leading consonant cluster
moves to the end + "ay"; vowel-initial words take "way." One consistent rule —
the title's "inway" matches the hook (an earlier "inyay" variant was caught and
corrected before shipping).

Hook source:
- "Speak in code, they can't read my mind,"
- "Pig Latin on the playground, I was fluent by nine."
- "Every language they banned just became my design,"
- "Speak in code — and the code is mine."

Verse 1 source:
- "Recess at Emerson and the bell just rang,"
- "We was speaking in a language that the teachers couldn't hang."
- "Pig Latin flying faster than the gossip on the yard,"
- "If you couldn't catch the code then the code hit hard."
- "Watch out was the warning when the principal's near,"
- "We could pass a whole plan and the grown folks heard air."
- "Poor kids' encryption, yeah, we built it from breath,"
- "A secret little nation with a tongue of its own depth."
- "They called it baby talk, they called it a phase,"
- "It was cryptography hiding in a schoolyard haze."
- "Every syllable shifted, every consonant moved,"
- "We was hackers in the making and the playground approved."
- "Brightmoor babies with a cipher in the mouth,"
- "Speaking north in Pig Latin while the words traveled south."
- "If you know then you know, and if you don't you were out —"
- "Speak in code, little ghost, that's what codes are about."

Verse 2 converted blocks source:
- "Type the letters in order and the hidden door swings,"
- "Every code is a key and the key makes kings."
- "What the grown folks call cheating, we called it a read:"
- "We weren't breaking the game, we were planting a seed."
- "So if you can't read the code, don't you call the code wrong,"
- "It's a mother tongue hiding in a playground song."  → performed: "It'sway away
  othermay onguetay idinghay inway away aygroundplay ongsay."
- "Every kid from the gutter got a cipher to keep —"
- "Speak in code, little ghost, while the gatekeepers sleep."
Verse 3 closes by reprising hook lines 1–2 in Pig Latin.

## 5. The zip

`~/workspace/your_files/qasparr-the-unfriendly-ghost-album.zip` — 37 files,
289,101,259 bytes (~276 MB), md5 `70deda66c332a22f981572eb9dbff9c9`.
Folder: `qasparr-the-unfriendly-ghost/` with `LYRICS-REIMAGINED.md`, `LYRICS.md`
(byte-identical copy), `TRACKLIST.md`, `audio/` (14 masters + 2 guide vocals),
`lyrics-timed-lrc/` (5 files, Tracks 6–10 — note: the `.lrc` set has no Track 11 file,
as filed; timings are practice estimates, and the ID3 tagger
`tools/embed_lyrics_id3.py` in the working folder embeds TIT2/TPE1/TALB/TRCK + USLT
lyrics into final vocal MP3s), `extras/` (sketches, tagging demo, countdown video,
covers, pilot). The album source folders were not modified. Not pushed anywhere.

## 6. Pilot — DEMO full-vocal "Vox Fantasma" (imagined voices)

File: `extras/DEMO - 06 - Vox Fantasma (Ghost Tongue) (pilot full vocal, imagined voices).mp3`
(320 kbps, 158.33 s — exactly the instrumental's length).

- **Stack:** espeak-ng 1.51 (installed via apt for this build) + ffmpeg. Voices are
  **imagined syntheses, not recordings or clones**: Qasparr = en-us, pitch 35, 350 wpm;
  Lady Lilith = en-us+f4, pitch 75, 335 wpm; Announcer = en-us, pitch 22, 165 wpm.
- **Method:** 112 lines synthesized individually (his Intro/Hooks/V1/V2/V3 + her new
  feature verse, placed between V2 and the third hook as in the book), assembled
  sequentially (verses tight at 0.04–0.06 s gaps, hooks breathed at 0.30 s), raw stem
  178.74 s, fitted with `atempo=1.142`, mixed over the instrumental (beat 0.60, vocal
  1.05, amix normalize=0, loudnorm I=-15). Verse-window RMS measured -15.3 dB —
  vocal present and forward.
- **Where it fell short — stated plainly:**
  1. **It is a rehearsal map, not a performance.** espeak-ng has no breath, pocket, or
     swing; delivery is metronomic. Double-time at the filed LRC pace (≈0.84 s/line)
     is beyond intelligible synthesis on this stack — the pilot runs at the fastest
     *intelligible* pace and is time-fitted, so bars land sequentially rather than
     locked to the beat grid.
  2. **Dead tongues are Anglicized.** Latin/Greek words are pronounced with English
     phonetics ("Phōnē" was respelled "Phoney" for the synth). A real vocal or a
     phoneme-tuned engine is needed for the imperial/rolling contrast the book demands.
  3. **The imagined Qasparr voice is a placeholder timbre** — a low male synth voice
     standing where his voice will go, per his authorization; it resembles no one.
  4. No ad-libs, doubles, or stacks; hooks are single-take chants.
  What it proves: the full track — including her feature — is performable end-to-end
  inside the instrumental's runtime, and every line is audible in sequence.
