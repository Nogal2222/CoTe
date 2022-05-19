T = int(input())
answers = [''] * T

for t in range(1, T+1):
    theta = int(input())
    hour = theta // 30
    minute = (theta % 30) * 2
        
    answers[t-1] = f'#{t} {hour} {minute}'

for i in answers:
    print(i)