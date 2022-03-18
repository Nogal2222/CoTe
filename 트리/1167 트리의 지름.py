# -*- coding: utf-8 -*-
import sys
from collections import deque
#input = sys.stdin.readline

def bfs(start):
    visit = [-1] * (v + 1)
    q = deque()
    q.append(start)
    visit[start] = 0
    visit_max = [0, 0]
    
    while q:
        temp = q.popleft()
        
        for i, j in graph[temp]:
            if visit[i] == -1:
                visit[i] = visit[temp] + j
                q.append(i)
                
                if visit_max[0] < visit[i]:
                    visit_max = visit[i], i
    
    return visit_max


v = int(input())
graph = [[] for _ in range(v + 1)]

for _ in range(v):
    tree = list(map(int, input().split()))
    
    for i in range(1, len(tree) - 2, 2):
        graph[tree[0]].append((tree[i], tree[i + 1]))

dis, node = bfs(1)
dis, node = bfs(node)
print(dis)