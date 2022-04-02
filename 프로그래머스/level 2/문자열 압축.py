def solution(s):
    if len(s) <= 1:
        return len(s)
    
    new_s_len_list = []
    
    for cut in range(1, len(s)//2 + 1):
        target = s[:cut]
        count = 1
        new_s = ''
        
        for i in range(cut, len(s)+1, cut):
            next_target = s[i : cut + i]
            
            if target == next_target:
                count += 1
            
            else:
                if count == 1:
                    count = ''
                
                new_s += str(count) + target
                count = 1
                target = next_target
        
        if count == 1:
            count = ''
        
        new_s += str(count) + target
        new_s_len_list.append(len(new_s))

    answer = min(new_s_len_list)
    
    return answer

s = ''
rslt = solution(s)