# -*- coding: utf-8 -*-
from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    while q:
        x, y, z = q.popleft()
        
        for i in range(6):
            nx = x + dx[i] #h
            ny = y + dy[i] #n
            nz = z + dz[i] #m
            
            if 0<=nx<h and 0<=ny<n and 0<=nz<m and graph[nx][ny][nz] == 0:
                graph[nx][ny][nz] = graph[x][y][z] + 1
                q.append([nx, ny, nz])


dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

m, n, h = map(int, input().split())
graph = [list(list(map(int, input().split())) for i in range(n)) for j in range(h)]
q = deque([])
answer = 0

#m, n, h 가 반대로 들어감 h, n, m으로
for i in range(h): #처음 익은 토마토 좌표 q에 저장
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                q.append([i,j,k])

bfs()

for i in graph:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        answer = max(answer, max(j))

print(answer - 1)