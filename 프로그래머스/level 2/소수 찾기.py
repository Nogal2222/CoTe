from itertools import permutations

def solution(numbers):
    #numbers 각 글자로 쪼갬
    number = [n for n in numbers]
    
    #다양한 조합 추가
    permutation = []
    
    for s in range(1, len(numbers) + 1):
        permutation += list(permutations(number, s))
    
    new_number = list(set(int(("").join(p)) for p in permutation))
    
    #소수인지 확인
    prime_number = []
    
    for n in new_number:
        if n < 2:
            continue
        
        check = True
        
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                check = False
                break
            
        if check:
            prime_number.append(n)
    
    answer = len(prime_number)
    
    return answer

numbers = '17'
result = solution(numbers)