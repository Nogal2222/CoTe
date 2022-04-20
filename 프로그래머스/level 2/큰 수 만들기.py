def solution(number, k):
    stack = []
    
    for num in number:
        while k > 0 and stack and stack[-1] < num:
            stack.pop()
            k -= 1
        
        stack.append(num)
    
    return ''.join(stack[:len(stack) - k])

number = "1231234"
k = 3

result = solution(number, k)

''' 시간초과 나는 코드
from itertools import combinations

def solution(number, k):
    new_k = len(number) - k
    
    combi = list(combinations(number, new_k))
    
    new_lst = [[0 for _ in range(new_k)] for _ in range(len(combi))]

    for i in range(len(combi)):
        for j in range(new_k):
            temp = int(combi[i][j])
            new_lst[i][j] = temp
    
    new_lst.sort(reverse = True)
    answer = ''
    
    for i in new_lst[0]:
        answer += str(i)
    
    return answer
'''