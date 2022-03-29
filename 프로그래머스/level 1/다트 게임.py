def solution(dartResult):
    answer = 0
    lens = len(dartResult)
    stack = []
    
    for i in range(lens):
        if dartResult[i] == '1' and dartResult[i+1] == '0':
            stack.append(10)
            continue
        
        elif dartResult[i-1] == '1' and dartResult[i] == '0':
            continue
        
        elif dartResult[i].isdigit() == True:
            stack.append(int(dartResult[i]))
        
        elif dartResult[i] == 'S':
            stack[-1] **= 1
        
        elif dartResult[i] == 'D':
            stack[-1] **= 2
        
        elif dartResult[i] == 'T':
            stack[-1] **= 3
        
        elif dartResult[i] == '*':
            stack[-1] *= 2
            
            if len(stack) < 2:
                continue
            else:
                stack[-2] *= 2
        
        elif dartResult[i] == '#':
            stack[-1] *= -1
        
    for i in stack:
        answer += i
    
    return answer

dartResult = '10D4S10D'
print(solution(dartResult))

'''다른 풀이 : 10을 k로 치환
def solution(dartResult):
    point = []
    answer = []
    dartResult = dartResult.replace('10','k')
    point = ['10' if i == 'k' else i for i in dartResult]
    print(point)

    i = -1
    sdt = ['S', 'D', 'T']
    for j in point:
        if j in sdt :
            answer[i] = answer[i] ** (sdt.index(j)+1)
        elif j == '*':
            answer[i] = answer[i] * 2
            if i != 0 :
                answer[i - 1] = answer[i - 1] * 2
        elif j == '#':
            answer[i] = answer[i] * (-1)
        else:
            answer.append(int(j))
            i += 1
    return sum(answer)
'''