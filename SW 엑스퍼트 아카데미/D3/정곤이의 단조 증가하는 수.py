def chkIncrease(number):
    number_string = str(number)
    for k in range(len(number_string) - 1):
        if number_string[k] > number_string[k+1]:
            return False
    return True


TC = int(input())
for t in range(1,TC+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    maxV = 0

    for i in range(N-1):
        for j in range(i+1,N):
            num = numbers[i] * numbers[j]
            
            if chkIncrease(num):
                maxV = max(maxV, num)
    
    if maxV == 0:
        maxV = -1

    print('#{} {}'.format(t,maxV))

''' 오답
T = int(input())
answers = [''] * T

for t in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    
    pro_lst = []
    max_dan = -1
    
    for i in range(N-1):
        pro_lst.append(nums[i] * nums[i+1])
    
    for i in range(len(pro_lst)):
        str_pro = str(pro_lst[i])
        flag = 0
        
        for j in range(len(str_pro)-1):
            if str_pro[j] > str_pro[j+1]:
                flag = 0
                break
            
            else:
                flag = 1
        
        if flag == 1:
            max_dan = max(max_dan, pro_lst[i])
    
    answers[t-1] = f'#{t} {max_dan}'

for i in answers:
    print(i)
'''