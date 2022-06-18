T = int(input())
answers = [''] * T

for t in range(1, T+1):
    n = list(map(int, input().split()))
    
    for i in range(len(n)):
        if n[i] < 40:
            n[i] = 40
    
    answer = sum(n) // len(n)
    
    answers[t-1] = f'#{t} {answer}'

for i in answers:
    print(i)