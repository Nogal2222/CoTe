# -*- coding: utf-8 -*-
n, m = map(int, input().split())
cards = list(map(int, input().split()))
result = 0
lst = []
lst_cards = []
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if cards[i] + cards[j] + cards[k] > m:
                continue
            else:
                lst.append(cards[i] + cards[j] + cards[k])
                lst_cards.append((cards[i],cards[j],cards[k]))
                

largest_cards = lst_cards[lst.index(max(lst))]
print(max(lst))
print(largest_cards)
