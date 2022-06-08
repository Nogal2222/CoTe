month = {0:0, 1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 
         8:31, 9:30, 10:31, 11:30, 12:31}
day = [3, 4, 5, 6, 0, 1, 2]

T = int(input())
answers = [''] * T

for t in range(1, T+1):
    m, d = map(int, input().split())
    date = 0
    
    for i in range(m):
        date += month[i]
    
    date += d
    
    answer = day[date%7]
    
    answers[t-1] = f'#{t} {answer}'

for i in answers:
    print(i)