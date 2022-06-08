T = int(input())
answers = [''] * T

for t in range(1, T+1):
    N = int(input())
    
    answer = N ** (1/3)
    
    if answer % 1 == 0:
        answer = int(answer)
    
    else:
        if 0.9999999 < answer - int(answer) < 1:
            answer = int(round(answer))
        else:
            answer = -1
    
    answers[t-1] = f'#{t} {answer}'

for i in answers:
    print(i)