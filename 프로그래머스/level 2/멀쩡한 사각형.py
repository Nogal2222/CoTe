from math import gcd 

def solution(w,h):
    g = gcd(w, h)
    answer = (w * h) - (g * (w//g + h//g -1))
    return answer

w = 3
h = 5
result = solution(w, h)
