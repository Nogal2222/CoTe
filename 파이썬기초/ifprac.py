# -*- coding: utf-8 -*-

""" 윤년
year = int(input())

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) :
    print(1)
else:
    print(0)
"""
"""사분면
a,b = int(input()), int(input())

if a > 0 and b > 0 :
    print(1)
elif a < 0 and b > 0 :
    print(2)
elif a < 0 and b < 0 :
    print(3)
else:
    print(4)
"""

H, M = map(int, input().split())

if M - 45 < 0 :
    if H - 1 < 0 :
        H = 23
    else:
        H = H - 1
    M = 60 + (M - 45)
    print(H, M, sep = " ")
else :
    print(H, M, sep = " ")