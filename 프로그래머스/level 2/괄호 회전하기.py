from collections import deque

def check(sentence):
    stack = []
    
    for char in sentence:
        if char == '(' or char == '{' or char == '[':
            stack.append(char)
        
        else:
            if not stack:
                return False
            
            temp = stack.pop()
            
            if char == ')' and temp != '(':
                return False
            
            elif char == ']' and temp != '[':
                return False
            
            elif char == '}' and temp != '{':
                return False
        
    return len(stack) == 0

def solution(s):
    s = deque(s)
    answer = 0
    
    for i in range(len(s)):
        s.rotate(-1)
        
        if check(s):
            answer += 1
    
    return answer

s = "}}}"
result = solution(s)