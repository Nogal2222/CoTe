T = 10
answers = [''] * T

for t in range(1, T+1):
    n, hint = input().split()
    n, hint = int(n), list(hint)
    i = 0
    
    while True:
        if i == len(hint) - 1:
            break
        
        if hint[i] == hint[i+1]:
            hint.pop(i)
            hint.pop(i)
            i = 0
            continue
        
        i += 1
    
    password = int(''.join(hint))
    
    answers[t-1] = f'#{t} {password}'

for i in answers:
    print(i)