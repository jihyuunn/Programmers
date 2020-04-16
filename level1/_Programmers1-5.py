def solution(n, lost, reserve):
    answer = 0
    clothes = {}
    for i in range(1,n+1):
        clothes[i] = 1
    for j in range(1,n+1):
        if j in reserve:
            clothes[j] += 1
        if j in lost:
            clothes[j] -= 1
    for m in range(1, n+1):
        if clothes[m] == 0:
            if m-1 > 0 and clothes[m-1] > 1:
                answer += 1
                clothes[m-1] -= 1
            elif m+1 < n+1 and clothes[m+1] >1:
                answer += 1
                clothes[m+1] -= 1
        else:
            answer += 1
    return answer