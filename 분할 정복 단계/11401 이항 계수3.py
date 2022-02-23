import sys
#input = sys.stdin.readline

def power(a, b):
    if b == 1:
        ret1 = a % C
        return ret1
    else:
        temp = power(a, b//2)
        
        if b % 2 == 0:
            ret2 = temp * temp % C
            return ret2
        else:
            ret3 = temp * temp * a % C
            return ret3

C = 1000000007

n, k = map(int, input().split())

fact = [1 for i in range(n + 1)]
for i in range(2, n+1):
    fact[i] = fact[i-1] * i % C

A = fact[n]
B = (fact[n-k] * fact[k]) % C

print((A % C) * (power(B, C-2) % C) % C)