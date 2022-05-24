T = int(input())
answers = [''] * T

for t in range(1, T+1):
    k = int(input())
    nums = []
    for i in range(k):
        num = int(input())
        
        if num == 0:
            nums.pop()
        
        else:
            nums.append(num)
    
    answer = sum(nums)
    answers[t-1] = f'#{t} {answer}'

for i in answers:
    print(i)