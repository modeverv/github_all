#!/bin/bash

for i in 1 2 3 4 5 6 7; do
    curl -u ${1} "https://api.github.com/user/repos?per_page=100&page=${i}" > repos${i}
done
python a.py > result.txt
open result.txt
