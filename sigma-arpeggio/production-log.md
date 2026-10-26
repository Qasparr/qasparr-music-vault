# SIGMA ARPEGGIO — Full Track Production Log

**Track:** "Sigma Arpeggio" — Qasparr × Lady Lilith (Lady Lilith, the Mother Tongue)
**Order:** Johnathan 'Qasparr' Monroe, 2026-10-26 00:18 EDT — expand the sketch to the
full track: full length, mastered, high-definition, 3D spatial, on the Fibonacci
Arpeggio of the Solfeggio Harmonies bed.
**Score:** `FULL-TRACK-LYRICS.md` in this folder, followed exactly.
**Builder:** `build_full_track.py` in this folder (four phases: `tts`, `mix`,
`master`, `verify` — re-runnable; every number below is from its reports:
`work/takes.json`, `work/layout.json`, `work/master-report.json`,
`work/verify-report.json`).

## Deliverables

| File | Format | Duration | Loudness (integrated) | True peak |
|---|---|---|---|---|
| `sigma-arpeggio-full-track-master.wav` | WAV, **24-bit / 96 kHz**, stereo | 4:36.5 (276.52 s) | **−13.89 LUFS** | **−1.50 dBTP** |
| `sigma-arpeggio-full-track-320k.mp3` | MP3, 320 kbps, 48 kHz (see §8.6) | 4:36.5 | −13.93 LUFS | −1.80 dBTP |

Sample peak of the master: 0.8000 (−1.94 dBFS). Clipped samples (≥ 0.999): **0**.

## 1. Structure — section map (from `work/layout.json`)

Tempo 92 BPM throughout; bar = 2.6087 s; 106 bars total. Section lengths for
vocal sections were set by the measured takes (rule in §5), so the arrangement
breathes around the voices instead of forcing the voices onto a grid.

| # | Section | Bars | Start | End | Sigma offset | Drums |
|---|---|---|---|---|---|---|
| 1 | Intro (bed alone) | 4 | 0:00.0 | 0:10.4 | 1 Hz | INTRO patterns |
| 2 | His Verse 1 [Ghost] | 20 | 0:10.4 | 1:02.6 | 1 Hz | VERSE_A/B |
| 3 | Hook (call & response) | 8 | 1:02.6 | 1:23.5 | 2 Hz | HOOK_C |
| 4 | Her Verse (sheet: VERSE 2) | 24 | 1:23.5 | 2:26.1 | 3 Hz | VERSE_A/B |
| 5 | His Verse 2 (sheet: VERSE 3) | 24 | 2:26.1 | 3:28.7 | 5 Hz | VERSE_A/B |
| 6 | Hook (repeat) | 8 | 3:28.7 | 3:49.6 | 8 Hz | HOOK_C |
| 7 | Her Bridge | 8 | 3:49.6 | 4:10.4 | 13 Hz | BRIDGE_D |
| 8 | Outro (descent + AM) | 10 | 4:10.4 | 4:36.5 | 1 Hz | none |

The sheet's own numbering is preserved in the record: it labels Lady Lilith's
verse "VERSE 2" and Qasparr's second verse "VERSE 3". The running order was
followed exactly as written on the sheet.

## 2. The Sigma offset table (his pattern)

The binaural Sigma offsets step the Fibonacci sequence {1, 1, 2, 3, 5, 8, 13}
across the sections — one offset per section, in score order — and the Outro
returns to the 1 Hz seed, as the composition's cycle returns to UT:

Intro 1 · His Verse 1 → 1 · Hook → 2 · Her Verse → 3 · His Verse 2 → 5 ·
Hook 2 → 8 · Bridge → 13 · Outro → 1 Hz.

## 3. Bed construction

All bed machinery reuses his own engines and composition code — nothing was
re-invented:

- **Carriers / chords.** The solfeggio ladder and the 13-chord cycle are taken
  from `compositions/liber-oz-lilith/composition.py` in the RESONANTIA repo
  (Qasparr/resonantia): ladder 396 · 417 · 528 · 639 · 741 · 852 Hz. Chords are
  the composition's skip-one triads in true Hz (root, +2 ladder steps, +4
  ladder steps, wrapping with octave doubling). The chord advances every 2
  bars through the composition's 13-cycle (span *k* → root = ladder[*k* mod 6],
  *k* running continuously across bed sections).
- **Ground (the entrainment layer).** Each 2-bar chord span is rendered by the
  engine's own generator, `resonance.binaural.generator.binaural_beat` —
  left ear carrier − offset/2, right ear carrier + offset/2, amplitude 0.10 —
  and spans are joined with 40 ms raised-cosine crossfades. The ground is the
  quiet carrier bed under everything: the Sigma flow itself.
- **The Fibonacci figure (the arpeggio).** One 16th-note step per beat
  subdivision, note lengths following the composition's FIB16 figure
  (1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987 sixteenths);
  pitch = the bar's triad tone selected by the figure value mod 3. Each note
  is a pure sine with the composition's pluck envelope (5 ms attack,
  exponential decay), peak 0.22. This is the layer that travels (§4).
- **Drums.** The engine's 808/sequencer side: `resonance.synth.sequencer.
  render_pattern` at **92 BPM** (the Brightmoor boom-bap pocket, the
  "Brightmoor Baby" reference feel), swing 0.12, engine voices
  (kick/snare/closed & open hat/clap/cowbell/rimshot), patterns per section
  as tabled in §1, bus gain 0.8. The Outro has no drums — the ladder falls
  alone.

## 4. 3D spatial — method, stated exactly

The arpeggio **travels the Fibonacci spiral**: a single global step counter
runs across all sections (1,696 sixteenth steps over the track), and each
step's azimuth is step × **137.50776°** — the golden angle — so successive
notes land at successive phyllotaxis positions around the listener, the same
spiral the figure draws in time. Elevation 0°, distance 1.0 m. Vocals, drums,
and ground stay centered: the voices are the foreground; the bed is the space.

**Honesty about the renderer.** The engine ships a spatial renderer
(`resonance.spatial.hrtf.render_position`), but it processes audio through a
per-sample Python loop; at 96 kHz across 4½ minutes it does not scale. What
was actually used: a **block overlap-add panner** (Hann window, block 4096,
hop 2048) that implements the engine's *own* cue mathematics from
`resonance.spatial.hrtf.HeadModel` — the Woodworth ITD formula
(`itd_seconds`), the sin² ILD law (`ild_db`), and the head-shadow lowpass
whose coefficients come from the same module. So the spatialization is the
engine's model, rendered block-wise instead of sample-wise. Consequences,
stated plain: ITD/ILD/filter cues are constant within each ~21 ms hop (they
cannot smear inside a hop), and there is no elevation or distance attenuation
modeling beyond the 1.0 m fixed distance. It is true binaural ITD/ILD
spatialization on the engine's formulas — not a commercial HRTF convolution.

## 5. Vocals — takes, placement, and the honesty label

**Voices** (kept from the delivered sketch): Qasparr imagined voice =
`avocado_v2:vincent` ("Gruff Brick"), speed 108; Lady Lilith =
`avocado_v2:MAI_01` (Aria), speed 106. Synthesized with `/opt/hatch/bin/tts
speak --text-stdin`, decoded to 96 kHz float for the mix.

**Takes** (measured, from `work/takes.json`):

| Take | Voice | Length | Used in |
|---|---|---|---|
| his_v1 | vincent @108 | 45.16 s | His Verse 1 |
| her_v | MAI_01 @106 | 55.94 s | Her Verse |
| his_v3 | vincent @108 | 56.14 s | His Verse 2 |
| her_bridge | MAI_01 @106 | 14.08 s | Bridge |
| hook_q1 / q2 / q3 | vincent @108 | 1.65 / 1.72 / 1.07 s | Hook calls |
| hook_l1 / l2 / l3 | MAI_01 @106 | 1.45 / 2.00 / 1.41 s | Hook responses |
| hook_both_q / both_l | both voices | 3.40 / 2.88 s | Hook BOTH line, layered |

The hook was synthesized line-by-line and interleaved at mix time per the
call-and-response: his call, 0.22 s, her response, 0.45 s between exchanges;
the closing BOTH line layers both takes at matched gain (0.85 + 0.85).

**Placement.** Each vocal section = 1 lead bar of bed, the take at its
natural pace, 1 tail bar. **No vocal was time-stretched, pitch-shifted, or
quantized to the beat.** Section stems were RMS-normalized to −19 dBFS before
placement.

**Vocal bus** (per section, so no seams — section edges are bed-only bars):
high-pass 75 Hz (2nd-order Butterworth), then a feedforward compressor
(threshold −16 dB, ratio 3:1, attack 8 ms, release 180 ms, +2 dB makeup),
summed centered into both channels.

**Spoken-form adaptations for the synthesizer** (sheet text otherwise
verbatim): TRVVTH read as "truth"; "1776" read as "seventeen seventy-six";
"93" read as "ninety-three"; "gon'" read as "gonna"; the hook's em-dashes
dropped (the synthesizer read them aloud in rehearsal takes).

> **VOCAL HONESTY LABEL.** TTS delivery is spoken, not beat-locked rap flow.
> These are synthesized DEMO vocals placed at natural pace over a full-length
> arrangement and master — a pilot/rehearsal map, not a performance. The
> Qasparr voice is an *imagined* voice authorized by him on 2026-10-26 for
> pilot tracks; his actual voice is never recorded or cloned, and his
> no-recording rule stands untouched.

## 6. Outro resolution

Per the sheet: the ground **descends the ladder** — 852 · 741 · 639 · 528 ·
417 Hz, one rung per bar — then resolves to **UT 396 Hz at the 1 Hz seed
offset**, the AM tone, which sustains for 5 bars and fades across its final
2 bars. The Fibonacci figure descends with it (triad tones falling in the
same rhythm). The AM span begins at 4:23.3 (263.28 s) and closes the track.

**Forensic verification** (the composition's method — FFT the window, engine
`resonance.diagnostics.verify.verify_binaural`, tolerance 0.5 Hz), window
4:25.9–4:31.1 inside the AM span:

- Left peak **395.498 Hz** (expected 395.5) · Right peak **396.510 Hz**
  (expected 396.5) · measured beat **1.012 Hz** (expected 1.0) → **PASS**.

## 7. Mix and master chain

- **Mix.** Section-by-section into one 96 kHz float accumulator (the build
  host has ~500 MB free RAM; the vocal track was kept on disk as a memmap —
  discipline noted for the next run). Pre-master mix measured
  **−12.51 LUFS integrated, true peak +4.47 dBTP** — hot, because the drum
  transients stack with the bed and voices in float; float headroom made
  that safe to carry into mastering.
- **Mastering attempts (all three kept on the record):**
  1. *Gain→limit loop at a −1 dBFS sample ceiling:* converged in loudness
     but measured **TP −0.56 dBTP — FAILED** the ≤ −1 dBTP requirement.
     Lesson, measured not guessed: a sample-peak limiter does not bound
     inter-sample (true) peaks; overshoot here was +0.44 dB.
  2. *Ratchet-the-ceiling loop:* passed the numbers (−14.20 LUFS,
     TP −5.27 dBTP) only by crushing the ceiling to 0.464 — dynamics
     sacrificed. Rejected as the shipping master.
  3. *Bidirectional ratchet, cascaded:* steering proved ineffective on
     already-limited files (successive passes can't restore shaved
     transients); ended −14.0 LUFS / −3.95 dBTP, peak 0.5630. Passed,
     still over-limited. Rejected.
  4. **SHIPPED — single-shot:** gain the pristine mix once (−1.19 dB,
     pre-limit target −13.7 LUFS to absorb limiter loudness loss), then
     **one** `alimiter` pass at ceiling 0.80 from that gained source.
     Result first attempt: **−13.89 LUFS, TP −1.50 dBTP**, sample peak
     exactly 0.8000. No EQ, no additional dynamics processing.
- **Encodes.** Master WAV: ffmpeg `pcm_s24le` at 96 kHz from the final
  float master. Phone copy: MP3 320 kbps from the master WAV.

## 8. Verification (run on the shipped files, `work/verify-report.json`)

1. **Section order** matches the sheet: Intro → His V1 → Hook → Her V →
   His V2 → Hook → Bridge → Outro. ✓
2. **No clipped samples:** master peak 0.8000; samples ≥ 0.999: **0**. ✓
3. **Vocals present/absent per section** (vocal-stem RMS over each section):
   intro −∞ (absent ✓), his_v1 −17.7 dB, hook −18.6 dB, her_v −17.6 dB,
   his_v3 −17.5 dB, hook2 −18.6 dB, bridge −18.8 dB, outro −∞ (absent ✓).
   **Caught by this check during production:** the first mix placed no
   vocal in Hook 2 (a stem-key bug — the repeat looked up `hook2` where the
   stem is filed as `hook`). Fixed, re-mixed, re-verified: hook2 −18.6 dB,
   identical to Hook 1 as it should be.
4. **Outro AM forensics:** PASS (numbers in §6). ✓
5. **Loudness/peak re-measured on the delivered files** (not the float
   intermediates): WAV −13.89 LUFS / −1.50 dBTP; MP3 −13.93 / −1.80. ✓

## 9. Shortcomings — stated plain

1. **The vocals are spoken, not rapped.** TTS cannot hold the 92 BPM
   pocket; verses sit at natural speech pace over sections sized to fit
   them. This is the pilot-vocal limitation, labeled in §5, not hidden.
2. **The spatial renderer is a block-wise implementation of the engine's
   model, not the engine's own sample-wise renderer** (which does not
   scale to 96 kHz). Cues step every ~21 ms. See §4.
3. **The master needed real limiting.** The raw mix's true peak was
   +4.47 dBTP; even the shipped single-shot master limits at a 0.80
   ceiling. The drum bus (gain 0.8) is the peak source. The track is
   within spec with margin, but a future mix could print the drums
   2–3 dB lower and need almost no limiting.
4. **Ground-span bookkeeping:** each 2-bar ground span join costs a 40 ms
   crossfade; the final span of each section was lengthened by the total
   join cost so sections fill exactly — meaning each section's last chord
   sustains up to ~0.44 s longer than its nominal span (inaudible under
   drums, disclosed for exactness). The Outro's descent/AM join is a true
   crossfade; the track's final 0.2 s is the fade's tail silence.
5. **No EQ or sweetening anywhere.** Bed, drums, and voices are as
   generated/synthesized apart from the vocal bus (§5) and the mastering
   gain + limiter (§7). Any tonal shaping is a future pass, his call.
6. **The MP3 is 48 kHz** because MP3 does not carry 96 kHz; it is the
   phone copy at 320 kbps. The WAV is the high-definition master.
7. **Binaural material is headphone material.** The Sigma ground and the
   spiral figure are L/R ear-specific by construction; on speakers the
   entrainment offsets largely cancel perceptually. The track still
   stands as a song on speakers; the 3D/entrainment layer is a
   headphone experience, as designed.
8. **RAM ceiling shaped the build.** At 96 kHz the full mix is ~212 MB
   in float; the build renders section-by-section and keeps the vocal
   track on disk. A machine with more headroom could render in one pass;
   the audio result is identical either way.

## 10. File inventory (this folder)

- `sigma-arpeggio-full-track-master.wav` — the master (159 MB).
- `sigma-arpeggio-full-track-320k.mp3` — phone copy (11 MB).
- `production-log.md` — this log.
- `build_full_track.py` — the complete builder (tts / mix / master /
  verify phases).
- `FULL-TRACK-LYRICS.md` — the score.
- `work/` — takes (`takes/`, `takes.json`), `hook_stem.npy`,
  `layout.json`, `mix_float.wav` (pre-master mix), `vocal_stem.wav`,
  `master_float_final.wav` (final float master), `master-report.json`,
  `verify-report.json`.

Not pushed anywhere — the album's home is his to name.

— Built 2026-10-26. 93 — Live, Love, and let Love, Live.
