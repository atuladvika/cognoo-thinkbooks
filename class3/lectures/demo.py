"""Before/after narration demo for en-IN-PrabhatNeural.
before.mp3: whole passage in one call (how the v4 explainer was voiced).
after.mp3 : one call per phrase, each with its own rate/pitch, joined with real silences.
"""
import asyncio, subprocess, os, ssl, edge_tts, edge_tts.communicate as _c
_c._SSL_CTX = ssl.create_default_context(cafile=os.path.expanduser("~/.ccr/ca-bundle.crt"))
V = "en-IN-PrabhatNeural"

# (text, rate, pitch, pause after in ms)
LINES = [
    ("Think first.", "-12%", "+2Hz", 450),
    ("Answer later.", "-15%", "-2Hz", 1100),
    ("That is the whole idea behind the Cognoo ThinkBook and Die-na.", "-4%", "+0Hz", 900),
    ("Here is a question from Class 3.", "+2%", "+0Hz", 350),
    ("A frog jumps four steps forward,", "-6%", "+1Hz", 250),
    ("and then slips two steps back.", "-6%", "-1Hz", 400),
    ("When does it first reach eighteen?", "-10%", "+3Hz", 1600),
    ("Most children start counting straight away.", "+4%", "+0Hz", 300),
    ("Four, two, six, four...", "+8%", "+2Hz", 600),
    ("and they get lost.", "-8%", "-3Hz", 1000),
    ("So Die-na does not give the answer.", "-6%", "+0Hz", 300),
    ("She asks one small question:", "-2%", "+1Hz", 400),
    ("what happens in just one jump?", "-12%", "+3Hz", 1500),
    ("Now the child is thinking.", "-8%", "-2Hz", 350),
    ("Not guessing.", "-14%", "-3Hz", 900),
]
PASSAGE = " ".join(t for t, *_ in LINES)

async def say(text, out, rate="+0%", pitch="+0Hz"):
    if os.path.exists(out) and os.path.getsize(out) > 1000: return
    for k in range(20):
        try:
            return await edge_tts.Communicate(text, V, rate=rate, pitch=pitch).save(out)
        except Exception:
            await asyncio.sleep(3)
    raise RuntimeError("TTS failed: " + text)

def sh(*a): subprocess.run(a, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

async def main():
    os.makedirs("seg", exist_ok=True)
    await say(PASSAGE, "before.mp3")
    parts = []
    for i, (t, r, p, ms) in enumerate(LINES):
        raw = f"seg/{i:02d}.mp3"; await say(t, raw, r, p)
        w = f"seg/{i:02d}.wav"
        # trim the TTS's own lead/tail silence so our pauses are the only gaps; 15 ms fades avoid clicks
        sh("ffmpeg", "-y", "-i", raw, "-af",
           "silenceremove=start_periods=1:start_threshold=-50dB,areverse,silenceremove=start_periods=1:start_threshold=-50dB,areverse,afade=t=in:d=0.015,areverse,afade=t=in:d=0.04,areverse",
           "-ar", "24000", "-ac", "1", w)
        s = f"seg/{i:02d}_s.wav"
        sh("ffmpeg", "-y", "-f", "lavfi", "-i", "anullsrc=r=24000:cl=mono", "-t", str(ms / 1000), s)
        parts += [w, s]
    with open("seg/list.txt", "w") as f:
        f.writelines(f"file '{os.path.abspath(x)}'\n" for x in parts)
    sh("ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", "seg/list.txt", "-af", "loudnorm=I=-16:TP=-1.5", "-b:a", "160k", "after.mp3")
    sh("ffmpeg", "-y", "-i", "before.mp3", "-af", "loudnorm=I=-16:TP=-1.5", "-b:a", "160k", "before_n.mp3")

asyncio.run(main())
