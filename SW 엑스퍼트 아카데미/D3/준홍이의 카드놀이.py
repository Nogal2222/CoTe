T = int(input())
answers = [''] * T

for t in range(1, T+1):
    N, M = map(int, input().split())
    lst_N = list(range(1, N + 1))
    lst_M = list(range(1, M + 1))
    lst_total = []
    cnt = 0
    cnt_lst = [0] * (N + M + 1)

    for i in lst_N:
        for j in lst_M:
            lst_total.append(i + j)

    for i in range(min(lst_total), max(lst_total) + 1):
        cnt = lst_total.count(i)
        cnt_lst[i] = cnt

    most = max(cnt_lst)
    answer_lst = []

    for i in range(len(cnt_lst)):
        if cnt_lst[i] == most:
            answer_lst.append(str(i))
    
    answer = ' '.join(answer_lst)
    answers[t-1] = f'#{t} {answer}'

for i in answers:
    print(i)