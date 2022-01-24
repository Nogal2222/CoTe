# -*- coding: utf-8 -*-
a = int(input())
b = int(input())
c = int(input())
result = list(str(a*b*c)) '''곱셈 결과를 문자형태로 받음'''

for i in range(10):'''0~9까지'''
    print(result.count(str(i)))'''i에 있는 수를 셈'''