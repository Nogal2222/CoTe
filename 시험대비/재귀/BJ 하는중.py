dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def dfs(r, c, h):
    stack = [(r, c)]
    visited[r][c] = 1
    
    while stack:
        y, x = stack.pop()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and mapp[ny][nx] > h:
                stack.append((ny, nx))
                visited[ny][nx] = 1

N = int(input())
mapp = [list(map(int, input().split())) for _ in range(N)]

maxV = -1

for h in range(max(map(max, mapp))):
    visited = [[0] * N for _ in range(N)]
    cnt = 0
    
    for r in range(N):
        for c in range(N):
            cnt += 1
            dfs(r, c, h)
    
    maxV = max(maxV, cnt)