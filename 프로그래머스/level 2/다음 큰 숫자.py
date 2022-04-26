n = 15

def solution(n):
    bi_n = bin(n)[2:]
    #가장 오른편의 마지막 0을 1로 바꿔줌

    if bi_n[-1] == '1':
        bin_number = list('0' + bi_n)
        idx = ''.join(bin_number).rfind('0')
        bin_number[idx] = '1'
        bin_number[idx+1] = '0'
        answer = int(''.join(bin_number), 2)

    else:#이부분만 있어도 됨
        if len(set(bi_n)) == 1:
            answer = int('10' + bi_n[1:], 2)
        
        cnt_one = bi_n.count('1')
        
        while True:
            n += 1
            
            if bin(n)[2:].count('1') == cnt_one:
                answer = n
                break
    
    return answer

result = solution(n)