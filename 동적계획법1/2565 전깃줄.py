# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline

n = int(input())
w = []
w_b = []
dp = [0 for i in range(n)]

for i in range(n):
    w.append(list(map(int, input().split())))

# 전봇대 A 기준으로 정렬
w.sort(key = lambda x:x[0])

# 전봇대 B의 번호 옮김
for i in range(n):
    w_b.append(w[i][1])

# 전봇대 B에서 가장 긴 증가하는 부분수열 구함
for i in range(n):
    for j in range(i):
        if w_b[i] > w_b[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

#max(dp)는 겹치지 않는 부분이니 총 개수에서 빼주면 겹치는 줄
print(n - max(dp))