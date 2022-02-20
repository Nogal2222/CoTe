# -*- coding: utf-8 -*-
from collections import deque
import sys
#input = sys.stdin.readline

n = int(input())
card = deque([i for i in range(1, n+1)])

while len(card) > 1:
    card.popleft()
    temp = card.popleft()
    card.append(temp)
    
print(card.pop())