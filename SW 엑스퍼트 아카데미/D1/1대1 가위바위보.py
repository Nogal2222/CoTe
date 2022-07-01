lst_ab = list(map(int, input().split()))

if lst_ab == [1,3] or lst_ab == [2, 1] or lst_ab == [3, 2]:
    answer = 'A'
else:
    answer = 'B'

print(answer)