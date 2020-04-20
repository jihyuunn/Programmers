def solution(arr):
    answer = []
    current = arr[0]
    answer.append(current)
    for i in range(1,len(arr)):
        if arr[i] != current:
            current = arr[i]
            answer.append(current)
    return answer