# -*- coding: utf-8 -*-
'''되긴 되는데 시간초과
m = int(input())
n = int(input())
lst = []
for i in range(m, n + 1):
    cnt_lst = []
    for j in range(1, i + 1):
        temp = i % j
        
        if temp == 0:
            cnt_lst.append(1)
        else:
            cnt_lst.append(0)
        
    cnt_1 = cnt_lst.count(1)
    if cnt_1 == 2:
        lst.append(i)

if len(lst) == 0:
    print(-1)
else:
    print(lst)
    print(sum(lst))
    print(min(lst))

'''
m = int(input())
n = int(input())
lst = []

for i in range(m, n+1):
    error = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                error += 1
                break
        if error == 0:
            lst.append(i)
    
if len(lst) > 0:
    print(sum(lst))
    print(min(lst))
else:
    print(-1)
