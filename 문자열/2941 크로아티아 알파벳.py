# -*- coding: utf-8 -*-
S = input()
cro_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in cro_alpha:
    S = S.replace(i,"*")

cnt = len(S)
print(cnt)