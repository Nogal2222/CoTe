# -*- coding: utf-8 -*-
a,b = int(input()),int(input())
first = b - (int(b/10)*10)
second = int((b - (int(b/100)*100))/10)
third = int(b/100)
print(a*first)
print(a*second)
print(a*third)
print((a*first)+(a*second*10)+(a*third*100))