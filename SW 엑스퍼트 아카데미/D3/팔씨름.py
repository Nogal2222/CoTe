T = int(input())

for i in range(1, T+1):
    S = input()
    
    x_cnt = S.count('x')
    
    if x_cnt > 7:
        print('#%d NO' %i)
    
    else:
        print('#%d YES' %i)