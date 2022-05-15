import sys
import copy
from itertools import permutations
from collections import deque

def ctrl_move(x, y, d):
    global board_c
    while True:
        nx = x + d[0]
        ny = y + d[1]
        if nx < 0 or nx >= 4 or ny < 0 or ny >= 4:
            return x, y
        
        else:
            if board_c[nx][ny] != 0:
                return nx, ny
            
            x, y = nx, ny
            
def bfs(sx, sy, ex, ey):
    global board_c
    
    dic = {0:[-1, 0], 1:[0, 1], 2:[1, 0], 3:[0, -1]}
    
    if sx == ex and sy == ey:
        return 1
    
    q = deque([[sx, sy]])
    table = [[0]*4 for _ in range(4)]
    visited = [[True]*4 for _ in range(4)]
    visited[sx][sy] = False
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dic[i][0]
            ny = y + dic[i][1]
            
            if 0 <= nx < 4 and 0 <= ny < 4 and visited[nx][ny]:
                table[nx][ny] = table[x][y] + 1
                visited[nx][ny] = False
                
                if nx == ex and ny == ey:
                    return table[nx][ny] + 1 # enter를 누르기때문에 +1 
                
                q.append([nx, ny])
        
            nx, ny = ctrl_move(x, y, dic[i])
            
            if visited[nx][ny]:
                table[nx][ny] = table[x][y] + 1
                visited[nx][ny] = False
                
                if nx == ex and ny == ey:
                    return table[nx][ny] + 1 # enter를 누르기때문에 +1 
                
                q.append([nx, ny])
    
def remove_card(card):
    global board_c, card_position
    
    for x, y in card_position[card]: 
        board_c[x][y] = 0

def restore_card(card):
    global board_c, card_position
    
    for x, y in card_position[card]: 
        board_c[x][y] = card
    

def go(sx, sy, order, card_num, count, move): 
    global answer, order_p, card_position, board_c
    
    if count == card_num:
        answer = min(answer, move)
        
        return
    
    card = order_p[order][count]
    
    left = card_position[card][0]
    right = card_position[card][1]
    
    d1 = bfs(sx, sy, left[0], left[1])             # 출발 지점 -> 해당카드 왼쪽
    d2 = bfs(left[0], left[1], right[0], right[1]) # 해당카드 왼쪽 -> 해당카드 오른쪽

    remove_card(card)
    go(right[0], right[1], order, card_num, count+1, move+d1+d2)
    restore_card(card)
    
    d1 = bfs(sx, sy, right[0], right[1])           # 출발 지점 -> 해당카드 오른쪽
    d2 = bfs(right[0], right[1], left[0], left[1]) # 해당카드 오른쪽 -> 해당카드 왼쪽
    
    remove_card(card)
    go(left[0], left[1], order, card_num, count+1, move+d1+d2)
    restore_card(card)
    
def solution(board, r, c):
    global answer, order_p, card_position, board_c
    
    answer = sys.maxsize
    board_c = copy.deepcopy(board)
    card_position = {}

    for i in range(4):
        for j in range(4):
            num = board[i][j]
            if num != 0:
                if num in card_position.keys():
                    card_position[num].append([i, j])
                
                else:
                    card_position[num] = [[i, j]]
    
    orders = [k for k, v in card_position.items()]
    order_p = list(permutations(orders, len(orders))) # 제거 순서
    
    for i in range(len(order_p)):
        go(r, c, i, len(card_position.keys()), 0, 0)
        
    return answer

board = [[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]]
r = 1
c = 0
result = solution(board, r, c)