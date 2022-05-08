T = int(input())
answers = [''] * T

for t in range(1, T+1):
    N = int(input())
    N_lst = list(map(int, input().split()))
    cnt = 0
    
    for i in range(1, N-1):
        if N_lst[i-1] < N_lst[i] < N_lst[i+1] or N_lst[i+1] < N_lst[i] < N_lst[i-1]:
            cnt += 1
    
    answers[t-1] = f'#{t} {cnt}'
    
for i in answers:
    print(i)