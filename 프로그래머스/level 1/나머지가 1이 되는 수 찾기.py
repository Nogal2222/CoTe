def getMyDivisor(n):

    divisorsList = []

    for i in range(1, int(n**0.5) + 1):
        if (n % i == 0):
            divisorsList.append(i) 
            if ( (i**2) != n) : 
                divisorsList.append(n // i)

    divisorsList.sort()
    
    return divisorsList

def solution(n):
    new_n = n - 1
    divisorsList = getMyDivisor(new_n)
    
    if len(divisorsList) == 2:
        answer = new_n
    
    else:
        if 1 in divisorsList:
            divisorsList[divisorsList.index(1)] = 10000000
        
        answer = min(divisorsList)
    
    return answer

n = 17
divisorsList = getMyDivisor(n-1)
print(solution(n))

''' 더 간단하게

def solution(n):
    x = n - 1
    if x % 2 == 0:
        return 2
    for i in range(2, int(n**0.5) + 1):
        if x % i == 0:
            return i
    return x
'''