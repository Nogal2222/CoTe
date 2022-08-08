for tc in range(1, 11):
    n = int(input())
    lst = list(map(int, input().split()))
    summ = 0
    
    for i in range(2, n-2):
        temp = lst[i-2:i+3]
        temp.pop(2)
        
        if lst[i] > max(temp):
            summ += (lst[i] - max(temp))
    
    print(f'#{tc} {summ}')