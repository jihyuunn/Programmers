# from collections import deque
# def solution(jobs):
#     answer = []
#     jobs = sorted(jobs, key=lambda x: [x[0], x[1]])
#     jobs = deque(jobs)
#     totalCnt = len(jobs)
#     totalTime = 0
#     currentQ = []
#     while len(answer)<totalCnt:
#         print(jobs, totalTime)
#         index = 0
#         if jobs:
#             for i,job in enumerate(jobs):
#                 request, duration = job
#                 if request <= totalTime:
#                     currentQ.append(job)
#                     index = i
#             for j in range(index+1):
#                 temp = jobs.popleft()
#         print(jobs, currentQ)
#         if currentQ:
#             currentQ = sorted(currentQ, key=lambda x: x[1])
#             currentQ = deque(currentQ)
#             temp = currentQ.popleft()
#             totalTime += temp[1]
#             answer.append(totalTime-temp[0])
#         else:
#             totalTime = sum(temp)
#             answer.append(temp[1])
#     print(answer)
#     print(sum(answer)//len(answer))
#     return sum(answer)//len(answer)
from collections import deque
def solution(jobs):
    answer = []
    totalTime = 0
    jobs = sorted(jobs, key=lambda x:x[1])
    while jobs:
        for i in range(len(jobs)):
            req = jobs[i]
            if req[0] <= totalTime:
                print(req)
                totalTime += req[1]
                answer.append(totalTime-req[0])
                jobs.pop(i)
                break
            if i == len(jobs)-1:
                totalTime += 1
    print(answer)
    return sum(answer)//len(answer)

solution([[0, 3], [4, 4], [5, 3], [4, 1]])
solution([[0, 9], [0, 4], [0, 5], [0, 7], [0, 3]])
solution([[0, 3], [1, 9], [500, 6]])
solution([[0,2],[0,3],[2,1]])
solution([[24, 10], [18, 39], [34, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]])
solution([[0, 10], [4, 10], [5, 11], [15, 2]])
solution([[0, 5], [1, 2], [5, 5]])