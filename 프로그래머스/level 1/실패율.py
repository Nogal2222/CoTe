# -*- coding: utf-8 -*-

def solution(n, stages):
    total_user = len(stages)
    difficulty = [0] * n
    answer = [0] * n
    
    #실패율 계산
    for stage in range(1, n+1):
        if total_user != 0: #분모가 0이 아닐 때:
            stop_user = stages.count(stage)
            difficulty[stage-1] = stop_user/total_user
            total_user -= stop_user

    #랭크 지정
    difficulty_sorted = sorted(difficulty,
                               reverse = True)
    
    for i in range(n):
        rank = difficulty.index(difficulty_sorted[i])
        answer[i] = (rank + 1)
        difficulty[rank] = 2 # 중복방지
    
    return answer


n = 5 # 스테이지 수
stages = [2, 1, 2, 6, 2, 4, 3, 3] # 사용자가 멈춰있는 스테이지 번호
print(solution(n, stages))