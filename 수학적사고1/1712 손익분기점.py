# -*- coding: utf-8 -*-
''' 반복문은 수가 커지면 너무 오래 걸림
A, B, C = map(int, input().split())
selling_point = 1
while True:
    spend = A + (B * selling_point)
    earn = C * selling_point
    
    if spend < earn:
        print(selling_point)
        break
    elif B >= C:
        print(-1)
        break
    selling_point += 1
'''

A, B, C = map(int, input().split())
if B>=C:
    print(-1)
else:
    BEP = int(A/(C-B) + 1)
    print(BEP)