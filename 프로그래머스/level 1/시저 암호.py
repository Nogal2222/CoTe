def solution(s, n):
    answer = ''
    upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 
             'H', 'I', 'J', 'K', 'L', 'M', 'N', 
             'O', 'P', 'Q', 'R', 'S', 'T', 'U', 
             'V', 'W', 'X', 'Y', 'Z']
    lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 
             'h', 'i', 'j', 'k', 'l', 'm', 'n', 
             'o', 'p', 'q', 'r', 's', 't', 'u', 
             'v', 'w', 'x', 'y', 'z']
    
    for i in range(len(s)):
        if s[i].isalpha() == False:
            answer += s[i]
            continue
        
        if s[i] in upper:
            temp = (upper.index(s[i]) + n) -26
            answer += upper[temp]
        
        if s[i] in lower:
            temp = (lower.index(s[i]) + n) -26
            answer += lower[temp]
    
    return answer

s = "a B z"
n = 4
result = solution(s, n)

'''isupper(), islower()
def caesar(s, n):
    s = list(s)
    
    for i in range(len(s)):
        ascii_num = ord(s[i])
        
        if s[i].isalpha() == False:
            continue
        
        if s[i].isupper():
            ascii_aA= ord('A')
            
        elif s[i].islower():
            ascii_aA = ord('a')
        
        password = (ascii_num - ascii_aA + n) % 26 + ascii_aA
        s[i]=chr(password)

    return "".join(s)
'''