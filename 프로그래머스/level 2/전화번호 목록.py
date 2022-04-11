import heapq

def solution(phone_book):
    len_book = len(phone_book)
    answer = True
    heapq.heapify(phone_book)
    p_num = heapq.heappop(phone_book)
    
    if len_book == 1:
        return True
    
    while phone_book:
        i = len(p_num)
        
        if p_num == phone_book[0][:i]:
            return False
        
        p_num = heapq.heappop(phone_book)

    return answer

phone_book = ["12", "123", "1235", "567", "88"]
result = solution(phone_book)

'''내가 처음 한 풀이 (몇개 오류)
def solution(phone_book):
    len_book = len(phone_book)
    
    if len_book == 1:
        return True
    
    phone_book.sort(key = lambda x: len(x))
    bools = []
    answer = True
    
    for i in range(len_book - 1):
        for j in range(i+1, len_book):
            if phone_book[i] in phone_book[j]:
                bools.append(False)
                break
    
    if False in bools:
        answer = False
    
    return answer
'''
''' 정말 파이써닉하다..
def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True
'''