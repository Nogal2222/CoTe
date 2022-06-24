def solve(idx, sum):
    global cnt
    
    if idx >= N:
        return
    
    temp = sum + nums[idx]
    
    if temp == K:
        cnt += 1
    
    solve(idx + 1, sum)
    solve(idx + 1, temp)

T = int(input())
answers = [''] * T

for t in range(1, T+1):
    N, K = map(int, input().split())
    nums = list(map(int, input().split()))
    cnt = 0
    
    solve(0, 0)
    
    answers[t-1] = f'#{t} {cnt}'

for i in answers:
    print(i)

''' 시간 초과
from itertools import combinations

T = int(input())
answers = [''] * T

for t in range(1, T+1):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    cnt = 0
    
    for i in range(1, n+1):
        comb = list(combinations(nums, i))
        
        for j in range(len(comb)):
            if sum(comb[j]) == k:
                cnt += 1
    
    answers[t-1] = f'#{t} {cnt}'

for i in answers:
    print(i)
'''