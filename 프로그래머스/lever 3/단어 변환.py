#BFS
from collections import deque

def solution(begin, target, words):
    answer = 0
    q = deque()
    q.append([begin, 0])
    v = [0 for _ in range(len(words))]
    
    while q:
        word, cnt = q.popleft()
        
        if word == target:
            answer = cnt
            break
        
        for i in range(len(words)):
            temp_cnt = 0
            
            if not v[i]:
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        temp_cnt += 1
                
                if temp_cnt == 1:
                    q.append([words[i], cnt+1])
                    v[i] = 1
    
    return answer

begin = 'hit'
target = 'cog'
words = ["hot", "dot", "dog", "lot", "log", "cog"]

result = solution(begin, target, words)