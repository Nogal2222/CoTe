# -*- coding: utf-8 -*-
T = int(input())

for i in range(T):
    k = int(input()) # k:층 
    n = int(input()) # n:호
    f0 = [x for x in range(1, n+1)]
    
    for j in range(k):
        for k in range(1, n):
            f0[k] += f0[k-1]
    print(f0[-1])