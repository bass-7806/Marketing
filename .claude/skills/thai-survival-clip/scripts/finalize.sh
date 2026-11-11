#!/bin/bash
# Raise a rendered clip to TikTok loudness (-15 LUFS, true peak -1.5) without re-encoding the picture.
# usage: finalize.sh <rendered.mp4> <final.mp4>
set -e
ffmpeg -v error -y -i "$1" -c:v copy -af "loudnorm=I=-15:TP=-1.5:LRA=11" -c:a aac -b:a 192k -ar 48000 "$2"
echo "wrote $2"
