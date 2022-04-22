def solution(line):
    star_list = []
    len_line = len(line)
    for i in range(len_line):
        for j in range(i+1, len_line):
            a, b, e = line[i]
            c, d, f = line[j]
            
            sol = (a * d) - (b * c)
            if sol != 0:
                x, y = ((b * f) - (e * d)) / sol, ((e * c) - (a * f)) / sol
                
                if x.is_integer() and y.is_integer():
                    x, y = int(x), int(y)
                    
                    if (x, y) not in star_list:
                        star_list.append((x, y))
    
    x_min = min(star_list)[0]
    x_max = max(star_list)[0]
    y_min = min(star_list, key = lambda x: x[1])[1]
    y_max = max(star_list, key = lambda x: x[1])[1]
    stars = [['.'] * (abs(x_max - x_min) + 1) for _ in range(abs(y_max - y_min) + 1)]
    
    for star in star_list:
        x, y = star
        new_x = abs(y_max - y)
        new_y = abs(x_min - x)
        stars[new_x][new_y] = '*'
    
    for index, value in enumerate(stars):
        stars[index] = ''.join(value)
    
    return stars

line = [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]

result = solution(line)