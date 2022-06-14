T = int(input())
answers = [''] * T

for t in range(1, T+1):
    N, K = map(int, input().split())
    scores = sorted(list(map(int, input().split())), reverse = True)
    sum_score = 0
    
    for i in range(K):
        sum_score += scores[i]
    
    answers[t-1] = f'#{t} {sum_score}'

for i in answers:
    print(i)