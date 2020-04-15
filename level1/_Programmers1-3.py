def solution(participant, completion):
    answer = ''
    check = {}
    for person in participant:
        if person in check:
            check[person] += 1
        else:
            check[person] = 1
    for i in completion:
        check[i] -= 1
    for j in check:
        if check[j] > 0:
            return j