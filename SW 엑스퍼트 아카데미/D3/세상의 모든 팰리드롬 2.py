T = int(input())
answers = [''] * T

for t in range(1, T+1):
    answer = 'Not exist'
    word = input()
    rev_word = word[::-1]
    
    for i in range(len(word)):
        if word[i] == rev_word[i]:
            continue
        
        if word[i] == '*' or rev_word[i] == '*':
            answer = 'Exist'
            break
        
        else:
            break
    
    else:
        answer = 'Exist'
    
    answers[t-1] = f'#{t} {answer}'

for i in answers:
    print(i)