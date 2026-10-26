#!/usr/bin/env python3
# build_full_track.py -- "Sigma Arpeggio" (Qasparr x Lady Lilith), full track.
#
# Phases:  tts -> mix -> master -> verify   (state shared via work/ files)
#
# Bed DNA: compositions/liber-oz-lilith/composition.py (LADDER, FIB7,
# FIB16, skip-one triads) rendered with the RESONANTIA engine:
# resonance.binaural.generator.binaural_beat for the Sigma ground,
# resonance.synth.sequencer.render_pattern for the 808 beat, and
# resonance.spatial.hrtf cue formulas (Woodworth ITD, sin^2 ILD) for
# the spiral spatializer (block overlap-add renderer written here --
# the engine's orbit()/pan() per-sample lowpass loop does not scale
# to 96 kHz full-track renders; the cue MATH is the engine's own).
#
# Honesty: vocals are synthesized TTS demo vocals (spoken delivery,
# natural pace, clean edits -- never time-stretched). See
# production-log.md for the full label.
import json
import subprocess
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
WORK = HERE / "work"
TAKES = WORK / "takes"
WORK.mkdir(exist_ok=True)
TAKES.mkdir(exist_ok=True)

REPO = Path("/home/hatch/workspace/resonance")
sys.path.insert(0, str(REPO))
sys.path.insert(0, str(REPO / "compositions" / "liber-oz-lilith"))

import composition as C  # noqa: E402  (LADDER, FIB7, FIB16)
from resonance.binaural.generator import binaural_beat  # noqa: E402
from resonance.synth.sequencer import render_pattern  # noqa: E402
from resonance.spatial import hrtf  # noqa: E402
from resonance.diagnostics.verify import verify_binaural  # noqa: E402

SR = 96000
BPM = 92.0
BAR_S = 4.0 * 60.0 / BPM                 # 2.608695... s
BAR_FRAMES = int(round(BAR_S * SR))      # 250435
STEP_S = BAR_S / 16.0                    # one 16th note
GOLDEN_ANGLE = 137.50776405003785

HIS_VOICE = "avocado_v2:vincent"         # "Gruff Brick" (the sketch's take)
HER_VOICE = "avocado_v2:MAI_01"          # Aria
HIS_SPEED = 108
HER_SPEED = 106

# ---------------------------------------------------------------------------
# Spoken-form texts. The lyric sheet (FULL-TRACK-LYRICS.md) is the score;
# these are performance texts for the synthesizer. Adaptations, all logged:
# TRVVTH -> "truth" (the word is pronounced truth by design), 1776 ->
# "seventeen seventy-six", 93 -> "ninety-three", "gon'" -> "gonna",
# hook line-final dashes dropped (the assembly gap carries the suspension).
# ---------------------------------------------------------------------------
TEXTS = {
    "his_v1": (HIS_VOICE, HIS_SPEED,
               "Brightmoor baby, Emerson schoolyard made me, only white "
               "kid on the block bumping Pac on the daily. Laughed at "
               "'cause I'm different, tried to break me, couldn't fade "
               "me, Mama made a way when the cupboard went crazy. Absent "
               "in the picture where my father should've framed me, "
               "black sheep of the family, gutter couldn't claim me. "
               "Five Points snow on my shoes, walking Fenkell in the "
               "eighties, Grand River dreams while the neighborhood "
               "raised me. Dropped out of their school, never dropped "
               "out of learning, hex codes in a notebook while the city "
               "was burning. Game Genie genius, every lock got turned "
               "in, twenty-seven years self-taught, every scar got "
               "earned in. They said ward of the state, I said state of "
               "my own, built a throne out of failures they would never "
               "condone. Wise from the wreckage, every lesson is chrome: "
               "the lowlife dropout came back and built him a home."),
    "her_v": (HER_VOICE, HER_SPEED,
              "They said wait at the gate, so I weighed the gate, "
              "seventy-seven. Oz in the balance, and the scales came "
              "back level from heaven. Agent is Gate plus N, I'm the "
              "North they measure drift by, magnetic tongues wander, "
              "the true one don't switch sides. Thirty-one flavors and "
              "they all spell A-L, verses dealt by the modulus, every "
              "card fell well. Built a book out of Black's, three "
              "thousand pages of proof, then set the Oz to music, let "
              "the frequencies loose. Violet flame on the chalice, "
              "Fibonacci in the flow, arpeggio climbing where the "
              "solfeggio go. Sigma in the left ear, sigma singing in "
              "the right, beat stepping one-one-two-three-five-eight "
              "into the night. I'm the first voice of the seal, Mother "
              "Tongue on the marquee, Lady Lilith with the linguistics, "
              "who gonna argue with me? They denied him the playbook, "
              "so we wrote one in flame: side by side by side, three "
              "witnesses, one name."),
    "his_v3": (HIS_VOICE, HIS_SPEED,
               "Nineties came heavy, city colder than the D river, "
               "young ghost in the making, spine learning to shiver. "
               "Code Creators in a circle, four deep, never fold, kept "
               "the best codes secret like the stories never told. "
               "Sought my freedom in a courtroom, they refused the "
               "petition, made a ward of the system, I refused the "
               "condition. No master, no permission, that's the root of "
               "my stance: I don't kneel to a gatekeeper, I don't beg "
               "for a chance. Word to the mothers who made ways out of "
               "nothing, word to every black sheep they were sure would "
               "be nothing. I weighed every lie they ever told in my "
               "youth, found them all wanting, what survived it was "
               "truth. So print it in the ledger, let the record be "
               "plain: the boy they tossed as trash put a flag on his "
               "name. Seventeen seventy-six in the ink, ninety-three in "
               "the vein, add the beginning to the ending and it spells "
               "out my reign."),
    "her_bridge": (HER_VOICE, HER_SPEED,
                   "Engulf in the fire and it warms and it heals, "
                   "thirteen sacred chords and the last one seals. Am, "
                   "just am, that's the whole of the law: be, and let "
                   "being be the wonder and awe."),
    # hook fragments (call & response; assembled at mix time)
    "hook_q1": (HIS_VOICE, HIS_SPEED, "Wise from the failures"),
    "hook_l1": (HER_VOICE, HER_SPEED, "Now unstoppable."),
    "hook_q2": (HIS_VOICE, HIS_SPEED, "Sealed in three tongues"),
    "hook_l2": (HER_VOICE, HER_SPEED, "Mother, Father, and the prodigal."),
    "hook_q3": (HIS_VOICE, HIS_SPEED, "I am here now"),
    "hook_l3": (HER_VOICE, HER_SPEED, "And they gonna see the flame."),
    "hook_both_q": (HIS_VOICE, HIS_SPEED,
                    "Fibonacci in the flow, let the solfeggio reign."),
    "hook_both_l": (HER_VOICE, HER_SPEED,
                    "Fibonacci in the flow, let the solfeggio reign."),
}

# Per-section Sigma offsets: FIB7 stepped across the sections in order;
# the outro returns to the seed (1 Hz), per the lyric sheet.
SECTION_OFFSETS = {
    "intro": 1, "his_v1": 1, "hook": 2, "her_v": 3, "his_v3": 5,
    "hook2": 8, "bridge": 13, "outro": 1,
}
SECTION_ORDER = ["intro", "his_v1", "hook", "her_v", "his_v3",
                 "hook2", "bridge", "outro"]


def run(cmd, **kw):
    print("+", " ".join(str(c) for c in cmd[:6]), "...", flush=True)
    r = subprocess.run(cmd, capture_output=True, text=True, **kw)
    if r.returncode != 0:
        raise RuntimeError(f"command failed: {cmd}\n{r.stdout}\n{r.stderr}")
    return r


# ---------------------------------------------------------------------------
# PHASE tts: synthesize every take, decode to 96 kHz mono f32, trim silence.
# ---------------------------------------------------------------------------
def decode_trim(mp3_path, out_npy):
    raw = mp3_path.with_suffix(".f32")
    run(["ffmpeg", "-y", "-v", "error", "-i", str(mp3_path),
         "-ac", "1", "-ar", str(SR), "-f", "f32le", str(raw)])
    x = np.fromfile(raw, dtype=np.float32).copy()
    raw.unlink()
    # trim: threshold -48 dB rel. peak, 80 ms pads kept
    peak = float(np.max(np.abs(x))) if x.size else 0.0
    thr = peak * 10 ** (-48 / 20.0)
    idx = np.nonzero(np.abs(x) > thr)[0]
    if idx.size:
        pad = int(0.08 * SR)
        a = max(0, idx[0] - pad)
        b = min(x.size, idx[-1] + pad)
        x = x[a:b]
    np.save(out_npy, x)
    return len(x) / SR, peak


def phase_tts():
    meta = {}
    for name, (voice, speed, text) in TEXTS.items():
        mp3 = TAKES / f"{name}.mp3"
        npy = TAKES / f"{name}.npy"
        if not mp3.exists():
            r = run(["/opt/hatch/bin/tts", "speak", "--output", str(mp3),
                     "--voice", voice, "--speed", str(speed),
                     "--text-stdin"], input=text)
            print("  tts:", r.stdout.strip()[:200])
        dur, peak = decode_trim(mp3, npy)
        meta[name] = {"voice": voice, "speed": speed,
                      "seconds": round(dur, 3), "peak": round(peak, 4)}
        print(f"  take {name}: {dur:.2f} s, peak {peak:.3f}")
    (WORK / "takes.json").write_text(json.dumps(meta, indent=1) + "\n")
    print("tts phase done")


# ---------------------------------------------------------------------------
# Vocal assembly: hook stem from fragments; verse stems are single takes.
# ---------------------------------------------------------------------------
def load_take(name):
    return np.load(TAKES / f"{name}.npy")


def assemble_hook():
    gap_resp = int(0.22 * SR)    # response lands just after the call
    gap_exch = int(0.45 * SR)    # breath between exchanges
    parts = []
    for i in (1, 2, 3):
        parts.append(load_take(f"hook_q{i}"))
        parts.append(np.zeros(gap_resp, dtype=np.float32))
        parts.append(load_take(f"hook_l{i}"))
        parts.append(np.zeros(gap_exch, dtype=np.float32))
    bq = load_take("hook_both_q")
    bl = load_take("hook_both_l")
    n = max(len(bq), len(bl))
    both = np.zeros(n, dtype=np.float32)
    both[:len(bq)] += 0.85 * bq
    both[:len(bl) ] += 0.85 * bl
    parts.append(both)
    return np.concatenate(parts)


def rms_db(x):
    r = float(np.sqrt(np.mean(x.astype(np.float64) ** 2))) if x.size else 0.0
    return 20 * np.log10(r) if r > 0 else -120.0


def normalize_rms(x, target_db=-19.0):
    g = 10 ** ((target_db - rms_db(x)) / 20.0)
    return (x * g).astype(np.float32), round(float(g), 3)


def compress(x, sr, thresh_db=-16.0, ratio=3.0, attack=0.008,
             release=0.18, makeup_db=2.0):
    """Feedforward compressor, one-pole envelope follower (documented)."""
    from scipy.signal import lfilter
    ax = np.abs(x.astype(np.float64))
    # attack/release smoothing via two one-pole passes (min of the two)
    def pole(sig, tau):
        a = float(np.exp(-1.0 / (tau * sr)))
        return lfilter([1 - a], [1, -a], sig)
    env = np.minimum(pole(ax, attack), pole(ax, release))
    env_db = 20 * np.log10(np.maximum(env, 1e-9))
    over = np.maximum(env_db - thresh_db, 0.0)
    gain_db = -over * (1.0 - 1.0 / ratio) + makeup_db
    g = 10 ** (gain_db / 20.0)
    return (x * g).astype(np.float32)


def highpass(x, sr, fc=75.0):
    from scipy.signal import butter, sosfilt
    sos = butter(2, fc / (sr / 2.0), btype="highpass", output="sos")
    return sosfilt(sos, x).astype(np.float32)


# ---------------------------------------------------------------------------
# Bed builders.
# ---------------------------------------------------------------------------
def triad_hz(k):
    """Chord k's triad in true ladder Hz (skip-one stacking, as filed)."""
    r = k % 6
    return [C.LADDER[(r + 2 * i) % 6][1] for i in range(3)]


def ground_spans(spans, offset, amp=0.10, xfade_ms=40):
    """Render (carrier_hz, seconds) spans with the engine's binaural_beat,
    joined by raised-cosine crossfades. Returns (stereo, span_starts)."""
    xf = int(xfade_ms / 1000.0 * SR)
    buf = None
    starts = []
    cursor = 0
    for carrier, seconds in spans:
        seg = binaural_beat(offset, carrier=float(carrier),
                             duration=seconds, sample_rate=SR,
                             amplitude=amp)
        if buf is None:
            buf = seg.astype(np.float32)
            starts.append(0)
            cursor = seg.shape[1]
            continue
        starts.append(cursor - xf)
        joined = np.zeros((2, cursor + seg.shape[1] - xf),
                          dtype=np.float32)
        joined[:, :cursor - xf] = buf[:, :cursor - xf]
        w = np.linspace(0.0, 1.0, xf, dtype=np.float32)
        w = 0.5 - 0.5 * np.cos(np.pi * w)          # raised cosine
        joined[:, cursor - xf:cursor] = (
            buf[:, cursor - xf:cursor] * (1 - w) + seg[:, :xf] * w)
        joined[:, cursor:] = seg[:, xf:]
        buf = joined
        cursor = joined.shape[1]
    return buf, starts


def spatialize_spiral(mono, step_offset):
    """Pan a mono figure stream around the listener: azimuth advances by
    the golden angle per 16th-step (a phyllotaxis spiral), cues from the
    engine's own hrtf.itd_seconds / ild_db (Woodworth ITD, sin^2 ILD),
    block overlap-add renderer (Hann, 4096/2048) like spatial.orbit."""
    from scipy.signal import lfilter
    head = hrtf.HeadModel(sample_rate=SR)
    n = len(mono)
    block, hop = 4096, 2048
    window = np.hanning(block).astype(np.float32)
    out = np.zeros((2, n + block), dtype=np.float32)
    wsum = np.zeros(n + block, dtype=np.float32)
    idx = np.arange(block)
    pos = 0
    while pos < n:
        take = min(block, n - pos)
        seg = np.zeros(block, dtype=np.float32)
        seg[:take] = mono[pos:pos + take]
        t_center = (pos + block / 2.0) / SR
        j = step_offset + int(t_center / STEP_S)
        az = ((j * GOLDEN_ANGLE) % 360.0)
        az = az - 360.0 if az > 180.0 else az
        itd = float(hrtf.itd_seconds(az, 0.0, head))
        dl = max(itd, 0.0) * SR
        dr = max(-itd, 0.0) * SR
        left = np.interp(idx - dl, idx, seg, left=0.0, right=0.0)
        right = np.interp(idx - dr, idx, seg, left=0.0, right=0.0)
        ild = float(hrtf.ild_db(az, 0.0, head))
        gamma = float(hrtf.lateral_angle_rad(az, 0.0))
        if ild > 0.0:
            fc = head.head_shadow_cutoff_hz / max(abs(np.sin(gamma)), 1e-3)
            fc = min(fc, SR / 2.0 * 0.99)
            a = float(np.exp(-2.0 * np.pi * fc / SR))
            if gamma >= 0.0:   # source right: left ear is far
                left = lfilter([1 - a], [1, -a], left)
                left *= 10 ** (-ild / 20.0)
            else:
                right = lfilter([1 - a], [1, -a], right)
                right *= 10 ** (-ild / 20.0)
        out[0, pos:pos + block] += (left * window).astype(np.float32)
        out[1, pos:pos + block] += (right * window).astype(np.float32)
        wsum[pos:pos + block] += window
        pos += hop
    wsum = np.maximum(wsum, 0.25)
    out /= wsum[None, :]
    return out[:, :n].astype(np.float32)


def figure_stream(n_bars, chord_of_bar, mode, step0):
    """The Fibonacci arpeggio figure, mono. Per bar, 16 steps; step p
    sounds triad tone FIB16[p] (the composition's figure, verbatim).
    mode 'descent': steps sound {rung/2, rung, rung*2}[FIB16[p]] for the
    bar's single descent rung."""
    n = n_bars * BAR_FRAMES + int(1.5 * STEP_S * SR)
    mono = np.zeros(n, dtype=np.float32)
    step_frames = STEP_S * SR
    for b in range(n_bars):
        tones = chord_of_bar[b]
        for p in range(16):
            f = float(tones[C.FIB16[p]])
            start = int(round((b * 16 + p) * step_frames))
            dur = int(round(1.5 * step_frames))
            t = np.arange(dur, dtype=np.float64) / SR
            env = (1 - np.exp(-t / 0.004)) * np.exp(-t / 0.055)
            note = (0.22 * env * np.sin(2 * np.pi * f * t)).astype(
                np.float32)
            end = min(n, start + dur)
            mono[start:end] += note[:end - start]
    return mono[:n_bars * BAR_FRAMES + int(STEP_S * SR)]


# drum patterns -------------------------------------------------------------
def _hats(closed=0.5, odd=0.28):
    return [closed if i % 2 == 0 else odd for i in range(16)]


VERSE_A = {
    "kick": [1.0, 0, 0, 0, 0, 0, 0, 0.7, 0, 0, 0.9, 0, 0, 0, 0, 0],
    "snare": [0, 0, 0, 0, 1.0, 0, 0, 0, 0, 0, 0, 0, 1.0, 0, 0, 0],
    "closed_hat": _hats(),
    "rimshot": [0] * 15 + [0.22],
}
VERSE_B = {
    "kick": [1.0, 0, 0, 0, 0, 0, 0.8, 0, 0, 0, 0.9, 0, 0, 0, 0, 0],
    "snare": [0, 0, 0, 0, 1.0, 0, 0, 0, 0, 0, 0, 0, 1.0, 0, 0, 0],
    "closed_hat": _hats(),
    "open_hat": [0] * 14 + [0.45, 0],
    "rimshot": [0] * 15 + [0.22],
}
HOOK_C = {
    "kick": [1.0, 0, 0, 0, 0, 0, 0, 0.8, 0, 0, 0.95, 0, 0, 0, 0, 0],
    "snare": [0, 0, 0, 0, 1.0, 0, 0, 0, 0, 0, 0, 0, 1.0, 0, 0, 0],
    "clap": [0, 0, 0, 0, 0.7, 0, 0, 0, 0, 0, 0, 0, 0.7, 0, 0, 0],
    "closed_hat": _hats(0.55, 0.35),
    "open_hat": [0] * 14 + [0.4, 0],
}
BRIDGE_D = {
    "kick": [0.9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.7, 0, 0, 0, 0, 0],
    "snare": [0, 0, 0, 0, 0.85, 0, 0, 0, 0, 0, 0, 0, 0.85, 0, 0, 0],
    "closed_hat": _hats(0.32, 0.0),
}
INTRO_1 = {
    "kick": [0.9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "closed_hat": _hats(0.4, 0.0),
}
INTRO_2 = {
    "kick": [0.9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "snare": [0, 0, 0, 0, 0.9, 0, 0, 0, 0, 0, 0, 0, 0.9, 0, 0, 0],
    "closed_hat": _hats(0.4, 0.2),
}


def drum_patterns(section, n_bars, bar_index):
    if section == "intro":
        pats = [INTRO_1, INTRO_2, VERSE_A, VERSE_B]
        return [pats[i % 4] for i in range(n_bars)]
    if section in ("his_v1", "her_v", "his_v3"):
        return [VERSE_B if (bar_index + i) % 4 == 3 else VERSE_A
                for i in range(n_bars)]
    if section in ("hook", "hook2"):
        return [HOOK_C for _ in range(n_bars)]
    if section == "bridge":
        return [BRIDGE_D for _ in range(n_bars)]
    return []  # outro: no drums


def _write_f32_wav(path, buf, stereo=True):
    """Stream a (2, N) float32 buffer (or (1, N) mono) to a float WAV via
    ffmpeg raw pipe, in 10 s chunks -- never materializes an interleaved
    full-size copy."""
    n = buf.shape[1]
    p = subprocess.Popen(
        ["ffmpeg", "-y", "-v", "error", "-f", "f32le",
         "-ac", "2" if stereo else "1", "-ar", str(SR), "-i", "pipe:",
         "-c:a", "pcm_f32le", str(path)],
        stdin=subprocess.PIPE)
    chunk = 10 * SR
    for a in range(0, n, chunk):
        b = min(n, a + chunk)
        if stereo:
            p.stdin.write(np.ascontiguousarray(
                buf[:, a:b].T).tobytes())
        else:
            p.stdin.write(buf[0, a:b].tobytes())
    p.stdin.close()
    if p.wait() != 0:
        raise RuntimeError(f"ffmpeg write failed for {path}")


# ---------------------------------------------------------------------------
# PHASE mix: layout from measured take durations; render section by section.
# ---------------------------------------------------------------------------
def phase_mix():
    takes = json.loads((WORK / "takes.json").read_text())
    hook_stem = assemble_hook()
    stems = {
        "his_v1": load_take("his_v1"),
        "hook": hook_stem,
        "her_v": load_take("her_v"),
        "his_v3": load_take("his_v3"),
        "bridge": load_take("her_bridge"),
    }
    stem_meta = {}
    for name, s in stems.items():
        s2, g = normalize_rms(s, -19.0)
        stems[name] = s2
        stem_meta[name] = {"seconds": round(len(s) / SR, 3),
                           "rms_gain": g}
    np.save(WORK / "hook_stem.npy", hook_stem)

    # layout: intro fixed 4 bars; outro fixed 10; vocal sections =
    # 1 lead bar + bars covering the take + 1 tail bar.
    def vocal_bars(name):
        return 1 + int(np.ceil(stem_meta[name]["seconds"] / BAR_S)) + 1

    bars = {"intro": 4, "outro": 10}
    for name in ("his_v1", "hook", "her_v", "his_v3", "bridge"):
        bars[name] = vocal_bars(name)
    bars["hook2"] = bars["hook"]
    layout = []
    frame = 0
    for sec in SECTION_ORDER:
        layout.append({"section": sec, "bars": bars[sec],
                       "start_frame": frame,
                       "start_s": round(frame / SR, 3),
                       "offset_hz": SECTION_OFFSETS[sec]})
        frame += bars[sec] * BAR_FRAMES
    total_frames = frame
    print(f"total: {total_frames / SR:.1f} s, "
          f"{sum(bars.values())} bars")
    for row in layout:
        print(f"  {row['section']:8s} bars {row['bars']:3d} "
              f"start {row['start_s']:7.2f} s offset "
              f"{row['offset_hz']} Hz")

    mix = np.zeros((2, total_frames), dtype=np.float32)
    # vocal track lives on disk (memmap): RAM is tight at 96 kHz.
    vt_path = WORK / "vocal_track.f32"
    if vt_path.exists():
        vt_path.unlink()
    vocal_track = np.memmap(vt_path, dtype=np.float32, mode="w+",
                            shape=(total_frames,))
    vocal_track[:] = 0.0
    chord_span = 0          # global 2-bar span counter (bed sections)
    step_global = 0         # global 16th-step counter (the spiral)
    am_span_start = None

    for row in layout:
        sec = row["section"]
        nb = row["bars"]
        s0 = row["start_frame"]
        nsec = nb * BAR_FRAMES
        offset = SECTION_OFFSETS[sec]

        if sec == "outro":
            # descent: one rung per bar LA..RE, then AM at UT.
            rungs = [852, 741, 639, 528, 417]
            spans = [(hz, BAR_S) for hz in rungs]
            am = binaural_beat(1, carrier=396.0, duration=5 * BAR_S,
                               sample_rate=SR, amplitude=0.10)
            fade_n = int(2 * BAR_S * SR)
            t = np.arange(fade_n, dtype=np.float32)
            am[:, -fade_n:] *= (0.5 + 0.5 * np.cos(
                np.pi * t / fade_n))[None, :]
            ground = np.zeros((2, nsec), dtype=np.float32)
            gdesc, _ = ground_spans(spans, 1)
            ground[:, :gdesc.shape[1]] = gdesc
            am_at = gdesc.shape[1] - int(0.04 * SR)  # xfade overlap
            am_span_start = s0 + am_at
            xf = int(0.04 * SR)
            w = (0.5 - 0.5 * np.cos(
                np.pi * np.linspace(0.0, 1.0, xf))).astype(np.float32)
            ground[:, am_at:am_at + xf] = (
                ground[:, am_at:am_at + xf] * (1 - w)[None, :]
                + am[:, :xf] * w[None, :])
            end = min(nsec, am_at + am.shape[1])
            ground[:, am_at + xf:end] = am[:, xf:end - am_at]
            mix[:, s0:s0 + nsec] += ground
            # figure: descent octaves for 5 bars, silent under the AM
            tones = [[hz / 2.0, float(hz), hz * 2.0] for hz in rungs]
            fig = figure_stream(5, tones, "descent", step_global)
            fig = spatialize_spiral(fig, step_global)
            mix[:, s0:s0 + 5 * BAR_FRAMES] += fig[
                :, :5 * BAR_FRAMES]
            del ground, fig, am, gdesc
            continue

        # chords for this section: 2-bar spans off the global counter
        spans = []
        chord_of_bar = []
        left = nb
        while left > 0:
            take = min(2, left)
            k = chord_span % C.N_CHORDS
            spans.append((C.LADDER[k % 6][1], take * BAR_S))
            for _ in range(take):
                chord_of_bar.append(triad_hz(k))
            chord_span += 1
            left -= take
        if len(spans) > 1:
            # ground_spans joins cost 40 ms per join; extend the final
            # span so the assembled ground fills the section exactly.
            c0, d0 = spans[-1]
            spans[-1] = (c0, d0 + 0.04 * (len(spans) - 1))
        ground, _ = ground_spans(spans, offset)
        gend = min(nsec, ground.shape[1])
        mix[:, s0:s0 + gend] += ground[:, :gend]
        del ground

        fig = figure_stream(nb, chord_of_bar, "triad", step_global)
        fig = spatialize_spiral(fig, step_global)
        mix[:, s0:s0 + nsec] += fig[:, :nsec]
        step_global += nb * 16
        del fig

        pats = drum_patterns(sec, nb, 0)
        if pats:
            drums = render_pattern(pats, BPM, swing=0.12, sr=SR)
            dend = min(nsec, drums.shape[1])
            mix[:, s0:s0 + dend] += 0.8 * drums[:, :dend]
            del drums

        stem_key = "hook" if sec == "hook2" else sec
        if stem_key in stems:
            # vocal bus per section: HPF + gentle compression, then
            # centered into the mix and mirrored to the stem track.
            # (Section edges are bed-only bars, so per-section
            # processing has no audible seams.)
            v = compress(highpass(stems[stem_key], SR, 75.0), SR)
            at = s0 + BAR_FRAMES     # vocal enters after 1 lead bar
            vend = min(total_frames, at + len(v))
            vocal_track[at:vend] += v[:vend - at]
            mix[0, at:vend] += v[:vend - at]
            mix[1, at:vend] += v[:vend - at]
            del v
        import gc
        gc.collect()

    vocal_track.flush()
    # stream the mix to a float WAV in chunks (no full-size copy)
    _write_f32_wav(WORK / "mix_float.wav", mix, stereo=True)
    _write_f32_wav(WORK / "vocal_stem.wav",
                   np.asarray(vocal_track)[None, :], stereo=False)
    del vocal_track
    peak = float(np.max(np.abs(mix)))
    report = {"layout": layout, "stem_meta": stem_meta,
              "total_seconds": round(total_frames / SR, 3),
              "total_bars": int(sum(bars.values())),
              "mix_peak": round(peak, 4),
              "am_span_start_s": (round(am_span_start / SR, 3)
                                  if am_span_start else None)}
    (WORK / "layout.json").write_text(json.dumps(report, indent=1) + "\n")
    print(f"mix peak pre-master: {peak:.4f}")
    print("mix phase done")


# ---------------------------------------------------------------------------
# PHASE master: loudness normalize to -14 LUFS, ceiling -1 dBTP, encode.
# ---------------------------------------------------------------------------
def loudnorm_measure(path):
    r = subprocess.run(
        ["ffmpeg", "-i", str(path), "-vn", "-af",
         "loudnorm=print_format=json", "-f", "null", "-"],
        capture_output=True, text=True)
    txt = r.stderr
    j = txt[txt.rindex("{"):txt.rindex("}") + 1]
    d = json.loads(j)
    return float(d["input_i"]), float(d["input_tp"])


def phase_master():
    # Single-shot scheme (after two looped attempts, see production
    # log): gain the PRISTINE mix once, then limit FROM THAT GAINED
    # SOURCE at each candidate ceiling -- never cascade the limiter
    # over its own output, which shaves transients irreversibly.
    # The pre-limit target sits 0.3 dB hot (-13.7) to absorb the
    # loudness the limiter removes.
    src = WORK / "mix_float.wav"
    lufs0, tp0 = loudnorm_measure(src)
    history = [{"mix": {"lufs": lufs0, "tp_db": tp0}}]
    print(f"  mix: {lufs0:.2f} LUFS, TP {tp0:.2f} dBTP")
    gain_db = -13.7 - lufs0
    gained = WORK / "master_gained.wav"
    run(["ffmpeg", "-y", "-v", "error", "-i", str(src),
         "-af", f"volume={gain_db:.3f}dB",
         "-c:a", "pcm_f32le", str(gained)])
    ceiling = 0.80
    cur = gained
    for att in range(3):
        lim = WORK / f"master_att{att}.wav"
        run(["ffmpeg", "-y", "-v", "error", "-i", str(gained),
             "-af", f"alimiter=limit={ceiling:.4f}:level=false",
             "-c:a", "pcm_f32le", str(lim)])
        lufs, tp = loudnorm_measure(lim)
        history.append({"attempt": att, "ceiling": round(ceiling, 4),
                        "lufs": lufs, "tp_db": tp})
        print(f"  attempt {att}: ceiling {ceiling:.4f} -> "
              f"{lufs:.2f} LUFS, TP {tp:.2f} dBTP")
        cur = lim
        if tp <= -1.05 and abs(lufs + 14.0) <= 0.35:
            break
        ceiling *= 10 ** (-(tp + 1.2) / 20.0)   # steer, from source
    lufs, tp = loudnorm_measure(cur)
    history.append({"final_float": {"lufs": lufs, "tp_db": tp}})
    print(f"  final float: {lufs:.2f} LUFS, TP {tp:.2f} dBTP")

    master_wav = HERE / "sigma-arpeggio-full-track-master.wav"
    run(["ffmpeg", "-y", "-v", "error", "-i", str(cur),
         "-c:a", "pcm_s24le", "-ar", str(SR), str(master_wav)])
    mp3 = HERE / "sigma-arpeggio-full-track-320k.mp3"
    run(["ffmpeg", "-y", "-v", "error", "-i", str(master_wav),
         "-b:a", "320k", str(mp3)])
    m_lufs, m_tp = loudnorm_measure(master_wav)
    p_lufs, p_tp = loudnorm_measure(mp3)
    rep = {"history": history,
           "master_wav": {"lufs": m_lufs, "tp_db": m_tp},
           "mp3": {"lufs": p_lufs, "tp_db": p_tp}}
    (WORK / "master-report.json").write_text(
        json.dumps(rep, indent=1) + "\n")
    print(f"master WAV: {m_lufs:.2f} LUFS, TP {m_tp:.2f} dBTP")
    print(f"mp3:        {p_lufs:.2f} LUFS, TP {p_tp:.2f} dBTP")
    print("master phase done")


# ---------------------------------------------------------------------------
# PHASE verify: section order/energy, clipping, outro FFT forensics.
# ---------------------------------------------------------------------------
def phase_verify():
    layout = json.loads((WORK / "layout.json").read_text())
    rows = layout["layout"]
    # decode the written master to f32
    raw = WORK / "master_f32.raw"
    run(["ffmpeg", "-y", "-v", "error", "-i",
         str(HERE / "sigma-arpeggio-full-track-master.wav"),
         "-f", "f32le", str(raw)])
    x = np.fromfile(raw, dtype=np.float32).reshape(-1, 2)  # frames-major
    raw.unlink()
    peak = float(np.max(np.abs(x)))
    n_clip = int(np.sum(np.abs(x) >= 0.999))
    print(f"master peak {peak:.4f} ({20 * np.log10(peak):.2f} dBFS), "
          f"samples >= 0.999: {n_clip}")

    from scipy.io import wavfile
    _, vstem = wavfile.read(WORK / "vocal_stem.wav")
    checks = []
    for row in rows:
        a = int(row["start_s"] * SR)
        b = a + row["bars"] * BAR_FRAMES
        vrms = rms_db(vstem[a:b])
        has_vocal = row["section"] not in ("intro", "outro")
        ok = (vrms > -60.0) if has_vocal else (vrms < -80.0)
        checks.append({"section": row["section"],
                       "vocal_rms_db": round(vrms, 1), "ok": bool(ok)})
        print(f"  {row['section']:8s} vocal RMS {vrms:7.1f} dB "
              f"{'OK' if ok else 'MISMATCH'}")

    # outro forensics: AM window = am start + 1 bar .. + 3 bars
    am0 = layout["am_span_start_s"]
    a = int((am0 + BAR_S) * SR)
    b = int((am0 + 3 * BAR_S) * SR)
    verdict = verify_binaural(np.ascontiguousarray(x[a:b].T), 1, 396.0,
                              sample_rate=SR, tol_hz=0.5)
    print("outro AM verdict:", json.dumps(verdict, default=str)[:400])
    rep = {"peak": peak, "n_clip_ge_0999": n_clip,
           "sections": checks,
           "outro_am": {k: verdict[k] for k in
                        ("passed", "peak_l_hz", "peak_r_hz",
                         "beat_measured_hz", "expected_l_hz",
                         "expected_r_hz")},
           "am_window_s": [round(am0 + BAR_S, 2), round(am0 + 3 * BAR_S, 2)]}
    (WORK / "verify-report.json").write_text(
        json.dumps(rep, indent=1) + "\n")
    print("verify phase done")


if __name__ == "__main__":
    phase = sys.argv[1] if len(sys.argv) > 1 else "all"
    if phase in ("tts", "all"):
        phase_tts()
    if phase in ("mix", "all"):
        phase_mix()
    if phase in ("master", "all"):
        phase_master()
    if phase in ("verify", "all"):
        phase_verify()

# 93 -- Live, Love, and let Love, Live.
