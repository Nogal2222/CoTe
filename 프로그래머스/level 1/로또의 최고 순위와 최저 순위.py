# -*- coding: utf-8 -*-

def solution(lottos, win_nums):
    zero_cnt = lottos.count(0)
    correct = 0
    answer = [0, 0]
    
    for i in lottos:
        if i in win_nums:
            correct += 1
    
    max_rank = 7 - (correct + zero_cnt)
    min_rank = 7 - correct
    
    if max_rank > 6:
        max_rank = 6
    
    if min_rank > 6:
        min_rank = 6
    
    answer[0] = max_rank
    answer[1] = min_rank
    
    return answer

lottos = list(map(int, input().split()))
win_nums = list(map(int, input().split()))

print(solution(lottos, win_nums))