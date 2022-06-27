tank = ['<', '^', '>', 'v']
obstacle = ['*','#','-']

def isgotank(x,y,dir,X,Y):
    if y < 0 or y == W:
        return False
    
    if x < 0 or x == H:
        return False
    
    if maps[x][y] in obstacle:
        return False
    
    maps[x][y] = tank[dir]
    maps[X][Y] = '.'
    
    return True

def isgobullet(x,y):
    if y < 0 or y == W:
        return False
    
    if x < 0 or x == H:
        return False
    
    if maps[x][y] == '#':
        return False
    if maps[x][y] == '*':
        maps[x][y] = '.'
        
        return False
    
    return True


def position():
    for i in range(H):
        for j in range(W):
            if maps[i][j] in tank:
                return (i,j)

def play():
    global dir
    x, y = start
    
    for code in codes:
        if code == 'U':
            dir = 1
            maps[x][y] = tank[dir]
            x -= 1
            
            if isgotank(x,y, dir, x + 1, y):
                pass
            
            else:
                x += 1
        
        elif code == 'D':
            dir = 3
            maps[x][y] = tank[dir]
            x += 1
            
            if isgotank(x, y, dir, x - 1, y):
                pass
            
            else:
                x -= 1
        
        elif code == 'L':
            dir = 0
            maps[x][y] = tank[dir]
            y -= 1
            
            if isgotank(x, y, dir, x, y + 1):
                pass
            
            else:
                y += 1
        
        elif code == 'R':
            dir = 2
            maps[x][y] = tank[dir]
            y += 1
            
            if isgotank(x, y, dir, x, y - 1):
                pass
            
            else:
                y -= 1
        
        elif code == 'S':
            bx, by = x, y
            
            if dir == 0:
                by -= 1
                
                while isgobullet(bx, by):
                    by -= 1
            
            elif dir == 1:
                bx -= 1
                
                while isgobullet(bx, by):
                    bx -= 1
            
            elif dir == 2:
                by += 1
                
                while isgobullet(bx, by):
                    by += 1
            
            elif dir == 3:
                bx += 1
                
                while isgobullet(bx, by):
                    bx += 1

for tc in range(1,int(input())+1):
    H,W = map(int,input().split())
    maps = [list(input()) for i in range(H)]
    n = int(input())
    codes = list(input())
    start = position()
    
    for i in range(len(tank)):
        if tank[i] == maps[start[0]][start[1]]:
            dir = i
    
    play()
    print('#{}'.format(tc), end=' ')
    
    for i in maps:
        print(''.join(i))