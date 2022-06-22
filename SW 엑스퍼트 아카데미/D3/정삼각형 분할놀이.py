T = int(input())
answers = [''] * T

for t in range(1, T+1):
    A, B = map(int, input().split())
    quotient = A // B
    answer = 0
    
    for i in range(quotient):
        answer += 2 * i + 1
    answers[t-1] = f'#{t} {answer}'

for i in answers:
    print(i)

''' 뭔가 안 되는 테스트 케이스가 있음
def triangle(N):
    low = N / 2
    height = ( (N ** 2) - (low ** 2) ) ** (1/2)
    
    return low * height * (1/2)

T = int(input())
answers = [''] * T

for t in range(1, T+1):
    A, B = map(int, input().split())
    answer = int(triangle(A) / triangle(B))
    answers[t-1] = f'#{t} {answer}'

for i in answers:
    print(i)
'''