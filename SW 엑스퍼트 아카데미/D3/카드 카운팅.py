def check(card):
    check_lst = [[0] * 13 for _ in range(4)]
    idx = 0
    l = len(card)
    dic = {'S':0, 'D':1, 'H':2, 'C':3}
    
    while idx < l:
        shp = dic[card[idx]]
        num = int(card[idx+1] + card[idx+2]) - 1
        
        if check_lst[shp][num]:
            return False
        
        check_lst[shp][num] += 1
        idx += 3
    
    result = [0] * 4
    
    for i in range(4):
        for j in range(13):
            if not check_lst[i][j]:
                result[i] += 1
    
    return result

T = int(input())

for tc in range(1, T+1):
    card = input()
    result = check(card)
    
    if result:
        print('#{}'.format(tc), *result)
    else:
        print('#{} ERROR'.format(tc))