def quad(y, x, N):
    if N == 1:
        return str(mapp[y][x])
    
    out = ''
    
    for i in range(y, y+N):
        for j in range(x, x+N):
            if mapp[i][j] != mapp[y][x]:
                out += '('
                out += quad(y, x, N//2)
                out += quad(y, x + N//2, N//2)
                out += quad(y + N//2, x, N//2)
                out += quad(y + N//2, x + N//2, N//2)
                out += ')'
                
                return out
    
    return str(mapp[y][x])


N = int(input())
mapp = [list(map(int, input())) for _ in range(N)]


print(quad(0, 0, N))