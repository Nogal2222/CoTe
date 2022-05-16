from itertools import permutations

def solution(n, weak, dist):
    len_weak = len(weak)
    answer = []
    weak_point = weak + [w + n for w in weak]
    
    for idx, start in enumerate(weak):
        for friends in permutations(dist):
            cnt = 1
            position = start
            
            for friend in friends:
                position += friend
                
                if position < weak_point[idx + len_weak - 1]:
                    cnt += 1
                    
                    position = [w for w in weak_point[idx + 1 : idx + len_weak] if w > position][0]
                
                else:
                    answer.append(cnt)
                    break
    
    return min(answer) if answer else -1

n = 12
weak = [1, 5, 6, 10]
dist = [1, 2, 3, 4]

result = solution( n, weak, dist)