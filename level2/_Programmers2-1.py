def solution(record):
    answer = []
    check = []
    dic = {}
    for i in range(len(record)):
        temp = record[i].split(' ')
        if temp[0] == 'Enter':
            dic[temp[1]] = temp[2]
        elif temp[0] == 'Change':
            dic[temp[1]] = temp[2]
    for j in range(len(record)):
        temp = record[j].split(' ')
        if temp[0] == 'Enter':
            answer.append(dic[temp[1]]+'님이 들어왔습니다.')
        elif temp[0] == 'Leave':
            answer.append(dic[temp[1]]+'님이 나갔습니다')
    print(answer)
    return answer
record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
solution(record)