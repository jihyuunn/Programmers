def solution(d, budget, index):
    global answer, ans
    if index ==len(d):
        print(budget, answer)
        ans = max(answer, ans)
        return
    if d[index] <= budget:
        # print(budget)
        answer += 1
        solution(d, budget-d[index], index+1)
        answer -= 1
    solution(d, budget, index+1)
    

# d = [1, 3, 2, 5, 4]
d = [2,2,2,3]
# budget = 9
budget = 10
answer = 0
ans = 0
solution(d, budget, 0)
print(ans)