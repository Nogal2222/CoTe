answer = 0

def dfs(dungeons, k, i, visited):
    global answer
    visited = visited[:] # 얕은 복사 방지
    visited[i] = 1
    k -= dungeons[i][1]
    
    answer = max(answer, sum(visited))
    
    for j in range(len(dungeons)):
        if not visited[j] and dungeons[j][0] <= k:
            dfs(dungeons, k, j, visited)

def solution(k, dungeons):
    visited = [0] * len(dungeons)
    
    for i in range(len(dungeons)):
        if k >= dungeons[i][0]:
            dfs(dungeons, k, i, visited)
    
    return answer

k = 80
dungeons = [[80,20],[50,40],[30,10]]

result = solution(k, dungeons)