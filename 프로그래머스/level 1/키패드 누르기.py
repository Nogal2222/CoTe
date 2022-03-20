# -*- coding: utf-8 -*-
def findDistance(currentKey, nextKey):
    keypad = {1: [0, 0], 2: [1, 0], 3: [2, 0],
              4: [0, 1], 5: [1, 1], 6: [2, 1],
              7: [0, 2], 8: [1, 2], 9: [2, 2],
              '*': [0, 3], 0: [1, 3], '#': [2, 3]}
    x1, y1 = keypad[currentKey]
    x2, y2 = keypad[nextKey]
    
    return abs(x1 - x2) + abs(y1 - y2)


def solution(numbers, hand):
    answer = ''
    current_left = '*'
    current_right = '#'
    
    for i in numbers:
        if i in [1, 4, 7]:
            answer += 'L'
            current_left = i
        
        elif i in [3, 6, 9]:
            answer += 'R'
            current_right = i
        
        elif i in [2, 5, 8, 0]:
            if findDistance(current_left, i) > findDistance(current_right, i):
                answer += 'R'
                current_right = i
            
            elif findDistance(current_left, i) < findDistance(current_right, i):
                answer += 'L'
                current_left = i
            
            else:
                if hand == 'left':
                    answer += 'L'
                    current_left = i
                
                else:
                    answer += 'R'
                    current_right = i
    
    return answer

numbers = list(map(int, input().split()))
hand = input()

print(solution(numbers, hand))