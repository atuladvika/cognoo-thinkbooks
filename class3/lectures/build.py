"""Re-voice the first 3 minutes of Class3_CT_Ch1_Lecture_v4 in the approved B style.
Each segment = a stretch of the original video (vs..ve) + its narration lines.
Video of a segment is the original stretch, trimmed or held on its last frame to fit the new narration.
"""
import asyncio, subprocess, os, ssl, json, wave
import numpy as np, edge_tts, edge_tts.communicate as _c
_c._SSL_CTX = ssl.create_default_context(cafile=os.path.expanduser("~/.ccr/ca-bundle.crt"))
V = "en-IN-PrabhatNeural"
SRC = "src.mp4"

K = ("-10%", "-2Hz")   # key line / conclusion
Q = ("-10%", "+3Hz")   # question to the student
N = ("-4%", "+0Hz")    # ordinary
F = ("+4%", "+1Hz")    # quick / aside
W = ("+2%", "+3Hz")    # warm greeting
def L(t, s, ms): return (t, s[0], s[1], ms)

SEGS = [  # (video start, video end, min length or 0, lead or None, lines)
 (0.0, 5.5, 0, 1.5, [L("Hello, young thinkers!", W, 350), L("Atul Sir, your Thinking Mentor, has guided this lesson.", ("-4%", "+0Hz"), 900)]),
 (5.9, 10.9, 0, 0.3, [L("Today we will learn Chapter 1 together.", N, 450), L("Ready?", Q, 550), L("Let's go!", F, 900)]),
 (10.9, 20.3, 7.5, 1.2, [L("Chapter 1.", K, 400), L("What's in a Name?", ("-12%", "+2Hz"), 1200)]),
 (20.3, 25.4, 0, 0.6, [L("Before we start,", N, 250), L("let's check four things you need to know.", ("-4%", "-1Hz"), 900)]),
 (25.4, 31.8, 0, 0.3, [L("One.", K, 350), L("Spell the number names,", N, 250), L("from zero to twenty,", N, 250),
                        L("and the tens,", N, 200), L("like thirty and fifty.", K, 900)]),
 (31.8, 37.4, 0, 0.3, [L("Two.", K, 350), L("The vowels are A, E, I, O, U.", ("-12%", "+1Hz"), 450),
                        L("All other letters are consonants.", K, 900)]),
 (37.4, 43.8, 0, 0.3, [L("Three.", K, 350), L("A B C order.", N, 400), L("Look at the first letter.", N, 450),
                        L("Same first letter?", Q, 500), L("Look at the second.", K, 900)]),
 (43.8, 50.6, 0, 0.3, [L("Four.", K, 350), L("Count every letter, even when it repeats.", N, 450),
                        L("N, I, N, E", ("-14%", "+1Hz"), 300), L("has four letters,", N, 250), L("not three.", K, 900)]),
 (50.6, 54.9, 0, 0.3, [L("In your ThinkBook, tick each one you know!", ("-2%", "+2Hz"), 1100)]),
 (54.9, 62.2, 0, 0.6, [L("Here is your starting routine.", N, 400), L("Use the same four steps for every question.", K, 900)]),
 (62.2, 66.1, 0, 0.3, [L("Step one: Read.", K, 350), L("What is given?", Q, 350), L("Read the Note too.", N, 800)]),
 (66.1, 70.9, 0, 0.3, [L("Step two: Mark.", K, 350), L("Underline what is asked.", N, 300), L("Number the clues.", N, 800)]),
 (70.9, 75.3, 0, 0.3, [L("Step three: Write.", K, 350), L("Write the number names of the options.", N, 800)]),
 (75.3, 80.1, 0, 0.3, [L("Step four: Check.", K, 350), L("Test every option against every clue.", N, 900)]),
 (80.1, 85.4, 0, 0.3, [L("Read,", ("-8%", "+1Hz"), 200), L("Mark,", ("-8%", "+1Hz"), 200), L("Write,", ("-8%", "+1Hz"), 200),
                        L("Check.", K, 450), L("Say it with me!", ("+2%", "+4Hz"), 1300)]),
 (85.4, 91.3, 0, 1.0, [L("Meet Die-na, your Thinking Coach!", W, 350), L("She lives inside your ThinkBook.", N, 900)]),
 (91.3, 95.0, 0, 0.2, [L("Step one:", K, 200), L("try it on your own first.", N, 700)]),
 (95.0, 99.5, 0, 0.2, [L("Step two:", K, 200), L("stuck?", Q, 300), L("Read Die-na's two skills.", N, 700)]),
 (99.5, 103.0, 0, 0.2, [L("Step three:", K, 200), L("your turn.", N, 250), L("Take the last step.", K, 700)]),
 (103.0, 106.3, 0, 0.2, [L("Step four:", K, 200), L("write your answer in the box.", N, 900)]),
 (106.3, 113.9, 0, 0.3, [L("Die-na guides your thinking.", N, 350), L("She never just gives the answer.", N, 450),
                          L("You take the last step!", ("-12%", "-2Hz"), 1200)]),
 (113.9, 119.8, 0, 0.8, [L("Question one.", K, 500), L("Find the biggest number name hiding in these letters!", N, 1000)]),
 (119.8, 126.4, 0, 0.2, [L("Don't start with the long string.", N, 400), L("Start with the options:", N, 300),
                          L("sixty, six, twenty, seventy.", ("-8%", "+0Hz"), 900)]),
 (126.4, 132.5, 0, 0.2, [L("It asks for the largest.", K, 400), L("So hunt for the biggest name first,", N, 250),
                          L("then work down.", K, 900)]),
 (132.5, 140.8, 0, 0.2, [L("Letters must sit side by side.", N, 400), L("I see S, E, V, E, N here.", ("-10%", "+0Hz"), 400),
                          L("Do the letters T, Y come right after it?", Q, 1500)]),
 (140.8, 148.1, 0, 0.5, [L("When you find a name,", N, 200), L("lightly underline it with your pencil.", N, 400),
                          L("Your eyes will never lose their place!", ("-6%", "+2Hz"), 1000)]),
 (148.1, 159.8, 0, 0.6, [L("Go down your list from biggest to smallest.", N, 400),
                          L("The first name you find complete", N, 200), L("is your answer!", K, 700),
                          L("Pause the video, and try!", ("-2%", "+3Hz"), 3000)]),
 (159.8, 166.2, 0, 1.0, [L("Question two.", K, 500), L("Let's find Roy's favourite number!", W, 900)]),
 (166.2, 171.7, 0, 0.3, [L("Slice the clue into two checks.", N, 400), L("Check one:", K, 250),
                          L("does the name have three letters?", Q, 1400)]),
 (171.7, 178.4, 0, 0.3, [L("All four pass Check one!", F, 400), L("So Check two must decide:", N, 300),
                          L("two vowels,", ("-10%", "+1Hz"), 250), L("and one consonant.", K, 1500)]),
]

def sh(*a): subprocess.run(a, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

async def say(text, out, rate, pitch):
    if os.path.exists(out) and os.path.getsize(out) > 1000: return
    for _ in range(25):
        try:
            return await edge_tts.Communicate(text, V, rate=rate, pitch=pitch).save(out)
        except Exception:
            await asyncio.sleep(3)
    raise RuntimeError(text)

def wav_len(p):
    with wave.open(p) as w: return w.getnframes() / w.getframerate()

TRIM = ("silenceremove=start_periods=1:start_threshold=-50dB,areverse,silenceremove=start_periods=1:start_threshold=-62dB,"
        "areverse,afade=t=in:d=0.015,areverse,afade=t=in:d=0.02,areverse")

async def main():
    os.makedirs("clips", exist_ok=True); os.makedirs("segs", exist_ok=True)
    plan = []
    for si, (vs, ve, mn, lead, lines) in enumerate(SEGS):
        pieces = [("sil", lead)]
        for li, (t, r, p, ms) in enumerate(lines):
            key = f"clips/{si:02d}_{li:02d}"
            await say(t, key + ".mp3", r, p)
            if not os.path.exists(key + ".wav"):
                sh("ffmpeg", "-y", "-i", key + ".mp3", "-af", TRIM, "-ar", "48000", "-ac", "1", key + ".wav")
            pieces += [("wav", key + ".wav"), ("sil", ms / 1000)]
        alen = sum(x if k == "sil" else wav_len(x) for k, x in pieces)
        D = max(alen, mn)
        if D > alen: pieces.append(("sil", D - alen))
        plan.append((vs, ve, D, pieces))
    # audio track
    with open("alist.txt", "w") as f:
        n = 0
        for si, (_, _, _, pieces) in enumerate(plan):
            for k, x in pieces:
                if k == "sil":
                    if x <= 0: continue
                    p = f"segs/sil_{n}.wav"; n += 1
                    sh("ffmpeg", "-y", "-f", "lavfi", "-i", "anullsrc=r=48000:cl=mono", "-t", f"{x:.3f}", p)
                    f.write(f"file '{os.path.abspath(p)}'\n")
                else:
                    f.write(f"file '{os.path.abspath(x)}'\n")
    sh("ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", "alist.txt", "-af", "loudnorm=I=-16:TP=-1.5", "-ar", "48000", "voice.wav")
    # video segments
    with open("vlist.txt", "w") as f:
        for si, (vs, ve, D, _) in enumerate(plan):
            out = f"segs/v{si:02d}.mp4"
            Dv = D + 0.15 if si in (0, 1) else D          # first two segments are joined by a 0.3 s cross-fade
            hold = max(0, Dv - (ve - vs)) + 0.1
            vf = f"tpad=stop_mode=clone:stop_duration={hold:.3f},trim=duration={Dv:.3f},setpts=PTS-STARTPTS,fps=30"
            if si == 0:   # new opening bubble text, faded in as the original bubble finishes popping in
                sh("ffmpeg", "-y", "-ss", f"{vs:.3f}", "-t", f"{ve - vs:.3f}", "-i", SRC, "-loop", "1", "-i", "patch.png", "-an",
                   "-filter_complex", f"[0:v]{vf}[b];[1:v]format=rgba,fade=t=in:st=1.55:d=0.15:alpha=1,trim=duration={Dv:.3f}[p];[b][p]overlay=594:521:shortest=1",
                   "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-pix_fmt", "yuv420p", out)
            else:
                sh("ffmpeg", "-y", "-ss", f"{vs:.3f}", "-t", f"{ve - vs:.3f}", "-i", SRC, "-an", "-vf", vf,
                   "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-pix_fmt", "yuv420p", out)
            if si == 1:
                D0 = plan[0][2]
                sh("ffmpeg", "-y", "-i", "segs/v00.mp4", "-i", out, "-filter_complex",
                   f"[0:v][1:v]xfade=transition=fade:duration=0.3:offset={D0 - 0.15:.3f},fps=30",
                   "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-pix_fmt", "yuv420p", "segs/v0001.mp4")
                f.write(f"file '{os.path.abspath('segs/v0001.mp4')}'\n")
            elif si > 1:
                f.write(f"file '{os.path.abspath(out)}'\n")
    sh("ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", "vlist.txt", "-c", "copy", "video.mp4")
    total = sum(p[2] for p in plan)
    json.dump([(p[0], p[1], p[2]) for p in plan], open("plan.json", "w"))
    sh("ffmpeg", "-y", "-i", "video.mp4", "-i", "voice.wav", "-map", "0:v", "-map", "1:a",
       "-af", f"afade=t=out:st={total - 1.2:.2f}:d=1.2", "-vf", f"fade=t=out:st={total - 1.0:.2f}:d=1.0",
       "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
       "-shortest", "out.mp4")
    print("total", round(total, 1))

asyncio.run(main())
