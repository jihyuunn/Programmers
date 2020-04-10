def solution(numbers, target):
    answer = [0]
    for i in range(len(numbers)):
        temp = []
        for j in range(len(answer)):
            temp.append(answer[j]+numbers[i])
            temp.append(answer[j]-numbers[i])
        answer = temp
    print(answer)
    return answer.count(target)

numbers = [1, 1, 1, 1, 1]
target = 3

solution(numbers, target)


answer = 0
def DFS(idx, numbers, target, value):
    global answer
    N = len(numbers)
    if(idx== N and target == value):
        answer += 1
        return
    if(idx == N):
        return

    DFS(idx+1,numbers,target,value+numbers[idx])
    DFS(idx+1,numbers,target,value-numbers[idx])
def solution(numbers, target):
    global answer
    DFS(0,numbers,target,0)
    return answer