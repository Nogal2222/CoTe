# -*- coding: utf-8 -*-

N = int(input())
group_word = 0

for i in range(N):
    word = input()
    error = 0
    test_circle = len(word) - 1
    
    for j in range(test_circle):
        if word[j] != word[j+1]: #연속된 글자가 다를 때
            new_word = word[j+1:]
            
            if new_word.count(word[j]) > 0:
                error += 1
            
    if error == 0:
        group_word += 1

print(group_word)