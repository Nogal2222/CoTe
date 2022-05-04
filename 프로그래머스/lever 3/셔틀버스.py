def solution(n, t, m, timetable):
    answer = 0
    crew_arrive_time = [int(time[:2]) * 60 + int(time[3:]) for time in timetable]
    crew_arrive_time.sort()
    bus_arrive_time = [9 * 60 + t * i for i in range(n)]
    
    idx = 0
    
    for time in bus_arrive_time:
        crew_cnt = 0
        
        while crew_cnt < m and idx < len(crew_arrive_time) and crew_arrive_time[idx] <= time:
            idx += 1
            crew_cnt += 1
        
        if crew_cnt < m:
            answer = time
        
        else:
            answer = crew_arrive_time[idx - 1] - 1
    
    return str(answer // 60).zfill(2) + ":" + str(answer % 60).zfill(2)

n = 1
t = 1
m = 5
timetable = ["08:00", "08:01", "08:02", "08:03"]

result = solution(n, t, m, timetable)