from itertools import combinations

T = int(input())
answers = [''] * T

for t in range(1, T+1):
    nums = list(map(int, input().split()))
    comb = list(combinations(nums, 3))

    sums = []

    for i in range(len(comb)):
        s = sum(comb[i])
        
        if s in sums:
            continue
        
        else:
            sums.append(s)

    sums.sort(reverse = True)
    
    answers[t-1] = f'#{t} {sums[4]}'

for i in answers:
    print(i)