# -*- coding: utf-8 -*-
import sys
#input = sys.stdin.readline

#4000000 이하의 모든 소수를 추출
prime_ox = [True for _ in range(4000001)]

#에라토스테네스의 체
for i in range(2, int(4000001 ** 0.5)):
    if prime_ox[i]:
        for j in range(i+i, 4000001, i):
            prime_ox[j] = False

prime_list = [i for i, j in enumerate(prime_ox) if j == True and i >= 2]


#0~i까지의 부분합 리스트를 만들어줌
sum_prime = [0] * (len(prime_list) + 1)

for i in range(len(prime_list)):
    sum_prime[i+1] = sum_prime[i] + prime_list[i]


#input
n = int(input())

#투포인터 설정
answer, start, end = 0, 0, 1

#알고리즘 실행
while start < len(sum_prime) and prime_list[end-1] <= n:
    #소수와 같을 경우
    if sum_prime[end] - sum_prime[start] == n:
        answer += 1
        start += 1
    
    #소수보다 클 경우 start += 1
    elif sum_prime[end] - sum_prime[start] > n:
        start += 1
    
    
    else:
        #소수보다 작을 경우 end += 1
        if end < len(sum_prime) - 1:
            end += 1
        else:
            start += 1

print(answer)