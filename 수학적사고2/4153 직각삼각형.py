# -*- coding: utf-8 -*-
while True:
    lst = list(map(int, input().split()))
    lst.sort()
    slope = max(lst)
    if slope == 0:
        break
    
    if slope**2 == lst[0]**2 + lst[1]**2:
        print("right")
    else:
        print("wrong")