def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x : x[2])
    routes = set([costs[0][0]])
    
    while len(routes) != n:
        for idx, cost in enumerate(costs):
            if cost[0] in routes and cost[1] in routes:
                continue
            
            if cost[0] in routes or cost[1] in routes:
                routes.update([cost[0], cost[1]])
                answer += cost[2]
                costs[idx] = [-1, -1, -1]
                break
    
    return answer

n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]

result = solution(n, costs)