n = 3

def solution(n):
    answer = [0,1]
    for i in range(2,n+1):
        answer.append((answer[i-1] + answer[i-2]) % 1234567)
    
    return answer[-1]	

result = solution(n)

''' 재귀함수는 시간 오류
def solution(n):
    if n < 2:
        return n
    else:
        return (solution(n-1)+solution(n-2)) % 1234567
'''