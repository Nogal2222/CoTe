# -*- coding: utf-8 -*-
import sys
#input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
left, right = 0, n - 1
answer = sys.maxsize
answer_list = []

while left < right:
    temp = arr[left] + arr[right]
    
    if abs(temp) < answer:
        answer = abs(temp)
        answer_list = [arr[left], arr[right]]
    
    if temp < 0:
        left += 1
    else:
        right -= 1

print(answer_list[0], answer_list[1])