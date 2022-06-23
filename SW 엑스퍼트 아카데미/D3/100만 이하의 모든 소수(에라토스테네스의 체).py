n = 1000000
a = [True] * (n + 1)
m = int(n**0.5)

for i in range(2, m + 1):
    if a[i] == True:
        for j in range(i + i, n + 1, i):
            a[j] = False

prime = [str(i) for i in range(2, n + 1) if a[i] == True]
answer = ' '.join(prime)
print(answer)