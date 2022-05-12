def str_to_int(time):
    h, m, s = time.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)


def int_to_str(time):
    h = time // 3600
    h = '0' + str(h) if h < 10 else str(h)
    time %= 3600

    m = time // 60
    m = '0' + str(m) if m < 10 else str(m)
    time %= 60

    s = '0' + str(time) if time < 10 else str(time)

    return h + ':' + m + ':' + s

def solution(play_time, adv_time, logs):
    play_time = str_to_int(play_time)
    adv_time = str_to_int(adv_time)
    total_time = [0 for i in range(play_time + 1)]
    
    for l in logs:
        start, end = l.split('-')
        start = str_to_int(start)
        end = str_to_int(end)
        total_time[start] += 1
        total_time[end] -= 1
    
    #구간별 시청자수 기록
    for i in range(1, len(total_time)):
        total_time[i] += total_time[i-1]
    
    #누적 시청자수 기록
    for i in range(1, len(total_time)):
        total_time[i] += total_time[i-1]
    
    max_view = 0
    max_time = 0
    
    for i in range(adv_time - 1, play_time):
        if i >= adv_time:
            if max_view < total_time[i] - total_time[i - adv_time]:
                max_view = total_time[i] - total_time[i - adv_time]
                max_time = i - adv_time + 1
               
        else:
            if max_view < total_time[i]:
                max_view = total_time[i]
                max_time = i - adv_time + 1
    
    return int_to_str(max_time)

play_time = "02:03:55"
adv_time = "00:14:15"
logs = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]

result = solution(play_time, adv_time, logs)