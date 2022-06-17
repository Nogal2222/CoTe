T = int(input())
answers = [''] * T

for t in range(1, T+1):
    n = int(input())
    
    s2 = n ** 2
    s3 = s2 + n
    s1 = s3 // 2
    
    answers[t-1] = f'#{t} {s1} {s2} {s3}'

for i in answers:
    print(i)