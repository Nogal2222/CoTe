# -*- coding: utf-8 -*-

N = int(input())

for i in range(N):
    testcase = list(input())
    result = 0
    weight = 1
    
    for j in testcase:
        if j == "O":
            result += weight
            weight += 1
        else:
            weight = 1
    
    print(result)