def solution(progresses, speeds):
    len_progresses = len(progresses)
    day_list = [0] * len_progresses
    answer = []
    cnt = 1
    
    #남은 일수 계산
    for i in range(len_progresses):
        remain_percent = 100 - progresses[i]
        
        if remain_percent % speeds[i]:
            remain_day = remain_percent // speeds[i] + 1
        else:
            remain_day = remain_percent // speeds[i]
        day_list[i] = remain_day
    
    #배포되는 작업물 수
    biggest = day_list[0]
    
    for i in range(1, len_progresses):
        if biggest >= day_list[i]:
            cnt += 1
        
        else:
            answer.append(cnt)
            cnt = 1
            biggest = day_list[i]
    
    answer.append(cnt)
    
    return answer

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
result = solution(progresses, speeds)