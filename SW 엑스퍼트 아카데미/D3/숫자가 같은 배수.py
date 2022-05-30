T = int(input())
answers = [''] * T

for t in range(1, T+1):
    N = input()
    lst_N = sorted(list(N))
    answer = 'impossible'
    
    for i in range(2, 10):
        Ni = sorted(list(str(int(N) * i)))
        
        if Ni == lst_N:
            answer = 'possible'
            break
    
    answers[t-1] = f'#{t} {answer}'

for i in answers:
    print(i)