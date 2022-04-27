def solution(n):
    cnt = 0
    
    for i in range(1, n+1):
        summation = 0
        
        for j in range(i, n+1):
            summation += j
            
            if summation == n:
                cnt += 1
                break
            
            if summation > n:
                break
    
    return cnt

n = 15

result = solution(n)