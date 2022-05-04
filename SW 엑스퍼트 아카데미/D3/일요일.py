T = int(input())
date_dict = {'SUN' : 0, 'MON' : 1, 'TUE' : 2,
             'WED' : 3, 'THU' : 4, 'FRI' : 5,
             'SAT' : 6}

for t in range(1, T+1):
    answer = 7 - date_dict[input()]
    print(f'#{t} {answer}')