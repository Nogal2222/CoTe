# -*- coding: utf-8 -*-
import sys
#input = sys.stdin.readline

def find_path(i, j):
    if trace[i][j] == 0:
        return []
    
    k = trace[i][j]
    
    return find_path(i, k) + [k] + find_path(k, j)

n = int(input())
m = int(input())
inf = sys.maxsize
dp = [[inf] * (n + 1) for _ in range(n + 1)]

for i in range(1, n+1):
    dp[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    dp[a][b] = min(dp[a][b], c)

trace = [[0] * (n + 1) for _ in range(n + 1)]

#플로이드 와샬
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if dp[i][j] > dp[i][k] + dp[k][j]:
                dp[i][j] = dp[i][k] + dp[k][j]
                trace[i][j] = k

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if dp[i][j] != inf:
            print(dp[i][j], end = ' ')
        else:
            print(0, end = ' ')
    
    print()

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if dp[i][j] in [0, inf]:
            print(0)
            continue
        
        path = [i] + find_path(i, j) + [j]
        print(len(path), end = ' ')
        print(*path)

print()