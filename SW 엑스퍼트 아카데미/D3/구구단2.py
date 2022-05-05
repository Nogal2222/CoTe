T = int(input())
answers = [''] * T

for t in range(1, T+1):
    A, B = map(int, input().split())
    if A > 9 or B > 9:
        answer = -1
    
    else:
        answer = A * B
    
    answers[t-1] = f'#{t} {answer}'

for i in answers:
    print(i)