T = int(input())
answers = [''] * T

for t in range(1, T+1):
    n = int(input())
    info = [[] for _ in range(n)]
    
    for i in range(n):
        info[i] = list(map(int, input().split()))
    
    answer = 0
    
    for i in range(n-1):
        for j in range(i+1, n):
            left1, right1 = info[i]
            left2, right2 = info[j]
            
            if (left1 > left2 and right1 < right2) or (left1 < left2 and right1 > right2):
                answer += 1
                
    answers[t-1] = f'#{t} {answer}'

for i in answers:
    print(i)