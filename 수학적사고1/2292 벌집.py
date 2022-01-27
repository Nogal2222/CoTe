# -*- coding: utf-8 -*-
N = int(input())
beehouse = 1
cnt = 1

while N > beehouse:
    beehouse += 6 * cnt
    cnt += 1
print(cnt)