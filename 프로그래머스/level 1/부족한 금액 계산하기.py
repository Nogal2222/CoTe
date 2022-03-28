def solution(price, money, count):
    total_price = 0
    
    for i in range(1, count + 1):
        total_price += (price * i)
    
    answer = money - total_price
    
    if answer > 0:
        return 0
    
    else:
        answer = abs(answer)
        
    return answer

price = 3
money = 20
count = 4
print(solution(price, money, count))