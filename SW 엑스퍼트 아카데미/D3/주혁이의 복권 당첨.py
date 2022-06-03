T = int(input())
answers = [''] * T

for t in range(1, T+1):
    lot_nums = []
    lot_moneys = []
    own_nums = []
    tot_mon = 0
    cnt = 1
    
    N, M = map(int, input().split())
    
    for i in range(N):
        lot_num, lot_money = input().split()
        lot_money = int(lot_money)
        lot_nums.append(lot_num)
        lot_moneys.append(lot_money)
    
    for i in range(M):
        own_nums.append(input())
    
    for i in range(len(own_nums)):
        for j in range(len(lot_nums)):
            for k in range(8):
                if (own_nums[i][k] == lot_nums[j][k]) or lot_nums[j][k] == '*':
                    continue
                
                else:
                    break
            
            if k == 7:
                tot_mon += lot_moneys[j]
    
    answers[t-1] = f'#{t} {tot_mon}'

for i in answers:
    print(i)