"""Generate every exercise of a chapter in order, numbering pages continuously from 12 (pages 3-5 are contents, 6-11 the front matter).
Usage: python3 build_chapter.py chapters/ch1_ex1.py chapters/ch1_ex2.py ..."""
import os, sys, subprocess, importlib.util
here = os.path.dirname(os.path.abspath(__file__)); os.chdir(here)
p = 12
for f in sys.argv[1:]:
    spec = importlib.util.spec_from_file_location('m', f); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    subprocess.run([sys.executable, '_class/guide_gen.py', f], check=True, env=dict(os.environ, FIRST=str(p)))
    p += len(m.PAGES)
print('last page', p - 1)
