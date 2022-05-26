T = int(input())
answers = [''] * T

for t in range(1, T+1):
    N, B, E = map(int, input().split())
    sand_cl = list(map(int, input().split()))
    
    min_B = B - E
    max_B = B + E
    cnt = 0
    
    for i in sand_cl:
        quote = B // i
        
        if min_B <= quote * i <= max_B:
            cnt += 1
    
    answers[t-1] = f'#{t} {cnt}'
    
for i in answers:
    print(i)