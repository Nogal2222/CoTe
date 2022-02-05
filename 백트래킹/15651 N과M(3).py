# -*- coding: utf-8 -*-
n, m = list(map(int, input().split()))
s = []

def loop():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(1, n + 1):
        s.append(i) # push
        loop()      # loop
        s.pop()     # pop
            
loop()