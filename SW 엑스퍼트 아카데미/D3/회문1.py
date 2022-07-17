for t in range(1, 11):
    size = int(input())
    mapp = [list(input()) for _ in range(8)]
    cnt = 0
    
    for r in range(8):
        for c in range(8):
            if c < (9-size):
                check_r = mapp[r][c:c+size]
                
                if check_r == list(reversed(check_r)):
                    cnt += 1
            
            if r < (9-size):
                check_c = []
                
                for nr in range(size):
                    check_c.append(mapp[r+nr][c])
                
                if check_c == list(reversed(check_c)):
                    cnt += 1
    
    print(f'#{t} {cnt}')