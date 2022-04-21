import itertools

def snail(x, y, i):
    if i % 3 == 0:
        x += 1
    
    elif i % 3 == 1:
        y += 1
    
    else:
        x -= 1
        y -= 1
    
    return x, y

def solution(n):
    triangle = [[0 for k in range(1, i+1)] for i in range(1, n+1)]
    x, y = -1, 0
    num = 1
    
    for i in range(n):
        for j in range(i, n):
            x, y = snail(x, y, i)
            triangle[x][y] = num
            num += 1
    
    answer = list(itertools.chain(*triangle))
    
    return answer