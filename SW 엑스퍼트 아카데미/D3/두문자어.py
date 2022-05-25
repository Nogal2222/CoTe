T = int(input())
answers = [''] * T

for t in range(1, T+1):
    words = list(input().split())
    
    for i in range(len(words)):
        words[i] = words[i][0].upper()
    
    answer = ''.join(words)
    answers[t-1] = f'#{t} {answer}'

for i in answers:
    print(i)