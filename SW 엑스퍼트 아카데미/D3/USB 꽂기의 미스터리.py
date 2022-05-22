T = int(input())
answers = [''] * T

for t in range(1, T+1):
    p, q = map(float, input().split())
    
    # 한 번 뒤집어서 제대로 꽂는 경우
    s1 = (1 - p) * q
    
    # 두 번 뒤집어서 제대로 꽂는 경우
    s2 = p * (1 - q) * q
    
    answer = "YES" if s1 < s2 else "NO"
    
    answers[t-1] = f'#{t} {answer}'

for i in answers:
    print(i)