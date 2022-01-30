# -*- coding: utf-8 -*-

x_num = []
y_num = []

for i in range(3):
    x, y = map(int, input().split())
    x_num.append(x)
    y_num.append(y)

for j in range(3):
    if x_num.count(x_num[j]) == 1:
        x4 = x_num[j]
    if y_num.count(y_num[j]) == 1:
        y4 = y_num[j]
print(x4, y4)