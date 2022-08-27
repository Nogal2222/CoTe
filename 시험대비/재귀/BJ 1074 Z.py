def recur(y, x, N, r, c):
    global cnt
    
    if N == 1:
        return
    
    if N == 2 and y <= r+y < y + N and x <= c+x < x + N:
        print(cnt + weight[r%2][c%2])
        return
    
    if 0 <= r < N//2 and 0 <= c < N//2: # 1사분면
        recur(y, x, N//2, r, c)
    
    elif 0 <= r < N//2 and  N//2 <= c < N: # 2사분면
        cnt += (N//2) ** 2
        c -= (N//2)
        recur(y, x+ N//2, N//2, r, c)
        
    elif N//2 <= r < N and 0 <= c < N//2: # 3사분면
        cnt += ((N//2) ** 2) * 2
        r -= (N//2)
        recur(y + N//2, x, N//2, r, c)
        
    else: # 4사분면
        cnt += ((N//2) ** 2 ) * 3
        r -= (N//2)
        c -= (N//2)
        recur(y+ N//2, x+ N//2, N//2, r, c)
        
N, r, c = map(int, input().split())
cnt = 0
weight = [[0, 1], [2, 3]]

recur(0, 0, 2**N, r, c)

''' 메모리초과
def recur(y, x, N):
    global cnt
    
    if N == 1:
        return
    
    if N == 2:
        for i in range(y, y+N):
            for j in range(x, x+N):
                lst[i][j] = cnt
                cnt += 1
    
    recur(y, x, N//2)
    recur(y, x+ N//2, N//2)
    recur(y + N//2, x, N//2)
    recur(y+ N//2, x+ N//2, N//2)

N, r, c = map(int, input().split())
cnt = 0
lst = [[0] * (2 ** N) for _ in range(2 ** N)]

recur(0, 0, 2**N)
print(lst[r][c])
'''
''' 시간초과
def recur(y, x, N):
    global cnt
    
    if N == 1:
        return
    
    if N == 2:
        for i in range(y, y+N):
            for j in range(x, x+N):
                if i == r and j == c:
                    print(cnt)
                    return
                cnt += 1
    
    recur(y, x, N//2)
    recur(y, x+ N//2, N//2)
    recur(y + N//2, x, N//2)
    recur(y+ N//2, x+ N//2, N//2)

N, r, c = map(int, input().split())
cnt = 0

recur(0, 0, 2**N)
'''