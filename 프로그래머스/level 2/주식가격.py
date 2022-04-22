from collections import deque

def solution(prices):
    q = deque(prices)
    answer = []
    
    while q:
        price = q.popleft()
        sec = 0
        
        for part in q:
            sec += 1
            
            if price > part:
                break
        
        answer.append(sec)
    
    return answer

prices = [1, 2, 3, 2, 3]

result = solution(prices)