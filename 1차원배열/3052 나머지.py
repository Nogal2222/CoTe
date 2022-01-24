# -*- coding: utf-8 -*-

lst = []

for i in range(10):
    n = int(input())
    lst.append(n % 42)

lst = set(lst) '''set함수는 중복을 정리하는 함수'''
print(len(lst))
