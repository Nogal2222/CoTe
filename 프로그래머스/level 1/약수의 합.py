def solution(n):
    answer = 0
    devisors = []
    
    for i in range(1, n+1):
        if n % i == 0:
            devisors.append(i)
    
    answer = sum(devisors)
    return answer

n = 12
result = solution(n)