T = int(input())
answers = [''] * T
alphas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for t in range(1, T+1):
    n = int(input())
    cnt = 0
    titles = [''] * n
    
    for i in range(n):
        title = input()
        titles[i] = title[0]

    titles = sorted(list(set(titles)))

    for alpha in alphas:
        if alpha not in titles:
            break
        
        for title in titles:
            if title == alpha:
                cnt += 1
                break
            
            else: continue
        
    
    answers[t-1] = f'#{t} {cnt}'

for i in answers:
    print(i)