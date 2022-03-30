strings = ["abce", "abcd", "cdx"]
n = 2


def solution(strings, n):
    answer = sorted(strings)
    answer.sort(key = lambda x: x[n])
    
    return answer

result = solution(strings, n)