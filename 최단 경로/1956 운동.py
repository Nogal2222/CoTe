# -*- coding: utf-8 -*-
import sys
#input = sys.stdin.readline

#V: 마을 갯수, E: 도로 갯수
V, E = map(int, input().split())
inf = sys.maxsize
s = [[inf for _ in range(V)] for _ in range(V)]

for _ in range(E):
    a, b, c = map(int, input().split())
    s[a-1][b-1] = c

for k in range(V):
    for i in range(V):
        for j in range(V):
            s[i][j] = min(s[i][j], s[i][k] + s[k][j])

rslt = inf

for i in range(V):
    rslt = min(rslt, s[i][i])

if rslt == inf:
    print(-1)
else:
    print(rslt)