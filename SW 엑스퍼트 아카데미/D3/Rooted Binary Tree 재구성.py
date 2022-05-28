def solve(tree, k):
    n = len(tree)
    if n == 1:
        answer[k].append(tree[0])
        return

    solve(tree[0 : n//2], k+1)
    answer[k].append(tree[n//2])
    solve(tree[n//2 + 1 : ], k+1)

for tc in range(1, int(input()) + 1):
    k = int(input())
    tree = list(map(int, input().split()))
    answer = [[] for _ in range(k)]
    
    solve(tree, 0)

    for i in range(k):
        if i == 0:
            print(f'#{tc}', end=' ')
            print(*answer[i])
        
        else:
            print(*answer[i])