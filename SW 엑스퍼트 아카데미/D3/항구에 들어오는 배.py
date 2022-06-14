T = int(input())
answers = [''] * T

for t in range(1, T+1):
    n = int(input())
    port = []
    
    for i in range(n):
        port.append(int(input()))
    
    ship = set()
    cnt = 0
    
    for i in range(1, len(port)):
        if port[i] in ship:
            continue
        
        gap = port[i] - 1
        
        for j in range(1 + gap, port[-1] + 1, gap):
            ship.add(j)
        
        cnt += 1
        
    answers[t-1] = f'#{t} {cnt}'

for i in answers:
    print(i)