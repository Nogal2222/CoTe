T = int(input())
answers = [''] * T

for t in range(1, T+1):
    N = int(input())
    huddle = list(map(int, input().split()))
    
    max_up = 0
    max_down = 0
    
    for i in range(N-1):
        if huddle[i] < huddle[i+1]:
            max_up = max(max_up, huddle[i+1] - huddle[i])
        
        else:
            max_down = max(max_down, huddle[i] - huddle[i+1])
            
    answers[t-1] = f'#{t} {max_up} {max_down}'

for i in answers:
    print(i)