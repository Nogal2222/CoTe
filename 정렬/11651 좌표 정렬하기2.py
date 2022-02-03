# -*- coding: utf-8 -*-
#import sys
n = int(input()) #int(sys.stdin.readline())
lst = [0] * n

for i in range(n):
    [x, y] = map(int, input().split()) #map(int, sys.stdin.readline().split())
    rev = [y, x]
    lst[i] = rev
    
lst.sort()

for j in range(n):
    print(lst[j][1], lst[j][0])