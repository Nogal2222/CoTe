def dfs(i, cnt):
    global max_v
    
    for j in range(1, n+1):
        if not visited[j] and adj[i][j]:
            visited[j] = 1
            dfs(j, cnt+1)
            visited[j] = 0
    
    else:
        if cnt > max_v:
            max_v = cnt

T = int(input())
answers = [''] * T

for t in range(1, T+1):
    n, m = map(int, input().split())
    adj = [[0] * (n+1) for _ in range(n+1)]
    visited = [0] * (n+1)
    max_v = 0
    
    for _ in range(m):
        x, y = map(int, input().split())
        adj[x][y] = 1
        adj[y][x] = 1
    
    for i in range(1, n+1):
        visited[i] = 1
        dfs(i, 1)
        visited[i] = 0
        
    answers[t-1] = f'#{t} {max_v}'

for i in answers:
    print(i)