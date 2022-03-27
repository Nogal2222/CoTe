# -*- coding: utf-8 -*-
def solution(d, budget):
    d = sorted(d)
    cnt = 0
    
    for i in d:
        if i <= budget:
            cnt += 1
            budget -= i
    
    return cnt

d = [2,2,3,3]
budget = 10

print(solution(d, budget))