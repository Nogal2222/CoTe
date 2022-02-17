# -*- coding: utf-8 -*-
import sys
#input = sys.stdin.readline

stack = []
sum_ = 0
k = int(input())

for i in range(k):
    n = int(input())
    
    if n == 0:
        if len(stack) == 0:
            stack.append(n)
        else:
            stack.pop()
    
    else:
        stack.append(n)
    
for i in stack:
    sum_ += i

print(sum_)