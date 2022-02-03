# -*- coding: utf-8 -*-
''' 최빈값이 리스트 형태라 양의 정수에서만 출력됨
import sys

n = int(sys.stdin.readline())
lst = [0] * n
for i in range(n):
    lst[i] = int(sys.stdin.readline())

#산술평균
san_avg = sum(lst) // n

#중앙값
sorted_lst = sorted(lst)
mid = sorted_lst[n//2]

#최빈값
fre_lst = [0] * 4001

for j in lst:
    fre_lst[j] += 1

if fre_lst.count(max(fre_lst)) > 1:
    for k in range(len(fre_lst)):
        if k == fre_lst.index(max(fre_lst)):
            fre_num = k
    
else:
    fre_num = fre_lst.index(max(fre_lst))



#범위
min_num = min(lst)
max_num = max(lst)
rng = max_num - min_num

#출력
print(san_avg)
print(mid)
print(fre_num)
print(rng)
'''

import sys
from collections import Counter

n = int(input()) #int(sys.stdin.readline())
nums = [0] * n

for i in range(n):
    nums[i] = int(input()) #int(sys.stdin.readline()))


#산술평균
avg = round(sum(nums) / n)

#중간값
nums.sort() # 크기순 정렬
med = nums[n // 2]

#최빈값
#빈도 높은 순으로 정렬 후 리스트 반환
nums_s = Counter(nums).most_common()
#만약 첫번째와 두번째의 value가 같으면 두번째 값 출력
if len(nums_s) > 1:
    if nums_s[0][1] == nums_s[1][1]:
        fre_num = nums_s[1][0]
    else:
        fre_num = nums_s[0][0]
else:
    fre_num = nums_s[0][0]

#범위
rng = nums[-1] - nums[0] #sort로 정렬되어 있으므로

#출력
print(avg)
print(med)
print(fre_num)
print(rng)