def solution(word):
    dict_word = {'A' : 0, 'E' : 1, 'I' : 2, 'O' : 3, 'U' : 4}
    weight = 781 #(((5 + 1) * 5 + 1) * 5 + 1) * 5 + 1
    answer = len(word)
    
    for i in word:
        answer += weight * dict_word[i]
        weight = (weight - 1) // 5 # 자리 넘어갈 때마다 가중치를 낮춰줌
    
    return answer

word = "I"

result = solution(word)