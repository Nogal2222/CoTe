def check_five(board):
    dx = [1, 0, 1, -1]
    dy = [0, 1, 1, 1]
    
    for y in range(N):
        for x in range(N):
            if board[y][x] == 'o':
                for i in range(4):
                    nx = x
                    ny = y
                    cnt = 0
                    
                    while 0 <= nx <= N-1 and 0 <= ny <= N-1 and board[ny][nx] == 'o':
                        cnt += 1
                        nx += dx[i]
                        ny += dy[i]
                    
                    if cnt >= 5:
                        return "YES"
    
    return "NO"

T = int(input())
answers = [''] * T

for t in range(1, T+1):
    N = int(input())
    board = [input() for _ in range(N)]
    answer = check_five(board)
    
    answers[t-1] = f'#{t} {answer}'

for i in answers:
    print(i)