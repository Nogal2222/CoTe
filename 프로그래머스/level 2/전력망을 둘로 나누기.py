from collections import deque

def bfs(start, visited, graph):
    q = deque([start])
    result = 1
    visited[start] = True
    
    while q:
        now = q.popleft()
        
        for i in graph[now]:
            if visited[i] == False:
                result += 1
                q.append(i)
                visited[i] = True
    
    return result

def solution(n, wires):
    answer = n
    graph = [[] for _ in range(n+1)]
    
    for tower1, tower2 in wires:
        graph[tower1].append(tower2)
        graph[tower2].append(tower1)
    
    for start, not_visited in wires:
        visited = [False] * (n + 1)
        visited[not_visited] = True
        result = bfs(start, visited, graph)
        
        gap = abs(result - (n - result))
        
        if gap < answer:
            answer = gap
    
    return answer

n = [9, 4, 7]
wires = [[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]],
         [[1,2],[2,3],[3,4]],
         [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]]

result = []
for i in range(3):
    result.append(solution(n[i], wires[i]))