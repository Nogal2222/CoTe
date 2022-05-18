T = int(input())
answers = [''] * T

for t in range(1, T+1):
    n, a, b = map(int, input().split())
    
    if n >= a + b:
        min_p = 0
        max_p = min(a, b)
    
    else:
        min_p = (a + b) - n
        max_p = min(a, b)
                
    answers[t-1] = f'#{t} {max_p} {min_p}'

for i in answers:
    print(i)