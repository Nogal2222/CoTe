import heapq

def solution(operations):
    heap = []
    
    for i in operations:
        if i[0] == 'I':
            heapq.heappush(heap, int(i[2:]))
        
        elif i[0] == 'D':
            if len(heap) == 0:
                continue
            
            elif i[2:] == '-1':
                heapq.heappop(heap)
            
            elif i[2:] == '1':
                heap = heapq.nlargest(len(heap), heap)[1:]
                heapq.heapify(heap)
        
    if len(heap) == 0:
        return [0, 0]
    
    else:
        return [max(heap), min(heap)]

operations = 	["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
result = solution(operations)

''' heap 없이 만든 코드
def solution(operations):
    stack = []
    
    for i in operations:
        if i[0] == 'I':
            stack.append(int(i[2:]))
        
        elif i[0] == 'D':
            if len(stack) == 0:
                continue
            
            if i[2:] == '1':
                stack.pop(stack.index(max(stack)))
            
            elif i[2:] == '-1':
                stack.pop(stack.index(min(stack)))
    
    if len(stack) == 0:
        return [0, 0]
    
    else:
        return [max(stack), min(stack)]
'''