# def solution(number, k):
#     answer = []
#     numbers = list(number)
#     start = 0
#     while k > 0 and start<len(numbers):
#         current = numbers[start:start+k+1]
#         temp = ['0', 0]
#         for j in range(len(current)):
#             if current[j] > temp[0]:
#                 temp = [current[j], j]
#         answer.append(temp[0])
#         k -= temp[1]
#         start += temp[1]+1
#         print(temp, answer, current, k)
#     if numbers[start:]:
#         for i in numbers[start:]:
#             answer.append(i)
#     if k > 0:
#         answer = answer[:-k]
#     return ''.join(answer)

def solution(number, k):
    answer = [number[0]]
    index = 1
    while index < len(number):
        cur = number[index]
        check = min(len(answer), k)
        for i in range(check):
            if answer[-1] < cur:
                answer.pop()
                k -= 1
            else: 
                break
        answer.append(cur)
        index += 1
    print(answer)
    return answer

print(solution("4177252841", 4))