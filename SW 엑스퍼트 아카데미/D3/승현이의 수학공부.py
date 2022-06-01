T = int(input())
answers = [''] * T

for t in range(1, T+1):
    dec = 0
    N, X = map(str, input().split())
    N = int(N)
    X = X[::-1]
    dec = 0
    
    for i in range(len(X)):
        dec += (int(X[i]) * (N ** i))
    
    answer = dec % (N-1)
    answers[t-1] = f'#{t} {answer}'

for i in answers:
    print(i)