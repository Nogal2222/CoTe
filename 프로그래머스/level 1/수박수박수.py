def solution(n):
    answer = '수'
    while n > 1:
        n -= 1
        
        if answer[-1] == '박':
            answer += '수'
        else:
            answer += '박'
        
        
    return answer

n = 10
result = solution(n)

'''
def water_melon(n):
    s = "수박" * n
    return s[:n]
'''