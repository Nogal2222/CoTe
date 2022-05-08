T = int(input())
answers = [''] * T

for t in range(1, T+1):
    s = input()
    cnt_lst = []
    kind_s = list(set(list(s)))
    
    for j in kind_s:
        if s.count(j) != 2:
            answer = 'No'
            break
        
        else:
            answer = 'Yes'
    
    answers[t-1] = f'#{t} {answer}'

for i in answers:
    print(i)