'''
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
'''
def rot90(lst, n):
    n_lst = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            n_lst[j][n-i-1] = str(lst[i][j])
    
    return n_lst

T = int(input())
answers = [''] * T
 
for t in range(1, T+1):
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]
    tot_lst = [['' for _ in range(3)] for _ in range(n)]
    
    for i in range(3):
        lst = rot90(lst, n)
        
        for j in range(n):
            s = ''.join(lst[j])
            tot_lst[j][i] = s
    
    print(f'#{t}')
    
    for i in range(n):
        new_s = ' '.join(tot_lst[i])
        print(new_s)