def solution(n):
    answer = 0
    numbers = [x for x in range(1, n+1)]
    total = [x for x in range(1,n+1)]
    i = 1
    while i < n//2:
        for j in range(len(numbers)):
            if total[j]+numbers[j]+i > n:
                break
            if total[j]+numbers[j]+i == n:
                total[j] += numbers[j]+i
                answer += 1
            elif total[j]+numbers[j]+i < n:
                total[j] += numbers[j]+i
        i += 1 
    return answer+1