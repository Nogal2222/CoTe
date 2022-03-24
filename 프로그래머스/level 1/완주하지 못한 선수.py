# -*- coding: utf-8 -*-
def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for p,c in zip(participant, completion):
        if p != c:
            return p
    
    return participant.pop()

participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]

print(solution(participant, completion))

''' 콜렉션 카운터 이용
import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
'''