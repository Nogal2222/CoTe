# -*- coding: utf-8 -*-
import sys
#input = sys.stdin.readline

n = int(input())
dp = list(map(int, input().split()))
x = int(input())
dp.sort()
left, right = 0, n - 1
answer = 0

while left < right:
    temp = dp[left] + dp[right]
    
    if temp == x:
        answer += 1
    
    if temp < x:
        left += 1
        continue
    
    right -= 1

print(answer)