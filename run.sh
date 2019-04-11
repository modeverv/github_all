#!/bin/bash

curl -u ${1} "https://api.github.com/user/repos?per_page=100&page=1" > repos1
python a.py > result.txt
rm -f repos1
open result.txt
rm -f result.txt

