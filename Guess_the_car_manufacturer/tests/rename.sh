#!/bin/bash
for img in ./miniprojet/*.jpg; do
newname=$(head /dev/urandom | tr -dc a-z0-9 | head -c 8)
mv "$img" ./miniprojet/"$newname".jpg
done

python3 mp_rename.py
