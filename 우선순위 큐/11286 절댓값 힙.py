# -*- coding: utf-8 -*-
import sys
import heapq
#input = sys.stdin.readline

N = int(input())
heap = []

for i in range(N):
    num = int(input())
    
    if num != 0:
        heapq.heappush(heap, (abs(num), num))
    else:
        try:
            print(heapq.heappop(heap)[1])
        except:
            print(0)