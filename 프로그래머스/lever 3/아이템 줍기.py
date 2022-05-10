from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    # 특정 상황에서 경로를 이탈해 숏컷을 치는
    # 오류 해결을 위해 전체 좌표를 두배
    for rec in rectangle:
        rec[0] *= 2
        rec[1] *= 2
        rec[2] *= 2
        rec[3] *= 2
    
    characterX *= 2
    characterY *= 2
    itemX *= 2
    itemY *= 2
    
    visited = [[0] * 101 for _ in range(101)]
    answer = 202
    
    # 위 아래 오른쪽 왼쪽 이동
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    q = deque([(characterX, characterY, 0)])
    visited[characterX][characterY] = 1
    check = [0 for _ in range(len(rectangle))]
    
    while q:
        x, y, cnt = q.popleft()
        
        if (x, y) == (itemX, itemY) and answer > cnt:
            answer = cnt
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if (1 <= nx <= 100 and 1 <= ny <= 100) and visited[nx][ny] != 1:
                for idx, rec in enumerate(rectangle):
                    sx, sy, ex, ey = rec
                    
                    if (nx < sx or nx > ex) or (ny < sy or ny > ey):
                        check[idx] = -1
                        continue
                    
                    if (sx < nx < ex) and (sy < ny < ey):
                        check[idx] = -2
                        break
                    
                    check[idx] = 1
                
                if (-2 not in check) and (1 in check):
                    visited[nx][ny] = 1
                    q.append((nx, ny, cnt + 1))
    
    return answer // 2

rectangle = [[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]]
characterX = 9
characterY = 7
itemX = 6
itemY = 1

result = solution(rectangle, characterX, characterY, itemX, itemY)