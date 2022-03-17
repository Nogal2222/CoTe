# -*- coding: utf-8 -*-
import sys, heapq
#input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

start, end = map(int, input().split())
dist = [float('inf')] * (n + 1)
visit = [False] * (n + 1)
hq = [(0, start, [start])]

#다익스트라
while hq:
    cur_dist, cur_node, path = heapq.heappop(hq)
    
    if visit[cur_node]:
        continue
    
    if cur_node == end:
        print(dist[end], len(path), sep = "\n")
        print(*path)
        break
    
    visit[cur_node] = True
    
    for to_node, to_dist in graph[cur_node]:
        total_dist = cur_dist + to_dist
        
        if visit[to_node] or total_dist >= dist[to_node]:
            continue
        
        dist[to_node] = total_dist
        heapq.heappush(hq, (total_dist, to_node, path + [to_node]))