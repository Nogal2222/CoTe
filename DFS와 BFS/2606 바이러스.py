# -*- coding: utf-8 -*-
import sys
#input = sys.stdin.readline

def dfs(v):
    global cnt
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0:
            dfs(i)
            cnt += 1


n = int(input())
m = int(input())
graph = [[] * n for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
visited = [0] * (n+1)

dfs(1)
print(cnt)