# -*- coding: utf-8 -*-
from heapq import heappush, heappop
import sys
#input = sys.stdin.readline

def shortest(start):
    dp = [inf for i in range(N+1)]
    dp[start] = 0
    heap = []
    heappush(heap, [0, start])
    
    while heap:
        W, C = heappop(heap)
        
        for new_N, new_W in S[C]:
            way = new_W + W
            
            if dp[new_N] > way:
                dp[new_N] = way
                heappush(heap, [way, new_N])
    return dp


N, E = map(int, input().split())
S = [[] for i in range(N+1)]
inf = sys.maxsize

for i in range(E):
    a, b, c = map(int, input().split())
    S[a].append([b, c])
    S[b].append([a, c])

V1, V2 = map(int, input().split())

one = shortest(1)
V1_rslt = shortest(V1)
V2_rslt = shortest(V2)
cnt = min(one[V1] + V1_rslt[V2] + V2_rslt[N], one[V2] + V2_rslt[V1] + V1_rslt[N])
print(cnt if cnt < inf else -1)