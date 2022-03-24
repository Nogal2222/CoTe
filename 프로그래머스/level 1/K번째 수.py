# -*- coding: utf-8 -*-
def solution(array, commands):
    len_commands = len(commands)
    answer = [0] * len_commands

    for order in range(len_commands):
        i = commands[order][0] - 1
        j = commands[order][1]
        k = commands[order][2] - 1
        array_cut = array[i:j]
        array_cut.sort()

        answer[order] = array_cut[k]
    return answer
    
''' 커맨드 한번에 받기
def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command
        answer.append(list(sorted(array[i-1:j]))[k-1])
    return answer
'''