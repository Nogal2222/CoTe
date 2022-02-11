# -*- coding: utf-8 -*-
import sys
#input = sys.stdin.readline

n = int(input())
score = [0 for i in range(301)]
sum_score = [0 for i in range(301)]

for i in range(n):
    score[i] = int(input())

sum_score[0] = score[0]
sum_score[1] = score[0] + score[1]
sum_score[2] = max(score[1] + score[2], score[0] + score[2])

for i in range(3, n):
    sum_score[i] = max(sum_score[i-3] + score[i-1] + score[i], sum_score[i-2] + score[i])

print(sum_score[n-1])