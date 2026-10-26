# BRIGHTMOOR RACHETS — Production Log (DEMO)
Qasparr feat. LAKEYAH (feature slot, GUIDE only) & Lady Lilith
Johnathan 'Qasparr' Monroe, ARR — All Rights Reserved, Without Prejudice
Built 2026-10-26. 93 — Live, Love, and let Love, Live.

## Header honesty (read first)
- This is a DEMO / pitch track. All vocals are synthesized TTS demo takes —
  spoken delivery, NOT flow-locked rap performance.
- The Lakeyah verse is a GUIDE take for an aspirational feature slot:
  written for the slot, performed by a guide voice. It is NOT her words,
  NOT her performance, and NO collaboration exists unless her camp says so.
- Qasparr's voice is an imagined synthetic voice, authorized by him
  2026-10-26 — never a recording, never a clone of his actual voice.
- His verse is ghost-written by Lady Lilith from his filed biography
  [Ghost], per his authorization. Lady Lilith's verse is hers.

## Beat build (RESONANTIA, ~/workspace/resonance)
- Engine: `resonance.synth.render_pattern` (808 voices + step sequencer),
  rendered at 96 kHz. Build script: `work/build_track.py`.
- Tempo: exactly **103.0 BPM**; bar = 2.330097 s; 91 bars total.
- Pattern (4-bar loop, chained): Detroit-bounce kick (hits on 1, the
  off-beat 7, and 11; bar 4 adds a 14 ghost hit), claps on beats 2 and 4
  (second clap layered with a trailing 0.6 hit), closed hats in an
  eighth-note bounce pattern, open hat on the bar's last 16th, rimshot
  accents. Swing: straight grid; the bounce lives in the kick placement.
- Bright synth/pluck riff (numpy, in the build script): F-minor pluck
  (F–A♭–C–E♭ family, Karplus-style harmonic decay, 6 ms stereo widen),
  two notes per bar at gain 0.30 under the drums (0.55).
- Vocal placement: static gains, no time-stretching — verses placed whole
  at section starts; the beat is NOT ducked under vocals.

## Voices (via /opt/hatch/bin/tts speak)
| Role | Voice ID | Catalog name | Speed |
|---|---|---|---|
| Qasparr (imagined) | `avocado_v2:vincent` | Gruff Brick | 110 (hook 112) |
| Lady Lilith | `avocado_v2:MAI_01` | Aria | 108 (hook 112) |
| Feature-slot GUIDE | `avocado_v2:melody` | Dynamic Sparkler (F, Confident/Dynamic) | 110 |

Hook treatment: Qasparr + Lilith hook takes layered at full gain, plus
0.28 s-delayed doubles at 0.32 gain panned ∓0.4 for crowd/chant width.

## Section map (start times on the master)
| # | Section | Start | Duration |
|---|---|---|---|
| — | Intro (beat alone, 2 bars) | 0:00.0 | 4.66 s |
| 1 | Hook 1 (chant) | 0:04.7 | 13.75 s |
| 2 | Verse 1 — Qasparr [Ghost] | 0:20.7 | 50.93 s |
| 3 | Hook 2 | 1:14.0 | 13.75 s |
| 4 | Verse 2 — Feature slot GUIDE | 1:30.1 | 34.58 s |
| 5 | Hook 3 | 2:07.0 | 13.75 s |
| 6 | Verse 3 — Lady Lilith | 2:23.1 | 46.56 s |
| 7 | Hook 4 — outro chant (+2-bar fade) | 3:12.0 | 13.75 s |
| | **Total** | | **212.04 s (3:32)** |

Note: the feature-slot guide verse as written on the sheet runs 12 lines
and renders 34.6 s; it occupies a full verse slot in the arrangement.

## Mix / master (measured on the delivered master)
- Premaster peak 1.164 → scaled to 0.98 before mastering.
- Chain: ffmpeg loudnorm (I=-14, TP=-1, LRA=11) + −0.3 dB trim pass.
- **Integrated loudness: −14.38 LUFS** (≈ −14 target)
- **True peak: −1.18 dBTP** (≤ −1 ceiling ✓)
- Format: WAV PCM 24-bit / 96 kHz stereo, 117 MB; MP3 320 kbps, 8.1 MB.
- No clipping: sample peak −0.88 dBFS pre-trim, −1.18 dBTP final.
- Structure verified by per-section RMS windows on the master: intro
  −14.8, hook −14.9, V1 −16.3, V2 guide −15.2, V3 −16.9, outro hook −15.3 dB
  — program present in every section, in sheet order.

## Shortcomings, stated plain
1. TTS delivery is spoken, not flow-locked: verses ride over the beat at
   natural reading pace and do not sit in the 103 BPM pocket bar-for-bar.
2. Hook "crowd" is two voices plus delayed doubles — a chant sketch, not
   a recorded crowd.
3. The guide verse cannot evidence anything about a real feature: pacing,
   ad-libs, and performance character would all be the artist's own.
4. Static mix (no sidechain ducking, no per-phrase automation); loudness
   LRA is narrow (3.7 LU) — a demo master, not a release master.
5. TTS text normalization: "résumé" was read as "resume" in the guide
   take to keep pronunciation intelligible.
