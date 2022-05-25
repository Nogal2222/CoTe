T = int(input())
answers = [''] * T

for t in range(1, T+1):
    nums = list(input().split())
    sums = []
    
    for num in nums:
        temp = 0
        
        for i in num:
            temp += int(i)
        
        sums.append(temp)
    
    max_sums = max(sums)
    min_sums = min(sums)
    answers[t-1] = f'#{t} {max_sums} {min_sums}'

for i in answers:
    print(i)