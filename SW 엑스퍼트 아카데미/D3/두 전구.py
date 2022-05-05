T = int(input())
answer = [''] * T

for t in range(1, T+1):
    A, B, C, D = map(int, input().split())
    
    if min(B, D) - max(A, C) > 0:
        gap = min(B, D) - max(A, C)
    
    else:
        gap = 0
    
    answer[t-1] = f'#{t} {gap}'

for i in answer:
    print(i)