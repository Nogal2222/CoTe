from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs():
    q = deque()
    q.append((0, 0))
    visited[0][0] = 1
    cnt = 0

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < row and 0 <= nx < column and not visited[ny][nx]:
                if not mapp[ny][nx]:
                    visited[ny][nx] = 1
                    q.append((ny, nx))

                else:
                    mapp[ny][nx] = 0
                    visited[ny][nx] = 1
                    cnt += 1

    cnt_lst.append(cnt)

    return cnt


row, column = map(int, input().split())
mapp = [list(map(int, input().split())) for _ in range(row)]

cnt_lst = []
time = 0
cnt = 1

while cnt:
    time += 1
    visited = [[0] * column for _ in range(row)]
    cnt = bfs()

print(time-1)
print(cnt_lst[-2])