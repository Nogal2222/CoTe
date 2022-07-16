dic_dec_to_word = {0 : 'ZRO', 1 : 'ONE', 2 : 'TWO', 3 : 'THR',
                   4 : 'FOR', 5 : 'FIV', 6 : 'SIX', 7 : 'SVN',
                   8 : 'EGT', 9 : 'NIN'}

dic_word_to_dec = {'ZRO' : 0, 'ONE' : 1, 'TWO' : 2, 'THR' : 3,
                   'FOR' : 4, 'FIV' : 5, 'SIX' : 6, 'SVN' : 7,
                   'EGT' : 8, 'NIN' : 9}

tc = int(input())

for t in range(1, tc+1):
    tc_num, len_tc = input().split()
    len_tc = int(len_tc)
    lst = list(input().split())
    
    for i in range(len_tc):
        lst[i] = dic_word_to_dec[lst[i]]
    
    lst = sorted(lst)
    
    for i in range(len_tc):
        lst[i] = dic_dec_to_word[lst[i]]
    
    answer = ' '.join(lst)
    print(tc_num)
    print(answer)