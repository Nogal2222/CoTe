# -*- coding: utf-8 -*-
import sys
#input = sys.stdin.readline

n, m = map(int, input().split())
A = []
for i in range(n):
    A.append(list(map(int, input().split())))

m, k = map(int, input().split())
B = []
for i in range(m):
    B.append(list(map(int, input().split())))

C = [[0 for i in range(k)] for j in range(n)]

for i in range(n):
    for j in range(k):
        for l in range(m):
            C[i][j] += A[i][l] * B[l][j]
            
for i in range(n):
    for j in range(k):
        print(C[i][j], end = ' ')
    print()