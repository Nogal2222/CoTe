# -*- coding: utf-8 -*-
import math
import sys
#input = sys.stdin.readline

def dijkstra():
    n, m, k = map(int, input().split())
    table = [[] for _ in range(n+1)]
    
    for _ in range(k):
        u, v, c, d = map(int, input().split())
        table[u].append([v, c, d])
    
    stat = [[inf] * (m + 1) for _ in range(n+1)]
    stat[1][0] = 0
    
    for money in range(m+1):
        for vertex in range(1, n+1):
            if stat[vertex][money] != inf:
                for v, c, d in table[vertex]:
                    if money + c <= m:
                        stat[v][money+c] = min(stat[v][money+c], stat[vertex][money] + d)
    
    rslt = min(stat[n])
    
    if rslt == inf:
        print("Poor KCM")
    else:
        print(rslt)


inf = math.inf
testcase = int(input())
for _ in range(testcase):
    dijkstra()