T = int(input())
answers = [''] * T

for t in range(1, T+1):
    n = list(input())
    
    while len(n) > 1:
        sm = 0
        
        for i in range(len(n)):
            sm += int(n[i])
        
        n = str(sm)
    
    answer = int(n)
    answers[t-1] = f'#{t} {answer}'

for i in answers:
    print(i)