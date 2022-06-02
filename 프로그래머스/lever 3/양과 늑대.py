def solution(info, edges):
    def next_nodes(v):
        temp = list()
        
        for e in edges:
            i, j = e
            
            if v == i:
                temp.append(j)
        
        return temp
    
    def dfs(sheep, wolf, current, path):
        if info[current]:
            wolf += 1
        
        else:
            sheep += 1
        
        if sheep <= wolf:
            return 0
        
        max_sheep = sheep
        
        for p in path:
            for node in next_nodes(p):
                if node not in path:
                    path.append(node)
                    max_sheep = max(max_sheep, dfs(sheep, wolf, node, path))
                    path.pop()
        
        return max_sheep
    
    answer = dfs(0, 0, 0, [0])
    
    return answer

info = [0,0,1,1,1,0,1,0,1,0,1,1]
edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]

result = solution(info, edges)