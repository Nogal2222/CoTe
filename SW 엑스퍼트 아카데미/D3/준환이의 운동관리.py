T = int(input())
answers = [''] * T

for t in range(1, T+1):
    L, U, X = map(int, input().split())
    
    if X > U:
        answer = -1
    elif L <= X <= U:
        answer = 0
    else:
        answer = L - X
    
    answers[t-1] = f'#{t} {answer}'

for i in answers:
    print(i)