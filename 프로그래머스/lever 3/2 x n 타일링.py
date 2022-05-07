def solution(n):
    d = [0] * 60001
    d[1] = 1
    d[2] = 2
    
    for i in range(3, n+1):
        d[i] = (d[i-1] + d[i-2]) %  1000000007
    
    answer = d[n]
    
    return answer

n = 4

result = solution(n)

'''
피보나치 수열을 DP로 구성
'''
