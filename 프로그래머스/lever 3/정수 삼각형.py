def solution(triangle):
    answer = 0
    triangle = [[0] + t + [0] for t in triangle]
    
    for i in range(1, len(triangle)):
        for j in range(1, i + 2):
            triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
    
    answer = max(triangle[-1])
    
    return answer

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

result = solution(triangle)