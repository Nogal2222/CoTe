# -*- coding: utf-8 -*-
def solution(n, lost, reserve):
    #intersection으로 공통 추출
    lost = sorted(lost)
    reserve = sorted(reserve)
    common = set(lost).intersection(reserve)
    
    for common_part in common:
        reserve.pop(reserve.index(common_part))
        lost.pop(lost.index(common_part))
    
    answer = n - len(lost)
    
    for index, number in enumerate(lost):
        if (number - 1) in reserve:
            answer += 1
            reserve.pop(reserve.index(number - 1))
            continue
        
        if (number + 1) in reserve:
            answer += 1
            reserve.pop(reserve.index(number + 1))
    
    return answer

n = 30
lost = 	[1, 15, 10, 29, 22, 21, 11]
reserve = [1, 19, 29, 30, 12]

print(solution(n, lost, reserve))

''' set 이용
def solution(n, lost, reserve):
    set_lost = set(lost) - set(reserve)
    set_reserve = set(reserve) - set(lost)
    
    for i in set_reserve:
        if (i - 1) in set_lost:
            set_lost.remove(i - 1)
        
        elif (i + 1) in set_lost:
            set_lost.remove(i + 1)
    
    answer = n - len(set_lost)
    
    return answer
'''
