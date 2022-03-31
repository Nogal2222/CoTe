def solution(s):
    answer = ''
    s_list = s.split(' ')
    len_list = len(s_list)
    
    for i in range(len_list):
        for j in range(len(s_list[i])):
            if j % 2 == 0:
                answer += s_list[i][j].upper()
            else:
                answer += s_list[i][j].lower()
        
        if i == len_list - 1:
            continue
        
        answer += ' '
    
    return answer

s = 'world'
result = solution(s)

'''