# -*- coding: utf-8 -*-
"""구구단
num = int(input())

for i in range(1,10):
    print(num, " * ", i, " = ", num*i)
"""
'''더하기
num = int(input())
lst = []

for i in range(num):
    a, b = map(int, input().split())
    lst.append(int(a + b))

for j in lst:
    print(j)
'''
'''별찍기
num = int(input())

for i in range(1,num+1):
    print("*"*i)
'''
'''역별찍기
num = int(input())

for i in range(1, num+1):
    print(" "*(num-i)+"*"*i)
'''

N, X = map(int, input().split())
A = list(map(int, input().split()))

for i in range(N):
    if A[i] < X:
        print(A[i], end=" ")
