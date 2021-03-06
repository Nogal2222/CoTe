# -*- coding: utf-8 -*-
import sys
#input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
order = max(dp)
lst = []

for i in range(n-1, -1, -1):
    if dp[i] == order:
        lst.append(arr[i])
        order -= 1

lst.reverse()

for i in lst:
    print(i, end = ' ')

print()