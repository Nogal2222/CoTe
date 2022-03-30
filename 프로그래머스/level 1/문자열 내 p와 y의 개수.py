def solution(s):
    cnt_p = s.count('p') + s.count('P')
    cnt_y = s.count('y') + s.count('Y')
    
    if cnt_p == cnt_y:
        answer = True
    
    else:
        answer = False
    
    return answer

s = "Pyy"
result = solution(s)

'''lower과 결과가 bools임을 이용한 풀이
def numPY(s):
    
    return s.lower().count('p') == s.lower().count('y')
'''