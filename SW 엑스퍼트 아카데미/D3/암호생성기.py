for t in range(1, 11):
    tc = int(input())
    lst = list(map(int, input().split()))
    sub = 1
    
    while True:
        target = lst.pop(0) - sub
        sub += 1
        
        if sub == 6:
            sub = 1
        
        if target <= 0:
            target = 0
            lst.append(target)
            break
        
        else:
            lst.append(target)
    
    for i in range(8):
        lst[i] = str(lst[i])
    
    answer =' '.join(lst)
    
    print(f'#{tc} {answer}')