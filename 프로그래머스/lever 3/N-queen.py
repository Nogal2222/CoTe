def dfs(queen, row, n):
    cnt = 0
    
    if n == row:
        return 1
    
    for col in range(n):
        queen[row] = col
        
        for i in range(row):
            if queen[i] == queen[row]:
                break
            
            if abs(queen[i] - queen[row]) == row - i:
                break
        
        else:
            cnt += dfs(queen, row + 1, n)
    
    return cnt

def solution(n):
    queen = [0] * n
    row = 0
    answer = dfs(queen, row, n)
    
    return answer

n = 4
result = solution(n)

'''시간초과
def solution(n):
    global ans 
    ans = 0
    row = [0] * n
    
    def is_promising(x):
        for i in range(x):
            
            if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
                return False
        
        return True
    
    def n_queens(x):
        global ans
        
        if x == n:
            ans += 1
    
        else:
            for i in range(n):
                # [x, i]에 퀸을 놓겠다.
                row[x] = i
                
                if is_promising(x):
                    n_queens(x+1)
    
    n_queens(0)
    
    return ans
'''