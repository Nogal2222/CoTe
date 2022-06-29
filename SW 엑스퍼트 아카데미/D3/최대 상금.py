T = int(input())
answers = [''] * T

for t in range(1, T+1):
    data, K = input().split() # 숫자판의 정보, 교환횟수
    K = int(K)
    N = len(data)
    now = set([data])
    nxt = set()
    
    for _ in range(K):
        while now:
            s = now.pop()
            s = list(s)
            
            for i in range(N):
                for j in range(i+1,N):
                    s[i],s[j] = s[j],s[i]
                    nxt.add(''.join(s))
                    s[i], s[j] = s[j], s[i]
        
        now,nxt = nxt,now
    
    answer = max(map(int, now))
    answers[t-1] = f'#{t} {answer}'

for i in answers:
    print(i)