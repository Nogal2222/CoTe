# -*- coding: utf-8 -*-

A, B, V = map(int, input().split())
last = V-A
meterperday = A - B
day = last / meterperday + 1
rnd = day - int(day)
if rnd > 0:
    day += 1
    print(int(day))
else:
    print(int(day))


#10미터 가는데 위로 5 아래로 2
#5 - 2 + 5 - 2