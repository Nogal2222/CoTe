hour, minute = map(int, input().split())
time = int(input())

def calculate_time(hour, minute, time):
    total_min = minute + time
    if total_min // 60 > 0:
        if total_min //60 == 1:
            hour += 1
            if hour > 23:
                hour -= 24
            minute = minute + time - 60
        
        else:
            hour += 1
            time -= 60
            return calculate_time(hour, minute, time)
            #여기 현실에 반영
        
    else:
        minute = total_min
    
    return hour, minute

new_hour, new_minute = calculate_time(hour, minute, time)
print(new_hour, new_minute)