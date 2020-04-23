def solution(citations):
    answer = 0
    n = len(citations)
    citations = sorted(citations, reverse=True)
    for i in range(n):
        cur = min(citations[i], i+1)
        answer = max(cur, answer)
    return answer

solution([22,42])