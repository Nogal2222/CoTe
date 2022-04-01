def solution(num):
    new_num = num
    cnt = 0
    
    while new_num > 1:
        if cnt == 500:
            cnt = -1
            break
        
        if new_num % 2 == 0:
            new_num //= 2
        else:
            new_num = new_num * 3 + 1
        
        cnt += 1
        
    return cnt

num = 626331
result = solution(num)