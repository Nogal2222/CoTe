# -*- coding: utf-8 -*-
import sys
#input = sys.stdin.readline

T = int(input())

for i in range(T):
    s = input()
    stack = []
    
    for j in s:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
    
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")