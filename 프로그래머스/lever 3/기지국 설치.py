from math import ceil

def solution(n, stations, w):
    answer = 0
    new_w = 2 * w + 1
    start = 1
    
    for station in stations:
        answer += max(ceil((station-w-start)/new_w), 0)
        start = station + w + 1
    
    if n >= start:
        answer += ceil((n - start +1) / new_w)
    
    return answer

n = 11
stations = [4, 11]
w = 1

result = solution(n, stations, w)