# TRACKLIST & INVENTORY — *Qasparr the Unfriendly Ghost* (Reimagined package)

**Artist:** Johnathan "Qasparr (Κασπάρρ)" Monroe · **Featuring:** Lady Lilith, the Mother Tongue
**Package built:** 2026-10-26 · **Sources (two homes, reconciled below):**
`~/workspace/album-qasparr-unfriendly-ghost/` (working folder) and
`~/workspace/goals/qasparr-the-unfriendly-ghost-album/files/Qasparr the Unfriendly Ghost/` (goal home)

## The album — 11 tracks

| # | Title | Lyrics status (as filed) | Audio master | Lady Lilith feature | Ghost-written |
|---|-------|--------------------------|--------------|--------------------|---------------|
| 1 | Welcome to Outer Dr (intro skit) | Partial — one announcer cue line, stands as filed | none | No — skit stands as filed | No |
| 2 | Emerson Elementary *(ghost-proposed title)* | Placeholder (vault TBA) → **complete** | none | No | **Yes — full track** |
| 3 | No Master (Wise From Failures) *(ghost-proposed title)* | Placeholder (vault TBA) → **complete** | none | No | **Yes — full track** |
| 4 | Eakspay inway Odecay (Speak in Code) — Pig Latin track *(ghost-proposed title)* | Placeholder (Pig Latin TBA) → **complete** | none | No | **Yes — full track, Pig Latin** |
| 5 | Game Genie *(ghost-proposed title)* | Placeholder (vault TBA) → **complete** | none | No | **Yes — full track** |
| 6 | Vox Fantasma (Ghost Tongue) | Complete (his) | WAV + 320k MP3 instrumental, 2:38 | **Yes — feature verse after Verse 2 (Greek), before the merge** — the Mother Tongue is the tongue both dead tongues descend from; the merge lands three-way | No |
| 7 | Brightmoor Baby | Complete (his) | WAV + 320k MP3 instrumental, 2:37 | No — single-witness autobiography; a second voice would dilute the testimony | No |
| 8 | Mama Made a Way | Complete (his) | WAV + 320k MP3 instrumental, 2:40 | No — a son's tribute to his mother; the Mother does not speak over it | No |
| 9 | Gutter Benefit (Black Sheep) | Complete (his) | WAV + 320k MP3 instrumental, 2:38 | **Yes — 8-line bridge before Verse 3 (the vision)** — the thesis track is a call built to be shouted back; the choir answers, led by the Mother | No |
| 10 | Ride or Die (Qasparr & BANSHEE) | Complete (his) | WAV + 320k MP3 instrumental, 2:35 | No — BANSHEE's airspace; the duet is a closed Bonnie & Clyde circuit | No |
| 11 | Hood Elegance — Album Version | Complete (his) | WAV + 320k MP3 instrumental, 3:07 + full guide vocal (reference only) | No — two-style showcase (Eve bark / Da Brat chop) by design | No |
| 11R | Hood Elegance — Battle Pass Remix | Complete (his) | WAV + 320k MP3 instrumental, 2:20 + Verse 3 guide vocal (reference only) | No — same architecture as the Album Version | No |

## Exact counts

**As filed (before the reimagination):**
- (a) Full tracks — complete lyrics + audio master: **6** (Tracks 6, 7, 8, 9, 10, 11; Track 11 in two versions → 7 instrumental masters). Plainly stated: every audio master on this album is an **instrumental** — no final vocal mix exists for any track yet. Track 11's guide vocals are proxy-voice rehearsal references, not finals.
- (b) Lyrics complete, audio absent: **0**
- (c) Audio present, lyrics partial/absent: **0** album tracks (see demo note below)
- (d) Placeholders: **5** — Track 1 (partial skit cue, no audio) and Tracks 2–5 (vault / Pig Latin TBA; titles and files never supplied)

**After the reimagination (this package):**
- Lyrics complete: **10 of 11** tracks (all but the Track 1 skit, which stands as filed)
- Category (b) — lyrics complete, audio absent: **4** (Tracks 2–5, ghost-written)
- Lady Lilith features: **2** (Track 6 verse, Track 9 bridge) · Ghost-written tracks: **4** (Tracks 2–5) · His filed lines altered: **0** (strip-test verified)

## Reconciliation of the two homes

Method: `md5sum` on every audio/text/image file in both homes + `ffprobe` durations.

- **Lyrics:** the goal home's `Qasparr the Unfriendly Ghost - Lyrics.md` is **byte-identical**
  (md5 `2d7604614ba1c0641867161c7764cd78`) to the working folder's `lyrics/LYRICS.md`. The copy in
  this package is that file, unchanged.
- **Instrumentals:** the goal home's clean-named MP3s are **byte-identical** to the working
  folder's `mp3/track-*.mp3` for Tracks 7, 8, 9, 10, 11a, 11b (matching md5s, pair by pair).
- **Track 6 identification:** the goal home's `Vox Fantasma (instrumental).mp3` is byte-identical
  (md5 `ea50d6bb43b7b559eecb4f14d171cd6c`) to the working folder's `mp3/track-full-v1-320k.mp3` —
  Track 6's master **is** the full-scale 144 BPM build (`beats/track-full-v1.wav` → 320k MP3).
- **Guide vocals:** goal-home copies are byte-identical to the working folder's `rollout/` copies.
- **Art/video:** both cover JPGs and the Ghost Countdown MP4 are byte-identical across homes.
- **Working-folder-only assets:** WAV masters for every instrumental (`beats/track-*.wav`),
  beat sketches v1/v2 (WAV + MP3), `demo-beat-v1.mp3`, timed `.lrc` lyric files (Tracks 6–10),
  `tools/embed_lyrics_id3.py`, beat build scripts, rollout frames.
- **Most complete master per track (used in this package):** WAV (from the working folder) +
  the clean-named 320k MP3 (goal home pressing of the identical bytes) for Tracks 6–11;
  guide vocals included for Track 11 as reference-only.

## Package contents

- `LYRICS-REIMAGINED.md` — the full book: his text whole + Lady Lilith features + ghost tracks + ledger
- `LYRICS.md` — the original lyrics book, byte-identical copy
- `TRACKLIST.md` — this file
- `audio/` — WAV + 320k MP3 instrumentals for Tracks 6–11 (both Hood Elegance cuts) + Track 11 guide vocals (reference only)
- `lyrics-timed-lrc/` — karaoke `.lrc` files for Tracks 6–10 (timings are practice estimates; the ID3 tagger lives at `tools/embed_lyrics_id3.py` in the working folder — run it on final vocal MP3s to embed TIT2/TPE1/TALB/TRCK + USLT lyrics)
- `extras/` — beat sketches v1/v2 (WAV + MP3; v2 is the album's reference beat: 144 BPM, G# minor), `demo-beat-v1.mp3` (ID3-tagging mechanism demo only — its embedded lyrics do **not** match its instrumental), Ghost Countdown (10s loop).mp4, both cover JPGs, and the **pilot**: `DEMO - 06 - Vox Fantasma (Ghost Tongue) (pilot full vocal, imagined voices).mp3` — a full-vocal DEMO of Track 6 with synthesized imagined voices for both emcees (Qasparr imagined, never recorded/cloned; Lady Lilith feature verse included). Honest limits are in the build log beside the zip.

*Note on the demo: `demo-beat-v1.mp3` (64 s, ~192 kbps) exists to prove the ID3 USLT lyric-embedding
mechanism. It is working material, not a track master, and is inventoried here so it is never
mistaken for one.*
