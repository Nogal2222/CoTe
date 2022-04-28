def solution(s):
    s2=s.split()
    print(s2)
    answer=""
    for i in range(len(s2)):
        if s2[i]:
            s2[i]=s2[i][0].upper()+s2[i][1:].lower()
        answer+= s2[i]+' '

    return answer[:-1]

s = " 3PeopLe 6unFollowed     Me"

result = solution(s)

'''테스트케이스 18번만 안됨
def solution(s):
    answer = ''
    
    for i in range(1, len(s)):
        if s[i-1].isalpha() and i - 1 == 0:
            answer += s[i-1].upper()
        
        elif (s[i-1].isnumeric() or s[i-1] == ' ') and i - 1 == 0:
            answer += s[i-1]
        
        if s[i-1] == ' ' and s[i].isalpha():
            answer += s[i].upper()
        
        else:
            answer += s[i].lower()
    
    return answer
'''