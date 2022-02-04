# -*- coding: utf-8 -*-
n, m = list(map(int, input().split()))
s = []

def loop():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(1, n + 1):
        if i not in s:
            s.append(i) # push
            loop()      # loop
            s.pop()     # pop
            
loop()

'''다른 방법
n, m = map(int, input().split())
s = []
def loop(s):
    if len(s) == m:
        print(' '.join(map(str, s)))   # pop
        return
    
    for i in range(1, n+1):
        if i in s:
            continue    # loop
        loop(s + [i])   # push

loop(s)
'''