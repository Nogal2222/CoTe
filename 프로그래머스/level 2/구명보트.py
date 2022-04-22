from collections import deque

def solution(people, limit):
    q = deque(sorted(people))
    boat = 0
    
    while q:
        if len(q) >= 2:
            if q[0] + q[-1] <= limit:
                q.pop()
                q.popleft()
                boat += 1
            
            elif q[0] + q[-1] > limit:
                q.pop()
                boat += 1
        
        else:
            if q[0] <= limit:
                q.pop()
                boat += 1
    
    return boat

people = [70, 80, 50]
limit = 100

result =solution(people, limit)