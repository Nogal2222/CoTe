# -*- coding: utf-8 -*-
import sys

n = int(input()) #int(sys.stdin.readline())
x_list = list(map(int,input().split())) #list(map(int,sys.stdin.readline().split()))
set_x = list(sorted(set(x_list)))

dic = {set_x[i] : i for i in range(len(set_x))}

for i in x_list:
    print(dic[i], end = ' ')
print()