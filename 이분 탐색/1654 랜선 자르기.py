# -*- coding: utf-8 -*-
import sys
#input = sys.stdin.readline

K, N = map(int, input().split())
LAN = list(int(input()) for i in range(K))
start = 1
end = max(LAN)

while start <= end:
    mid = (start + end) // 2
    lines = 0
    
    for i in LAN:
        lines += i // mid
    
    if lines >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)