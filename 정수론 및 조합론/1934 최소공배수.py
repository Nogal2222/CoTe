# -*- coding: utf-8 -*-
import sys
#input = sys.stdin.readline

def gcd(a, b): # 최대공약수
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b): # 최소공배
    return a * b // gcd(a, b)

T = int(input())
for i in range(T):
    x, y = map(int, input().split())
    print(lcm(x, y))
