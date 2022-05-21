def isPalindrome(x):
    if x==x[::-1]:
        return True
def solution(s):
    MAX=0
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            if isPalindrome(s[i:j]):
                if MAX<len(s[i:j]):
                    MAX=len(s[i:j])
    return MAX

s = 'abcdcba'
result = solution(s)

'''시간 초과
def solution(s):
    answer = 1
    
    for i in range(len(s)):
        for j in range(1, len(s) + 1):
            if s[i:j] == s[i:j][::-1]:
                answer = max(answer, len(s[i:j]))
    
    return answer
'''