# -*- coding: utf-8 -*-
import sys
#input = sys.stdin.readline

Testcase = int(input())

for i in range(Testcase):
    chapters = int(input())
    pages = list(map(int, input().split()))
    dp = [[0] * (chapters + 1) for _ in range(chapters + 1)]
    
    for j in range(chapters - 1):
        dp[j][j+1] = pages[j] + pages[j+1]
        
        for k in range(j+2, chapters):
            dp[j][k] = dp[j][k-1] + pages[k]
    
    for l in range(2, chapters):
        for m in range(chapters - l):
            temp = l + m
            dp[m][temp] += min([dp[m][o] + dp[o+1][temp] for o in range(m, temp)])
            
    print(dp[0][chapters - 1])