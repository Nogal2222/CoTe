def solution(arr):
    answer = [arr[0]]
    len_arr = len(arr)
    
    for i in range(1, len_arr):
        if arr[i] != arr[i-1]:
            answer.append(arr[i])
        
    return answer

arr = [1,1,3,3,0,1,1]
print(solution(arr))