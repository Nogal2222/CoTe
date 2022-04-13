from collections import deque

def solution(priorities, location):
    cnt = 0
    dq = deque([(value, index) for index, value in enumerate(priorities)])
    
    while len(dq):
        printed = dq.popleft()
        
        if dq and max(dq)[0] > printed[0]:
            dq.append(printed)
        
        else:
            cnt += 1
            
            if printed[1] == location:
                break
    
    return cnt

priorities = [1, 1, 9, 1, 1, 1]
location = 0
result = solution(priorities, location)