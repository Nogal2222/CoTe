# -*- coding: utf-8 -*-
from collections import deque
import sys
#input = sys.stdin.readline

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

def bfs(x, y, target_x, target_y):
    q = deque()
    q.append([x, y])
    s[x][y] = 1
    
    while q:
        a, b = q.popleft()
        
        if a == target_x and b == target_y:
            print(s[target_x][target_y] - 1)
            return
        
        for i in range(8):
            nx = a + dx[i]
            ny = b + dy[i]
            
            if 0 <= nx < length and 0 <= ny < length and s[nx][ny] == 0:
                q.append([nx, ny])
                s[nx][ny] = s[a][b] + 1


testcase = int(input())

for i in range(testcase):
    length = int(input())
    x, y = map(int, input().split())
    target_x, target_y = map(int, input().split())
    s = [[0] * length for i in range(length)]
    bfs(x, y, target_x, target_y)