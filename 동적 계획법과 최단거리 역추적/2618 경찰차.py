# -*- coding: utf-8 -*-
import sys
#input = sys.stdin.readline

#거리 구하는 함수
def dist(a, b):
    if b == 0:
        return n - w_list[a][0] + n - w_list[a][1]
    
    elif a == 0:
        return w_list[b][0] - 1 + w_list[b][1] - 1
    
    return abs(w_list[a][0] - w_list[b][0]) + abs(w_list[a][1] - w_list[b][1])


n = int(input()) #도로의 개수
w = int(input()) #사건의 개수
w_list = [0] #사건 리스트

for _ in range(w):
    w_list.append(list(map(int, input().split())))

#dp[x][y]=경찰1이 마지막으로 x를 처리하고
#경찰2가 마지막으로 y를 처리했을때의 최소이동거리
dp = [[0 for _ in range(w+1)] for _ in range(w+1)]
#해당위치에 어떤 경찰차가 도착햇는지 표시
dp_trace = [[0 for _ in range(w+1)] for _ in range(w+1)]

#모든 사건에 한 경찰만 이동할 때
for i in range(1, w+1):
    if i == 1: #첫 사건
        dp[i][0] = w_list[1][0] - 1 + w_list[1][1] - 1
        dp[0][i] = n - w_list[1][0] + n - w_list[1][1]
    
    else: #이후 모든 사건
        dp[0][i] = dp[0][i-1] + dist(i-1, i)
        dp[i][0] = dp[i-1][0] + dist(i-1, i)
    
    dp_trace[i][0] = i - 1
    dp_trace[0][i] = i - 1

#모든 경우의 수 구하기
for i in range(1, w+1):
    for j in range(1, w+1):
        if i < j:
            if i - j == -1:
                for k in range(j-1):
                    if k == 0:
                        dp[i][j] = dp[i][k] + dist(j, k)
                        dp_trace[i][j] = 0
                    
                    else:
                        if dp[i][j] > dp[i][k] + dist(j, k):
                            dp[i][j] = dp[i][k] + dist(j, k)
                            dp_trace[i][j] = k
            
            else:
                dp[i][j] = dp[i][j-1] + dist(j-1, j)
                dp_trace[i][j] = j - 1
        
        elif i > j:
            if i - j == 1:
                for k in range(0, i-1):
                    if k == 0:
                        dp[i][j] = dp[k][j] + dist(k, i)
                        dp_trace[i][j] = 0
                    
                    else:
                        if dp[i][j] > dp[k][j] + dist(k, i):
                            dp[i][j] = dp[k][j] + dist(k, i)
                            dp_trace[i][j] = k
            
            else:
                dp[i][j] = dp[i-1][j] + dist(i-1, i)
                dp_trace[i][j] = i - 1

minVal = sys.maxsize
pol1 = 0
po12 = 0
trace = []

for i in range(w+1):
    if i != w:
        if dp[w][i] < minVal:
            minVal = dp[w][i]
            #가장 작을 때 경찰 위치 저장
            pol1 = w
            pol2 = i
        
        if dp[i][w] < minVal:
            minVal = dp[i][w]
            pol1 = i
            pol2 = w

for i in range(w):
    if pol1 >= pol2:
        pol1 = dp_trace[pol1][pol2]
        trace.append(1)
    
    else:
        pol2 = dp_trace[pol1][pol2]
        trace.append(2)

print(minVal)

for i in trace[::-1]:
    print(i)