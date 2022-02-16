# -*- coding: utf-8 -*-
import sys
from math import lcm
#input = sys.stdin.readline

n = int(input())
ring = list(map(int, input().split()))


for i in range(1, n):
    first = lcm(ring[0],ring[i]) // ring[i]
    last = lcm(ring[0],ring[i]) // ring[0]
    
    print(first, "/" , last, sep = '')