def solution(s):
    if len(s) == 0:
        return 0
    
    s_list = list(s)
    stack = []
    stack.append(s_list.pop())
    
    while s_list:
        stack.append(s_list.pop())
        if len(stack) == 1:
            continue
        
        if stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
        
    if len(stack) > 0:
        return 0
    else:
        return 1

s = ''
result = solution(s)

'''for문을 이용한 풀이
def solution(s):
    answer = []
    for i in s:
        if not(answer):
            answer.append(i)
        else:
            if(answer[-1] == i):
                answer.pop()
            else:
                answer.append(i)    
    return not(answer)
'''