T = int(input())
answers = [''] * T

for t in range(1, T+1):
    A, B = map(int, input().split())
    cnt = 0
    
    for i in range(A, B+1):
        lst_i = list(str(i))
        rev_i = lst_i[::-1]
        
        i2 = i ** 0.5
        
        if i2 % 1 == 0:
            i2 = int(i2)
            lst_i2 = list(str(i2))
        else:
            continue
        
        rev_i2 = lst_i2[::-1]
        
        if lst_i == rev_i and lst_i2 == rev_i2:
            cnt += 1
    
    answers[t-1] = f'#{t} {cnt}'

for i in answers:
    print(i)