def solution(x):
    x_sum = sum(list(map(int, str(x))))
    
    return x % x_sum == 0
        

x = 13
result = solution(x)