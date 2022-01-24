# -*- coding: utf-8 -*-
N = int(input())
lst = list(map(int, input().split()))
smallest = lst[0]
tallest = lst[0]

for i in range(len(lst)):
    if tallest < lst[i] :
        tallest = lst[i]

for j in range(len(lst)):
    if smallest > lst[j]:
        smallest = lst[j]

print(smallest, tallest, sep=" ")
