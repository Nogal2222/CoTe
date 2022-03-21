# -*- coding: utf-8 -*-
import re

def solution(new_id):
    #isdigit(), isalpha(), ['-', '_', '.']
    alphabet = ['1', '2', '3', '4', '5', '6',
                '7', '8', '9', '0', 
                'a', 'b', 'c', 'd', 'e', 'f',
                'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r',
                's', 't', 'u', 'v', 'w', 'x',
                'y', 'z',
                '-', '_', '.']
    id_list = []
    
    #1단계
    new_id = new_id.lower()
    
    #2단계
    for i in new_id:
        if i in alphabet:
            id_list.append(i)
    
    new_id = ''.join(id_list)
    
    #3단계
    new_id = re.sub('(([.])\\2{1,})', '.', new_id)
    
    '''
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
    '''
    
    #4단계
    new_id = new_id.strip('.')
    
    #5단계
    len_id = len(new_id)
    
    if len_id <= 2:
        if len_id == 0:
            new_id += 'a'
        #7단계
        while 1:
            len_id = len(new_id)
            if len_id == 3:
                break
            else:
                new_id += new_id[len_id - 1]
    
    #6단계
    elif len_id >= 16:
        new_list = list(new_id)
        target = ''.join(new_list[15:len_id])
        new_id = new_id.replace(target, '')
        new_id = new_id.strip('.')
    
    return new_id

#정규식
def solution2(new_id):
    st = new_id
    #1
    st = st.lower()
    #2
    st = re.sub('[^a-z0-9\-_.]', '', st)
    #3
    st = re.sub('\.+', '.', st)
    #4
    st = re.sub('^[.]|[.]$', '', st)
    #5, 6
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    #7
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st
new_id = '=.='

print(solution(new_id))