def notation_convert(n, k):
    result = ''
    
    while n > 0:
        n, mod = divmod(n, k)
        result += str(mod)
    
    return result[::-1]

def is_prime(num):
    if num == 1:
        return False
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    
    return True

def solution(n, k):
    k_list = notation_convert(n, k)
    total = 0
    
    for num in k_list.split('0'):
        if num.isdigit():
            if is_prime(int(num)):
                total += 1
    
    return total

n = 437674
k = 3

result = solution(n, k)