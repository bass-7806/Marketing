# Build an episode's HyperFrames project from its shots.py.
# usage: python3 build.py <episode>/shots.py <episode>/video <episode>/audio/captions.json
# Writes video/compositions/*.html and video/index.html; reads video/audio_cues.json when present.
import sys, os, runpy
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
shots, out, caps = (os.path.abspath(p) for p in sys.argv[1:4])
import framework
framework.init(out, caps)
sys.path.insert(0, os.path.dirname(shots))  # an episode may keep its own extra drawing helpers beside shots.py
runpy.run_path(shots, init_globals=vars(framework).copy(), run_name="__main__")
