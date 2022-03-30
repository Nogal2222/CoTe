def solution(s):
    answer = int(s)
    return answer

s = '-1234'
result = solution(s)

'''알고리즘으로 하면
def strToInt(str):
    result = 0

    for idx, number in enumerate(str[::-1]):
        if number == '-':
            result *= -1
        else:
            result += int(number) * (10 ** idx)

    return result
'''