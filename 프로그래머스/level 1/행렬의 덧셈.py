def solution(arr1, arr2):
    outside_len = len(arr1)
    inside_len = len(arr1[0])
    answer = [[0 for i in range(inside_len)] for i in range(outside_len)]
    
    for i in range(outside_len):
        for j in range(inside_len):
            answer[i][j] = arr1[i][j] + arr2[i][j]
    
    return answer

arr1 = [[1, 2], [2, 3]]
arr2 = [[3, 4], [5, 6]]

rslt = solution(arr1, arr2)

''' zip을 이용한 풀이
def sumMatrix(A,B):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]
    return answer
'''