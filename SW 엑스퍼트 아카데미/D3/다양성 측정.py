T = int(input())
answers = [''] * T

for t in range(1, T+1):
    N = set(input())
    answer = len(N)
    answers[t-1] = f'#{t} {answer}'

for i in answers:
    print(i)