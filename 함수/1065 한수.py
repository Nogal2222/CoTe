# -*- coding: utf-8 -*-

def hansu(N):
    cnt = 0
    for i in range(1, N + 1):
        lst = list(map(int, str(i)))
        
        if i < 100:
            cnt += 1
        elif lst[0] - lst[1] == lst[1] - lst[2]:
            cnt += 1
    return cnt

N = int(input())
print(hansu(N))