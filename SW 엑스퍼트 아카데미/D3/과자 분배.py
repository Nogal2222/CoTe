T = int(input())
answers = [''] * T

for t in range(1, T+1):
    n, k = map(int, input().split())
    
    if n % k == 0:
        answer = 0
    else:
        answer = 1
        
    answers[t-1] = f'#{t} {answer}'

for i in answers:
    print(i)