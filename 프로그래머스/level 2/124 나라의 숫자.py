def solution(n):
    answer = ''
    
    while n:
        if n % 3 != 0:
            answer += str(n % 3)
            n //= 3
        
        else:
            answer += '4'
            n = n // 3 - 1
    
    answer = answer[::-1]
    
    return answer

n = 6
result = solution(n)

''' 리스트로 푸는 방법
def change124(n):
    num = ['1','2','4']
    answer = ""

    while n > 0:
        n -= 1
        answer = num[n % 3] + answer
        n //= 3

    return answer
'''