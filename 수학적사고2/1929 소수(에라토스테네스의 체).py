# -*- coding: utf-8 -*-
'''시간초과
m, n = map(int, input().split())

for i in range(m, n+1):
    if i > 1:
        error = 0
        for j in range(2, i):
            temp = i%j
            if temp == 0:
                error += 1
                break
        if error == 0:
            print(i)
'''
#에라토스테네스의 체
m, n = map(int, input().split())

n += 1
prime = [True] * n

for i in range(2, int(n**0.5) + 1):
    if prime[i]:
        for j in range(2*i, n, i):
            prime[j] = False

for i in range(m, n):
    if i > 1 and prime[i] == True:
        print(i)