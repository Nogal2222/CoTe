def dp_cal(L):
    dp = [0, 1, 4]
    
    if L == 3:
        return dp[1]
    
    for i in range(7, L+1, 2):
        dp.append( (i - 2) + dp[i//2 - 1] )
    
    return dp[-1]

T = int(input())
answers = [''] * T

for t in range(1, T+1):
    L = int(input())
    
    answer = dp_cal(L)
    answers[t-1] = f'#{t} {answer}'

for i in answers:
    print(i)