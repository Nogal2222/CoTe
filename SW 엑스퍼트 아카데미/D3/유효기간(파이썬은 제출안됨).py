T = int(input())
answers = [''] * T

for t in range(1, T+1):
    MY = input()
    front = int(MY[:2])
    rear = int(MY[2:])
    
    if 1 <= front <= 12 and rear > 12:
        answer = "MMYY"
    
    elif front > 12 and 1 <= rear <= 12:
        answer = "YYMM"
    
    elif 1 <= front <= 12 and 1 <= rear <= 12:
        answer = "AMBIGUOUS"
    
    else:
        answer = "NA"
    
    answers[t-1] = f'#{t} {answer}'

for i in answers:
    print(i)