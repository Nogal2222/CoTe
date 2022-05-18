def solution(a):
    result = [False for _ in range(len(a))]
    min_front, min_rear = float('inf'), float('inf')
    
    for i in range(len(a)):
        if a[i] < min_front:
            min_front = a[i]
            result[i] = True
        
        if a[-1-i] < min_rear:
            min_rear = a[-1-i]
            result[-1-i] = True
    
    answer = sum(result)
    
    return answer

a = [-16,27,65,-2,58,-92,-71,-68,-61,-33]

result = solution(a)