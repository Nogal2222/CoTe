# -*- coding: utf-8 -*-
from collections import deque
import sys
#input = sys.stdin.readline

def bfs(start):
    q = deque()
    q.append((start, 0))
    visit = [0] * n
    visit[start-1] = 1
    result = [0, 0]
    
    while q:
        cur, cnt = q.popleft()
        
        for i in tree[cur]:
            next_number, value = i[0], i[1]
            
            if visit[next_number-1] == 0:
                visit[next_number-1] = 1
                q.append((next_number, cnt + value))
                
                if result[1] < cnt + value:
                    result[0] = next_number
                    result[1] = cnt + value
    
    return result


n = int(input())
tree = {i : [] for i in range(n + 1)}

for i in range(n - 1):
    a, b, weight = map(int, input().split())
    tree[a].append((b, weight))
    tree[b].append((a, weight))

a = bfs(1)
b = bfs(a[0])

print(b[1])