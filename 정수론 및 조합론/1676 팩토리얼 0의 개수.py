# -*- coding: utf-8 -*-
from math import factorial
import sys
#input = sys.stdin.readline

n = int(input())
a = str(factorial(n))
cnt = 0
for i in range(len(a)-1, -1, -1):
    if int(a[i]) == 0:
        cnt += 1
    else:
        break

print(cnt)