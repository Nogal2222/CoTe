T = int(input())
answers = [''] * T

for t in range(1, T+1):
    alpha = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0, }
    n = int(input())
    words = [''] * n
    alpha_check = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    for i in range(n):
        words[i] = input()
    
    for j in words:
        for k in j:
            alpha[k] += 1
    
    min_set = alpha['a']
    
    for l in alpha_check:
        min_set = min(min_set, alpha[l])
    
    answers[t-1] = f'#{t} {min_set}'

for i in answers:
    print(i)