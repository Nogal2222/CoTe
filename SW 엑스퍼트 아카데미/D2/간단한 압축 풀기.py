T = int(input())
answers = [''] * T

for t in range(1, T+1):
    n = int(input())
    s = ''

    for _ in range(n):
        word, nums = map(str, input().split())
        nums = int(nums)
        s += word*nums

    s = list(s[::-1])
    cnt = 0
    answer = ''
    print(f'#{t}')
    
    while s:
        answer += s.pop()
        cnt += 1
        
        if cnt == 10:
            cnt = 0
            print(answer)
            answer = ''

    print(answer)