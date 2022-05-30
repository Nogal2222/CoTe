def solution(A, B):
    answer = 0
    
    A.sort()
    B.sort()
    
    ai, bi = 0, 0
    
    while ai != len(A) and bi != len(B):
        if B[bi] > A[ai]:
            answer += 1
            ai += 1
            bi += 1
        
        else:
            bi += 1
    
    return answer

A = [5, 1, 3, 7]
B = [2, 2, 6, 8]

result = solution(A, B)