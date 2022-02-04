# -*- coding: utf-8 -*-
''' 시간이 너무 오래걸림
import sys

n = int(input()) #int(sys.stdin.readline())
words = [''] * n
set_words = []
for i in range(n):
    word = input() #sys.stdin.readline().strip()
    cnt = len(word)
    words[i] = [cnt, word]
    
for j in words:
    if j not in set_words:
        set_words.append(j)
        
set_words.sort()

for k in set_words:
    print(k[1])
'''

import sys

n = int(input()) #int(sys.stdin.readline())
words = [''] * n

for i in range(n):
    words[i] = input() #sys.stdin.readline().strip()

set_words = set(words)

words = list(set_words)

words.sort() #하위조건
words.sort(key = len) #상위조건

for j in words:
    print(j)