T = int(input())
answers = [''] * T

for t in range(1, T+1):
    N = int(input())
    weight = [0] * N
    weight[0] = 2

    for i in range(1, N):
        weight[i] = weight[i-1] + 4

    left = 1 + sum(weight[:N-1])
    right = 1 + sum(weight) - 2
    answers[t-1] = f'#{t} {left} {right}'
    
for i in answers:
    print(i)