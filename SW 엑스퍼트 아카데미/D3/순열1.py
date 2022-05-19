T = int(input())
answers = [''] * T

for t in range(1, T+1):
    n = int(input())
    lst = sorted(list(map(int, input().split())))
    answer = "Yes"
    
    for i in range(1, n+1):
        if i not in lst:
            answer = "No"
            break
        
    answers[t-1] = f'#{t} {answer}'

for i in answers:
    print(i)