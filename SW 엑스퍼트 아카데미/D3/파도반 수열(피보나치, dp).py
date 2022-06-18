def fib(dp, n):
    if n < 3:
        return dp[0:n]
    
    for i in range(3, n):
        dp[i] = dp[i-3] + dp[i-2]
    
    return dp

T = int(input())
answers = [''] * T

for t in range(1, T+1):
    n = int(input())
    dp = [0] * n
    dp[:3] = [1, 1, 1]
    
    answer = fib(dp, n)[-1]
    answers[t-1] = f'#{t} {answer}'

for i in answers:
    print(i)