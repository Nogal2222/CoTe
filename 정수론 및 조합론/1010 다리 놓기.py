# -*- coding: utf-8 -*-
import sys
from math import factorial
#input = sys.stdin.readline

def bi_co(n, k):
    if k >= 0 and k <= n:
        return factorial(n)//(factorial(k)*factorial(n-k))
    elif k < 0:
        return 0
    else:
        return 0

T = int(input())
for i in range(T):
    lst = list(map(int, input().split()))
    print(bi_co(lst[1], lst[0]))