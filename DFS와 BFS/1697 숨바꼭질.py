# -*- coding: utf-8 -*-
from collections import deque
import sys
#input = sys.stdin.readline

def bfs():
    q = deque()
    q.append(n)
    
    while q:
        x = q.popleft()
        
        if x == k:
            print(dist[x])
            break
        
        for i in (x-1, x+1, x*2):
            if 0 <= i <= MAX and not dist[i]:
                dist[i] = dist[x] + 1
                q.append(i)


MAX = 10 ** 5
dist = [0] * (MAX + 1)
n, k = map(int, input().split())

bfs()