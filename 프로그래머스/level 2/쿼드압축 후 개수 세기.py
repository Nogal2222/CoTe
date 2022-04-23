def solution(arr):
    
    
    def quadtree(x, y, n):
        if n == 1:
            return(str(arr[x][y]))
        
        result = []
        
        for i in range(x, x + n):
            for j in range(y, y + n):
                if arr[i][j] != arr[x][y]:
                    result.extend(quadtree(x, y, n//2))
                    result.extend(quadtree(x, y + n//2, n//2))
                    result.extend(quadtree(x + n//2, y, n//2))
                    result.extend(quadtree(x + n//2, y + n//2, n//2))
                    
                    return result
        
        return str(arr[x][y])
    
    
    quad = quadtree(0, 0, len(arr))
    answer = [quad.count('0'), quad.count('1')]
    
    return answer

arr = [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]

result = solution(arr)

'''내가 하고 싶었던 것
def solution(arr):
    answer = [0, 0]

    def check(size, x, y):
        if size == 1:
            answer[arr[y][x]] += 1
            return
        else:
            first = arr[y][x]

            for dy in range(size):
                for dx in range(size):
                    if first != arr[y + dy][x + dx]:
                        check(size // 2, x, y)
                        check(size // 2, x + size // 2, y)
                        check(size // 2, x, y + size // 2)
                        check(size // 2, x + size // 2, y + size // 2)
                        return
            answer[first] += 1
    check(len(arr),0,0)


    return answer
'''