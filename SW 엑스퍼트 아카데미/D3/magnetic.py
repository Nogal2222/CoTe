for t in range(1, 11):
    N = int(input())
    mag = [list(map(int, input().split())) for _ in range(N)]
    answer = 0
    
    for i in range(N):
        target = 0
        
        for j in range(N):
            if mag[j][i] == 1 and target == 0:
                target = 1
            elif mag[j][i] == 2 and target == 1:
                target = 0
                answer += 1
    
    print(f'#{t} {answer}')