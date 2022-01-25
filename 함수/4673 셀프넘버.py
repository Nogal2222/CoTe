# -*- coding: utf-8 -*-
''' list 사용
num_lst = list(range(1, 10001))
rmv_lst = []

for num in num_lst:
    for n in str(num):
        num += int(n)
    if num <= 10000:
        rmv_lst.append(num)

for rmv_num in set(rmv_lst):
    num_lst.remove(rmv_num)

for rslt_num in num_lst:
    print(rslt_num)
'''
'''set 사용
num_lst = set(range(1, 10000))
rmv_set = set()

for num in num_lst:
    for n in str(num):
        num += int(n)
    rmv_set.add(num)
    
rslt_lst = num_lst - rmv_set

for rlst_num in sorted(rslt_lst):
    print(rlst_num)
'''