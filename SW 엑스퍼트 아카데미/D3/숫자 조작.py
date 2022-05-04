from itertools import combinations

T = int(input())

for i in range(1, T+1):
    num = input()
    num_lst = [int(num)]
    
    for fst, snd in combinations(range(len(num)), 2):
        n_parts = list(num)
        n_parts[fst], n_parts[snd] = n_parts[snd], n_parts[fst]
        
        if n_parts[0] == '0':
            continue
        
        num_lst.append(int(''.join(n_parts)))
    
    print(f'#{i} {min(num_lst)} {max(num_lst)}')