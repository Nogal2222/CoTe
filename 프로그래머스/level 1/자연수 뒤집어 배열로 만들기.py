def solution(n):
    n_list = list(str(n))
    answer = []
    
    for i in range(len(n_list)-1, -1, -1):
        answer.append(int(n_list[i]))
    
    return answer

n = 12345
result = solution(n)

''' 간단한 풀이
def digit_reverse(n):
    answer = list(map(int, reversed(str(n))))
    return answer
'''