T = int(input())
answers = [''] * T

for t in range(1, T+1):
    walls = list(map(int, input().split()))
    
    stack = []
    
    for i in range(len(walls)):
        if walls[i] not in stack:
            stack.append(walls[i])
        
        else:
            stack.pop(walls.index(walls[i]))
    
    answer = stack[0]
    answers[t-1] = f'#{t} {answer}'

for i in answers:
    print(i)