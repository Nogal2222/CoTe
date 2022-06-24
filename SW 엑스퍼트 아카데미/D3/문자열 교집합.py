T = int(input())
answers = [''] * T

for t in range(1, T+1):
    N, M = map(int, input().split())
    fst = list(input().split())
    scd = list(input().split())
    
    tot = list(set(fst+scd))
    
    answer = N + M - len(tot)
    answers[t-1] = f'#{t} {answer}'

for i in answers:
    print(i)