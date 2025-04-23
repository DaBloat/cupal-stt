#!/bin/bash

TMPDIR=~/Project/tmp/sox

for fn in $(find ~/Project/data-open-voice/voices/ -name "*.mp3"); do
  TMPFILE=$TMPDIR/$(basename $fn)
  sox $fn $TMPFILE rate 16000
  mv $TMPFILE $fn
done
