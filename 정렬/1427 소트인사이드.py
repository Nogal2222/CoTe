# -*- coding: utf-8 -*-
import sys

n = input() #sys.stdin.readline()
lst = []

for i in n:
    lst.append(int(i))

lst.sort(reverse = True)

for j in lst:
    print(j, end = '')
print()