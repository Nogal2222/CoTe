# -*- coding: utf-8 -*-
from collections import deque
import sys
#input = sys.stdin.readline

n = int(input())
q = deque([])

for i in range(n):
    s = input().split()
    order = s[0]
    
    if order == 'push':
        q.append(s[1])
    
    elif order == 'pop':
        if not q:
            print(-1)
        else:
            print(q.popleft())
    
    elif order == 'size':
        print(len(q))
    
    elif order == 'empty':
        if not q:
            print(1)
        else:
            print(0)
    
    elif order == 'front':
        if not q:
            print(-1)
        else:
            print(q[0])
    
    elif order == 'back':
        if not q:
            print(-1)
        else:
            print(q[-1])