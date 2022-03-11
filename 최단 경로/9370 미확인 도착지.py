# -*- coding: utf-8 -*-
from heapq import heappush, heappop
import sys
#input = sys.stdin.readline

def shortest(start):
    heap = []
    heappush(heap, [0, start])
    dp = [100000000 for i in range(n+1)]
    dp[start] = 0
    
    while heap:
        we, nu = heappop(heap)
        
        for ne, nw in s[nu]:
            way = we + nw
            
            if dp[ne] > way:
                dp[ne] = way
                heappush(heap, [way, ne])
                
    return dp


t = int(input())

for _ in range(t):
    n, m, c = map(int, input().split())
    start, g, h = map(int, input().split())
    s = [[] for i in range(n+1)]
    de = []
    
    for j in range(m):
        a, b, d = map(int, input().split())
        s[a].append([b, d])
        s[b].append([a, d])
        
    for k in range(c):
        de.append(int(input()))
    
    new_start = shortest(start)
    new_g = shortest(g)
    new_h = shortest(h)
    an = []
    
    for l in de:
        con1 = new_start[g] + new_g[h] + new_h[l]
        con2 = new_start[h] + new_g[l] + new_h[g]
        
        if con1 == new_start[l] or con2 == new_start[l]:
            an.append(l)
    
    an.sort()
    
    for f in an:
        print(f, end=' ')
        
    print()