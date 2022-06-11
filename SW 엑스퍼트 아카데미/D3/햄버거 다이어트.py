def check(idx, score, cal):
    global max_score
    
    if cal > L:
        return 
    
    if score > max_score:
        max_score = score
    
    if idx == N:
        return
    
    check(idx+1, score, cal)
    
    check(idx+1, score + lst[idx][0], cal + lst[idx][1])

T = int(input())
answers = [''] * T

for t in range(1, T+1):
    N, L = map(int, input().split())
    lst = []
    max_score = 0
    score = 0
    
    for _ in range(N):
        lst.append(list(map(int, input().split())))
    
    check(0, 0, 0)
    
    answers[t-1] = f'#{t} {max_score}'

for i in answers:
    print(i)