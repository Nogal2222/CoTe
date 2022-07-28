'''
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
'''
T = int(input())
answers = [''] * T
 
for t in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    answer = 1
    tbt = [[[] for _ in range(3)] for _ in range(3)]
    
    for i in range(9):
        row = []
        col = []
        
        for j in range(9):
            if sudoku[i][j] in row or sudoku[j][i] in col or sudoku[i][j] in tbt[i//3][j//3]:
                answer = 0
                break
            
            row.append(sudoku[i][j])
            col.append(sudoku[j][i])
            tbt[i//3][j//3].append(sudoku[i][j])
        
        if not answer:
            break
    
    answers[t-1] = f'#{t} {answer}'
 
for i in answers:
    print(i)
        

