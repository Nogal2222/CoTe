from copy import deepcopy

max_diff = 0
max_board = []

def solution(n, info):
    def dfs(a_score, l_score, cnt, idx, board):
        global max_diff, max_board
        
        if cnt > n:
            return 
        
        if idx > 10:
            diff = l_score - a_score
            
            if diff > max_diff:
                board[10] = n - cnt
                max_board = board
                max_diff = diff
            
            return 
        
        if cnt < n:
            board2 = deepcopy(board)
            board2[10-idx] = info[10-idx] + 1
            
            dfs(a_score, l_score+idx, cnt+info[10-idx]+1, idx+1, board2)
        
        board1 = deepcopy(board)
        
        if info[10-idx] > 0:
            dfs(a_score+idx, l_score, cnt, idx+1, board1)
        
        else:
            dfs(a_score, l_score, cnt, idx+1, board1)
    
    dfs(0, 0, 0, 0, [0]*11)
    
    answer = max_board if max_board else [-1]
    
    return answer