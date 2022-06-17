T = int(input())
answers = [''] * T

for t in range(1, T+1):
    n = int(input())
    card = list(map(str, input().split()))
    
    if n % 2 == 1:
        fst = card[:n//2 + 1]
        scd = card[n//2 + 1:]
    
    else:
        fst = card[:n//2]
        scd = card[n//2:]
    
    result = []
    
    while fst:
        result.append(fst.pop(0))
        
        if scd:
            result.append(scd.pop(0))
        else:
            continue
    
    answer = ' '.join(result)
    answers[t-1] = f'#{t} {answer}'

for i in answers:
    print(i)