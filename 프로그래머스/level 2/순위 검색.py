from itertools import combinations
from collections import defaultdict
# bisect_left = lower bound
# 원하는 값 이상이 처음 나오는 위치를 찾는 과정
from bisect import bisect_left

def solution(information, queries):
    answer = []
    dic = defaultdict(list)
    
    for info in information:
        info = info.split()
        condition = info[:-1]  
        score = int(info[-1])
        
        for i in range(5):
            case = list(combinations([0,1,2,3], i))
            
            for c in case:
                tmp = condition.copy()
                
                for idx in c:
                    tmp[idx] = "-"
                    
                key = ''.join(tmp)
                dic[key].append(score) 

    for value in dic.values():
        value.sort()   

    for query in queries:
        query = query.replace("and ", "")
        query = query.split()
        target_key = ''.join(query[:-1])
        target_score = int(query[-1])
        count = 0
        
        if target_key in dic:
            target_list = dic[target_key]
            idx = bisect_left(target_list, target_score)
            count = len(target_list) - idx
            
        answer.append(count)
        
    return answer

info = ["java backend junior pizza 150",
        "python frontend senior chicken 210",
        "python frontend senior chicken 150",
        "cpp backend senior pizza 260",
        "java backend junior chicken 80",
        "python backend senior chicken 50"]

query = ["java and backend and junior and pizza 100",
         "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250",
         "- and backend and senior and - 150",
         "- and - and - and chicken 100",
         "- and - and - and - 150"]

result = solution(info, query)

''' 효율성 실패
def solution(info, query):
    #info 분류
    new_info = []

    for i in info:
        temp = list(i.split(' '))
        temp[4] = int(temp[4])
        new_info.append(temp)

    #query 분류
    new_query = []

    for i in query:
        i = i.replace(' and', '')
        temp = list(i.split(' '))
        temp[4] = int(temp[4])
        new_query.append(temp)
    
    #조건 탐색
    answer = []

    for n_q in range(len(new_query)):
        cnt = 0
        flag = True
        
        for n_i in range(len(new_info)):
            for i in range(4):
                if (new_info[n_i][i] == new_query[n_q][i] or new_query[n_q][i] == '-') and new_info[n_i][4] >= new_query[n_q][4]:
                    continue
                
                else:
                    flag = False
                    break
            
            if flag:
                cnt += 1
            
            flag = True
        
        answer.append(cnt)
    return answer
'''