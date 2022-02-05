# -*- coding: utf-8 -*-
import sys

graph = []
blank = []
#스도쿠 문제 입력
for i in range(9):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))
#문제 중 구멍(0) 인 곳을 blank리스트에 좌표 입력
for i in range(9):
    for j in range(9):
        if graph[i][j] == 0:
            blank.append((i,j))

#행중 중복 숫자 확인
def checkRow(x, a):
    for i in range(9):
        if a == graph[x][i]:
            return False
    return True

#열중 중복 숫자 확인
def checkColumn(y,a):
    for i in range(9):
        if a == graph[i][y]:
            return False
    return True

#3x3중 중복 숫자 확인
def check3x3(x,y,a):
    nx = x//3*3
    ny = y//3*3
    for i in range(3):
        for j in range(3):
            if a == graph[nx+i][ny+j]:
                return False
    return True

def sudokoo(idx):
    if idx == len(blank):
        for i in range(9):
            print(*graph[i])
        exit(0)
    
    for i in range(1, 10):
        x = blank[idx][0]
        y = blank[idx][1]
        
        if checkRow(x,i) and checkColumn(y,i) and check3x3(x,y,i):
            graph[x][y] = i
            sudokoo(idx+1)
            graph[x][y] = 0

sudokoo(0)