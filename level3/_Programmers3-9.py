def solution(n, times):
    answer = 0
    left = 1
    right = max(times)*n
    while left <= right:
        mid = (left+right)//2
        temp = 0
        # print(left, right, mid)
        for i in times:
            temp += mid//i
        if temp < n:
            left = mid+1
        else:
            answer = mid
            right = mid-1
    return answer

solution(6, [7, 10])
solution(5, [6, 6, 6, 6, 6])