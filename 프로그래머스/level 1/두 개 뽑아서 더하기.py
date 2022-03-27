# -*- coding: utf-8 -*-
def solution(numbers):
    answer = []
    
    while numbers:
        len_numbers = len(numbers)
        
        for i in range(1, len_numbers):
            temp = numbers[0] + numbers[i]
            
            if temp not in answer:
                answer.append(temp)
        
        numbers.pop(0)
    
    answer = sorted(answer)
    
    return answer

numbers = [5,0,2,7]
print(solution(numbers))

'''j 를 i+1로 중복 안되게 함
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    return sorted(list(set(answer)))
'''