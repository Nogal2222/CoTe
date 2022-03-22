# -*- coding: utf-8 -*-
def solution(s):
    answer = ''
    len_s = len(s)
    cursor = 0

    while cursor < len_s: 
        if s[cursor].isdigit():
            answer += s[cursor]
            cursor += 1

        else:
            if s[cursor] == 'o':
                answer += '1'
                cursor += 3

            elif s[cursor] == 't':
                if s[cursor+1] == 'w':
                    answer += '2'
                    cursor += 3
                elif s[cursor+1] == 'h':
                    answer += '3'
                    cursor += 5

            elif s[cursor] == 'f':
                if s[cursor+1] == 'o':
                    answer += '4'
                    cursor += 4
                elif s[cursor+1] == 'i':
                    answer += '5'
                    cursor += 4

            elif s[cursor] == 's':
                if s[cursor+1] == 'i':
                    answer += '6'
                    cursor += 3
                elif s[cursor+1] == 'e':
                    answer += '7'
                    cursor += 5

            elif s[cursor] == 'e':
                answer += '8'
                cursor += 5

            elif s[cursor] == 'n':
                answer += '9'
                cursor += 4

            else:
                answer += '0'
                cursor += 4

    answer = int(answer)
    return answer

'''딕셔너리 사용
num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)
'''
'''replace 사용
def solution(s):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i in range(len(words)):
        s = s.replace(words[i], str(i))

    return int(s)
'''