T = int(input())
answers = [''] * T

for t in range(1, T+1):
    cities, limit = map(int, input().split())
    map_info = list(map(int, input().split()))

    answer = 0
    cnt = 0

    if map_info[0] == 0:
        answer += 1
        map_info[0] = 1

    if map_info[-1] == 0:
        answer += 1
        map_info[-1] = 1

    for i in range(cities):
        if map_info[i] == 1:
            cnt = 0
        
        else:
            cnt += 1
            
            if cnt >= limit:
                answer += 1
                cnt = 0

    answers[t-1] = f'#{t} {answer}'

for i in answers:
    print(i)