def solution(s):
    new_s = sorted(s)
    new_s.sort(reverse = True)
    answer = ''.join(new_s)
    
    return answer

s = "Zbcdefg"
result = solution(s)

''' 간단하게
def solution(s):
    answer = ''.join(sorted(s, reverse=True))
    
    return answer
'''