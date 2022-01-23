# -*- coding: utf-8 -*-
'''while 10952번
while True:
    A, B = map(int, input().split())
    
    if A == 0 and B == 0 :
        break
    else:
        print(A+B)
'''

''' 10952번 출력만 따로 뺸것
lst = []
n = 0

while True:
    A, B = map(int, input().split())
    lst.append(A+B)
    
    if A == 0 and B == 0:
        break

while n < len(lst)-1:
    print(lst[n])
    n += 1
'''
'''while 10951 EOF Error 처리
while True:
    try:
        A, B = map(int, input().split())
    
    except:
        break
    print(A+B)
'''

num = int(input())
check = num
new_num, temp, N = 0, 0, 0

while True:
    temp = int(num/10) + num%10
    new_num = (num%10)*10 + temp%10
    N += 1
    num = new_num
    if new_num == check:
        break

print(N)

