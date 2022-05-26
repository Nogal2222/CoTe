T = int(input())
answers = [''] * T

for t in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    
    answer = sum(nums) + (max(nums) * 2)
    answers[t-1] = f'#{t} {answer}'
    
for i in answers:
    print(i)