from itertools import combinations

def solution(relation):
    rows = len(relation)
    columns = len(relation[0])
    
    combination = []
    
    for i in range(1, columns + 1):
        combination.extend(combinations(range(columns), i))
    
    uniqueness = []
    
    for i in combination:
        temp = [tuple([item[key] for key in i]) for item in relation]
        
        if len(set(temp)) == rows:
            put = True
            
            for j in uniqueness:    # 유일성
                if set(j).issubset(set(i)):     #최소성
                    put = False
                    break
            
            if put:
                uniqueness.append(i)
    
    return len(uniqueness)

relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
result = solution(relation)