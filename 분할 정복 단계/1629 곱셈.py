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


A, B, C = map(int, input().split())

result = power(A, B)

print(result)