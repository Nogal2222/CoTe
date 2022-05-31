T = int(input())
answers = [''] * T

for t in range(1, T+1):
    s1, s2 = input().split()
    left = 0
    right = 0
    answer = "SAME"
    
    for i in range(len(s1)):
        if len(s1) != len(s2):
            answer = "DIFF"
            break
        
        if s1[i] == 'B':
            left = 2
        
        elif s1[i] == 'A' or s1[i] == 'D' or s1[i] == 'P' or s1[i] == 'Q' or s1[i] == 'O' or s1[i] == 'R':
            left = 1
        
        else:
            left = 0
        
        if s2[i] == 'B':
            right = 2
        
        elif s2[i] == 'A' or s2[i] == 'D' or s2[i] == 'P' or s2[i] == 'Q' or s2[i] == 'O' or s2[i] == 'R':
            right = 1
        
        else:
            right = 0
        
        if left != right:
            answer = "DIFF"
            break
        
    answers[t-1] = f'#{t} {answer}'

for i in answers:
    print(i)