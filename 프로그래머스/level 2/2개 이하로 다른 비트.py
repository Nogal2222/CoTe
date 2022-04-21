def solution(numbers):
    answer = []

    for number in numbers:
        bin_number = list('0' + bin(number)[2:])
        #가장 오른편의 마지막 0을 1로 바꿔줌
        idx = ''.join(bin_number).rfind('0')
        bin_number[idx] = '1'
        
        if number % 2 == 1:
            bin_number[idx+1] = '0'
        
        answer.append(int(''.join(bin_number), 2))

    return answer

numbers = [2, 7]

result = solution(numbers)

'''시간 초과
def solution(numbers):
    answer = [0 for i in range(len(numbers))]

    for i in range(len(numbers)):
        diff = 0
        next_num = numbers[i]
        
        while True:
            next_num += 1
            xor = format(numbers[i] ^ next_num, 'b')
            diff = xor.count('1')
            
            if diff == 1 or diff == 2:
                answer[i] = next_num
                break
    
    return answer
'''