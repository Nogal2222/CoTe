T = int(input())
answers = [''] * T

for t in range(1, T+1):
    N = int(input())
    AB_lst = []
    
    for i in range(N):
        AB = list(map(int, input().split()))
        AB_lst.append(AB)
    
    P = int(input())
    C_lst = []
    
    for i in range(P):
        C = int(input())
        C_lst.append(C)
    
    cnt_lst = []
    for c in C_lst:
        cnt = 0
        
        for ab in AB_lst:
            if ab[0] <= c <= ab[1]:
                cnt += 1
        
        cnt_lst.append(str(cnt))
    
    answer = ' '.join(cnt_lst)
    answers[t-1] = f'#{t} {answer}'

for i in answers:
    print(i)