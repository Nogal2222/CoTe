# -*- coding: utf-8 -*-
import sys
#input = sys.stdin.readline

def router_counter(distance):
    count = 1
    current_house = house[0]
    
    for i in range(1, N):
        if current_house + distance <= house[i]:
            count += 1
            current_house = house[i]
    
    return count


N, C = map(int, input().split())
house = list(int(input()) for i in range(N))
house.sort()
start = 1
end = house[-1] - house[0]

while start <= end:
    mid = (start + end) // 2
    
    if router_counter(mid) >= C:
        answer = mid
        start = mid + 1
    
    else:
        end = mid - 1

print(answer)