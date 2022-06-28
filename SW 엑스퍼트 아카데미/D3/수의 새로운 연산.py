def make_list(start_list, target):
    while start_list[-1] <= target:
        start_list.append(len(start_list)+start_list[-1])
    
    gap = (target-start_list[-2])
    x, y = 1+ gap, (len(start_list)-1) - gap
    
    return x, y

T = int(input())

for test_case in range(1, T + 1):
    number_list = list(map(int, input().split()))
    number_list.sort()
    start_list = [1]
    x1, y1 = make_list(start_list, number_list[0])
    x2, y2 = make_list(start_list, number_list[1])
    x = x1+x2
    y = y1+y2
    
    while len(start_list) < (x+y):
        start_list.append(len(start_list)+start_list[-1])
    
    answer = start_list[-2] + (x-1)
    print(f"#{test_case} {answer}")

'''메모리 오버
def make_points():
    point = 1
    points = [[0] for _ in range(141)]
    x = 1
    y = 1

    while point < 10001:
        points[x].append(point)
        point += 1
        
        if y - 1 == 0:
            x = 1
            y = len(points[x])
        
        else:
            x += 1
            y -= 1
    
    
    return points

def sharp(x, y):
    return points[x][y]

def and_mark(p):
    for i in range(141):
        if p in points[i]:
            x = i
            y = points[i].index(p)
            break
    
    return x, y

def plus(x1, y1, x2, y2):
    nx = x1+x2
    ny = y1+y2
    
    return nx, ny

def star(p, q):
    x1, y1 = and_mark(p)
    x2, y2 = and_mark(q)
    
    nx, ny = plus(x1, y1, x2, y2)
    
    answer = sharp(nx, ny)
    
    return answer

T = int(input())
answers = [''] * T
for t in range(1, T+1):
    p, q = map(int, input().split())
    points = make_points()
    answer = star(p, q)
    answers[t-1] = f'#{t} {answer}'

for i in answers:
    print(i)
'''