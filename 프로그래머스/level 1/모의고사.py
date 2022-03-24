# -*- coding: utf-8 -*-
answers = [1,3,2,4,2] 

def solution(answers):
    student1 = [1, 2, 3, 4, 5]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    cnt_answer = [0, 0, 0]
    result = []
    
    for i, answer in enumerate(answers):
        if answer == student1[i % len(student1)]:
            cnt_answer[0] += 1
        
        if answer == student2[i % len(student2)]:
            cnt_answer[1] += 1
        
        if answer == student3[i % len(student3)]:
            cnt_answer[2] += 1
    
    for index, factor in enumerate(cnt_answer):
        if factor == max(cnt_answer):
            result.append(index + 1)
    
    return result