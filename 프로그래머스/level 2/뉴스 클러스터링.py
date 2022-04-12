from collections import Counter

def solution(str1, str2):
    new_str1 = str1.lower()
    new_str2 = str2.lower()

    str1_list = []
    str2_list = []

    for i in range(len(new_str1) - 1):
        if new_str1[i].isalpha() and new_str1[i+1].isalpha():
            str1_list.append(new_str1[i] + new_str1[i+1])

    for i in range(len(new_str2) - 1):
        if new_str2[i].isalpha() and new_str2[i+1].isalpha():
            str2_list.append(new_str2[i] + new_str2[i+1])

    cnt1 = Counter(str1_list)
    cnt2 = Counter(str2_list)

    inter = list((cnt1 & cnt2).elements()) # 교집합
    union = list((cnt1 | cnt2).elements()) # 합집합

    if len(union) == 0 and len(inter) == 0:
        answer = 65536

    else:
        answer = int(len(inter) / len(union) * 65536)
    
    return answer

str1 = 'handshake'
str2 = 'shake hands'
result = solution(str1, str2)

