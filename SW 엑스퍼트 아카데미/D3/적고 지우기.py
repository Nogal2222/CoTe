T = int(input())
answers = [''] * T

for t in range(1, T+1):
    s = input()
    stack =[]
    
    for i in s:
        num = int(i)
        
        if num not in stack:
            stack.append(num)
        else:
            stack.pop(stack.index(num))
    
    answer = len(stack)
    answers[t-1] = f'#{t} {answer}'

for i in answers:
    print(i)