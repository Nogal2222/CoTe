def solution(arr, divisor):
    answer = []
    for i in range(len(arr)):
        if arr[i] % divisor == 0:
            answer.append(arr[i])
    answer = sorted(answer)
    
    if len(answer) == 0:
        answer = [-1]
    
    return answer

arr = [5, 9, 7, 10]
divisor = 5

result = solution(arr, divisor)