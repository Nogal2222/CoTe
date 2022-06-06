T = int(input())
answers = [''] * T

for t in range(1, T+1):
    N = int(input())
    salary = 0
    
    for i in range(N):
        p, n = map(float, input().split())
        
        salary += p * n
    
    answer = "{:.6f}".format(salary)
    answers[t-1] = f'#{t} {answer}'

for i in answers:
    print(i)