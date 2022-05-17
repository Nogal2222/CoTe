T = int(input())
answers = [''] * T

for t in range(1, T+1):
    n, m = map(int, input().split())
    bi_m = bin(m)[2:].zfill(n + 1)
    target = bi_m[-1:len(bi_m)-n-1:-1]
    
    if '0' in target:
        answer = "OFF"
    
    else:
        answer = "ON"
    
    answers[t-1] = f'#{t} {answer}'

for i in answers:
    print(i)