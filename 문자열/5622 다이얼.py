# -*- coding: utf-8 -*-

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
S = input()
rslt = 0

for i in range(len(S)):
    for j in dial:
        if S[i] in j:
            rslt += dial.index(j) + 3

print(rslt)