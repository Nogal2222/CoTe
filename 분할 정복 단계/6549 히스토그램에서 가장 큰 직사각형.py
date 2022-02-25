# -*- coding: utf-8 -*-
from collections import deque
import sys
#input = sys.stdin.readline

while True:
    rec = list(map(int, input().split()))
    n = rec.pop(0)
    
    if n == 0:
        break
    
    stack = deque([])
    answer = 0
    
    for i in range(n):
        while len(stack) != 0 and rec[stack[-1]] > rec[i]:
            temp = stack.pop()
            
            if len(stack) == 0:
                width = i
            else:
                width = i - stack[-1] -1
            
            answer = max(answer, width * rec[temp])
        
        stack.append(i)
    
    while len(stack) != 0:
        temp = stack.pop()
        
        if len(stack) == 0:
            width = n
        else:
            width = n - stack[-1] -1
        answer = max(answer, width * rec[temp])
    
    print(answer)