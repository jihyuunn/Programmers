def solution(budgets, M):
    answer = 0
    left = 0
    right = M
    if sum(budgets) > M:
        while left <= right:
            mid = (left+right)//2
            if go(budgets, M, mid):
                answer = max(mid, answer)
                left = mid+1
            else:
                right = mid-1
    else:
        return max(budgets)
    return answer

def go(budgets, M, mid):
    total = 0
    for i in budgets:
        if i < mid:
            total += i
        else:
            total += mid
    if total <= M:
        return True
    else: 
        return False