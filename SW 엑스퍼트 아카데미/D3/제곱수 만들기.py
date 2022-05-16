T = int(input())
answers = [''] * T
prime = [2]

for i in range(3, int(10000000 ** (0.5)), 2):
    for p in prime:
        if not i % p:
            break
    
    else:
        prime.append(i)

for t in range(1, T+1):
    A = int(input())
    answer = 1
    
    if (A ** 0.5) % 1 != 0:
        for p in prime:
            cnt = 0
            
            while not A % p:
                A //= p
                cnt += 1
            
            if cnt % 2:
                answer *= p
            
            if A == 1 or p > A:
                break
        
        if A > 1:
            answer *= A
    
    answers[t-1] = f'#{t} {answer}'

for i in answers:
    print(i)

''' 시간 초과
T = int(input())
answers = [''] * T

for t in range(1, T+1):
    A = int(input())
    B = 1
    
    while True:
        AXB = A*B
        
        if (AXB ** (0.5)) % 1 == 0:
            answer = B
            break
        
        B += 1
            
    answers[t-1] = f'#{t} {answer}'

for i in answers:
    print(i)
'''