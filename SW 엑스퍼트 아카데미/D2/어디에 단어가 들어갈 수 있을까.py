T = int(input())
answers = [''] * T
 
for t in range(1, T+1):
    n, k= map(int, input().split())
    maps = [[]] * n
    
    for i in range(n):
        maps[i] = list(map(int, input().split()))
    answer = 0
    
    for i in range(n):
        cnt = 0
        #row
        for j in range(n):
            if maps[i][j] == 1:
                cnt += 1
            if maps[i][j] == 0 or j == n - 1:
                if cnt == k:
                    answer += 1
                cnt = 0
        #column
        for j in range(n):
            if maps[j][i] == 1:
                cnt += 1
            if maps[j][i] == 0 or j == n - 1:
                if cnt == k:
                    answer += 1
                cnt = 0

    answers[t-1] = f'#{t} {answer}'
 
for i in answers:
    print(i)