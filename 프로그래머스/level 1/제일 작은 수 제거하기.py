def solution(arr):
    try:
        arr.pop(arr.index(min(arr)))
        
        if len(arr) == 0:
            return [-1]
        
        else:
            return arr
    
    except:
        return [-1]

arr = [10, 9, 9, 9]	
result = solution(arr)

''' 중복이 있을 경우 풀이
def rm_small(mylist):
    return [i for i in mylist if i > min(mylist)]
'''