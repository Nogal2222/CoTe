def solution(n, s):
    if n > s:
        return [-1]
    
    answer = []
    initial = s // n
    
    for _ in range(n):
        answer.append(initial)
    
    idx = len(answer) - 1
    
    for _ in range(s % n):
        answer[idx] += 1
        idx -= 1
    
    return answer

n = [2, 2, 2]
s = [9, 1, 8]
result = [[], [], []]

for i in range(3):
    result[i] = solution(n[i], s[i])