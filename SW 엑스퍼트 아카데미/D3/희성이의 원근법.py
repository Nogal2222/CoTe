T = int(input())
answers = [''] * T

for t in range(1, T+1):
    d = float(input()) * 0.001
    
    if d < 0.1:
        answer = 0
    
    elif d < 1:
        answer = 1
    
    elif d < 10:
        answer = 2
    
    elif d < 100:
        answer = 3
    
    elif d < 1000:
        answer = 4
    
    else:
        answer = 5
    
    answers[t-1] = f'#{t} {answer}'

for i in answers:
    print(i)