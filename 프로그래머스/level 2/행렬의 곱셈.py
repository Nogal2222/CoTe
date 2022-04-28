def solution(arr1, arr2):
    m, n, p = len(arr1), len(arr1[0]), len(arr2[0])
    answer = [[0 for _ in range(p)] for _ in range(m)]

    for i in range(m):
        for j in range(p):
            for k in range(n):
                answer[i][j] += (arr1[i][k] * arr2[k][j])
    
    return answer

arr1 = [[1, 4], [3, 2], [4, 1]]
arr2 = [[3, 3], [3, 3]]

result = solution(arr1, arr2)