'''
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
'''
answers = [''] * 10
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(maps, start):
    stack = start
    
    while stack:
        x, y = stack.pop()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < 16 and 0 <= ny < 16:
                if maps[nx][ny] == '0':
                    stack.append((nx, ny))
                    maps[nx][ny] = 'o'
                
                elif maps[nx][ny] == '3':
                    answer = 1
                    stack.clear()
                    break
                
                else:
                    answer = 0
                    
    return answer

for t in range(1, 11):
    tc = int(input())
    maps = [list(input()) for _ in range(16)]
    start = 0
    
    for i in range(16):
        for j in range(16):
            if maps[i][j] == '2':
                start = [(i, j)]
                break
        
        if start:
            break
    answer = dfs(maps, start)
    
    answers[t-1] = f'#{t} {answer}'
 
for i in answers:
    print(i)