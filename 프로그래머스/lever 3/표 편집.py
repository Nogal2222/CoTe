n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]

def solution(n, k, cmd):
    cur = k
    table = {i:[i-1, i+1] for i in range(n)}
    answer = ['O'] * n
    table[0] = [None, 1]
    table[n-1] = [n-2, None]
    stack = []
    
    for c in cmd:
        # 삭제
        if c == 'C':
            answer[cur] = 'X'
            Prev, Next = table[cur]
            stack.append([Prev, cur, Next])
            
            # 끝행일때
            if Next == None:
                cur = table[cur][0]
            
            else:
                cur = table[cur][1]
            
            # 첫행일때
            if Prev == None:
                table[Next][0] = None
            
            elif Next == None:
                table[Prev][1] = None
            
            else:
                table[Prev][1] = Next
                table[Next][0] = Prev
        
        # 복구
        elif c == 'Z':
            Prev, now, Next = stack.pop()
            answer[now] = 'O'
            
            if Prev == None:
                table[Next][0] = now
            
            elif Next == None:
                table[Prev][1] = now
            
            else:
                table[Next][0] = now
                table[Prev][1] = now
        
        # 커서 이동
        else:
            c1, c2 = c.split()
            c2 = int(c2)
            
            if c1 == 'D':
                for _ in range(c2):
                    cur = table[cur][1]
            
            else:
                for _ in range(c2):
                    cur = table[cur][0]
        
    return ''.join(answer)

result = solution(n, k, cmd)