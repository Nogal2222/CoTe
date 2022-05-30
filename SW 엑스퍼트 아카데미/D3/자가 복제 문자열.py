T = int(input())
answers = [''] * T

for t in range(1, T+1):
    k = int(input()) - 1
    answer = 0
    
    while k >= 0:
        if k % 2 == 1:
            k = (k - 1) // 2
        
        if k % 4 == 0:
            answer = 0
            break
        
        elif k % 2 == 0:
            answer = 1
            break
        
    answers[t-1] = f'#{t} {answer}'

for i in answers:
    print(i)