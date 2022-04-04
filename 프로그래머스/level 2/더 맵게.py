import heapq #파이썬 내장함수 heapq는 최소힙

def solution(scoville, k):
    answer = 0
    scoville.sort() #heapify와 같음
    
    while scoville[0] < k:
        if len(scoville) <= 1:
            return -1
        
        else:
            first = heapq.heappop(scoville)
            second = heapq.heappop(scoville)
            blended = first + (second * 2)
            #heappush는 최솟값을 배열 제일 앞으로 해줌
            heapq.heappush(scoville, blended)
            answer += 1
        
    return answer

scoville = [1, 2, 3, 9, 10, 12]
k = 7
result = solution(scoville, k)

''' 시간초과 (min함수가 시간을 오래 씀)
def solution(scoville, k):
    cnt = 0
    scoville = list(i for i in scoville if i < k)

    while len(scoville) > 1:
        if min(scoville) >= k:
            break
        
        first = scoville.pop(scoville.index(min(scoville)))
        second = scoville.pop(scoville.index(min(scoville)))
        blended = first + (second * 2)
        scoville.append(blended)
        cnt += 1

    if max(scoville) < k:
        answer = -1
    else:
        answer = cnt
        
    return answer
'''