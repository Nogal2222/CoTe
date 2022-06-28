T = int(input())
answers = [''] * T

for t in range(1, T+1):
    n, a, b = map(int, input().split())
    minimum = 9999999
    
    for r in range(1, n+1):
        c = 1
        
        while r * c <= n:
            res = a * abs(r-c) + b * (n - r * c)
            minimum = min(minimum, res)
            c += 1
    
    answers[t-1] = f'#{t} {minimum}'

for i in answers:
    print(i)