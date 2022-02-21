# -*- coding: utf-8 -*-
from collections import deque
import sys
#input = sys.stdin.readline

n, m = map(int, input().split())
s = list(map(int, input().split()))
q = deque([i for i in range(1, n + 1)])
cnt = 0

for i in range(m):
    q_len = len(q)
    q_index = q.index(s[i])
    
    if q_index < q_len - q_index:
        while True:
            if q[0] == s[i]:
                q.popleft()
                break
            else:
                q.append(q.popleft())
                cnt += 1
    
    else:
        while True:
            if q[0] == s[i]:
                q.popleft()
                break
            else:
                q.appendleft(q.pop())
                cnt += 1

print(cnt)