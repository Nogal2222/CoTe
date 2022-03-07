# -*- coding: utf-8 -*-
from collections import deque
import sys
#input = sys.stdin.readline

def bfs():
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append([nx, ny])


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for i in range(n)]
q = deque([])
answer = 0

for i in range(n): #처음 익은 토마토 좌표 q에 저장
    for j in range(m):
        if graph[i][j] == 1:
            q.append([i,j])

bfs()

for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    answer = max(answer, max(i))

print(answer - 1)