n = 16 # 진법
t = 16 # 구해야 할 숫자 갯수
m = 2 # 플레이어 수
p = 1 # 튜브 순서

def notation_convert(num, base):
    temp = '0123456789ABCDEF'
    qoute, remainder = divmod(num, base)
    
    if qoute == 0:
        return temp[remainder]
    
    else:
        return notation_convert(qoute, base) + temp[remainder]

def solution(n, t, m, p):
    answer = ''
    test = ''
    
    for i in range(m * t):
        test += str(notation_convert(i, n))
    
    while len(answer) < t:
        answer += test[p-1]
        p += m
    
    return answer

result = solution(n, t, m, p)