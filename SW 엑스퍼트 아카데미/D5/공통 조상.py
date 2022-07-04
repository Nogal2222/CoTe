'''
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
'''

T = int(input())
answers = [''] * T

def bfs(n):
    cnt = 1
    temp = []
    
    for i in range(1, 3):
        if arr[n][i] != 0:
            temp.append(arr[n][i])
            cnt += 1
    
    while len(temp) != 0:
        x = temp.pop(0)
        
        for i in range(1, 3):
            if arr[x][i] != 0:
                temp.append(arr[x][i])
                cnt += 1
    
    return cnt

for t in range(1, T+1):
    v, e, a, b = map(int, input().split())
    e_lst = list(map(int, input().split()))
    
    arr = [[0, 0, 0] for _ in range(v+1)]
    
    for i in range(e):
        if arr[e_lst[i*2]][1] == 0:
            arr[e_lst[i*2]][1] = e_lst[i*2 + 1]
        
        else:
            arr[e_lst[i*2]][2] = e_lst[i*2 + 1]
        
        arr[e_lst[i*2 +1]][0] = e_lst[i*2]
        
    a_lst = []
    b_lst = []
    
    while 1:
        if a != 0:
            a = arr[a][0]
            a_lst.append(a)
        
        if b != 0:
            b = arr[b][0]
            b_lst.append(b)
        
        if a == 0 and b == 0:
            break
        
    answer = 0
    
    for i in a_lst:
        if answer != 0:
            break
        
        for j in b_lst:
            if i == j:
                answer = i
                break
    
    cnt = bfs(answer)
    
    answers[t-1] = f'#{t} {answer} {cnt}'
 
for i in answers:
    print(i)