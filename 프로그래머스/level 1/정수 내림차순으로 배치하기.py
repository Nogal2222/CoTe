def solution(n):
    answer = 0
    n_list = list(str(int(n)))
    n_list.sort(reverse = True)
    answer = ''.join(n_list)
    answer = int(answer)

    return answer

n = 100

result = solution(n)