# -*- coding: utf-8 -*-
n = int(input())
lst = list(map(int, input().split()))
cnt = 0
for i in range(n):
    cnt_lst = []
    for j in range(1, lst[i]+1):
        temp = lst[i] % j
        
        if temp == 0:
            cnt_lst.append(1)
        else:
            cnt_lst.append(0)
        
    cnt_1 = cnt_lst.count(1)
    if cnt_1 == 2:
        cnt += 1
print(cnt)