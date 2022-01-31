# -*- coding: utf-8 -*-
def hanoi(n, a, b, c):
    if n == 1:
        print(a, c)
    else:
        hanoi(n-1, a, c, b)
        print(a, c)
        hanoi(n-1, b, a, c)
        

n = int(input())
sum_= 1
for i in range(n-1):
    sum_ = sum_ * 2 + 1
print(sum_)
hanoi(n, 1, 2, 3)