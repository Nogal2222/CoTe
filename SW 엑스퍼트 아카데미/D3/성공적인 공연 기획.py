T = int(input())
answers = [''] * T

for t in range(1, T+1):
    seq = input()
    people = 0
    employment = 0
    
    for need, cnt in enumerate(seq):
        cnt = int(cnt)
        
        if need <= people:
            people += cnt
        
        else:
            employment += need - people
            people += need - people + cnt
            
    answers[t-1] = f'#{t} {employment}'

for i in answers:
    print(i)