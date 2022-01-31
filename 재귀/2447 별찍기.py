# -*- coding: utf-8 -*-
'''
def star(n):
    global Map
    
    if n == 3:
        Map[0][:3] = Map[2][:3] = [1]*3 #첫번째 세번째 줄 [1,1,1]
        Map[1][:3] = [1,0,1] #두번째 줄 [1,0,1]
        return
    
    a = n//3
    star(a)
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            for k in range(a):
                Map[a*i+k][a*j:a*(j+1)] = Map[k][:a]



N = int(input())

Map = [[0 for i in range(N)] for i in range(N)]
star(N)

for i in Map:
    for j in i:
        if j:
            print('*', end = '')
        else:
            print(' ', end = '')
    print()
'''

def star(n:int, x:list)->list:
    out = []
    if n == 3:
        return x
    else:
        for i in x:
            out.append(i*3)
        for i in x:
            out.append(i + ' ' * len(x) + i)
        for i in x:
            out.append(i*3)
        return star(n//3, out)


n = int(input())
first = ['***', '* *', '***']
final = star(n, first)
for i in final:
    print(i)