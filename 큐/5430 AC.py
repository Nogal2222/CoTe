# -*- coding: utf-8 -*-
from collections import deque
import sys
#input = sys.stdin.readline

T = int(input())

for i in range(T):
    p = input().rstrip()
    n = int(input())
    arr = input().rstrip()[1:-1].split(",")
    q = deque(arr)
    
    rev, front, back = 0, 0, len(q) - 1
    flag = 0
    
    if n == 0:
        q = []
        front = 0
        back = 0
    
    for j in p:
        if j == "R":
            rev += 1
        elif j == "D":
            if len(q) < 1:
                flag = 1
                print("error")
                break
            else:
                if rev % 2 == 0:
                    q.popleft()
                else:
                    q.pop()
    
    if flag == 0:
        if rev % 2 == 0:
            print("[" + ",".join(q) + "]")
        else:
            q.reverse()
            print("[" + ",".join(q) + "]")