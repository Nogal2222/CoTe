# -*- coding: utf-8 -*-
import sys
import heapq
#input = sys.stdin.readline
''' 시간초과
N = int(input())
heap = []

for i in range(N):
    num = int(input())
    heapq.heappush(heap, num)
    temp_heap = list(heap)
    
    for j in range((len(temp_heap) + 1) // 2 - 1):
        heapq.heappop(temp_heap)
    print(temp_heap[0])
'''

N = int(input())
max_heap = []
min_heap = []

for i in range(N):
    num = int(input())
    
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, (-num, num))
    else:
        heapq.heappush(min_heap, (num, num))
    
    if min_heap and max_heap[0][1] > min_heap[0][1]:
        temp_max = heapq.heappop(max_heap)[1]
        temp_min = heapq.heappop(min_heap)[1]
        heapq.heappush(max_heap, (-temp_min, temp_min))
        heapq.heappush(min_heap, (temp_max, temp_max))
    
    print(max_heap[0][1])