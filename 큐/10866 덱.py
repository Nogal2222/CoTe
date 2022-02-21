# -*- coding: utf-8 -*-
from collections import deque
import sys
#input = sys.stdin.readline

n = int(input())
q = deque([])
for i in range(n):
    s = input().split()
    order = s[0]
    
    if order == 'push_front':
        q.appendleft(int(s[1]))
    
    elif order == 'push_back':
        q.append(int(s[1]))
    
    elif order == 'pop_front':
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    
    elif order == 'pop_back':
        if len(q) == 0:
            print(-1)
        else:
            print(q.pop())
    
    elif order == 'size':
        print(len(q))
    
    elif order == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    
    elif order == 'front':
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    
    elif order == 'back':
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])