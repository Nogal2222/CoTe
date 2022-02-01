# -*- coding: utf-8 -*-
n = int(input())
result = 0
lst = []
for i in range(1, n+1):
    words = list(map(int, str(i)))
    result = i + sum(words)
    if result == n:
        lst.append(i)
        #print(i)
        #break
    #if i == n:
        #print(0)
if len(lst) == 0:
    print(0)
else:
    print(min(lst))