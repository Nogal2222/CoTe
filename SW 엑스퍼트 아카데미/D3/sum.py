for t in range(1, 11):
    tc = int(input())
    lst = [list(map(int, input().split())) for _ in range(100)]
    
    maxx = 0
    

        
    #가로, 세로
    for i in range(100):
        temp_c = [] # 세로
        temp_rs = [] # 오른대각
        temp_ls = [] # 왼대각
        
        temp_rs.append(lst[i][i])
        temp_ls.append(lst[99-i][i])
        
        for j in range(100):
            temp_c.append(lst[j][i])
        
        maxx= max(maxx, sum(temp_c), sum(lst[i]), sum(temp_rs), sum(temp_ls))
    
    print(f'#{tc} {maxx}')