T = int(input())
answers = [''] * T

for t in range(1, T+1):
    cur_time, target_time = map(int, input().split())
    
    answer = cur_time + target_time
    
    if answer >= 24:
        answer -= 24
    
    answers[t-1] = f'#{t} {answer}'

for i in answers:
    print(i)