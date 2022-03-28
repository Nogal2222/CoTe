def solution(s):
    mid_len = len(s)//2
    if len(s) % 2 != 0:
        answer = s[mid_len]
    else:
        answer = s[mid_len-1:mid_len+1]
    return answer