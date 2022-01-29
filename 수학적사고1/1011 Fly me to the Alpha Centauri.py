# -*- coding: utf-8 -*-

T = int(input())

for i in range(T):
    x, y = map(int, input().split())
    distance = y - x
    cnt = 0
    movable_dis = 1 # 횟수별 이동할 수 있는 최대 이동거리
    total_moved_dis = 0 # 횟수별 총 이동한 거리
    
    while total_moved_dis < distance:
        cnt += 1
        total_moved_dis += movable_dis
        
        if cnt % 2 == 0:
            movable_dis += 1
    print(cnt)