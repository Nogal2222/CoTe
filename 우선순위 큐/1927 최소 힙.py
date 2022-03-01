# -*- coding: utf-8 -*-
import heapq
import sys
#input = sys.stdin.readline

n = int(input())
heap = []

for i in range(n):
    num = int(input())
    
    if num != 0:
        heapq.heappush(heap, num)
    
    else:
        try:
            print(heapq.heappop(heap))
        except:
            print(0)