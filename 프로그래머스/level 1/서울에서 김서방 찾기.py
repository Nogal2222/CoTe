def solution(seoul):
    answer = ''
    for i in range(len(seoul)):
        if seoul[i] == 'Kim':
            answer = '김서방은 %d에 있다' %i
            break
    return answer

seoul = ["Jane", "Kim"]
result = solution(seoul)

'''
def findKim(seoul):
    answer = "김서방은 {}에 있다".format(seoul.index('Kim'))
    
    return answer
'''