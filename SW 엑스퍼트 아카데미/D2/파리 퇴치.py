T = int(input())
answers = [''] * T
 
for t in range(1, T+1):
    n, m = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(n)]
    answer = 0
    
    for i in range(n-m+1):
        for j in range(n-m+1):
            summ = 0
            
            for col in range(m):
                for row in range(m):
                    summ += flies[i+col][j+row]
            
            answer = max(summ, answer)
    
    answers[t-1] = f'#{t} {answer}'
 
for i in answers:
    print(i)