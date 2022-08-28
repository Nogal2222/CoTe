from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def mapping():
    lst = [[0] * column for _ in range(row)]

    for r in range(row):
        for c in range(column):
            if mapp[r][c]:
                q.append((r, c))

            else:
                lst[r][c] = -1

    return lst


def melting(y, x):
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < row and 0 <= nx < column and n_mapp[ny][nx] == -1:
            n_mapp[y][x] += 1


def check_land(y, x):
    land = deque()
    land.append((y, x))
    n_mapp[y][x] = 0

    while land:
        y, x = land.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < row and 0 <= nx < column:
                if n_mapp[ny][nx] != -1:
                    n_mapp[ny][nx] = -1
                    land.append((ny, nx))



row, column = map(int, input().split())
mapp = [list(map(int, input().split())) for _ in range(row)]

flag = 1
year = 0

while flag:
    q = deque()
    n_mapp = mapping()

    for y, x in q:
        melting(y, x)
        mapp[y][x] -= n_mapp[y][x]

        if mapp[y][x] < 0:
            mapp[y][x] = 0

    if not q:
        year = 1
        break

    cy, cx = q[0]
    check_land(cy, cx)

    for r in range(row):
        for c in range(column):
            if n_mapp[r][c] != -1:
                flag = 0
                break

        if not flag:
            break

    year += 1

print(year - 1)