a, b = map(int, input().strip().split(' '))
for _ in range(b):
    print('*' * a)


''' for문 없이
a, b = map(int, input().strip().split(' '))
answer = ('*' * a + '\n') * b
print(answer)
'''