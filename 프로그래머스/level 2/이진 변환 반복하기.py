def solution(x):
    cnt_zero = 0
    cnt_round = 0

    while x != '1':
        cnt_round += 1
        cnt_zero += x.count('0')
        x = x.replace('0', '')
        c = len(x)
        x = format(c, 'b')

    answer = [cnt_round, cnt_zero]
    
    return answer

x = "110010101001"

result = solution(x)