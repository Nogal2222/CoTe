from collections import Counter

def solution(a):
    answer = -1
    
    if len(a) == 1:
        return 0
    
    cnt = Counter(a)
    
    for key, value in cnt.items():
        if cnt[key] * 2 < answer:
            continue
        
        idx = 0
        max_value = key
        length = 0
        
        while idx < len(a) - 1:
            if (a[idx] != max_value and a[idx+1] != max_value) or a[idx] == a[idx+1]:
                idx += 1
                continue
            
            length += 2
            idx += 2
        
        answer = max(answer, length)
    
    return answer

a = [5, 2, 3, 3, 5, 3]
result = solution(a)