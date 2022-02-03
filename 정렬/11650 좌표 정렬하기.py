# -*- coding: utf-8 -*-
#import sys
n = int(input()) #int(sys.stdin.readline())
lst = [0] * n

for i in range(n):
    lst[i] = list(map(int, input().split())) #list(map(int, sys.stdin.readline().split()))

lst.sort()

for j in range(n):
    print(lst[j][0], lst[j][1], sep = ' ')