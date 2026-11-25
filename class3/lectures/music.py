"""Rebuild the v4 background loop (measured from the v4 lecture) and duck it under the new voice.
Loop: C - Am - F - G, 2.6 s per chord (10.4 s loop); sine pad (root in octave 3 + triad in octave 4)
plus arpeggio plucks in octave 5 every 0.325 s, alternately panned. Ducked 6 dB under speech."""
import numpy as np, wave, sys
SR = 48000
def hz(n): return 440 * 2 ** ((n - 69) / 12)          # MIDI -> Hz
CHORDS = [(48, 52, 55), (45, 48, 52), (41, 45, 48), (43, 47, 50)]   # C, Am, F, G (root, 3rd, 5th) in octave 3
CH, NOTE = 2.6, 0.325
ARP = [1, 2, 1, 0, 2, 1, 0, 1]

def read(p):
    with wave.open(p) as w:
        x = np.frombuffer(w.readframes(w.getnframes()), np.int16) / 32768.
        return x.reshape(-1, w.getnchannels()).mean(1), w.getframerate()

voice, sr = read(sys.argv[1]); assert sr == SR
T = len(voice) / SR; n = len(voice)
t = np.arange(n) / SR
L = np.zeros(n); R = np.zeros(n)

# pad: each chord 2.6 s with 0.6 s overlapping cross-fade
nch = int(np.ceil(T / CH)) + 1
for k in range(nch):
    a = k * CH - 0.3; b = a + CH + 0.6
    i0, i1 = max(0, int(a * SR)), min(n, int(b * SR))
    if i0 >= i1: continue
    tt = t[i0:i1] - a
    env = np.minimum(1, np.minimum(tt / 0.6, (b - a - tt) / 0.6))
    r, th, fi = CHORDS[k % 4]
    sig = 0.5 * np.sin(2 * np.pi * hz(r) * tt)
    for m in (r + 12, th + 12, fi + 12):
        sig += 0.33 * np.sin(2 * np.pi * hz(m) * tt + m)
    sig *= env * 0.06
    L[i0:i1] += sig; R[i0:i1] += sig

# arpeggio plucks
nn = int(T / NOTE) + 1
for j in range(nn):
    st = j * NOTE + 0.025
    k = int(st // CH); chord = CHORDS[k % 4]
    m = chord[ARP[j % 8]] + 24
    i0 = int(st * SR); i1 = min(n, i0 + int(0.9 * SR))
    if i0 >= n: break
    tt = t[i0:i1] - st
    env = (1 - np.exp(-tt / 0.006)) * np.exp(-tt / 0.28)
    sig = (np.sin(2 * np.pi * hz(m) * tt) + 0.15 * np.sin(4 * np.pi * hz(m) * tt)) * env * 0.05
    pan = 0.62 if j % 2 == 0 else 0.38
    L[i0:i1] += sig * pan * 2 * 0.8; R[i0:i1] += sig * (1 - pan) * 2 * 0.8

# ducking from the voice envelope: -6 dB under speech, smooth 150 ms attack, 400 ms release
hop = 480
e = np.sqrt(np.convolve(voice ** 2, np.ones(hop) / hop, 'same'))[::hop]
db = 20 * np.log10(e + 1e-9)
sp = (db > -40).astype(float)
g = np.zeros_like(sp); cur = 0
for i, v in enumerate(sp):
    c = 0.067 if v > cur else 0.025          # per 10 ms step
    cur += (v - cur) * c; g[i] = cur
gain = 10 ** (-6 * np.interp(np.arange(n) / hop, np.arange(len(g)), g) / 20)

# level: bed about 16 dB under the speech, like v4
mus = np.stack([L, R], 1) * gain[:, None]
vr = np.sqrt(np.mean(voice[voice ** 2 > 1e-4] ** 2)); mr = np.sqrt(np.mean(mus ** 2))
mus *= vr * 10 ** (-21 / 20) / mr
# fade in 1 s, fade out 2 s
fi = np.minimum(1, t / 1.0); fo = np.minimum(1, (T - t) / 2.0)
mus *= (fi * fo)[:, None]
mix = mus + voice[:, None]
mix /= max(1, np.abs(mix).max() / 0.95)
with wave.open(sys.argv[2], 'w') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((mix * 32767).astype(np.int16).tobytes())
print('ok', round(T, 1))
