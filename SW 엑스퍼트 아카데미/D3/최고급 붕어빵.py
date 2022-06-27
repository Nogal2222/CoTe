T = int(input())
answers = [''] * T

for t in range(1, T+1):
    n, m, k = map(int, input().split())
    guest = sorted(list(map(int, input().split())))
    
    answer = "Possible"
    
    for i in range(n):
        bread = (guest[i] // m) * k - (i + 1)
        
        if bread < 0:
            answer = "Impossible"
            break
    
    answers[t-1] = f'#{t} {answer}'

for i in answers:
    print(i)