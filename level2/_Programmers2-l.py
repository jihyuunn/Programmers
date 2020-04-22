def solution(clothes):
    answer = 1
    cnt = {}
    for item, category in clothes:
        if category in cnt:
            cnt[category] += 1
        else:
            cnt[category] = 1
    for i in cnt.values():
        answer *= (i+1)
    return answer-1