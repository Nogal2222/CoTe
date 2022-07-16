for t in range(1, 11):
    N = int(input())
    ori_pw = list(map(str, input().split()))
    com_cnt = int(input())
    orders = list(map(str, input().split()))
    
    for i in range(len(orders)):
        if orders[i] == 'I':
            x, y = int(orders[i+1]), int(orders[i+2])
            
            for j in range(y):
                ori_pw.insert(x, orders[i+j+3])
                x += 1
        
        elif orders[i] == 'D':
            x, y = int(orders[i+1]), int(orders[i+2])
            
            for j in range(y):
                ori_pw.pop(x)
    
    answer = ' '.join(ori_pw[:10])
    
    print(f'#{t} {answer}')