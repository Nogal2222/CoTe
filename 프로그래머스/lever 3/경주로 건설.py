from collections import deque
import sys

def solution(board):
    dx = [0, 1, -1, 0]
    dy = [-1, 0, 0, 1]
    q = deque()
    q.append([0, 0, -1])
    len_b = len(board)
    n_board = [[[sys.maxsize] * 4 for _ in range(len_b)] for _ in range(len_b)]
    n_board[0][0] = [0, 0, 0, 0]
    
    while q:
        x, y, car_dr = q.popleft()
        
        for road_dr in range(4):
            if road_dr + car_dr == 3:
                continue
            
            nx = x + dx[road_dr]
            ny = y + dy[road_dr]
            cost = 100
            
            if road_dr != car_dr and car_dr != -1:
                cost += 500
            
            if 0 <= nx < len_b and 0 <= ny < len_b and board[nx][ny] != 1 and n_board[nx][ny][road_dr] > cost + n_board[x][y][car_dr]:
                n_board[nx][ny][road_dr] = cost + n_board[x][y][car_dr]
                q.append([nx, ny, road_dr])
    
    answer = min(n_board[len_b - 1][len_b - 1])
    
    return answer

board = [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]

result = solution(board)

''' 마지막 테스트 케이스 실패
def solution(board):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q = deque([])
    q.append((0, 0, 0, 0))
    len_b = len(board)
    n_board = list([0] * len_b for _ in range(len_b))
    
    while q:
        x, y, car_dr, cost = q.popleft()
        
        for road_dr in range(4):
            nx = x + dx[road_dr]
            ny = y + dy[road_dr]
            
            if 0 <= nx < len_b and 0 <= ny < len_b:
                if board[ny][nx] != 1:
                    if nx == 0 and ny == 0:
                        continue
                    
                    if x == 0 and y == 0:
                        n_cost = cost + 100
                    
                    else:
                        if car_dr == road_dr:
                            n_cost = cost + 100
                        
                        else:
                            n_cost = cost + 600
                    
                    if n_board[ny][nx] == 0:
                        n_board[ny][nx] = n_cost
                        q.append((nx, ny, road_dr, n_cost))
                    
                    else:
                        if n_board[ny][nx] >= n_cost:
                            n_board[ny][nx] = n_cost
                            q.append((nx, ny, road_dr, n_cost))
    
    answer = n_board[-1][-1]
    
    return answer
'''