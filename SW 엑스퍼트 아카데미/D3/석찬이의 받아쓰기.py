T = int(input())
answers = [''] * T

for t in range(1, T+1):
    length = int(input())
    parrent = input()
    child = input()
    cnt = 0
    
    for i in range(length):
        if parrent[i] == child[i]:
            cnt += 1
    
    answers[t-1] = f'#{t} {cnt}'

for i in answers:
    print(i)