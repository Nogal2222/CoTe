def solution(a, b):
    answer = 0
    if a != b:
        for i in range(min(a, b), max(a, b) + 1):
            answer += i
    else:
        answer = a
    
    return answer

a = 5
b = 3
resutl = solution(a, b)

'''절대값을 이용한 풀이
def adder(a, b):
    return (abs(a-b)+1)*(a+b)//2

print( adder(3, 5))
'''