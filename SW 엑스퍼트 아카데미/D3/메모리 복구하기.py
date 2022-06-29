T = int(input())
answers = [''] * T

for t in range(1, T+1):
    bits = list(input())
    recovery = ['0'] * len(bits)
    cnt = 0
    
    for i in range(len(recovery)):
        if recovery[i] != bits[i]:
            recovery[i:] = bits[i] * len(recovery[i:])
            cnt += 1
    
    answers[t-1] = f'#{t} {cnt}'

for i in answers:
    print(i)