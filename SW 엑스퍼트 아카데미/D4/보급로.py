'''
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
'''
from collections import deque

T = int(input())
answers = [''] * T
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(maps, visited, acc, start, end):
    dq = deque([start])
    
    while dq:
        x, y = dq.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < N:
                if nx == 0 and ny == 0:
                    continue
                
                elif visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    acc[nx][ny] = acc[x][y] + maps[nx][ny]
                    dq.append((nx, ny))
                
                else:
                    if acc[nx][ny] > acc[x][y] + maps[nx][ny]:
                        acc[nx][ny] = acc[x][y] + maps[nx][ny]
                        dq.append((nx, ny))
    
    return acc[end[0]][end[1]]

for t in range(1, T+1):
    N = int(input())
    maps = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    acc = [[0] * N for _ in range(N)]
    start = [0, 0]
    end = [N-1, N-1]
    
    answer = bfs(maps, visited, acc, start, end)
    
    answers[t-1] = f'#{t} {answer}'
 
for i in answers:
    print(i)