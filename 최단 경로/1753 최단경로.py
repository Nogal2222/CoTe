# -*- coding: utf-8 -*-
import sys
from heapq import heappush, heappop
#input = sys.stdin.readline

def shortest(start):
    dp[start] = 0
    heappush(heap, [0, start])
    
    while heap:
        w, n = heappop(heap)
        
        for new_n, wei in S[n]:
            new_w = wei + w
            
            if new_w < dp[new_n]:
                dp[new_n] = new_w
                heappush(heap, [new_w, new_n])


inf = 100000000
V, E = map(int, input().split())
K = int(input())
S = [[] for _ in range(V+1)]
dp = [inf] * (V + 1)
heap = []

for i in range(E):
    U, V, W = map(int, input().split())
    S[U].append([V, W])

shortest(K)

for i in dp[1:]:
    print(i if i != inf else "INF")