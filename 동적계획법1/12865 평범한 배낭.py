# -*- coding: utf-8 -*-
import sys
#input = sys.stdin.readline

n, k = map(int, input().split())
dp = [[0] * (k + 1) for i in range(n + 1)]
w = [0]
v = [0]

for i in range(n):
    w_, v_ = map(int, input().split())
    w.append(w_)
    v.append(v_)

#dp[i][j] 에서 [i]에는 입력회차, [j]에는 w를 정하고
#dp[i][j]위치의 값은 v값이다
#https://pacific-ocean.tistory.com/226 참조
for i in range(1, n + 1):
    for j in range(k, 0, -1):
        if j - w[i] >= 0:
            dp[i][j] = max(dp[i-1][j], v[i] + dp[i-1][j-w[i]])
        else:
            dp[i][j] = dp[i-1][j]

print(max(dp[n]))