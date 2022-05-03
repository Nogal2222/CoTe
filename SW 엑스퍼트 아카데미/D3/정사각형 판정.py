T = int(input())

for t in range(1, T + 1):
    N=int(input())

    check=True

    graph=[]
    coordinates = [[] for _ in range(N)]

    for i in range(N):
        graph.append(list(input()))

    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j]=='#':
                coordinates[i].append(j)

    res=[]

    for i in coordinates:
        if len(i)>0:
            res.append(i)
    
    if len(res) != len(res[0]) or len(res) == 0:
        check = False
    
    else:
        if len(res) != 1:
            for i in range(1, len(res)):
                if res[i] != res[i-1]:
                    check = False
                    break
    
    print(f"#{t} yes" if check else f"#{t} no")