# -*- coding: utf-8 -*-
n, m = list(map(int, input().split()))
s = []

def loop(start):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(start, n + 1):
        s.append(i)      # push
        loop(i)          # loop
        s.pop()          # pop
        
loop(1)