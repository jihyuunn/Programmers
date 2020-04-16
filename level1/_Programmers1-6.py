def solution(array, commands):
    answer = []
    for command in commands:
        start,end,index = command
        temp = sorted(array[start-1:end])
        answer.append(temp[index-1])
    return answer