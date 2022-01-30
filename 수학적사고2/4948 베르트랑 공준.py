# -*- coding: utf-8 -*-
'''시간 초과
while True:
    n = int(input())
    if n == 0:
        break
    cnt = 0
    for i in range(n+1, 2*n + 1):
        if i > 1:
            error = 0
            for j in range(2, i):
                temp = i % j
                if temp == 0:
                    error += 1
                    break
            if error == 0:
                cnt += 1
                print(i)
    print(cnt)
'''

while True:
    n = int(input())
    if n == 0:
        break
    cnt = 0
    m = 2*n + 1
    prime = [True] * m
    
    for i in range(2, int(m**0.5) + 1):
        if prime[i]:
            for j in range(2*i, m, i):
                prime[j] = False
    
    for i in range(n+1, m):
        if i > 1 and prime[i] == True:
            cnt += 1
    print(cnt)