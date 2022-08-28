from collections import deque
import copy

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs():
    global answer
    q = deque()
    c_mapp = copy.deepcopy(mapp)

    for r in range(row):
        for c in range(col):
            if c_mapp[r][c] == 2:
                q.append((r, c))

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 < ny <= row or 0 <= nx < col and not c_mapp[ny][nx]:
                c_mapp[ny][nx] = 2
                q.append((ny, nx))

    cnt = 0

    for i in range(row):
        cnt += c_mapp[i].count(0)

    answer = max(answer, cnt)


def wall(cnt):
    if cnt == 3:
        bfs()
        return

    for r in range(row):
        for c in range(col):
            if mapp[r][c] == 0:
                mapp[r][c] = 1
                wall(cnt+1)
                mapp[r][c] = 0


row, col = map(int, input().split())
mapp = [list(map(int, input().split())) for _ in range(row)]

answer = 0
wall(0)
print(answer)