from itertools import combinations

T = int(input())
answers = [''] * T

for t in range(1, T+1):
    n = int(input())
    nums = list(map(int, input().split()))
    n_nums = list(combinations(nums, 2))
    cal = []
    
    for i in range(len(n_nums)):
        cal.append(n_nums[i][0] * n_nums[i][1])
    
    answer = -1
    
    for i in cal:
        n_i = list(str(i))
        if len(n_i) == 1:
            answer = i
            break
        
        for j in range(1, len(n_i)):
            if int(n_i[j]) - int(n_i[j-1]) == 1:
                answer = i
    
    answers[t-1] = f'#{t} {answer}'

for i in answers:
    print(i)