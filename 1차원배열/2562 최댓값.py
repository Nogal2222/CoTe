# -*- coding: utf-8 -*-
''' 내가 한거
largest = 0
N = -1
lst = []

for i in range(9):
    lst.append(int(input()))

for j in range(len(lst)):
    N += 1
    if largest < lst[j]:
        largest = lst[j]

print(largest)
print(N)
'''

'''다른 코드'''

lst = []
for i in range(9):
    lst.append(int(input()))

print(max(lst))
print(lst.index(max(lst))+1)