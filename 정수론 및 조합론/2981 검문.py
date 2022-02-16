# -*- coding: utf-8 -*-
import sys
from math import gcd
from math import sqrt
#input = sys.stdin.readline

# 선언부
n = int(input())
ns = [int(input()) for i in range(n)]
ns.sort()
interval = []
ans = []

# 입력된 숫자들 사이의 차이
for i in range(1, n):
    interval.append(ns[i] - ns[i-1])
prev = interval[0]

# 차이들의 최대공약수
for i in range(1, len(interval)):
    prev = gcd(prev, interval[i])

# 최대공약수의 약수(제곱근까지만 탐색)
for i in range(2, int(sqrt(prev)) + 1):
    if prev % i == 0:
        ans.append(i)
        ans.append(prev//i)
ans.append(prev)

ans = list(set(ans)) # 중복제거
ans.sort()
print(*ans)