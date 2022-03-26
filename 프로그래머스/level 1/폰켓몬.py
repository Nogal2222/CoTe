# -*- coding: utf-8 -*-
def solution(nums):
    answer = 0
    length = len(nums) // 2
    temp = list(set(nums))
    
    for routine in range(len(temp)):
        if answer < length:
            answer += 1
    
    return answer

nums = [3,3,3,2,2,4]

print(solution(nums))