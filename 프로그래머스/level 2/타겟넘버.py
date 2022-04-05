def solution(numbers, target):
    answer = 0
    q = [[numbers[0], 0], [-1 * numbers[0], 0]]
    len_numbers = len(numbers)
    
    while q:
        temp, idx = q.pop()
        idx += 1
        
        if idx < len_numbers:
            q.append([temp + numbers[idx], idx])
            q.append([temp - numbers[idx], idx])
            
        else:
            if temp == target:
                answer += 1
        
    return answer

numbers = [1, 1, 1, 1, 1]
target = 3
result = solution(numbers, target)