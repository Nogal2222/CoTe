from collections import deque

# 이동방향
d = [[1,0], [-1, 0], [0,1], [0,-1]]

def solution(maps):
    rows = len(maps)
    columns = len(maps[0])
    progress_map = [[-1 for _ in range(columns)] for _ in range(rows)]
    q = deque()
    q.append([0,0]) # 큐에 초기값 추가
    progress_map[0][0] = 1 # 출발점

    while q:
        y, x = q.popleft()

        for i in range(4):
            new_y = y + d[i][0]
            new_x = x + d[i][1]

            if -1 < new_y < rows and -1 < new_x < columns:
                if maps[new_y][new_x] == 1:
                    if progress_map[new_y][new_x] == -1:
                        progress_map[new_y][new_x] = progress_map[y][x] + 1
                        q.append([new_y, new_x])

    answer = progress_map[-1][-1]
    
    return answer

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
result = solution(maps)