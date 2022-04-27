fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

import math

def change_min(IN, OUT):
    hour_in, minute_in = map(int, IN.split(':'))
    hour_out, minute_out = map(int, OUT.split(':'))
    minutes_in = hour_in * 60 + minute_in
    minutes_out = hour_out * 60 + minute_out
    parked_time = minutes_out - minutes_in
    
    return parked_time

def solution(fees, records):
    base_min, base_fee, per_min, per_fee = fees
    check = {}
    check_time = {}
    
    for record in records:
        time, car_num, inout = record.split()
        
        if inout == "IN":
            check[car_num] = time
        
        else:
            if car_num not in check_time:
                check_time[car_num] = change_min(check[car_num], time)
            
            else:
                check_time[car_num] += change_min(check[car_num], time)
            
            check[car_num] = '0'
    
    for key, value in check.items():
        if value != '0':
            if key in check_time:
                check_time[key] += change_min(value, '23:59')
            
            else:
                check_time[key] = change_min(value, '23:59')
    
    check_time = sorted(check_time.items())
    
    answer = []
    
    for car_num, total_time in check_time:
        if total_time <= base_min:
            answer.append(base_fee)
        
        else:
            answer.append(base_fee + math.ceil((total_time - base_min) / per_min) * per_fee)
    
    return answer

result = solution(fees, records)