T = int(input())
answers = [''] * T

for t in range(1, T+1):
    N, M = map(int, input().split())
    lst = [[] for _ in range(N)]
    
    for i in range(N):
        lst[i] = list(map(int, input().split()))
    
    lst_correct = [0] * N
    
    for j in range(N):
        cnt_correct = 0
        
        for k in range(M):
            if lst[j][k] == 1:
                cnt_correct += 1
        
        lst_correct[j] = cnt_correct
    
    fst = max(lst_correct)
    cnt_fst = lst_correct.count(fst)
    
    answers[t-1] = f'#{t} {cnt_fst} {fst}'

for i in answers:
    print(i)