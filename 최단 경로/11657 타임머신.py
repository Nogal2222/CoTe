# -*- coding: utf-8 -*-
import sys
#input = sys.stdin.readline

def bellmanFord():
    global flag
    
    for re in range(n):
        
        for i in range(1, n+1):
            
            for new_n, weight in graph[i]:
                
                if dp[i] != inf and dp[new_n] > dp[i] + weight:
                    dp[new_n] = dp[i] + weight
                    
                    if re == (n - 1):
                        flag = 0


inf = sys.maxsize
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
dp = [inf] * (n+1)
dp[1] = 0
flag = 1

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

bellmanFord()

if not flag:
    print(-1)
else:
    for i in dp[2:]:
        print(i if i != inf else -1)