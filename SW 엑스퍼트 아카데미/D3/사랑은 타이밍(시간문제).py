T = int(input())
answers = [''] * T

for t in range(1, T+1):
    D, H, M = map(int, input().split())
    dDay = (11 * 24 * 60) + (11 * 60) + 11
    minute = (D * 24 * 60) + (H * 60) + M
    
    answer = minute - dDay
    
    if answer < 0:
        answer = -1
     
    answers[t-1] = f'#{t} {answer}'

for i in answers:
    print(i)