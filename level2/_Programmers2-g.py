import math
def solution(progresses, speeds):
    answer = []
    temp = []
    for i in range(len(progresses)):
        x = math.ceil((100-progresses[i])/speeds[i])
        temp.append(x)
    print(temp)
    deploy = 1
    compare = temp[0]
    for j in range(1, len(temp)):
        if compare < temp[j]:
            answer.append(deploy)
            deploy = 1
            compare = temp[j]
        else: 
            deploy += 1
    answer.append(deploy)
    print(answer)
    return answer

# progresses = [93,30,55]
# progresses = [40, 93, 30, 55, 60, 65]
progresses = [93, 30, 55, 60, 40, 65]
# speeds = [1,30,5]
# speeds = [60, 1, 30, 5 , 10, 7]
speeds = [1, 30, 5 , 10, 60, 7]
solution(progresses, speeds)