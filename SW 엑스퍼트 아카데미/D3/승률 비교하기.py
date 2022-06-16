T = int(input())
answers = [''] * T

for t in range(1, T+1):
    A, B, C, D = map(int, input().split())
    A_winrate = A/B
    B_winrate = C/D
    
    if A_winrate == B_winrate:
        answer = "DRAW"
    
    elif A_winrate > B_winrate:
        answer = "ALICE"
    
    else:
        answer = "BOB"
    
    answers[t-1] = f'#{t} {answer}'

for i in answers:
    print(i)