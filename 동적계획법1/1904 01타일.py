# -*- coding: utf-8 -*-
import sys
#input = sys.stdin.readline
n = int(input())
first = 1
second = 2
temp = 0

for _ in range(1, n):
    temp = first
    first = second
    second = (temp + second) % 15746
    
print(first)
#결국은 피보나치 수열