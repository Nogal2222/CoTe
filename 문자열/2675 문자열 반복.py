# -*- coding: utf-8 -*-
''' 내가 짠 코드 결과는 나오는데 틀렸다고 나옴
T = int(input())

for i in range(T):
    RS = list(input().split())
    
    for j in range(len(RS[1])):
        print(RS[1][j] * int(RS[0]), end = "")
'''

T = int(input())

for i in range(T):
    R, S = input().split()
    rslt = ''
    
    for j in S:
        rslt += int(R) * j
    
    print(rslt)