# -*- coding: utf-8 -*-

S = input()
lst = []

for i in 'abcdefghijklmnopqrstuvwxyz':
    cnt = 0
    for j in S:
        if i == j:
            break
        else:
            cnt += 1
            if cnt == len(S):
                cnt = -1
    lst.append(cnt)

for k in lst:
    print(k, end = " ")


'''find함수
S = input()
lst = list(range(97, 123))

for i in lst:
    print(S.find(chr(i)))
'''