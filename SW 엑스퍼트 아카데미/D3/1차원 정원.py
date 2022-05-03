import sys
#input = sys.stdin.readline
T = int(input())

for i in range(1, T+1):
    N, D = map(int, input().split())
    new_D = D * 2 + 1
    temp = N // new_D
    
    if N % new_D == 0:
        answer = temp
    else:
        answer = temp + 1
    
    print("#%d " %i, end = '')
    print(answer)
    answer = 0