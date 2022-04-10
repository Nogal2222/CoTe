def divide(p):
    open_p = 0
    close_p = 0
    
    for i in range(len(p)):
        if p[i] == '(':
            open_p += 1
        
        else:
            close_p += 1
        
        if open_p == close_p:
            return p[:i+1], p[i+1:]

def check(u):
    stack = []
    
    for p in u:
        if p == '(':
            stack.append(p)
        
        else:
            if not stack:
                return False
            
            stack.pop()
    
    return True

def solution(p):
    if not p:
        return ''
    
    u, v = divide(p)
    
    if check(u):
        return u + solution(v)
    
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        
        for p in u[1:len(u) -1]:
            if p == '(':
                answer += ')'
            else:
                answer += '('
        
        return answer

'''다른 풀이
def solution(p):
    if p=='': return p
    r=True; c=0
    for i in range(len(p)):
        if p[i]=='(': c-=1
        else: c+=1
        if c>0: r=False
        if c==0:
            if r:
                return p[:i+1]+solution(p[i+1:])
            else:
                return '('+solution(p[i+1:])+')'+''.join(list(map(lambda x:'(' if x==')' else ')',p[1:i]) ))
'''