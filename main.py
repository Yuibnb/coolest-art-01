"""Coolest-art entry: copy the art beside this file to the output dir."""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(OUT, exist_ok=True)
src = os.path.join(HERE, "entry.png")
dst = os.path.join(OUT, "entry.png")
shutil.copyfile(src, dst)
# Fail loudly rather than submit a truncated copy: the two runs must
# write identical bytes, so the copy must match the source exactly.
if os.path.getsize(dst) != os.path.getsize(src):
    raise SystemExit("entry.png copy size mismatch")
