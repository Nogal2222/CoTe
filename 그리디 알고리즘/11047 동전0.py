# -*- coding: utf-8 -*-
import sys
#input = sys.stdin.readline

n, k = map(int, input().split())
m = []
num = 0 #동전 개수

for i in range(n):
    m.append(int(input()))

for i in range(n-1, -1, -1):
    #금액을 줄이다 0이 되면 이탈
    if k == 0:
        break
    #가진 동전이 목표금액보다 크면 넘김
    if m[i] > k:
        continue
    
    num += k//m[i] #나눈 몫이 동전의 개수
    k %= m[i] #목표 금액 줄어듬
print(num)