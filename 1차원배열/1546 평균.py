# -*- coding: utf-8 -*-
''' 내가 짠 거
N = int(input())
score = list(map(int, input().split()))
avg = 0
M = max(score)

for j in range(N): 
    score[j] = score[j]/M*100
    avg += score[j]

avg /= N     
print("%.2f" %(avg))
'''

N = int(input())
score = list(map(int, input().split()))
M = max(score)

for i in range(N):
    score[i] = score[i]/M*100

print("%.2f" %(sum(score)/N))