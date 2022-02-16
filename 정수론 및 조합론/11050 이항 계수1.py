# -*- coding: utf-8 -*-
import sys
from math import factorial

def bi_co(n, k):
    if k >= 0 and k <= n:
        return factorial(n)//(factorial(k)*factorial(n-k))
    elif k < 0:
        return 0
    else:
        return 0

n, k = map(int, input().split())
print(bi_co(n, k))