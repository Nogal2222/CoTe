T = int(input())
answers = [''] * T

for t in range(1, T+1):
    N = int(input())
    
    a = [i for i in range(1, 10)]
    max_a = []
    
    for i in a:
        if (N/i) % 1 == 0:
            max_a.append(i)
    
    b = N // max(max_a)
    
    if b < 10:
        answer = "Yes"
    else:
        answer = "No"
    
    answers[t-1] = f'#{t} {answer}'

for i in answers:
    print(i)