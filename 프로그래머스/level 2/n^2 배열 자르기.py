def solution(n, left, right):
    answer = []
    
    for i in range(left, right + 1):
        first = i // n
        second = i % n
        
        if first < second:
            first, second = second, first
        
        answer.append(first + 1)
    
    return answer

n = 4
left = 7
right = 14

result = solution(n, left, right)
''' 시간초과
def solution(n, left, right):
    matrix = [[-1 for _ in range(n)] for _ in range(n)]

    for step in range(1, n+1):
        for i in range(step):
            for j in range(step):
                if matrix[i][j] == -1:
                    matrix[i][j] = str(step)

    strings = ''

    for i in matrix:
        string = ''.join(i)
        strings += string

    answer = list(strings)[left:right + 1]

    for i in range(len(answer)):
        answer[i] = int(answer[i])
    
    return answer
'''

''' 시간초과 2
def solution(n, left, right):
    answer = []
    
    for i in range(n ** 2):
        first = i // n
        second = i % n
        
        if first < second:
            first, second = second, first
        
        answer.append(first + 1)
    
    return answer[left:right + 1]
'''