T = int(input())
answers = [''] * T

for t in range(1, T+1):
    n = int(input())
    cnt = 0
    
    for i in range(1, n+1):
        sumn = 0
        
        for j in range(i, n+1):
            sumn += j
            
            if sumn == n:
                cnt += 1
                break
            
            elif sumn > n:
                break
    
    answers[t-1] = f'#{t} {cnt}'

for i in answers:
    print(i)