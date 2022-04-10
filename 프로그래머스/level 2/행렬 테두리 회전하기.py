def solution(rows, columns, queries):
    answer = []
    
    # (rows + 1) * (column + 1) 행렬 생성
    matrix = [[0 for i in range(columns+1)] for j in range(rows+1)]
    num = 1 # 1 ~ rows * column 까지
    
    for row in range(1, rows + 1):
        for column in range(1, columns + 1):
            matrix[row][column] = num
            num += 1
    
    # 한칸씩 이동
    for x1, y1, x2, y2 in queries:
        temp = matrix[x1][y1] # 옮기기 전에 하나 저장
        put_answer = temp # answer에 넣을 가장 작은 값
        
        # 좌열 상이동
        for k in range(x1, x2):
            move_part = matrix[k+1][y1]
            matrix[k][y1] = move_part # 값 이동
            put_answer = min(put_answer, move_part)
        
        # 하행 좌이동
        for k in range(y1, y2):
            move_part = matrix[x2][k+1]
            matrix[x2][k] = move_part
            put_answer = min(put_answer, move_part)
        
        # 우열 하이동
        for k in range(x2, x1, -1):
            move_part = matrix[k-1][y2]
            matrix[k][y2] = move_part
            put_answer = min(put_answer, move_part)
        
        # 상열 우이동
        for k in range(y2, y1, -1):
            move_part = matrix[x1][k-1]
            matrix[x1][k] = move_part
            put_answer = min(put_answer, move_part)
        
        matrix[x1][y1+1] = temp # 저장한 것 끼워넣기
        answer.append(put_answer) # 가장 작은 값 answer에 넣기
    
    return answer

rows = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]

test = solution(rows, columns, queries)