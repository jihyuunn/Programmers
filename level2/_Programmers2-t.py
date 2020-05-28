def solution(brown, yellow):
    answer = []
    total = brown + yellow
    for i in range(total//2, 2, -1):
        if total %i == 0:
            temp = 2*i + 2*(total//i)-4
            if temp == brown:
                return [i,total//i]