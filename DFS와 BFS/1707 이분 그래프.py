# -*- coding: utf-8 -*-
from collections import deque
import sys
#input = sys.stdin.readline

def bfs(start):
    bi[start] = 1
    q = deque()
    q.append(start)
    
    while q:
        a = q.popleft()
        
        for i in s[a]:
            
            if bi[i] == 0:
                bi[i] = -bi[a]
                q.append(i)
            
            else:
                
                if bi[i] == bi[a]:
                    return 0
        
    return 1


testcase = int(input())

for i in range(testcase):
    V, E = map(int, input().split())
    flag = 1
    s = [[] for i in range(V+1)]
    bi = [0 for i in range(V+1)]
    
    for j in range(E):
        u, v = map(int, input().split())
        s[u].append(v)
        s[v].append(u)
    
    for k in range(1, V+1):
        if bi[k] == 0:
            if not bfs(k):
                flag = 0
                break
    
    print("YES" if flag else "NO")