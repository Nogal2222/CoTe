from itertools import permutations

def operation(num1, num2, op):
    if op == '+':
        return str(int(num1) + int(num2))
    
    if op == '-':
        return str(int(num1) - int(num2))
    
    if op == '*':
        return str(int(num1) * int(num2))
    
def calculate(exp,op):
    array=[]
    tmp=""
    
    for i in exp:
        if i.isdigit()==True:
            tmp+=i
        
        else:
            array.append(tmp)
            array.append(i)
            tmp=""
    
    array.append(tmp)
    
    for o in op:
        stack=[]
        
        while len(array)!=0:
            tmp=array.pop(0)
            
            if tmp==o:
                stack.append(operation(stack.pop(), array.pop(0), o))
            else:
                stack.append(tmp)
        
        array=stack
            
    return abs(int(array[0]))

def solution(expression):
    op = ['+', '-', '*']
    op = list(permutations(op, 3))
    result=[]
    for i in op:
        result.append(calculate(expression, i))
    return max(result)

'''다른 풀이
def solution(expression):
    operations = [('+', '-', '*'), ('+', '*', '-'),
                  ('-', '+', '*'), ('-', '*', '+'),
                  ('*', '+', '-'), ('*', '-', '+')]
    answer = []
    for op in operations:
        a = op[0]
        b = op[1]
        temp_list = []
        for e in expression.split(a):
            temp = [f"({i})" for i in e.split(b)]
            temp_list.append(f'({b.join(temp)})')
        answer.append(abs(eval(a.join(temp_list))))
    return max(answer)
'''