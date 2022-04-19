def getMyDivisor(n):
    divisorsList = []
    
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisorsList.append(i) 
            
            if i ** 2 != n : 
                divisorsList.append(n // i)

    divisorsList.sort()
    
    return divisorsList

def solution(brown, yellow):
    y_divisors = getMyDivisor(yellow)
    

    while y_divisors:
        len_divisors = len(y_divisors)
        if len_divisors != 1:
            y_width = y_divisors.pop(-1)
            y_height = y_divisors.pop(0)
            
        
        else:
            y_width = y_divisors.pop(0)
            y_height = y_width
        
        if (y_width + 2) * 2 + y_height * 2 == brown:
            width = y_width + 2
            height = y_height + 2
            break
    
    answer = [width, height]
    
    return answer

brown = 20
yellow = 16

result = solution(brown, yellow)


'''근의 공식을 이용한 풀이
import math

def solution(brown, yellow):
    w = ((brown+4)/2 + math.sqrt(((brown+4)/2)**2-4*(brown+yellow)))/2
    h = ((brown+4)/2 - math.sqrt(((brown+4)/2)**2-4*(brown+yellow)))/2
    return [w,h]
'''

'''둘레 길이를 이용한 풀이
def solution(brown, yellow):
    for i in range(1, int(yellow ** 0.5) + 1):
        if red % i == 0:
            if 2 * (i + red // i) == brown - 4:
                return [red // i + 2, i + 2]
'''