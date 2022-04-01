def solution(n):
    if (n ** 0.5) % 1 == 0:
        answer = (int(n ** 0.5) + 1) ** 2
    
    else:
        answer = -1
    return answer

n = 25000000
result = solution(n)