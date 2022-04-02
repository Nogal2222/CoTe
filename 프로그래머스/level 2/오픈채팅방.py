def solution(record):
    new_record = []
    id_nick_dict = {}
    answer = []
    
    #커맨드, id, 닉네임 분리하는 for문
    for i in range(len(record)):
        temp = list(record[i].split(' '))
        new_record.append(temp)
    
    #id닉네임 dict에 입장과 변경 결과 반영
    for i in range(len(new_record)):
        if new_record[i][0] == 'Enter':
            id_nick_dict[new_record[i][1]] = new_record[i][2]
        
        elif new_record[i][0] == 'Change':
            id_nick_dict[new_record[i][1]] = new_record[i][2]
    
    #방장이 보는 메세지 추가
    for i in range(len(new_record)):
        if new_record[i][0] == 'Enter':
            message = '{nick}님이 들어왔습니다.'.format(nick = id_nick_dict[new_record[i][1]])
            answer.append(message)
        
        elif new_record[i][0] == 'Leave':
            message = '{nick}님이 나갔습니다.'.format(nick = id_nick_dict[new_record[i][1]])
            answer.append(message)
    
    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan", "Enter uid8901 Muzi", "Change uid8901 Apitchi"]
result = solution(record)