T = int(input())
answers = [''] * T

for t in range(1, T+1):
    N = int(input())
    
    if N % 2 == 1:
        answer = "Odd"
    
    else:
        answer = "Even"
    
    answers[t-1] = f'#{t} {answer}'

for i in answers:
    print(i)