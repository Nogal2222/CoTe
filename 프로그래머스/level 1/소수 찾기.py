def solution(n):
    answer = 0
    for i in range(2, n+1):
        if is_prime_number(i):
            answer += 1
    
    return answer

def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(x**0.5) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임

n = 10
result = solution(n)

''' 에라토스테네스의 체 풀이
def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)
'''