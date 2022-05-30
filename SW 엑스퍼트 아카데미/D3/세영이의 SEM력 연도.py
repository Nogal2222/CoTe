T = int(input())
answers = [''] * T

for t in range(1, T+1):
    S, E, M = map(int, input(). split())
    S, E, M = S-1, E-1, M-1
    
    k = S
    
    while True:
        if k % 24 == E and k % 29 == M:
            answer = k + 1
            break
        
        k += 365
    
    answers[t-1] = f'#{t} {answer}'

for i in answers:
    print(i)