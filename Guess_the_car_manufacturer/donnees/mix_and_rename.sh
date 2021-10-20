#!/bin/bash
for img in ./generated/Audi/*.jpg; do
newname=$(head /dev/urandom | tr -dc a-z0-9 | head -c 8)
mv "$img" ./generated/Audi/"$newname".jpg
done

for img in ./generated/BMW/*.jpg; do
newname=$(head /dev/urandom | tr -dc a-z0-9 | head -c 8)
mv "$img" ./generated/BMW/"$newname".jpg
done

for img in ./generated/Mercedes/*.jpg; do
newname=$(head /dev/urandom | tr -dc a-z0-9 | head -c 8)
mv "$img" ./generated/Mercedes/"$newname".jpg
done

python3 rename.py
