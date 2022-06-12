T = int(input())
answers = [''] * T

for t in range(1, T+1):
    A, B, C = map(int, input().split())
    bread = min(A, B)
    
    answer = C // bread
    answers[t-1] = f'#{t} {answer}'

for i in answers:
    print(i)