def solution(citations):
    citations = sorted(citations)
    n = len(citations)
    
    for i in range(n):
        if citations[i] >= n - i:
            return n - i
    
    return 0

citations = [5, 3, 0, 6, 1]

result = solution(citations)

''' 내가 짠 코드 왜 안되는거지?
def solution(citations):
    n = len(citations)
    h = 0

    for i in range(n):
        cnt = 0
        
        if citations[i] > n:
            continue
        
        elif citations[i] == n:
            for j in range(n):
                if citations[j] < n:
                    break
                
                else:
                    cnt += 1
            
            if cnt >= citations[i]:
                h = max(h, citations[i])
        
        else:
            for j in range(n):
                if citations[j] >= citations[i]:
                    cnt += 1
            
            if cnt >= citations[i]:
                h = max(h, citations[i])
    
    return h
'''