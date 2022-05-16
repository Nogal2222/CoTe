from collections import deque

T = int(input())
answers = [''] * T

for t in range(1, T+1):
    s = deque(input())
    stack = []
    
    while s:
        if s[0] not in stack:
            stack.append(s.popleft())
        
        else:
            stack.pop(stack.index(s[0]))
            s.popleft()
        
    if stack:
        stack.sort()
        answer = ''.join(stack)
    
    else:
        answer = 'Good'
    
    answers[t-1] = f'#{t} {answer}'

for i in answers:
    print(i)