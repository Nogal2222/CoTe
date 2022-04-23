def solution(n):
    # 한 칸 점프 후 2^n만큼 이동 후 남은 거리 점프
    # 즉 n의 이진수에 있는 1의 개수가 답
    answer = len([i for i in bin(n)[2:] if i == '1'])
    
    return answer


''' 시간초과
from collections import deque

def solution(n):
    visited = {0:0}
    q = deque([0])
    
    while q:
        current = q.popleft()
        
        if current == n:
            break
        
        # 한 칸 점프
        moved = current + 1
        
        if visited.get(moved, 0) == 0:
            visited[moved] = visited[current] + 1
            q.append(moved)
        
        else:
            visited[moved] = min(visited[moved], visited[current])
        
        # 순간이동
        moved = current * 2
        
        if visited.get(moved, 0) == 0 and moved != 0:
            visited[moved] = visited[current]
            q.append(moved)
        
        else:
            visited[moved] = min(visited[moved], visited[current])
    
    return visited[n]
'''
n = 5

result = solution(n)