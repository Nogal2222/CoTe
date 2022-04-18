clothes = [["yellowhat", "headgear"],
           ["bluesunglasses", "eyewear"],
           ["green_turban", "headgear"]]

def solution(clothes):
    dict_clothes = {}
    
    for value, key in clothes:
        dict_clothes[key] = dict_clothes.get(key, 0) + 1
    
    answer = 1
    
    for key in dict_clothes:
        answer *= (dict_clothes[key] + 1)
    
    answer -= 1
    
    return answer