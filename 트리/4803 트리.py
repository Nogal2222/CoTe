# -*- coding: utf-8 -*-
import sys
#input = sys.stdin.readline

def bfs(x):
    flag = 1
    q = [x]
    
    while q:
        curr = q.pop(0)
        
        if visited[curr] == 1:
            flag = 0
        
        visited[curr] = 1
        
        for i in graph[curr]:
            if visited[i] == 0:
                q.append(i)
    
    return flag

case = 0

while 1:
    case += 1
    n, m = map(int, input().split())
    
    if [n, m] == [0, 0]:
        break
    
    graph = [[] for _ in range(n+1)]
    
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    cnt = 0
    visited = [0] * (n + 1)
    
    for i in range(1, n+1):
        if visited[i] == 1:
            continue
        
        if bfs(i) == 1:
            cnt += 1
        
    if cnt == 0:
        print('Case {}: No trees.'.format(case))
    elif cnt == 1:
        print('Case {}: There is one tree.'.format(case))
    else:
        print('Case {}: A forest of {} trees.'.format(case, cnt))