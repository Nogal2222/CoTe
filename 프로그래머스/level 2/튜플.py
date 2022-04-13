def solution(s):
    answer = []
    s = s.strip('{}')
    s = s.split('},{')
    s.sort(key = lambda x: len(x))
    
    for part in s:
        new_parts = part.split(',')
        
        for new_part in new_parts:
            if int(new_part) not in answer:
                answer.append(int(new_part))
    
    return answer

s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
result = solution(s)