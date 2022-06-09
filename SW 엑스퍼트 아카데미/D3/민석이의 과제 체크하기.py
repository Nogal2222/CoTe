T = int(input())
answers = [''] * T

for t in range(1, T+1):
    n, k = map(int, input().split())
    data = list(map(int, input().split()))
    answer = []

    for i in range(1, n + 1) :
        if i not in data :
            answer.append(i)
    
    answers[t-1] = f'#{t} {answer}'

for i in answers:
    print(i)

'''
T = int(input())
answers = [''] * T

for t in range(1, T+1):
    N, K = map(int, input().split())
    N_lst = set([str(i) for i in range(1, N+1)])
    submit = set(list(map(str, input().split())))
    unsub = N_lst - submit
    unsub = sorted(unsub)
    answer = ' '.join(unsub)
    answers[t-1] = f'#{t} {answer}'

for i in answers:
    print(i)
'''