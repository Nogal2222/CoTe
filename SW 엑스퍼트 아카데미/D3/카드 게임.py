T = int(input())
answers = [''] * T

for t in range(1, T+1):
    card_num = {2:4, 3:4, 4:4, 5:4, 6:4, 7:4, 8:4, 9:4, 10:16, 11:4}
    
    n = int(input())
    cur_val = 0
    
    for _ in range(n):
        card = int(input())
        cur_val += card
        card_num[card] -= 1
    
    rem_val = 21 - cur_val
    rem_card = 52 - n
    
    less = 0
    
    for i in range(2, rem_val + 1):
        less += card_num[i]
        
    over = rem_card - less
    
    if over >= less:
        answer = "STOP"
    
    else:
        answer = "GAZUA"
    
    answers[t-1] = f'#{t} {answer}'

for i in answers:
    print(i)