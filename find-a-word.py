#!/usr/bin/env python3

import re

regex = re.compile("[a-zA-Z0-9_]+")

n = int(input())
sentences = [input() for _ in range(n)]
word_lists = [regex.findall(s) for s in sentences]

n = int(input())
for _ in range(n):
    word = input()
    print(' '.join(str(l.count(word)) for l in word_lists))
