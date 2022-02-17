# -*- coding: utf-8 -*-
import sys
#input = sys.stdin.readline
''' 시간초과
from math import factorial

def bi_co(n, k):
    if k >= 0 and k <= n:
        return factorial(n)//(factorial(k)*factorial(n-k))
    elif k < 0:
        return 0
    else:
        return 0

n, k = map(int, input().split())
num = str(bi_co(n, k))
cnt = 0
for i in range(len(num)-1, -1, -1):
    if int(num[i]) == 0:
       cnt += 1
    else:
        break

print(cnt)
'''

#10의 배수만 세는 방법
def fcount(n, k):
    count = 0
    while n:
        n //= k
        count += n
    return count

n, m = map(int, input().split())
five = fcount(n, 5) - fcount(m, 5) - fcount(n - m, 5)
two = fcount(n, 2) - fcount(m, 2) - fcount(n - m, 2)
ans = min(five, two)
print(ans)