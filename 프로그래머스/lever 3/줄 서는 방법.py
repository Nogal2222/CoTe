from math import factorial

def solution(n, k):
    answer = []
    numberList = [i for i in range(1, n+1)]
    while (n != 0):
        temp = factorial(n) // n
        index = k // temp
        k = k % temp
        
        if k == 0:
            answer.append(numberList.pop(index-1))
        
        else :
             answer.append(numberList.pop(index))

        n -= 1
    
    return answer

n = 3
k = 5

result = solution(n, k)

''' 시간초과 (permutations는 n!의 반복횟수)
from itertools import permutations

def solution(n, k):
    lst_n = list(range(1, n+1))
    n_perm = list(permutations(lst_n, n))

    answer = list(n_perm[k-1])
    
    return answer
'''