# -*- coding: utf-8 -*-
x, y = map(int, input().split())

def gcd(a, b): # 최대공약수
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b): # 최소공배수
    return a * b // gcd(a, b)

print(gcd(x, y))
print(lcm(x, y))
