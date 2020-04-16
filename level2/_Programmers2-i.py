def solution(prices):
    answer = [0]*len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] > prices[j]:
                answer[i] += 1
                break
            else:
                answer[i] += 1
    print(answer)
    return answer

prices = [1, 2, 3, 2, 3]
# prices = [9, 8, 7, 6]
solution(prices)