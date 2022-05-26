from fractions import Fraction

T = int(input())
answers = [''] * T

for t in range(1, T+1):
    s = input()
    order = []
    
    # s를 리스트로
    while s:
        if s[0] == 'n':
            order.append('n')
            s = s[5:]
        
        else:
            order.append('w')
            s = s[4:]
    
    # 제일 끝이 방향
    if order.pop(-1) == 'n':
        dir_a = 0
    
    else:
        dir_a = 90
    
    # 끝쪽부터 계산하기 위해 뒤집음
    order.reverse()
    
    for i in range(len(order)):
        if order[i] == 'w':
            dir_a += (90 / (2 ** (1 + i) ) )
        
        else:
            dir_a -= (90 / (2 ** (1 + i) ) )
    
    # Fraction : 소수를 분수로 바꿔줌
    answer = Fraction(dir_a)
    answers[t-1] = f'#{t} {answer}'
    
for i in answers:
    print(i)