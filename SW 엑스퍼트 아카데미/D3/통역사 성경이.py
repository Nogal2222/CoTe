T = int(input())
end_item = ['.', '!', '?']

for t in range(1, T+1):
    N = int(input())
    s = list(map(str, input().split()))
    
    cnt = 0
    res = []
    
    for part in s:
        if len(part) == 1:
            if part[0].isupper():
                cnt += 1
        
        else:
            if part[-1] not in end_item:
                if part[0].isupper() and part[1:].isalpha() and part[1:].islower():
                    cnt += 1
            
            else:
                if part[0].isupper() and part[1:len(part)-1].isalpha() and part[1:len(part)-1].islower():
                    cnt += 1
                
                res.append(cnt)
                cnt = 0
    
    print('#{}'.format(t), *res)