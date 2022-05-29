T = int(input())
answers = [''] * T

for t in range(1, T+1):
    cur_hh, cur_mm, cur_ss = map(int,input().split(':'))
    pro_hh, pro_mm, pro_ss = map(int,input().split(':'))
    
    rem_hh, rem_mm, rem_ss = pro_hh - cur_hh, pro_mm - cur_mm, pro_ss - cur_ss
    
    if rem_ss < 0:
        rem_ss += 60
        rem_mm -= 1
        
    if rem_mm < 0:
        rem_mm += 60
        rem_hh -= 1
            
    if rem_hh < 0:
        rem_hh += 24
    
    rem_hh = str(rem_hh).zfill(2)
    rem_mm = str(rem_mm).zfill(2)
    rem_ss = str(rem_ss).zfill(2)
    
    answers[t-1] = f'#{t} {rem_hh}:{rem_mm}:{rem_ss}'

for i in answers:
    print(i)