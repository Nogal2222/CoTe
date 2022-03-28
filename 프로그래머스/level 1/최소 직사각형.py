# -*- coding: utf-8 -*-
def solution(sizes):
    answer = 1
    
    for j in range(2):
        stack = []
        
        for i in range(len(sizes)):
            if sizes[i][0] < sizes[i][1]:
                temp = sizes[i][1]
                sizes[i][1] = sizes[i][0]
                sizes[i][0] = temp
        
            
            stack.append(sizes[i][j])
        
        answer *= max(stack)
    
    return answer

sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
print(solution(sizes))

''' 다른 사람 풀이
def solution(sizes):
    answer = max(max(x) for x in sizes) * max(min(x) for x in sizes)
    
    return answer
'''