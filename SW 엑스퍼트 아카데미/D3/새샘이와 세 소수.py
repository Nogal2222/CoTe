prime = []

for i in range(2, 1000):
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            break
        
    else:
        prime.append(i)

T = int(input())
answers = [''] * T

for t in range(1, T+1):
    n = int(input())
    m = len(prime)
    
    answer = 0
    
    for i in range(len(prime)):
        if prime[i] > n:
            break
        
        for j in range(i, m):
            if prime[j] > n:
                break
            
            for k in range(j, m):
                if prime[k] > n:
                    break
                
                if prime[i] + prime[j] + prime[k] == n:
                    answer += 1
    
    answers[t-1] = f'#{t} {answer}'

for i in answers:
    print(i)