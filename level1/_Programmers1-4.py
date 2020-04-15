def solution(answers):
    answer = [0,0,0]
    first = [1,2,3,4,5]
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]
    for i in range(len(answers)):
        fleft = i%5
        sleft = i%8
        tleft = i%10
        if answers[i] == first[fleft]:
            answer[0] += 1
        if answers[i] == second[sleft]:
            answer[1] += 1
        if answers[i] == third[tleft]:
            answer[2] += 1
    ans = []
    maxx = max(answer)
    for j in range(len(answer)):
        if answer[j] == maxx:
            ans.append(j+1)
    return ans