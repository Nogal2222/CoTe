def solution(stones, k):
    left = 1
    right = 200000000
    
    while left <= right:
        temps = stones.copy()
        mid = (left + right) // 2
        cnt = 0
        
        for temp in temps:
            if temp - mid <= 0:
                cnt += 1
            
            else:
                cnt = 0
            
            if cnt >= k:
                break
        
        if cnt >= k:
            right = mid - 1
        
        else:
            left = mid + 1
    
    return left

stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3

result = solution(stones, k)