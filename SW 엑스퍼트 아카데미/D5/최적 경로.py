'''
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
'''
from itertools import permutations

T = int(input())
answers = [''] * T

for t in range(1, T+1):
    n = int(input())
    points = list(map(int, input().split()))
    
    company = (points[0], points[1])
    home = (points[2], points[3])
    points = points[4:]
    guests = list((points[i], points[i+1]) for i in range(0, len(points), 2))
    min_dist = float(9999999)
    
    for i in permutations(guests):
        path = [company, *list(i), home]
        dist = 0
        
        for j in range(len(path)-1):
            dist += abs(path[j][0] - path[j+1][0]) + abs(path[j][1] - path[j+1][1])
        
        min_dist = min(min_dist, dist)
    
    answers[t-1] = f'#{t} {min_dist}'
 
for i in answers:
    print(i)