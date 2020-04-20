import heapq
def solution(scoville, K):
    n = len(scoville)
    answer = 0
    heapq.heapify(scoville)
    while True:
        print(scoville)
        first = heapq.heappop(scoville)
        if first >= K:
            return answer
        if answer >= n-1:
            return -1
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first+(second*2))
        answer += 1
# scoville = [1, 2, 3, 9, 10, 12]
# k = 7
scoville = [1,1,1]
k = 10
print(solution(scoville, k))