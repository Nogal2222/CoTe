T = int(input())
answers = [''] * T

for t in range(1, T+1):
    route = input()
    temp = [1, 1]
    
    for i in route:
        if i == 'L':
            temp[1] += temp[0]
        
        else:
            temp[0] += temp[1]
    answer = ' '.join(map(str, temp))        
    answers[t-1] = f'#{t} {answer}'

for i in answers:
    print(i)