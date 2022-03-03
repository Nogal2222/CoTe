# -*- coding: utf-8 -*-
import sys
#input = sys.stdin.readline

def cal(num, weight):
    if num > num_scale:
        return
    
    if dp[num][weight]:
        return
    
    dp[num][weight] = 1
    
    cal(num+1, weight)
    cal(num+1, weight + scale[num-1])
    cal(num+1, abs(weight - scale[num-1]))

num_scale = int(input())
scale = list(map(int, input().split()))
num_marble = int(input())
marble = list(map(int, input().split()))
dp = [[0 for j in range((i+1) * 500 + 1)] for i in range(num_scale + 1)]
answer = []

cal(0, 0)

for i in marble:
    if i > 30 * 500:
        answer.append("N")
        continue
    if dp[num_scale][i] == 1:
        answer.append("Y")
    else:
        answer.append("N")

print(*answer)