def solution(genres, plays):
    answer = []
    temp = sorted([[genres[i], plays[i], i] for i in range(len(genres))], key = lambda x: (x[0], -x[1], x[2]))
    total_genre = {}
    
    for g in temp:
        if g[0] not in total_genre:
            total_genre[g[0]] = g[1]
        else:
            total_genre[g[0]] += g[1]
    
    total_genre = sorted(total_genre.items(), key = lambda x: -x[1])
    
    for i in total_genre:
        cnt = 0
        
        for j in temp:
            if i[0] == j[0]:
                cnt += 1
                
                if cnt > 2:
                    break
                
                else:
                    answer.append(j[2])
    
    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

result = solution(genres, plays)