from itertools import combinations

T = int(input())
answers = [''] * T

for t in range(1, T+1):
    n, m = map(int, input().split())
    snacks = list(map(int, input().split()))
    
    c_snacks = list(combinations(snacks, 2))
    sums = [0] * len(c_snacks)
    
    for i in range(len(c_snacks)):
        sums[i] = c_snacks[i][0] + c_snacks[i][1]
    
    maximum = sums[0]
    
    for i in range(1, len(sums)):
        if maximum < sums[i] <= m:
            maximum = sums[i]
    
    if maximum > m:
        maximum = -1
    
    answers[t-1] = f'#{t} {maximum}'

for i in answers:
    print(i)