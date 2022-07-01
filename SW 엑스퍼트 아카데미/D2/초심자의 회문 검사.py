T = int(input())
answers = [''] * T
 
for t in range(1, T+1):
    word = input()
    answer = 1 if word == word[::-1] else 0
    answers[t-1] = f'#{t} {answer}'
 
for i in answers:
    print(i)