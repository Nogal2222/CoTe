# -*- coding: utf-8 -*-
n = int(input())

def solution(n):
    temp = ''
    
    while n != 0:
        temp += str((n%3))
        n //= 3
    
    answer = int(temp, 3)
    
    return answer

print(solution(n))