T = int(input())
answers = [''] * T

for t in range(1, T+1):
    word = input()
    a = '..#.'
    b = '.#.#'
    ab_last = '.'
    c1 = '#.'
    c2 = '.'
    c_last = '#'
    
    N = len(word)
    
    answer = [''] * 5
    answer[0] += a*N + ab_last
    answer[1] += b*N + ab_last
    
    for w in word:
        answer[2] += c1 + w + c2
    answer[2] += c_last
    
    answer[3] += b*N + ab_last
    answer[4] += a*N + ab_last
    
    for i in answer:
        print(i)