# -*- coding: utf-8 -*-
import sys

n = int(input()) #int(sys.stdin.readline())

lst = [''] * n
for i in range(n):
    age, name = input().split() #sys.stdin.readline().split()
    age = int(age)
    lst[i] = [age, name]

lst.sort(key = lambda x : x[0])

for j in lst:
    print(j[0], j[1])