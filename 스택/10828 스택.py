# -*- coding: utf-8 -*-
import sys
#input = sys.stdin.readline

n = int(input())
num = []

for i in range(n):
    word = input().split()
    order = word[0]
    
    if order == 'push':
        num.append(int(word[1]))
    
    elif order == 'pop':
        if len(num) == 0:
            print(-1)
        else:
            print(num.pop())
    
    elif order == 'size':
        print(len(num))
    
    elif order == 'empty':
        if len(num) == 0:
            print(1)
        else:
            print(0)
    
    elif order == 'top':
        if len(num) == 0:
            print(-1)
        else:
            print(num[-1])
