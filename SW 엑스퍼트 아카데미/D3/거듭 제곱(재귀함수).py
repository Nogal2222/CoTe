''' 2^n의 시간복잡도
def square(num, times):
    rslt = 1
    
    for i in range(times):
        rslt *= num
    
    return rslt
'''

for t in range(1, 11):
    tc = int(input())
    num, times = map(int, input().split())
    #dp로 구현해보자
    dp = [0 for _ in range(times+1)]
    dp[0] = num
    
    def power(times):
        if times <= 1:
            return num
        
        if dp[times] == 0:
            dp[times] = power(times-1) * num
    
        return dp[times]
    
    answer = power(times)
    
    print(f'#{tc} {answer}')