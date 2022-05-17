T = int(input())
answers = [''] * T

for t in range(1, T+1):
    s = list(input())
    s.reverse()
    
    for i in range(len(s)):
        if s[i] == 'b':
            s[i] = 'd'
        elif s[i] == 'd':
            s[i] = 'b'
        elif s[i] == 'p':
            s[i] = 'q'
        else:
            s[i] = 'p'
    
    answer = ''.join(s)
    answers[t-1] = f'#{t} {answer}'

for i in answers:
    print(i)