T = int(input())
answers = [''] * T

for t in range(1, T+1):
    n, k = map(int, input().split())
    
    group = [[] for _ in range(k)]
    students = n * k
    cnt, idx, flag = 1, 0, 1

    while cnt <= students:
        group[idx].append(cnt)
        
        cnt += 1
        
        if flag:
            idx += 1
            
            if idx == k:
                idx -= 1
                flag = 0
        
        else:
            idx -= 1
            
            if idx == -1:
                idx += 1
                flag = 1

    group_sum = [str(sum(group[i])) for i in range(k)]

    answer = ' '.join(group_sum)
    answers[t-1] = f'#{t} {answer}'
    
for i in answers:
    print(i)