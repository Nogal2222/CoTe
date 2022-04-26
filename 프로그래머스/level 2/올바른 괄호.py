def solution(s):
    stack = []
    answer = True

    if s.count('(') == s.count(')'):
        for i in s:
            if i == '(':
                stack.append(i)
            
            elif i == ')' and stack and stack[-1] == '(':
                stack.pop()
            
            else:
                answer = False
                break

    else:
        answer = False
        
    if answer == False or stack:
        answer = False

    else:
        answer = True
    
    return answer

s = "(()("

result = solution(s)