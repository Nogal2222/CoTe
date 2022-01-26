# -*- coding: utf-8 -*-
words = input().upper()
words_lst = list(set(words))

cnt_lst = []
for i in words_lst:
    cnt = words.count(i)
    cnt_lst.append(cnt)

max_cnt_lst = max(cnt_lst)
if cnt_lst.count(max_cnt_lst) > 1:
    print("?")
else:
    max_index = cnt_lst.index(max_cnt_lst)
    print(words_lst[max_index])