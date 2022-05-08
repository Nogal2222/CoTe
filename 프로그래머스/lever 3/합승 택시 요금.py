import heapq

inf = int(1e9)
graph =[[]]

def preprocess(n, fares):
    global graph
    graph = [[] for i in range(n+1)]
    
    for fare in fares:
        src, dst, cost = fare[0], fare[1], fare[2]
        graph[src].append([dst, cost])
        graph[dst].append([src, cost])

def dijkstra(src, dst):
    global graph
    n = len(graph)
    table = [inf for i in range(n)]
    table[src] = 0
    heap = [[0, src]]
    
    while heap:
        w, x = heapq.heappop(heap)
        
        if table[x] < w:
            continue
        
        for i in graph[x]:
            new_x, new_cost = i[0], i[1]
            new_cost += w
            
            if new_cost < table[new_x]:
                table[new_x] = new_cost
                heapq.heappush(heap, [new_cost, new_x])
    
    return table[dst]

def solution(n, s, a, b, fares):
    preprocess(n, fares)
    cost = inf
    
    for i in range(1, n+1):
        cost = min(cost, dijkstra(s, i) + dijkstra(i, a) + dijkstra(i, b))
        
    return cost

n = 6
s = 4
a = 6
b = 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]

result = solution(n, s, a, b, fares)