T = int(input())
answers = [''] * T

for t in range(1, T+1):
    x1, y1, x2, y2 = map(int, input().split())
    cnt_line, cnt_inside, cnt_outside = 0, 0, 0
    
    N = int(input())
    
    for i in range(N):
        x, y = map(int, input().split())
        
        if ((y == y1 or y == y2) and min(x1, x2) <= x <= max(x1, x2)) or ((x == x1 or x == x2) and min(y1, y2) <= x <= max(y1, y2)):
            cnt_line += 1
        
        elif (min(y1, y2) < y < max(y1, y2)) and (min(x1, x2) < x < max(x1, x2)):
            cnt_inside += 1
        
        else:
            cnt_outside += 1
    
    answers[t-1] = f'#{t} {cnt_inside} {cnt_line} {cnt_outside}'

for i in answers:
    print(i)