# 문제당 점수
def s_p_p(N, T, results):
    scores = []
    
    for i in range(T):
        score = 0
        
        for j in range(N):
            score += results[j][i]
        
        scores.append(N-score)
    
    return scores

# 참가자별 총점
def t_s(N, T, results, scores):
    total_scores = []
    
    for i in range(N):
        total_score = 0
        
        for j in range(T):
            total_score += (results[i][j] * scores[j])
            
        total_scores.append(total_score)
    
    return total_scores
 
# P의 등수
def P_rank(N, P, results, total_scores):
    cnt = 0
    me = P-1
    
    for i in range(N):
        if i == me:
            continue
        
        if total_scores[i] > total_scores[me]:
            cnt += 1
            continue
        
        elif total_scores[i] == total_scores[me]:
            if results[i].count(1) > results[me].count(1):
                cnt += 1
                continue
            
            elif results[i].count(1) == results[me].count(1):
                if i < me:
                    cnt += 1
                    continue
        
    answer = 1 + cnt
    
    return answer

T = int(input())
answers = [''] * T

for t in range(1, T+1):
    N, T, P = map(int, input().split())
    
    # 참가자별 성적표
    results = []

    for i in range(N):
        results.append(list(map(int, input().split())))
    
    # 각 문제의 점수
    scores = s_p_p(N, T, results)
    
    # 참가자별 총점, 
    total_scores = t_s(N, T, results, scores)
    
    answer = P_rank(N, P, results, total_scores)
    
    answers[t-1] = f'#{t} {answer}'

for i in answers:
    print(i)