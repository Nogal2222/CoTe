A = [1, 2]
B = [3, 4]

def solution(A, B):
    A.sort()
    B.sort(reverse = True)
    answer = 0
    
    for i in range(len(A)):
        answer += (A[i] * B[i])
    
    return answer

result = solution(A, B)