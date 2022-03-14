# -*- coding: utf-8 -*-
import sys
#input = sys.stdin.readline

n = int(input())
result = [[0, []] for _ in range(n+1)]
result[1][0] = 0
result[1][1] = [1]

for i in range(2, n+1):
    #f(x-1) + 1
    result[i][0] = result[i-1][0] + 1
    result[i][1] = result[i-1][1] + [i]
    
    #f(x/3) + 1
    if i % 3 == 0 and result[i//3][0] + 1 < result[i][0]:
        result[i][0] = result[i//3][0] + 1
        result[i][1] = result[i//3][1] + [i]
    
    #f(x/2) + 1
    if i % 2 == 0 and result[i//2][0] + 1 < result[i][0]:
        result[i][0] = result[i//2][0] + 1
        result[i][1] = result[i//2][1] + [i]
    
print(result[n][0])

for i in result[n][1][::-1]:
    print(i, end = ' ')

print()