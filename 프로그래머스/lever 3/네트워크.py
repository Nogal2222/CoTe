#'''
# dfs를 이용한 풀이
def solution(n, computers):
    def dfs(i):
        visited[i] = 1
        
        for num in range(n):
            if computers[i][num] and not visited[num]:
                dfs(num)
    
    answer = 0
    visited = [0 for i in range(len(computers))]
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
    
    return answer
#'''

'''
#bfs를 이용한 풀이

from collections import deque

def solution(n, computers):
    def bfs(i):
        q = deque()
        q.append(i)
        
        while q:
            i = q.popleft()
            visited[i] = 1
            
            for num in range(n):
                if computers[i][num] and not visited[num]:
                    q.append(num)
    
    answer = 0
    visited = [0 for i in range(len(computers))]
    
    for i in range(n):
        if not visited[i]:
            bfs(i)
            answer += 1
    
    return answer
'''

n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

result = solution(n, computers)