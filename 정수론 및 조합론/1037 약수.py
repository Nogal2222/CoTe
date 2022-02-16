# -*- coding: utf-8 -*-
import sys
#input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))

if n == 1:
    print(num[0] * num[0])
else:
    print(max(num) * min(num))