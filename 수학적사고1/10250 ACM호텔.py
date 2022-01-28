# -*- coding: utf-8 -*-

t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())
    #h:층수 w:층의 방수 n:몇번째손님
    floor = n % h
    
    if floor == 0:
        room_num = n//h
        floor = h
    else:
        room_num = n//h + 1
    
    print(floor*100 + room_num)
    