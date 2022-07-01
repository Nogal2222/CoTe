from collections import deque

T = int(input())
answers = [''] * T
 
for t in range(1, T+1):
    n, m = map(int, input().split())
    A = deque(list(map(int, input().split())))
    B = deque(list(map(int, input().split())))
    
    if m < n:
        A, B = B, A
        n, m = m, n
    
    answer = 0
    
    while n <= m:
        summ = 0
        
        for i in range(n):
            summ += (A[i] * B[i])
        
        answer = max(answer, summ)
        A.appendleft(0)
        n += 1
    
    answers[t-1] = f'#{t} {answer}'
 
for i in answers:
    print(i)