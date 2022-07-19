for t in range(1, 11):
    dump = int(input())
    lst = list(map(int, input().split()))
    
    for _ in range(dump):
        lst[lst.index(max(lst))] -= 1
        lst[lst.index(min(lst))] += 1
    
    answer = max(lst) - min(lst)
    
    print(f'#{t} {answer}')