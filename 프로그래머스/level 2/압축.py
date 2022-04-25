def solution(msg):
    answer = []
    words = []
    idx = 0
    
    while idx < len(msg):
        if msg[idx:idx+2] in words:
            for i in range(idx+2, len(msg)):
                if msg[idx:i+1] not in words:
                    words.append(msg[idx:i + 1])
                    answer.append(words.index(msg[idx:i]) + 27)
                    idx += (i-idx)
                    break
            
            else:
                answer.append(words.index(msg[idx:len(msg)]) + 27)
                break
        
        else:
            answer.append(ord(msg[idx]) - 64)
            words.append(msg[idx:idx+2])
            idx += 1
    
    return answer

msg = 'TOBEORNOTTOBEORTOBEORNOT'

result = solution(msg)

''' 알파벳을 더 쉽게 구현한 코드
def solution(msg):
    answer = []
    tmp = {chr(e + 64): e for e in range(1, 27)}
    num = 27
    while msg:
        tt = 1
        while msg[:tt] in tmp.keys() and tt <= msg.__len__():
            tt += 1
        tt -= 1
        if msg[:tt] in tmp.keys():
            answer.append(tmp[msg[:tt]])
            tmp[msg[:tt + 1]] = num
            num += 1
        msg = msg[tt:]
    return answer
'''