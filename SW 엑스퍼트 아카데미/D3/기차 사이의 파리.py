T = int(input())
answers = [''] * T

for t in range(1, T+1):
    D, A, B, F = map(int, input().split())
    answer = F*D / (A+B)
    answers[t-1] = f'#{t} {answer}'

for i in answers:
    print(i)