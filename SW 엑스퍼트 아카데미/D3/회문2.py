for t in range(1, 11):
    tc = int(input())
    mapp = [list(input()) for _ in range(100)]
    flag = 0
    
    for size in range(100, -1, -1):
        if flag:
            break
        
        for r in range(100):
            if flag:
                break
            
            for c in range(100):
                if c < (101-size):
                    check_r = mapp[r][c:c+size]
                    
                    if check_r == list(reversed(check_r)):
                        flag = 1
                        
                        break
                
                if r < (101-size):
                    check_c = []
                    
                    for nr in range(size):
                        check_c.append(mapp[r+nr][c])
                    
                    if check_c == list(reversed(check_c)):
                        flag = 1
                        
                        break
    
    # size가 하나 더 줄어들고 break 되기 때문에 +1을 해준다.
    print(f'#{t} {size + 1}')