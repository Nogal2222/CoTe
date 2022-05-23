# 총 금액 구하는 함수
def cal_price(n, m, park_price, car_weight, orders):
    parking_lot = [0] * n
    waiting_zone = []
    total_price = 0
    
    for i in orders:
        if i > 0:
            for j in range(n):
                # 빈 자리 없으면 대기
                if 0 not in parking_lot:
                    waiting_zone.append(i)
                    break
                # 빈 자리 있으면 주차
                if parking_lot[j] == 0:
                    parking_lot[j] = i
                    break
        
        else:
            index = parking_lot.index(abs(i))
            parking_lot[index] = 0
            total_price += (car_weight[abs(i)-1] * park_price[index])
            
            # 대기 차량 있으면 나가고 바로 주차
            if waiting_zone:
                parking_lot[index] = waiting_zone.pop(0)
    
    return total_price

T = int(input())
answers = [''] * T

for t in range(1, T+1):
    n, m = map(int, input().split())
    
    # 주차장 자리에 단위무게당 요금 Ri 설정
    park_price = [0] * n
    for i in range(n):
        park_price[i] = int(input())
    
    # 차량 무게 Wi
    car_weight = [0] * m
    for i in range(m):
        car_weight[i] = int(input())
    
    # 입장순서 orders
    orders = [0] * 2 * m
    for i in range(2 * m):
        orders[i] = int(input())
    
    total_price = cal_price(n, m, park_price, car_weight, orders)
    
    answers[t-1] = f'#{t} {total_price}'

for i in answers:
    print(i)