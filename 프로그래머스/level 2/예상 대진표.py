n = 8
a = 4
b = 7

def solution(n,a,b):
    cnt = 0

    while a != b:
        a = (a + 1) // 2
        b = (b + 1) // 2
        
        cnt += 1
        
    return cnt

result = solution(n, a, b)