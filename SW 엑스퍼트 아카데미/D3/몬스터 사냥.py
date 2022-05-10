T = int(input())
answers = [''] * T

for t in range(1, T+1):
    D, L, n = map(int, input().split())
    
    ''' 시간 초과
    total_D = 0
    
    for k in range(n):
            total_D += int((D * (1 + (k * L * 0.01))))
    '''
    # 같은 식인데 이를 수학적으로 풀은 식
    total_D = int((D*n) + (D * L * n * (n - 1) * 0.005))
    
    answers[t-1] = f'#{t} {total_D}'

for i in answers:
    print(i)