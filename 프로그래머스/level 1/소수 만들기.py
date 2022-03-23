# -*- coding: utf-8 -*-
import math

def is_prime_number(x): #소수인지 확인하는 함수
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

def solution(nums):
    sums = []
    answer = 0
    
    # sums에 세개의 수를 더한 모든 숫자를 append
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                sums.append(nums[i] + nums[j] + nums[k])

    for i in sums:
        if is_prime_number(i):
            answer += 1
    
    return answer

nums = [1,2,7,6,4]
print(solution(nums))