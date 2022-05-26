def draft(draw, gap):
    next_round = []
    
    if len(draw) == 1:
        return gap
    
    for i in range(0, len(draw), 2):
        gap += abs(draw[i] - draw[i+1])
        next_round.append(max(draw[i], draw[i+1]))
    
    return draft(next_round, gap)

T = int(input())
answers = [''] * T

for t in range(1, T+1):
    K = int(input())
    draw = list(map(int, input().split()))
    answer = draft(draw, 0)
    answers[t-1] = f'#{t} {answer}'
    
for i in answers:
    print(i)