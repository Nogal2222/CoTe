def erathenes(start, end):
    arr = [True for i in range(end+1)]
    if start == 1:
        start = 2
    
    for i in range(2, int(end**0.5) + 1):
        if arr[i] == True:
            j = 2
            
            while i * j <= end:
                arr[i*j] = False
                j += 1
    
    return [i for i in range(start, end + 1) if arr[i]]

T = int(input())
answers = [''] * T

for t in range(1, T+1):
    D, A, B = map(int, input().split())
    D = str(D)
    
    arr = erathenes(A, B)
    cnt = 0
    
    for i in range(len(arr)):
        target = str(arr[i])
        
        if D in target:
            cnt += 1
    
    answers[t-1] = f'#{t} {cnt}'

for i in answers:
    print(i)