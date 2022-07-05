T = int(input())
answers = [''] * T

def find_idx(word):
    for i in range(N):
        for j in range(M-1, 0, -1):
            if info[i][j]:
                line = i
                idx = j
                
                return line, idx

def change(number):
    dic = {'0001101': '0', '0011001': '1',
           '0010011': '2', '0111101': '3',
           '0100011': '4', '0110001': '5',
           '0101111': '6', '0111011': '7',
           '0110111': '8', '0001011': '9'}

    return dic[number]

for t in range(1, T+1):
    N, M = map(int, input().split())
    info = [list(map(int, input()))for _ in range(N)]

    line = find_idx(info)[0]
    idx = find_idx(info)[1]

    password = info[line][idx-55:idx+1]
    result = ''
    
    for i in range(0, len(password), 7):
        temp = ''
        
        for j in range(i, i+7):
            temp += str(password[j])
        
        result += change(temp)

    odd = 0
    even = 0

    for i in range(7):
        if i % 2:
            even += int(result[i])
        
        else:
            odd += int(result[i])
    
    check = odd * 3 + even + int(result[7])

    if check % 10:
        total = 0
    
    else:
        total = 0
        
        for i in range(8):
            total += int(result[i])
    
    answers[t-1] = f'#{t} {total}'

for i in answers:
    print(i)