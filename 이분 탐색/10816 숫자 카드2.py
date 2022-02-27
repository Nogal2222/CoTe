# -*- coding: utf-8 -*-
import sys
#input = sys.stdin.readline

def binary(N_factor, N_list, start, end):
    if start > end:
        return 0
    
    mid = (start + end) // 2
    
    if N_factor == N_list[mid]:
        return N_list[start:end + 1].count(N_factor)
    elif N_factor < N_list[mid]:
        return binary(N_factor, N_list, start, mid - 1)
    else:
        return binary(N_factor, N_list, mid + 1, end)

N = int(input())
N_list = list(map(int, input().split()))
N_list.sort()

M = int(input())
M_list = list(map(int, input().split()))

N_factor_dic = {}

for N_factor in N_list:
    start = 0
    end = len(N_list) - 1
    
    if N_factor not in N_factor_dic:
        N_factor_dic[N_factor] = binary(N_factor, N_list, start, end)

print(' '.join(str(N_factor_dic[x]) if x in N_factor_dic else '0' for x in M_list ))