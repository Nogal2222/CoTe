# -*- coding: utf-8 -*-
import sys
#input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))
sum_list = [0] * (n + 1)

for i in range(1, n+1):
    sum_list[i] = sum_list[i-1] + arr[i-1]

answer = sys.maxsize
left, right = 0, 1

while left != n:
    if sum_list[right] - sum_list[left] >= s:
        if right - left < answer:
            answer = right - left
        
        left += 1
    
    else:
        if right != n:
            right += 1
        else:
            left += 1
    
if answer != sys.maxsize:
    print(answer)
else:
    print(0)