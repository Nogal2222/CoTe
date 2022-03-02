# -*- coding: utf-8 -*-
import sys
#input = sys.stdin.readline

N = int(input())
matrix = [list(map(int, input().split())) for i in range(N)]
dp = [[0] * N for i in range(N)]

for i in range(1, N):
    for j in range(N - i):
        temp = i + j
        dp[j][temp] = 2 ** 32
        
        for k in range(j, temp):
            dp[j][temp] = min(dp[j][temp], dp[j][k] + dp[k+1][temp] + matrix[j][0] * matrix[k][1] * matrix[temp][1])

print(dp[0][N-1])