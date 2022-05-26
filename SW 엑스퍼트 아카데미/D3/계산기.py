T = int(input())
answers = [''] * T

for t in range(1, T+1):
    N = int(input())
    nums = sorted(list(map(int, input().split())))
    
    for i in range(1, len(nums)):
        if nums[i] <= 1 or nums[i-1] <= 1:
            nums[i] += nums[i-1]
        else:
            nums[i] *= nums[i-1]
    answer = max(nums)        
    answers[t-1] = f'#{t} {answer}'
    
for i in answers:
    print(i)