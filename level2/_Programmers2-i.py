def solution(prices):
    answer = []
    left = 0
    right = 1
    temp = 0
    while left < len(prices)-1:
        if prices[left] <= prices[right]:
            temp += 1
            right += 1
        elif prices[left] > prices[right]:
            if temp == 0:
                answer.append(1)
            else:
                answer.append(temp+1)
                temp = 0
            left += 1
            right = left + 1
        if right == len(prices):
            left += 1
            right = left+1
            answer.append(temp)
            temp = 0
        print(left, right, temp)
    print(answer)
    return answer.append(0)

solution([1, 2, 3, 1, 2, 3])