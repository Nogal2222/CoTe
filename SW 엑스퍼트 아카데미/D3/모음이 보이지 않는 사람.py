vowel = ['a', 'e', 'i', 'o', 'u']

T = int(input())
answers = [''] * T

for t in range(1, T+1):
    words = list(input())
    i = 0
    answer = ''
    
    for i in range(len(words)):
        if words[i] not in vowel:
            answer += words[i]
    
    answers[t-1] = f'#{t} {answer}'

for i in answers:
    print(i)