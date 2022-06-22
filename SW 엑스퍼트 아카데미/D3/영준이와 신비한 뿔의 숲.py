T = int(input())
answers = [''] * T

for t in range(1, T+1):
    horns, animals = map(int, input().split())
    twin = horns - animals
    uni = animals - twin
    
    answers[t-1] = f'#{t} {uni} {twin}'

for i in answers:
    print(i)