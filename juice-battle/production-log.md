# JUICE BATTLE (BAMF SCRATCH DUEL) — Production Log

**PRIVATE DEMO — not for release, not for sale, not for public posting as a
commercial work.** The voice samples are the user's own BAMF announcer pack
(Heroes of Newerth announcer clips, Samuel L. Jackson-voiced; © their
original makers and the voice artist), drawn from the user's private backup
(Qasparr/bamf-audio). They are used here under a fair-use-style
transformative-parody posture: short announcer calls recontextualized as
the dialogue of a fictional DJ battle, chopped and scratched into new
phrases. **Clearance from the rights holders would be required for any
commercial use.** The scratch side is an original synthetic performance in
the classic turntablist style — an homage to the craft, with no affiliation
with, participation by, or endorsement from any living DJ (the "Jeff side"
is a style, not the man). The scene is a parody homage to the club-battle
sequence in *Juice* (1992); no audio from the film itself is used.

Build: 2026-10-26 · Builder: production subagent for Johnathan 'Qasparr'
Monroe · Script: `work/build.py` (rerunnable) · Engine: RESONANTIA
(`resonance.synth.render_pattern`, ~/workspace/resonance)

---

## Deliverables

| File | Spec | Measured |
|---|---|---|
| `juice-battle-demo-master.wav` | 24-bit / 96 kHz stereo | 142.00 s, **−14.03 LUFS** int., **true peak −1.13 dBTP**, LRA 5.3 LU, sample peak −1.19 dBFS, **0 samples ≥ 0.99 FS** |
| `juice-battle-demo-320k.mp3` | 320 kbps | 5.68 MB, encoded from the trimmed master |

Tempo: **96.0 BPM**, swing 0.10, bar = 2.500 s, 53 bars of beat + cold open
and crowd tail.

## Inputs

- **BAMF pack** (`work/BAMF/`, 40 clips): decoded with ffmpeg to mono
  float at 96 kHz, silence-trimmed at 4 % of clip peak with 30 ms handles,
  each call peak-normalized to 0.9 so every rung of the ladder hits with
  equal authority.
- **Pack quirk, stated plain:** in this pack `startgame.ogg` and
  `get_it_on.ogg` are *byte-identical files* (md5
  `9eb140a13ebf8ee5e91fe07c80d6`). The cold open keeps both placements the
  scene calls for by arranging the second as a club-PA slap-echo double of
  the same call (90 ms slap delay, 0.35 feedback tap, 3.2 kHz lowpass,
  −1.3 dB) — the repeat reads as the room answering itself, and the log
  says so rather than pretending two different lines exist.

## Beat build (RESONANTIA)

`render_pattern` chains one validated 16-step grid per bar at 96 BPM,
swing 0.10 (odd 16ths late — the boom-bap pocket). Bar types:

- **full** — kick 1 / ghost-7 / 10, snare 4 & 12, 8th-note closed hats
  (accented quarters), open hat on 14, rimshot ticks on 3 & 11.
- **sparse** — anchors only (kick 1/10, snare 4/12, quiet 8th hats): under
  the long taunt calls (nemesis, payback, retribution) and the annihilation
  / genocide rungs so the voice owns the room.
- **half** — halftime under the `immortal` coronation.
- **out** — beat gone (a single faint hat tick per bar) under `rage_quit`:
  the challenger storms off into a beatless room.

A numpy sub-bass (A1/A1/F1/G1 two-bar loop, sine + 2nd harmonic, exp
decay, anchored to kick steps 0 and 10) runs under full/sparse bars at
−5 dB rel. the drums. Beat gain 0.85 into the mix.

## Crowd / room

Filtered-noise crowd bed: white noise → 2nd-order Butterworth bandpass
400–2600 Hz, slow random-walk LFO on the gain, base level ≈ −38 dBFS.
Swells: raised-cosine bumps (+0.030 gain, 1.6 s) after double_kill,
massacre, annihilation, humiliation, nemesis, immortal, victory. Cold open
ramps the room in over the first 7 s; final 2 s fade to zero under the
master fade (last 1.5 s). It is a noise-bed crowd — atmosphere, not
individual voices (see Shortcomings).

## Scratch technique (the "Jeff side")

Synthetic turntablism, implemented honestly in code. A scratch is a
**playhead position curve** p(u) over a source fragment, rendered by
interpolation — varispeed playback, so pitch and time bend together
exactly as a hand on vinyl bends them. The crossfader is a gate curve
multiplied over the segment (3 ms smoothed, never clicky); each gesture
carries 2 ms boundary fades. Sources are fragments of the announcer calls
themselves — the loudest 0.45 s window of each call, the classic battle-DJ
move of answering a voice record with itself — plus a synthesized 660 Hz
harmonic "aaah" tone burst scratched in the three momentum-swing rounds.

Gestures: **baby** (forward-and-back cosine sweep, fader open) ·
**chirp** (fast smoothed forward throw, fader shut on the return) ·
**wiggle** (back-cueing: sinusoidal rock ±0.22 around the cue point,
3 cycles) · **drag** (u^2.2 accelerating pull — pitch climbs out of the
mud) · **tear** (three gated forward tears with fader cuts between) ·
**stop** (record stop: 2u−u², speed bleeds to zero). Each round's routine
is a named gesture list time-scaled proportionally to fill its allotted
bars (1 bar for rungs 1–4, 2 bars thereafter).

## Round-by-round map (verified against the master)

Calls verified by normalized cross-correlation of the finished master in
each placed window (lag-searched ±0.3 s); all 20 PASS, corr. 0.65–0.99.
Scratch windows verified by RMS/crest: all 15 present, crest 4.5–6.5.

| # | Time | Event | Answer |
|---|---|---|---|
| — | 0:01.10 | startgame (cold open, room tone) | — |
| — | 0:03.55 | get_it_on (PA slap-echo double — identical file, see above) | beat drops 0:07.00 |
| R1 | 0:07.00 | first_blood | baby ×2 (1 bar) |
| R2 | 0:12.00 | double_kill | chirp, chirp, baby |
| R3 | 0:19.50 | triple_kill | wiggle, chirp, chirp, baby |
| R4 | 0:24.50 | quad_kill | drag, tear, baby |
| R5 | 0:29.50 | 5_kills | chirp ×2, wiggle, tear (2 bars) |
| R6 | 0:37.00 | 6_kills | tear, chirp, drag, baby |
| S1 | 0:44.50 | **nemesis** (sparse beat) | tonal riff: chirp, drag, chirp, tear |
| R7 | 0:54.50 | 7_kills | wiggle, tear, chirp ×2, drag |
| R8 | 1:02.00 | 8_kills | drag, tear, wiggle, chirp, baby |
| S2 | 1:09.50 | **payback** | tonal riff routine (2 bars) |
| R9 | 1:19.50 | massacre | tear ×2, chirp, drag, wiggle |
| R10 | 1:27.00 | annihilation (sparse) | chirp, tear, drag, tear, chirp, baby |
| S3 | 1:37.00 | **retribution** | tonal riff routine (2 bars) |
| R11 | 1:47.00 | genocide (sparse) | wiggle, drag, tear ×2, chirp, stop |
| R12 | 1:54.50 | humiliation | tear, chirp, drag, wiggle, tear, **stop** |
| F | 2:04.50 | **immortal** (halftime beat, crowd peak) | coronation |
| F | 2:12.00 | rage_quit (beat out) | the storm-off |
| F | 2:17.00 | victory (one full bar) | closing sting, crowd out by 2:22.00 |

## Mix & master chain

Stems summed in float64 at 96 kHz (uncrowded headroom: pre-master peak
1.80, no stem clipping by construction), peak-normalized to 0.89, 1.5 s
end fade. Mastering via ffmpeg loudnorm: measured mix −16.10 LUFS /
−1.01 dBTP → single dynamic pass to I=−14, TP=−1.0 → measured
−13.83 LUFS / −0.93 dBTP (peak 0.07 dB over ceiling) → −0.2 dB trim →
**final: −14.03 LUFS integrated, true peak −1.13 dBTP, sample peak
−1.19 dBFS, zero samples at or above 0.99 full scale.** MP3 320k encoded
from the final master.

## Shortcomings, stated plain

- **The scratch is synthetic.** The playhead model reproduces gesture
  geometry and varispeed pitch-bend faithfully, but there is no vinyl
  noise, no hand jitter, no turntable torque character — a real
  turntablist's phrases breathe in ways these curves only approximate.
- **TTS-free but also performance-free:** no human DJ performed any part
  of this record; both "sides" are one script.
- **Crowd is a noise bed** — swells and room tone, no individual shouts
  or reactions; at demo level it reads as atmosphere, not a roomful of
  people.
- **Beat is a two-grid pocket:** the RESONANTIA 808 kit (kick/snare/hats/
  clap-family voices) with a synthesized sub — no sampled break, no chop
  variation beyond the four bar types.
- **Loudnorm dynamic pass** applies gentle program-dependent gain riding
  (LRA lands at 5.3 LU — a fairly even club-demo loudness, less dynamic
  contrast than a hand-mixed battle recording would keep).
- Two ladder-adjacent pack clips (`9_kills`, `10_kills`, `3_kills`,
  `4_kills` — the numerical rungs) and the remaining pack material
  (smackdown, denied, defeat, etc.) were not used: the scene's ladder is
  the one specified, and the unused clips stay in the pack untouched.
