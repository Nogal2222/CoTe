# -*- coding: utf-8 -*-

N = input().split()
lst = []
for i in range(len(N)):
    temp = ''
    len_part = len(N[i])
    for j in range(len_part):
        add = N[i][(len_part - 1) - j]
        temp += add
    lst.append(int(temp))

max_lst = max(lst)
print(max_lst)

'''if-else 코드
N, M = input().split()
N = int(N[::-1]) #[::-1] 역순
M = int(M[::-1])

if N > M :
    print(N)
else :
    print(M)
'''

''' 삼항 연산자 코드
N, M = input().split()
N = int(N[::-1]) #[::-1] 역순
M = int(M[::-1])

print(N) if N > M else print(M)