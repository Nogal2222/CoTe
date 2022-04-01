def solution(phone_number):
    num_len = len(phone_number)
    answer = phone_number.replace(phone_number[0:num_len - 4], '*' * (num_len- 4))
    
    return answer

phone_number = "027778888"
result = solution(phone_number)