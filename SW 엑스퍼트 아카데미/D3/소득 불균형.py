T = int(input())
answers = [''] * T

for t in range(1, T+1):
    peoples = int(input())
    scores = list(map(int, input().split()))
    avg = sum(scores) // peoples
    cnt = 0
    
    for i in scores:
        if i <= avg:
            cnt += 1
                
    answers[t-1] = f'#{t} {cnt}'

for i in answers:
    print(i)