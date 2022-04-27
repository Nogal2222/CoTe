s = "-1 -1"

def solution(s):
    s_list = list(map(int, s.split()))
    
    answer = str(min(s_list)) + ' ' + str(max(s_list))
    
    return answer

result = solution(s)