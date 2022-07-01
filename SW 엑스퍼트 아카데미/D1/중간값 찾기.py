N = int(input())
scores = sorted(list(map(int, input().split())))

answer = scores[N//2]
print(answer)