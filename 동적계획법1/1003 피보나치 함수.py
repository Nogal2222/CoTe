# -*- coding: utf-8 -*-

import sys
input = sys.stdin.readline
''' 시간초과
cnt0 = 0
cnt1 = 0
def fibonacci(n):
    global cnt0
    global cnt1
    
    if n == 0:
        cnt0 += 1
        return 0
    
    elif n == 1:
        cnt1 += 1
        return 1
    
    else:
        return fibonacci(n-1) + fibonacci(n-2)

t = int(input())

for _ in range(t):
    n = int(input())
    fibonacci(n)
    
    print(cnt0, cnt1)
    
    cnt0 = 0
    cnt1 = 0
'''
t = int(input())

for _ in range(t):
    n = int(input())
    lst = [0,1]
    temp_n_1 = 0
    temp_n_2 = 0
    
    if n == 0:
        print(1, 0)
        
    else:
        for _ in range(1,n):
            temp_n_2 = temp_n_1
            temp_n_1 = lst[1]
            lst.pop(0)
            lst.append(temp_n_2 + temp_n_1)
        print(lst[0],lst[1])        