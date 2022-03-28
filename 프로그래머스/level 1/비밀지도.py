# -*- coding: utf-8 -*-
def solution(n, arr1, arr2):
    answer = [""] * n
    
    map1 = []
    map2 = []
    
    for i in arr1:
        binary = list(format(i, 'b').zfill(n))
        map1.append(binary)

    for i in arr2:
        binary = list(format(i, 'b').zfill(n))
        map2.append(binary)
    
    for i in range(n):
        map_string = ''
        
        for j in range(n):
            if map1[i][j] == '1' or map2[i][j] == '1':
                map_string += "#"
            
            else:
                map_string += " "
        
        answer[i] = map_string
        
    return answer
n = 5 # 한 변의 길이
arr1 = 	[9, 20, 28, 18, 11] #비밀지도 1
arr2 = [30, 1, 21, 17, 28] #비밀지도 2

print(solution(n, arr1, arr2))

''' 다른 사람 풀이

def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2): #zip함수로 묶음
        a12 = str(bin(i|j)[2:]) #|(비트연산자 or)
        a12=a12.rjust(n,'0') #rjust = zfill
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer
'''
