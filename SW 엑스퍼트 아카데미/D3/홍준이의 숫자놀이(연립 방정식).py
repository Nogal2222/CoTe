def gcd(a, b):
    x,y, u,v = 0,1, 1,0
    
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    
    return [x, y]

for t in range(int(input())):
    A, B = map(int, input().split())
    print(f"#{t+1} {' '.join(map(str, gcd(A,B)))}")