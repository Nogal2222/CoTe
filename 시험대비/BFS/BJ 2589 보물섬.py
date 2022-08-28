from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(y, x):
    visited = [[-1] * col for _ in range(row)]
    visited[y][x] = 0
    q = deque()
    q.append((y, x))
    cnt = 1

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < row and 0 <= nx < col and visited[ny][nx] == -1 and mapp[ny][nx] == 'L':
                visited[ny][nx] = visited[y][x] + 1
                cnt = visited[ny][nx]
                q.append((ny, nx))

    return cnt


row, col = map(int, input().split())
mapp = []
start = []

for r in range(row):
    mapp.append(list(input()))

    for c in range(col):
        if mapp[r][c] == 'L':
            start.append((r, c))

maxV = 0

for y, x in start:
    maxV = max(maxV, bfs(y, x))

print(maxV)