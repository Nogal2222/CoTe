T = int(input())
answers = [''] * T

for t in range(1, T+1):
    word = input()
    cnt = 1
    len_word = len(word)

    for i in range(len_word):
        check = 1
        
        if i == 0:
            if word[i] != word[i+1]:
                check += 1
        
        elif i == len_word - 1:
            if word[i-1] != word[i]:
                check += 1
        
        else:
            if word[i-1] != word[i]:
                check += 1
            
            if word[i] != word[i+1]:
                check += 1
            
            if check > 1 and word[i-1] == word[i+1]:
                check -= 1
        
        cnt *= check
    
    answers[t-1] = f'#{t} {cnt}'

for i in answers:
    print(i)