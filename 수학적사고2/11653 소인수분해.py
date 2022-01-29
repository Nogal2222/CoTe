# -*- coding: utf-8 -*-
'''되긴 되는데 시간초과
n = int(input())
lst = []
#소수 구하기
for i in range(1, n+1):
    error = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                error += 1
                break
        if error == 0:
            lst.append(i)
#소수로 나눠서 결과
while n > 1:
    for j in lst:
        if n%j == 0:
            print(j)
            break
    n /= j
'''

n = int(input())

if n == 1:
    print('')

for i in range(2, n+1):
    if n%i == 0:
        while n%i == 0:
            print(i)
            n /= i