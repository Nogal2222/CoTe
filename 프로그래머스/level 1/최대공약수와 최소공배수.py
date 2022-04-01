def gcd(n, m):
    while m:
        n, m = m, n % m
    
    return n

def lcm(n, m):
    lcm = n * m // gcd(n, m)
    
    return lcm

def solution(n, m):
    answer = [gcd(n, m), lcm(n, m)]
    
    return answer

n = 5
m = 2
result = solution(n, m)

''' lcm 함수를 안받아서 못씀
import math

def solution(n, m):
    answer = [math.gcd(n, m), math.lcm(n, m)]
    return answer
'''
