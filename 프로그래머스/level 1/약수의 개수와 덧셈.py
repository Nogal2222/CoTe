# -*- coding: utf-8 -*-
def getMyDivisor(n):
    divisorsList = []

    for i in range(1, int(n**(1/2)) + 1):
        if n % i == 0:
            divisorsList.append(i)
            
            if (i**2) != n : 
                divisorsList.append(n // i)

    divisorsList.sort()
    
    return divisorsList

def solution(left, right):
    answer = 0
    
    for i in range(left, right + 1):
        cnt = len(getMyDivisor(i))
        
        if cnt % 2 == 0:
            answer += i
        else:
            answer -= i
    
    return answer

left = int(input())
right = int(input())
print(solution(left, right))

''' 다른 사람 코드
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer
'''