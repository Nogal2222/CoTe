T = int(input())
answers = [''] * T

for t in range(1, T+1):
    s = list(input())
    H = int(input())
    hyp = sorted(list(map(int, input().split())), reverse=True)
    
    for i in hyp:
        s.insert(i, '-')
    
    answer = ''.join(s)
    answers[t-1] = f'#{t} {answer}'

for i in answers:
    print(i)
    
'''처음에 짠거 (라잌 언에듀케이티드)
T = int(input())
answers = [''] * T

for t in range(1, T+1):
    s = list(input())
    H = int(input())
    hyp = sorted(list(map(int, input().split())))
    
    for i in range(H):
        if hyp[i] == 0:
            s[0] = '-' + s[0]
        
        elif hyp[i] == 1:
            s[0] += '-'
        
        elif hyp[i] == 2:
            s[1] += '-'
        
        elif hyp[i] == 3:
            s[2] += '-'
        
        elif hyp[i] == 4:
            s[3] += '-'
        
        elif hyp[i] == 5:
            s[4] += '-'
        
        elif hyp[i] == 6:
            s[5] += '-'
        
        elif hyp[i] == 7:
            s[6] += '-'
        
        elif hyp[i] == 8:
            s[7] += '-'
        
        elif hyp[i] == 9:
            s[8] += '-'
        
        elif hyp[i] == 10:
            s[9] += '-'
        
        elif hyp[i] == 11:
            s[10] += '-'
        
        elif hyp[i] == 12:
            s[11] += '-'
        
        elif hyp[i] == 13:
            s[12] += '-'
        
        elif hyp[i] == 14:
            s[13] += '-'
        
        elif hyp[i] == 15:
            s[14] += '-'
        
        elif hyp[i] == 16:
            s[15] += '-'
        
        elif hyp[i] == 17:
            s[16] += '-'
        
        elif hyp[i] == 18:
            s[17] += '-'
        
        elif hyp[i] == 19:
            s[18] += '-'
        
        elif hyp[i] == 20:
            s[19] += '-'
    
    answer = ''.join(s)
    answers[t-1] = f'#{t} {answer}'

for i in answers:
    print(i)
'''