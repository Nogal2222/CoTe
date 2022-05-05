def dictAdd(dict, value):
    if value in dict:
        dict[value] += 1
    else:
        dict[value] = 1

def setStartPointer(start, dict, gems):
    while True:
        if dict[gems[start]] > 1:
            dict[gems[start]] -= 1
            start += 1
        
        else:
            return start

def solution(gems):
    kinds = len(set(gems))
    length = len(gems)
    answer = [0, 1000002]
    dic = dict()
    start, end = 0, 0
    dictAdd(dic, gems[0])
    
    while True:
        start = setStartPointer(start, dic, gems)
        
        if len(dic) == kinds and (end - start) < (answer[1] - answer[0]):
            answer = [start + 1, end + 1]
        
        end += 1
        
        if end == length:
            return answer
        
        dictAdd(dic, gems[end])
    
    return [start + 1, end + 1]

gems =[["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"],
       ["AA", "AB", "AC", "AA", "AC"],
       ["XYZ", "XYZ", "XYZ"],
       ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]]

result = [solution(i) for i in gems]