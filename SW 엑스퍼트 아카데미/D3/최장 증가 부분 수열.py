T = int(input())
answers = [''] * T

for t in range(1, T+1):
    n = int(input())
    lst = list(map(int, input().split()))
    dp = [0] * n
    dp[0] = 1
    
    for i in range(1, n):
        max_cnt = 0
        
        for j in range(i-1, -1, -1):
            if lst[i] >= lst[j]:
                if max_cnt < dp[j]:
                    max_cnt = dp[j]
        
        dp[i] = max_cnt + 1
    answers[t-1] = f'#{t} {max(dp)}'

for i in answers:
    print(i)