# -*- coding: utf-8 -*-
C = int(input())

for i in range(C):
    score = list(map(int, input().split()))
    N = 0
    
    for j in range(len(score)-1):
        if score[j+1] > sum(score[1:])/score[0]:
            N += 1
    
    result = N/score[0]*100
    print("%.3f" %(result) + "%")