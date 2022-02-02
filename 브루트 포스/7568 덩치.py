# -*- coding: utf-8 -*-
n = int(input())
xy_lst = []

for i in range(n):
    x, y = map(int, input().split())
    xy_lst.append((x, y))
    
for j in xy_lst:
    rank = 1
    for k in xy_lst:
        if j[0] < k[0] and j[1] < k[1]:
            rank += 1
    print(rank, end = ' ')

print()