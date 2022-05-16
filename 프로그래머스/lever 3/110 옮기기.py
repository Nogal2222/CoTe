from collections import deque

def solution(s):
    answer = []
    
    for strings in s:
        stack = []
        cnt = 0
        
        for string in strings:
            if string == '0':
                if stack[-2:] == ['1', '1']:
                    cnt += 1
                    
                    for _ in range(2):
                        stack.pop()
                
                else:
                    stack.append(string)
            
            else:
                stack.append(string)
        
        if cnt == 0:
            answer.append(strings)
        
        else:
            result = deque()
            
            while stack:
                if stack[-1] == '1':
                    result.append(stack.pop())
                
                elif stack[-1] == '0':
                    break
            
            while cnt > 0:
                result.appendleft('0')
                result.appendleft('1')
                result.appendleft('1')
                cnt -= 1
            
            while stack:
                result.appendleft(stack.pop())
            
            answer.append(''.join(result))
    
    return answer

s = ["1110","100111100","0111111010"]

rslt = solution(s)