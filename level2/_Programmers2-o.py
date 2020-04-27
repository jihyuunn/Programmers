from itertools import permutations
def solution(baseball):
    answer = 0
    numbers = list(map(''.join, permutations('123456789', 3)))
    for i in numbers:
        ans = True
        for k in baseball:
            cur, s, b = k
            ball = 0
            strike = 0
            for j in range(len(i)):
                if i[j] == str(cur)[j]:
                    strike += 1
                elif i[j] in str(cur):
                    ball += 1
            print(strike, ball, i, cur)
            if s!= strike or b!=ball:
                ans = False
                break
        if ans == True:
            answer += 1
    print(answer)
    return answer
solution([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]])