'''
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
'''
from collections import deque

T = 10
answers = [''] * T

def bfs(now_dq):
    global answer
    
    answer = max(now_dq)
    next_dq = deque()
    
    while now_dq:
        now = now_dq.pop()
        
        for i in dict_arr[now]:
            if visited[i] == 0:
                next_dq.append(i)
                visited[i] = 1
    
    if next_dq:
        bfs(next_dq)

for t in range(1, T+1):
    n, start = map(int, input().split())
    arr = list(map(int, input().split()))
    dict_arr = {i:[] for i in range(1, 101)}
    
    for i in range(0, n, 2):
        dict_arr[arr[i]].append(arr[i+1])
    
    visited = [0] * 101
    visited[start] = 1
    answer = 0
    dq = deque()
    dq.append(start)
    
    bfs(dq)
    
    answers[t-1] = f'#{t} {answer}'
 
for i in answers:
    print(i)